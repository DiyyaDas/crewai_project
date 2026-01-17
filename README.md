🧠 Latest AI Development Crew (CrewAI Agent)

This project is a CrewAI-based autonomous agent system that researches the latest developments in AI Agents and generates a structured markdown report using multiple AI agents working collaboratively.

📌 Features

Multi-agent workflow using CrewAI
Research + reporting agents
Uses a free LLM (Groq – LLaMA 3.1)
Config-driven agents and tasks (YAML)
Generates a final report in Markdown format

🧰 Prerequisites

Before running this project, make sure you have the following installed:

1️⃣ Python (Required)

Python 3.10 or higher (Python 3.11 recommended)
Download Python:
👉 https://www.python.org/downloads/
⚠️ During installation:

✅ Check “Add Python to PATH”
✅ Install pip when prompted

2️⃣ Git (Optional but recommended)

Download from:
👉 https://git-scm.com/downloads

📁 Project Structure
crewai_project/
├── main.py
├── crew.py
├── config/
│   ├── agents.yaml
│   └── tasks.yaml
├── requirements.txt
└── README.md

🧪 Step 1: Create a Virtual Environment (Local Setup)

Open Command Prompt or VS Code Terminal in the project folder:
python -m venv .venv

Activate the environment:
.\.venv\Scripts\Activate.ps1

📦 Step 2: Install Dependencies

pip install --upgrade pip
pip install crewai groq litellm python-dotenv

🔑 Step 3: Set Up Free LLM (Groq)

This project uses Groq’s free LLaMA 3.1 model.
1️⃣ Create a Groq account
👉 https://console.groq.com
2️⃣ Generate an API key
3️⃣ Set the environment variable

Windows (CMD)
setx GROQ_API_KEY your_actual_api_key_here
Restart terminal after setting the key.
Verify:
echo %GROQ_API_KEY%

🤖 Step 4: Model Configuration

The project uses this free model internally:
model="groq/llama-3.1-8b-instant"
No OpenAI key, no paid models required.

▶️ Step 5: Run the Agent
python main.py

If successful, the crew will:

Research the topic
Analyze findings
Generate a Markdown report
Output file:
report.md

🛠 Common Issues & Fixes
❌ ModuleNotFoundError: crewai
✔ Ensure:
Virtual environment is activated
crewai is installed in .venv

❌ LLM connection error
✔ Fix:
Confirm GROQ_API_KEY is set
Use supported Groq models only

📌 Notes
.venv is not included in the repository
Environment variables are kept local for security
Configuration is fully editable via YAML files

📄 License
This project is for educational and research purposes.
