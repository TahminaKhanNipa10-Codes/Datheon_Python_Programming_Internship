<div align="center">

# 🤖 Rule-Based Customer Support Chatbot

**Datheon Python Programming Internship: Task 4**

A terminal-based customer support chatbot built with Python. It uses Regular Expressions (Regex) and JSON data parsing to identify user intents, extract keywords, and give contextual responses from a predefined FAQ dataset.

![Python](https://img.shields.io/badge/Python-3-blue?logo=python&logoColor=white)
![Regex](https://img.shields.io/badge/NLP-regex%20based-purple)
![Status](https://img.shields.io/badge/status-complete-brightgreen)

</div>

---

## 🎯 Features

- **Intent Matching:** Uses Python's `re` module to map user input to specific FAQ categories.
- **Dynamic Dataset:** Loads the knowledge base directly from `sample_faq.json`.
- **Conversational Flow:** Understands standard greetings and exits gracefully on commands like `bye`, `exit`, or `quit`.
- **Graceful Fallbacks:** Shows a helpful default navigation message when a query is not recognized.

## 🛠️ Technology Stack

| Category  | Details                                  |
|-----------|------------------------------------------|
| Language  | Python 3                                 |
| Libraries | `re` (Regex), `json`, `sys`              |
| Interface | Command Line Interface (CLI) / Terminal  |

## 📂 Project Structure

```text
task4-rule-based-chatbot/
├── chatbot.py        # Core script with state management and regex logic
└── sample_faq.json   # Dataset: greetings and FAQs
```

The dataset covers greetings and FAQs on hours of operation, project submission, and certificate issuance.

## 🚀 How to Run

1. **Open** your terminal or command prompt.

2. **Navigate to the project directory** (if not already there)
   ```bash
   cd task4-rule-based-chatbot
   ```

3. **Run the script**
   ```bash
   python chatbot.py
   ```

4. **Start chatting!** Try asking:
   - `What are your hours?`
   - `How do I submit my internship project?`
   - `When will I receive my certificate?`

## 💬 Sample Conversation

```text
You: Hi
Bot: Hello! How can I help you today?

You: What are your hours?
Bot: <your bot's actual reply here>

You: bye
Bot: Goodbye! Have a great day!
```

> Replace the sample replies with your chatbot's real output so the README matches the code.

## 👩‍💻 Author

**Tahmina Khan Nipa**

- GitHub: [@TahminaKhanNipa10-Codes](https://github.com/TahminaKhanNipa10-Codes)
- Datheon Batch: 01

---

<div align="center">⭐ If you found this useful, consider giving it a star!</div>
