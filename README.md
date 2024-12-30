# Financial and Web Search Agents Playground

This repository contains a Python-based application that uses the `PHIDATA` library and `GROQ` to create and serve agents for web and financial data search. It features a playground with two specialized agents:

1. **Web Search Agent**: Searches the web for general financial information using DuckDuckGo.
2. **Financial Search Agent**: Retrieves detailed stock and financial data using YFinance tools.

---

## Features
- **Web Search Agent**: Provides financial information from the web, displaying sources.
- **Financial Search Agent**: Displays stock prices, analyst recommendations, fundamentals, and news in tabular format.
- Interactive Playground UI for testing and using agents.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Priyam-28/agentic-ai.git
   cd your-repo-name

2. Set up a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate      # For Linux/Mac
    venv\Scripts\activate 
            # For Windows
3. Install dependencies:
    ```bash
    pip install -r requirements.txt

4. Set up environment variables:
    Create a .env file in the project root and add your API key:

    PHI_API_KEY=your_phi_api_key
