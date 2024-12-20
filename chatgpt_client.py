import openai;
import time

openai.api_key = "sk-proj-xx";

def generate_chatgpt_response(prompt):
    # Every Python module (file) has a special built-in variable called __name__.
    # When a file is run directly, the value of __name__ is set to "__main__".
    # When a file is imported as a module, the value of __name__ is set to the module's name.
    print(__name__)  # //chatgpt_client
    try:
        if __name__ == "__main__":
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
    except openai.BadRequestError:
        print("Error occured")
    except Exception as e:
        print(f"{e}")