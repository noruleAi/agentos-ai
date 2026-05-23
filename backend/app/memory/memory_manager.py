memory_store = []

async def save_memory(data):

    memory_store.append(data)

    return True

async def get_memories():

    return memory_store