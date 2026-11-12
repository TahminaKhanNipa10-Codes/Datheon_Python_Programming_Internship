import re
import json
import sys

# Conversation states: greeting -> intent -> resolved -> exit
STATE_GREETING = "greeting"
STATE_INTENT = "intent"
STATE_RESOLVED = "resolved"
STATE_EXIT = "exit"

def load_data(filepath):
    """Load the dataset from the JSON file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"[!] Error: '{filepath}' not found. Please ensure it exists.")
        sys.exit()

def find_intent_answer(user_input, faqs):
    """Return the FAQ answer matching the user's keywords, or None."""
    # Mapping regex keywords to the index of the FAQs list
    intent_patterns = {
        r"\b(hour|hours|operation|time|open)\b": 0,         # FAQ 1: hours
        r"\b(submit|project|github|repo|repository)\b": 1,  # FAQ 2: project submission
        r"\b(certificate|receive|issue|when)\b": 2          # FAQ 3: certificate
    }
    for pattern, index in intent_patterns.items():
        if re.search(pattern, user_input) and index < len(faqs):
            return faqs[index]["answer"]
    return None

def get_bot_response(user_input, dataset, state):
    """Returns (response, new_state)."""
    # 1). Normalize user input (lowercase, strip whitespace)
    user_input = user_input.lower().strip()

    # 2). Clean exit commands
    if re.search(r"\b(bye|exit|quit)\b", user_input):
        return "Goodbye! Best of luck with your Datheon internship!", STATE_EXIT

    # 3). Intent identification (works even if the message also has a greeting)
    answer = find_intent_answer(user_input, dataset.get("faqs", []))
    if answer:
        return answer + "\nAnything else I can help you with?", STATE_RESOLVED

    # 4). Greetings only
    for greeting in dataset.get("greetings", []):
        if re.search(rf"\b{re.escape(greeting.lower())}\b", user_input):
            return "Hello! How can I assist you with your Datheon internship today?", STATE_INTENT

    # 5). Graceful fallback (state unchanged)
    return ("I'm sorry, I didn't quite catch that. You can ask about our hours, "
            "how to submit your project, or certificate issuance."), state

def main():
    print("Loading Datheon chatbot system...")
    dataset = load_data('sample_faq.json')

    print("\n" + "="*60)
    print("   Datheon Support Bot (Type 'exit' to quit)   ")
    print("="*60)

    state = STATE_GREETING
    while state != STATE_EXIT:
        try:
            user_input = input("\nYou: ")
            if not user_input.strip():
                continue

            response, state = get_bot_response(user_input, dataset, state)
            print(f"Chatbot: {response}")
        except (KeyboardInterrupt, EOFError):
            print("\nChatbot: Goodbye! Have a great day!")
            break

if __name__ == "__main__":
    main()
