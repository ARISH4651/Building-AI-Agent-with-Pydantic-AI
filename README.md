# 🔎 GenAI Search Agent

This repository contains a simple yet powerful Generative AI Search Agent built with [Pydantic AI](https://github.com/pydantic/pydantic-ai), [Streamlit](https://streamlit.io/), and [Groq](https://groq.com/). The agent utilizes the **Llama 3.1** model and **Tavily Search** to provide real-time, accurate search results for user queries.

## 🚀 Features

- **Generative Search:** Uses an AI agent to search the web and synthesize answers.
- **Interactive UI:** Built with Streamlit for a clean and easy-to-use interface.
- **Powered by Groq:** Leverages the speed of Groq's Llama 3.1 model.
- **Tavily Integration:** accurate and reliable web search capabilities.

## 🛠️ Prerequisites

Before running the application, ensure you have the following:

- Python 3.9 or higher installed.
- **Groq API Key:** Get it from [Groq Cloud](https://console.groq.com/).
- **Tavily API Key:** Get it from [Tavily](https://tavily.com/).

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ARISH4651/Pydantic-ai-agent.git
   cd Pydantic-ai-agent
   ```

2. **Install dependencies:**
   It is recommended to use a virtual environment.
   ```bash
   pip install -r requirements.txt
   ```

## ⚙��� Configuration

1. Create a `.env` file in the root directory of the project.
2. Add your API keys to the `.env` file:

   ```env
   GROQ_API_KEY=your_groq_api_key_here
   TAVILY_API_KEY=your_tavily_api_key_here
   ```

   Alternatively, you can set these as environment variables in your system.

## ▶️ Usage

To run the application, execute the following command:

```bash
streamlit run app.py
```

The application will open in your default web browser. Enter your query in the input box and click **Search** to get results.

## 📂 Project Structure

- `app.py`: The main entry point for the Streamlit application. Handles the UI and user interaction.
- `agent_utils.py`: Contains the logic for initializing the Pydantic AI agent, configuring tools (Tavily), and handling API keys.
- `requirements.txt`: Lists the Python dependencies required for the project.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.