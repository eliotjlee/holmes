from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
import openai
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import TextLoader
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.embeddings.cohere import CohereEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.elastic_vector_search import ElasticVectorSearch
from langchain.vectorstores import Chroma
from langchain.docstore.document import Document
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory

class SuspectAgent:
    def __init__(self, plot, i):
        self.suspect = plot.suspects[i]
        self.memory_path = self.suspect.memory_path
        self.chat_memory = ConversationBufferMemory(memory_key="chat_history", input_key="human_input")

        embeddings_model = OpenAIEmbeddings()

        raw_docs = TextLoader(self.memory_path).load()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = 1000,
            chunk_overlap  = 200,
            length_function = len,
            is_separator_regex = False,
        )

        memory_docs = text_splitter.split_documents(raw_docs)

        self.db = Chroma.from_documents(memory_docs, OpenAIEmbeddings())

        template = "You are a suspect in a murder, and you are currently being questioned by the lead investigator.\n\n"
        template += f"Here are the details about the case: \n\n{plot.get_this_suspect_summary(i)}\n\n"

        template += """

        Given the following extracted parts of your memory and a question, respond to the investigator.

        {context}

        {chat_history}
        Human: {human_input}
        Chatbot:"""

        prompt = PromptTemplate(
            input_variables=["chat_history", "human_input", "context"], template=template
        )
        
        self.chain = load_qa_chain(
            ChatOpenAI(
                temperature=0,          
                model="gpt-3.5-turbo-16k"
            ), 
            chain_type="stuff", 
            memory=self.chat_memory, 
            prompt=prompt
        )


    def get_suspect_response(self, user_message):
        doc_search = self.db.similarity_search(user_message, 4)
        self.chain({"input_documents": doc_search, "human_input": user_message}, return_only_outputs=True)
        return self.chain.get("output_text")









