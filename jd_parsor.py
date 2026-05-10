import json
import re
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# -----------------------------
# Load Model + Tokenizer
# -----------------------------
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")


# -----------------------------
# Prompt Template (FIXED JSON BRACES)
# -----------------------------
PROMPT_TEMPLATE = """
You are a strict JSON generator.

Extract skills from the job description.

RULES:
- Output ONLY valid JSON
- No explanation
- No extra text
- No job description repetition

Format:
{{
  "must_have": [],
  "intermediate": [],
  "good_to_have": []
}}

Job Description:
{jd_text}
"""


# -----------------------------
# Safe JSON Parser (IMPORTANT)
# -----------------------------
def safe_json_parse(text: str):
    try:
        match = re.search(r"\{.*\}", text, re.DOTALL)

        if match:
            return json.loads(match.group())
        else:
            raise ValueError("No JSON found")

    except Exception:
        return {
            "must_have": [],
            "intermediate": [],
            "good_to_have": [],
            "error": "Failed to parse LLM output",
            "raw_output": text
        }


# -----------------------------
# Main Function
# -----------------------------
def parse_jd_with_llm(jd_text: str):

    prompt = PROMPT_TEMPLATE.format(jd_text=jd_text)

    try:
        # Tokenize input
        inputs = tokenizer(prompt, return_tensors="pt", truncation=True)

        # Generate output (controlled decoding)
        outputs = model.generate(
            **inputs,
            max_new_tokens=200,
            do_sample=False,
            temperature=0.0,
            num_beams=2
        )

        # Decode output
        output_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Parse safely
        parsed_output = safe_json_parse(output_text)

        return parsed_output

    except Exception as e:
        return {
            "must_have": [],
            "intermediate": [],
            "good_to_have": [],
            "error": str(e)
        }