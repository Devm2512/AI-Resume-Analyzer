import re

def extract_skills_from_resume(resume_text, skill_list):


    found_skill = []

    for skill in skill_list:

        skill_lower = skill.lower()

        if re.search(rf"\b{re.escape(skill_lower)}\b", resume_text):

            found_skill.append(skill)

    return found_skill