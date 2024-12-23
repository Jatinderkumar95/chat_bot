from chatgpt_client import generate_chatgpt_response
from chatgpt_client import generate_embed
from chatgpt_client import generate_chatgpt_chat_response

selected_option = input("Select one option: 1. completion 2. embedding 3. chat")
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