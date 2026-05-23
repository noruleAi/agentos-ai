async def planner_agent(prompt: str):

    prompt = prompt.lower()

    if "code" in prompt:
        return "Routing task to Coding Agent"

    elif "security" in prompt:
        return "Routing task to Security Agent"

    elif "research" in prompt:
        return "Routing task to Research Agent"

    else:
        return "General AI execution complete"