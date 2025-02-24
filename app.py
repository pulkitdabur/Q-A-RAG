from pypdf import PdfReader
from langchain.document_loaders import TextLoader
from langchain_openai import AzureChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_community.document_loaders import PyPDFLoader

# llm4=AzureChatOpenAI(openai_api_key="",
#                      openai_api_version="",
#                      azure_deployment="",
#                      azure_endpoint="",
#                      temperature=0)

vector_store_name="rag_qa"

def main_func(question):
    document="E:\\budget_speech.pdf"
    loader=PyPDFLoader(document)
    all_splits = loader.load_and_split(text_splitter=RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=200, add_start_index=True))
    embedding=FastEmbedEmbeddings(model_name="BAAI/bge-base-en-v1.5")
    FAISS.from_documents(all_splits,embedding)
    docsearch = FAISS.from_documents(all_splits,embedding)
    docsearch.save_local(vector_store_name)
    loaded_db=FAISS.load_local(vector_store_name,embedding,allow_dangerous_deserialization=True)
    retriever=loaded_db.as_retriever(search_type="similarity",search_kwargs={"k":6})

    retrieved_docs=retriever.invoke("what are the taxes imposed on electronic goods")
    
    # template="""Use the following pieces of context to answer the question at the end.
    #             If you don't know the answer, just say that you don't know, don't try to make up an answer.
    #             Kep the answer as concise as possible. Please give answer in points
                
    #             {context}
                
    #             Question: {question}
                
    #             Answer: """
    # prompt=PromptTemplate.from_template(template)
    
    # def format_docs(docs):
    #     print(len(docs))
    #     return "\n\n".join(doc.page_content for doc in docs)

    # rag_chain = (
    #     { "context": retriever | format_docs, "question": RunnablePassthrough()}
    #     | prompt
    #     | llm4
    #     | StrOutputParser()
    # ) 
    # aa=rag_chain.invoke(question)
    return retrieved_docs

if __name__=="__main__":
    main_func("what are the taxes imposed on electronic goods")