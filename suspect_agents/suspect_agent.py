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

        print(f"SUSPECT: {self.suspect.name}")
        print(f"MEMORY PATH: {self.memory_path}")
        
        with open(self.memory_path) as f:
            memory_stream = f.read()

        embeddings = OpenAIEmbeddings()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = 1000,
            chunk_overlap  = 200,
            length_function = len,
        )

        texts = text_splitter.split_text(memory_stream)

        self.docsearch = Chroma.from_texts(
            texts, embeddings
        )


        template = "You are a suspect in a murder, and you are currently being questioned by the lead detective.\n\n"
        template += f"Here are the details about the case: \n\n{plot.get_this_suspect_summary(i)}\n\n"

        template += """

        Here are the memories that pop into your head as you hear the detective's question:

        {context}

        Selectively choose which to incorporate into your response. But NEVER quote them directly. These are your internal thoughts.
        """

        if self.suspect.guilty:
            template += """
            
            Remember, if you ARE guilty, you do not want the detective to know it. When the detective's question makes you think of the murder, you get very anxious and agitated and start to stutter.
            """
        else:
            template += """

            If the detective begins to wrongly accuse you of being guilty, you get really anxious and stutter a lot.
            """

        template += """
        
        {chat_history}

        Only answer this one question. Speak as your character would, based on their bio and tags--do not regurgitate these, but emobdy them. Do not be overly rigid and formal.

        Detective's question: {human_input}
        Your response to this question:"""

        prompt = PromptTemplate(
            input_variables=["chat_history", "human_input", "context"], template=template
        )
        
        '''
        Instead of passing memory into chain, send chain output into RCI chain
        Store RCI-corrected output into memory:

        But then how to pass in memory wihtout saving to that memory??
        Temp memory object? that is discarded --- oh yesss
        old/new versions - first chain initially saves history, but then new chainreplaces n-1 message history with new history, cycles back

        memory = ConversationBufferMemory()
        memory.save_context({"input": "hi"}, {"output": "whats up"})

        OR sentiment analysis on output, see if detective is threatening 
        '''

        self.chain = load_qa_chain(
            ChatOpenAI(
                temperature=0,          
                model="gpt-4"
            ), 
            chain_type="stuff", 
            memory=self.chat_memory, 
            prompt=prompt
        )


    def get_suspect_response(self, user_message):
        
        doc_search = self.docsearch.similarity_search(user_message, 4)
        response = self.chain({"input_documents": doc_search, "human_input": user_message}, return_only_outputs=True)
        return response.get("output_text")









