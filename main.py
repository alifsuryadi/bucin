from generative_text_bucin.chat import get_response

def main():
    print("Romantic Chat with Your Love")
    print("Type 'exit' or 'keluar' to end the chat.")
    
    while True:
        user_message = input("You: ").strip()
        
        if user_message.lower() in ["exit", "keluar"]:
            print("Program dihentikan oleh pengguna.")
            break
        
        response = get_response(user_message)
        
        if "error" in response:
            print(f"Error: {response['error']}")
        else:
            print(f"Bot: {response['response']} (Time taken: {response['time_taken']:.2f}s)")

if __name__ == "__main__":
    main()
