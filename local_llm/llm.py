# local_llm/llm.py

def generate_response(prompt: str, context: str) -> str:
    """
    Simulate a local LLM call based on the given prompt and context.
    
    Parameters:
    prompt (str): The input prompt for the LLM.
    context (str): The context in which the prompt is given.
    
    Returns:
    str: A simulated response from the LLM based on the context.
    
    If no context is provided, return 'NO' to indicate insufficient information.
    """
    if not context or len(context.strip()) == 0:
        return "NO"
    
    # In a real scenario, you would call your local LLM here.
    # For demonstration, we return a dummy response.
    return f"LLM Response to '{prompt}' based on context: {context[:50]}..."
