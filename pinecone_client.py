# insert data set vectors 

# ask it - what is the closest one to make predictions  
from pinecone import Pinecone
import pandas as pd

pc = Pinecone(api_key="")
index = pc.Index("movie")

def upsert_data_set(data_set : pd.DataFrame ,data_vector):
    for i in range(len(data_set)):
        upsert_response = index.upsert(
            vectors=[
                {
                    "id":str(i),
                    "values":data_vector[i],
                    "metadata":{'title': data_set.iloc[i]['title']}
                }
            ],
            namespace="ns1"
        )
    return upsert_response

def query_matches(input_embedding):
    matches = index.query(vector= input_embedding,top_k=10,include_metadata=True,namespace="ns1")
    return matches
