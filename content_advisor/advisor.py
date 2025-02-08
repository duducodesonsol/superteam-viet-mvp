"""
content_advisor/advisor.py
"""
from local_llm.llm import generate_response
def advise_content(platform: str, content: str) -> str:
    """
    Given a platform and content, use the local LLM to suggest improvements.
    """
    prompt = f"Improve the following content for {platform}: {content}"
    advice = generate_response(prompt, content)
    return advice

if __name__ == '__main__':
    platform = "Twitter"
    content = "Check out our new project launch!"
    enhanced_content = advise_content(platform, content)
    print("Improved content:", enhanced_content)
