# member_finder/finder.py

import json
import re
from functools import lru_cache

def load_members(filename: str = 'members.json') -> dict:
    """
    Load Superteam member data from a JSON file.
    """
    with open(filename, 'r') as f:
        return json.load(f)

@lru_cache(maxsize=128)
def extract_skills_from_query(query: str) -> list:
    """
    Extracts capitalized keywords from the query as a simplistic method of
    identifying required skills (e.g., RUST, DEFI).
    """
    skills = re.findall(r'\b[A-Z]{2,}\b', query)
    return skills

def find_matching_member(query: str, members: list):
    """
    Matches members from the JSON database based on extracted skills.
    
    Parameters:
    query (str): The search query containing required skills.
    members (list of dict): A list of dictionaries where each dictionary represents a member.
    Returns an explanation and the member information if a match is found,
    or "NO" otherwise.
    """
    required_skills = extract_skills_from_query(query)
    matching_members = []
    for member in members:
        member_skills = member.get('skills', [])
        member_skills_upper = [skill.upper() for skill in member_skills]
        if all(skill in member_skills_upper for skill in required_skills):
            matching_members.append(member)
    
    if matching_members:
        member = matching_members[0]
        explanation = f"Member {member['name']} matches skills: {', '.join(required_skills)}."
        return explanation, member
    return "NO", None

if __name__ == '__main__':
    members = load_members()
    query = "I want to find a RUST developer to build a DEFI project with Twitter integration."
    explanation, member = find_matching_member(query, members)
    print("Member Finder Output:", explanation)
