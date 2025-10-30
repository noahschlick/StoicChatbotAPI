from dotenv import load_dotenv
import responses
import time

if __name__ == "__main__":
    user_response = input("What's on your mind? ")
    response = responses.get_response(user_response)
    print("The Stoic Philosopher says...")
    for ch in response:
        print(ch, end="")
        time.sleep(0.05)
    print("\n")   