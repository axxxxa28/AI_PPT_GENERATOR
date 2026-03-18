import os 
from dotenv import load_dotenv
from llama_index.core import GPTVectorStoreIndex, SimpleDirectoryReader, Document
from llama_index.llms.openai import OpenAI
from llama_index.core.settings import Settings

load_dotenv()
OpenAI_API_KEY = os.getenv("OPENAI_API_KEY")

class Summarizer:
    def __init__(self, directory="data/"):
        Settings.llm = OpenAI(model="gpt-4", api_key=OpenAI_API_KEY)

    def summarize_text(self, text):
        documents = [Document(text=text)]
        index = GPTVectorStoreIndex.from_documents(documents)
        query_engine = index.as_query_engine()
        response = query_engine.query("Summarize this text into key points suitable for a presentation.")
        return response.response
   
if __name__ == "__main__":
    
    sample_text = "Artificial Intelligence (AI) is the simulation of human intelligence processes by machines, especially computer systems. These processes include learning, reasoning, and self-correction."
    summarizer = Summarizer()
    summary = summarizer.summarize_text(sample_text)
    print("\nSummary: \n\n", summary)  # Output the summary for verification