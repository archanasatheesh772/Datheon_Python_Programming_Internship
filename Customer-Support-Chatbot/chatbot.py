
import json
import re
from pathlib import Path


# Load FAQ dataset
def load_faq():
    try:
        file_path = Path(__file__).parent / "sample_faq.json"

        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print("Error: FAQ dataset not found.")
        return None

    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return None


# Normalize user input
def normalize_input(user_input):
    return re.sub(r"\s+", " ", user_input.lower().strip())


# Check user intent
def get_response(user_input, data):
    message = normalize_input(user_input)

    if not message:
        return "Please enter a message."

    # Exit commands
    if re.search(r"\b(bye|exit|quit)\b", message):
        return "Goodbye! Thank you for chatting with us."

    responses = []

    # Greeting detection
    greetings = data.get("greetings", [])

    if any(re.search(r"\b" + re.escape(word) + r"\b", message)
           for word in greetings):
        responses.append("Hello! Welcome to Customer Support. How can I help you?")

    # FAQ keyword matching
    faq_keywords = {
        "hours": ["hours", "operation", "working time", "opening time"],
        "project": ["project", "submit", "submission", "github"],
        "certificate": ["certificate", "certification", "when will i receive"]
    }

    matched_intents = []

    for intent, keywords in faq_keywords.items():
        if any(keyword in message for keyword in keywords):
            matched_intents.append(intent)

    # Match FAQ questions
    for intent in matched_intents:
        for faq in data.get("faqs", []):
            question = normalize_input(faq.get("question", ""))
            if intent == "hours" and "hours" in question:
                responses.append(faq["answer"])
                break
            elif intent == "project" and "project" in question:
                responses.append(faq["answer"])
                break
            elif intent == "certificate" and "certificate" in question:
                responses.append(faq["answer"])
                break

    if responses:
        return "\n".join(responses)

    return "Sorry, I didn't understand your question. Could you please rephrase it?"


# Main chatbot program
def main():
    data = load_faq()

    if data is None:
        return

    print("=" * 45)
    print("       CUSTOMER SUPPORT CHATBOT")
    print("=" * 45)
    print("Type 'bye', 'exit', or 'quit' to end the chat.")

    while True:
        try:
            user_input = input("\nYou: ")
            response = get_response(user_input, data)

            print("Bot:", response)

            if re.search(r"\b(bye|exit|quit)\b",
                         normalize_input(user_input)):
                break

        except (EOFError, KeyboardInterrupt):
            print("\nBot: Goodbye! Have a nice day!")
            break


if __name__ == "__main__":
    main()
