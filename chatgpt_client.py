import openai
import httpcore
import time
import httpx

openai.api_key = "sk-proj-xx"
# openai.timeout = 60
retries = 1

def generate_chatgpt_chat_response(prompt):
    for i in range(retries):
        try:
            if __name__ == "chatgpt_client":
                response = openai.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=prompt,
                    max_tokens=10,
                    temperature=0.7,
                    n=1,
                    stop=["\n"]
                )
                print(response)
                return response
            print("empty")
            return "empty"
        except httpcore.ConnectTimeout:
            print(f"httpcore Timeout, retry attempt: {i}")
            time.sleep(5)
        except httpx.ConnectTimeout:
            print(f"httpx Timeout, retry attempt: {i}")
            time.sleep(5)
        except openai.error.OpenAIError as e:
            print(f"OpenAIError catch: {e}")
        except openai.BadRequestError as e:
            print(f"bad request catch: Error occured {e}")
        except Exception as e:
            print(f"last catch: {e}")

def generate_chatgpt_response(promptt):
    # Every Python module (file) has a special built-in variable called __name__.
    # When a file is run directly, the value of __name__ is set to "__main__".
    # When a file is imported as a module, the value of __name__ is set to the module's name.
    print(__name__)  # //chatgpt_client
    for i in range(retries):
        try:
            if __name__ == "chatgpt_client":
                response = openai.completions.create(
                    model="gpt-3.5-turbo-instruct",
                    prompt=promptt,
                    max_tokens=10,
                    temperature=0.7,
                    n=1,
                    stop=["\n"]
                )
                print(response)
                return response
            print("empty")
            return "empty"
        except httpcore.ConnectTimeout:
            print(f"httpcore Timeout, retry attempt: {i}")
            time.sleep(5)
        except httpx.ConnectTimeout:
            print(f"httpx Timeout, retry attempt: {i}")
            time.sleep(5)
        except openai.error.OpenAIError as e:
            print(f"OpenAIError catch: {e}")
        except openai.BadRequestError as e:
            print(f"bad request catch: Error occured {e}")
        except Exception as e:
            print(f"last catch: {e}")

def generate_embed(prompt):
    response = openai.embeddings.create(
        model="text-embedding-ada-002",
        input=prompt
    )
    pure_embeds =[]
    for embedding in response.data:
        pure_embeds.append(embedding.embedding)
    return pure_embeds