import google.generativeai as genai

# Replace with your Gemini API key
genai.configure(api_key="AIzaSyDGmnu3rsg41YTloDkLhCHKvOQ5KXAGQkEpython chatbot.py")

model = genai.GenerativeModel("gemini-1.5-flash")

print("Chatbot Ready! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye! 👋")
        break

    response = model.generate_content(user_input)
    print("Chatbot:", response.text)
