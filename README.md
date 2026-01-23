# GenAI Search Agent

A lightweight, powerful generative AI search tool that combines real-time web search with LLM synthesis. Built with Pydantic AI and Streamlit, it leverages Groq's Llama 3.1 for rapid inference and Tavily for accurate search results.

## Overview

This application serves as an intelligent search assistant. Instead of just returning a list of links, it performs a web search based on your query, analyzes the results, and synthesizes a direct, comprehensive answer using a Large Language Model (LLM).

## Features

- **Generative Search**: Synthesizes answers from multiple web sources rather than just listing links.
- **High-Performance AI**: Powered by Groq's Llama 3.1 model for near-instant inference speeds.
- **Accurate Retrieval**: Uses Tavily Search API for optimized, factual web scraping.
- **Clean UI**: Minimalist interface built with Streamlit for easy interaction.

## Tech Stack

- **Framework**: [Streamlit](https://streamlit.io/)
- **AI Agent**: [Pydantic AI](https://github.com/pydantic/pydantic-ai)
- **LLM Provider**: [Groq](https://groq.com/) (Llama 3.1)
- **Search Tool**: [Tavily AI](https://tavily.com/)
- **Language**: Python

## Installation

### Prerequisites
- Python 3.9 or higher
- A [Groq API Key](https://console.groq.com/)
- A [Tavily API Key](https://tavily.com/)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/ARISH4651/Pydantic-ai-agent.git
   cd Pydantic-ai-agent
