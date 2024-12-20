from chatgpt_client import generate_chatgpt_response

while True:
    user_imput= input("Enter input: ")
    if(user_imput=="q"):
        break
    generate_chatgpt_response(user_imput)