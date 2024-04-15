from langchain.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.vectorstores import faiss
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings()

#video_url = "https://www.youtube.com/watch?v=-Osca2Zax4Y"

def create_vector_db_from_youtube_url(video_url: str) -> faiss:
    loader = YoutubeLoader.from_youtube_url(video_url)
    transcript = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunks_size=1000, 
    chunk_overlap=100)
    docs = text_splitter.split_documents(transcript)

    db = faiss.from_documents(docs, embeddings)
    return db 
# if you write return docs you see few text here 

print(create_vector_db_from_youtube_url(video_url))

#to run this code type python langchain_helper.py in terminal 

def get_response_from_query(db, query, k=4):

    docs = db.similarity_search(query, k=k)
    docs_page_content = " ".join([d.docs_page_content for d in docs])

    llm = OpenAI(model="text-devinci-003")

    prompt = PromptTemplate(
        input_variables= ["question", "docs"],
        template = """
        you are a helpful youtube assistant that can answer questions about 
        videos 
        based on the video's transcript.

        Answer the foloowing question: {question}
        By searching the following video transcript: {docs}

        Only use the factual information from the transcripts to answer the question.

        If you feel like you don't have enough information to answer the question,
        say "I don't know".

        Your answers should be detailed.
        """
    )

    chain = LLMChain(llm=llm, prompt=prompt)

    response = chain.run(question=query , docs = docs_page_content)

    response = response.replace("in", "")

