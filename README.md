# 📁 PorteføljeBot

A simple chatbot that helps students reflect on their projects and build academic portfolios.  
Built with Streamlit and OpenAI's GPT-4o.

---

## ✅ Features

- 🧠 GPT-4o chatbot with a custom prompt focused on reflection and identity-building
- 📎 Upload your own project files:
  - PDF, DOCX, TXT, CSV, MD, PPTX, XLSX, HTML
- 🔍 Uses a shared vector store for reference material (e.g. example portfolios)
- 💬 Maintains full conversation memory within the session

---

## ⚙️ Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/portefoljebot.git
   cd portefoljebot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=sk-...
   ```

4.  Create a `prompt.txt` file with your custom prompt

4. Run the app:
   ```bash
   streamlit run app.py
   ```

---

Thanks for the screenshot! Based on your actual project structure, here’s the updated `📂 Structure` section for the `README.md`:

---

## 📂 Project Structure

```
PortfolioBot/
├── src/
│   ├── app.py           # Streamlit UI
│   └──main.py           # Backend logic (OpenAI call, file parsing)
│ 
├── prompt.txt           # System prompt used by the assistant
├── .env                 # OpenAI API key
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 🛠 Requirements

- Python 3.9+
- OpenAI Python SDK
- Streamlit
- PyPDF2, python-docx, python-pptx, openpyxl, beautifulsoup4

---

## 🔐 Notes

- Uploaded files are only used during the active chat session.
- Shared vector store data is static and anonymized.

