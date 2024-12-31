from chatgpt_client import generate_chatgpt_response
from chatgpt_client import generate_embed
from chatgpt_client import generate_chatgpt_chat_response
import pandas as pd
from pinecone_client import upsert_data_set,query_matches
from scipy import spatial
import numpy as np


# user_inp = np.array([1,2,3]).reshape(1,-1)
# user_inp = np.array([[1,2,3],[100,2000,3000]])
# sample_inp = np.array([[111,2222,3333],[1,2,3],[1,2,3]])
# #argsort array in ascending 
# #argsort 1 -array, sort the array in descending order
# print(np.argsort(1- spatial.distance.cdist(user_inp,sample_inp,'cosine')))
# print(np.argsort(spatial.distance.cdist(user_inp,sample_inp,'cosine')))

selected_option = input("Select one option: 1. completion 2. embedding 3. chat 4. load movie csv data 5. Query matches")
while True:
    user_imput= input("Enter input: ")
    if(user_imput=="q"):
        break
    if(selected_option == "1"):
     generate_chatgpt_response(user_imput)
    if(selected_option == "2"):
       generate_embed(user_imput)
    if(selected_option == "3"):
       generate_chatgpt_chat_response(user_imput)
    if(selected_option == "4"):
       user_imput = "m.csv" if user_imput.__contains__("d") else user_imput
       dataset = pd.read_csv(user_imput, low_memory=False)
       subset = dataset[['title','overview']]
       subset.dropna(inplace=True)
      #  print(subset['overview'])
      #  print(subset['overview'].values)
      #  print(subset['overview'].values.tolist())
       response = generate_embed(subset['overview'].values.tolist())
      # print(response)
       upsert_response = upsert_data_set(subset,response)
    if(selected_option == "5"):
       input_embed = generate_embed(user_imput)[0]
       #print(input_embed)
       matches = query_matches(input_embed)
       print(matches)
    else:
       print("end")