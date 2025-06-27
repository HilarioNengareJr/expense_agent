from langchain_community.chat_models import ChatOllama

def get_local_llm():
    return ChatOllama(model="llama3")