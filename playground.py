from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo


import phi
from phi.playground import Playground,serve_playground_app

import os
from dotenv import load_dotenv
load_dotenv()
phi.api=os.getenv("PHI_API_KEY")
# openai.api_key = os.getenv("OPENAI_API_KEY")

web_search_agent= Agent(
    name="Web Search Agent",
    role="Search the web for financial information",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()], 
    instructions=["Always search for the latest information and include sources"],
    show_tool_calls=True,
    markdown=True,
)

financial_search_agent= Agent(
    name="Financial Search Agent",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True,company_news=True)], 
    instructions=["Use Tables to display the information"],
    show_tool_calls=True,
    markdown=True,
)

app=Playground(agents=[financial_search_agent, web_search_agent]).get_app()
if __name__ == "__main__":
    serve_playground_app("playground:app",reload=True)



