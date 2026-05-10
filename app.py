from utils.pdf_parser import extract_text_from_pdf
from utils.text_preprocessing import preprocessing_text
from models.jd_parsor import parse_jd_with_llm

resume_path = "C:/Users/dewan/OneDrive/Desktop/AI Resume Analyzer and Selector/Data/Resume/Dewang_Moghe__Resume.pdf"


jd_text = """
We are hiring a Data Scientist.

Must Have: Python, SQL, Machine Learning
Intermediate: NLP, Statistics
Good to Have: AWS, Docker
"""


raw_data = extract_text_from_pdf(resume_path)

clean_text = preprocessing_text(raw_data)

result = parse_jd_with_llm(jd_text)

print("\n--- PARSED JD OUTPUT ---\n")
print(result)

print("\n--- CLEANED TEXT ---\n")
print(clean_text[:500])

if isinstance(result, dict) and "error" not in result:
    print("\n--- Structured Output ---")
    print("Must Have:", result.get("must_have"))
    print("Intermediate:", result.get("intermediate"))
    print("Good to Have:", result.get("good_to_have"))
else:
    print("\n Error in parsing:")
    print(result)