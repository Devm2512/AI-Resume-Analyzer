from models.resume_parsor import extract_skills_from_resume

def calculate_match_score(resume_test, jd_skills):

    must_have = jd_skills.get("must_have", [])
    intermediate = jd_skills.get("intermediate", [])
    good_to_have = jd_skills.get("good_to_have", [])

    def score_category(skills, weights):

        if not skills:

            return 0, []
        
        matched = extract_skills_from_resume(resume_test, skills)

        score = len(matched)/ len(skills)

        return score * weights, matched
    
    must_score, must_matched = score_category(must_have, 0.5)
    int_score, int_matched = score_category(intermediate, 0.3)
    good_score, good_matched = score_category(good_to_have, 0.2)

    final_score = (must_score + int_score + good_score) * 100

    return {
        "final_score": round(final_score, 2),
        "must_have_matched": must_matched,
        "intermediate_matched": int_matched,
        "good_to_have_matched": good_matched
    }