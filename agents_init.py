from langchain.vectorstores import Chroma, FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import TextLoader

def init_agent(save_path, suspect_id):

    loader = TextLoader("{save_path}/accounts/suspect_{suspect_id}.txt")