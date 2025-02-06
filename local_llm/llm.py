# local_llm/llm.py

def generate_response(prompt: str, context: str) -> str:
    """
    Simulate a local LLM call. If no context is provided,
    return 'NO' to indicate insufficient information.
    """
    if not context or len(context.strip()) == 0:
        return "NO"
    
    # In a real scenario, you would call your local LLM here.
    # For demonstration, we return a dummy response.
    return f"LLM Response based on context: {context[:50]}..."
