import numpy as np
import pandas as pd
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
import langchain
import langchain_community
from langchain_text_splitters import RecursiveCharacterTextSplitter
model=HuggingFaceEmbeddings(model_name="intfloat/multilingual-e5-base")
import os
all_docs=os.listdir(path="./data")
from langchain_community.document_loaders import Docx2txtLoader
for i in all_docs:
    loader=Docx2txtLoader(".\\data\\"+i)
    doc=loader.load()
    print(f'Data loaded successfully {i} file')

    chunk_obj=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=100)

    result=chunk_obj.split_documents(doc)
    print(f'Number of Chuncks in {len(result)} in file name {i}')

    chromadb=Chroma.from_documents(result,embedding=model,persist_directory="./DB/"+i+" Database")
    
    print(f'DB created Successfully for {i} file name')
print("all DBs created successfully")    

