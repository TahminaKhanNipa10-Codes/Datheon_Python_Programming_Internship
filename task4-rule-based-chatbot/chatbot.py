import re
import json
import sys

def load_data(filepath):
    """Load the dataset from the JSON file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"[!] Error: '{filepath}' not found. Please ensure it exists.")
        sys.exit()

def get_bot_response(user_input, dataset):
    # 1). Normalize user input (lowercase, strip whitespace)
    user_input = user_input.lower().strip()
    
    # 2). Clean exit commands handling
    if re.search(r"\b(bye|exit|quit)\b", user_input):
        return "Goodbye! Best of luck with your Datheon internship!", True
        
    # 3). Handle Greetings
    for greeting in dataset.get("greetings", []):
        if re.search(rf"\b{greeting}\b", user_input):
            return "Hello! How can I assist you with your Datheon internship today?", False
            
    # 4). Intent Identification (Regex keyword extraction mapped to JSON FAQs)
    faqs = dataset.get("faqs", [])
    
    # Mapping regex keywords to the index of the FAQs list
    intent_patterns = {
        r"\b(hour|hours|operation|time|open)\b": 0,         ## Matches FAQ 1
        r"\b(submit|project|github|repo|repository)\b": 1,  ## Matches FAQ 2
        r"\b(certificate|receive|issue|when)\b": 2          ## Matches FAQ 3
    }
    
    for pattern, index in intent_patterns.items():
        if re.search(pattern, user_input):
            if index < len(faqs):
                return faqs[index]["answer"], False
                
    # 5). Graceful fallback for unrecognized queries
    return "I'm sorry, I didn't quite catch that. You can ask about our hours, how to submit your project, or certificate issuance.", False

def main():
    print("Loading Datheon chatbot system...")
    dataset = load_data('sample_faq.json')
    
    print("\n" + "="*60)
    print("   Datheon Support Bot (Type 'exit' to quit)   ")
    print("="*60)
    
    # Conversational state management loop
    while True:
        try:
            user_input = input("\nYou: ")
            if not user_input.strip():
                continue
                
            response, should_exit = get_bot_response(user_input, dataset)
            print(f"Chatbot: {response}")
            
            if should_exit:
                break
        except (KeyboardInterrupt, EOFError):
            print("\nChatbot: Goodbye! Have a great day!")
            break

if __name__ == "__main__":
    main()
