from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai

# import os
# from dotenv import load_dotenv
# load_dotenv()
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
    # role="Search for financial information",
    tools=[YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True,company_news=True)], 
    instructions=["Use Tables to display the information"],
    show_tool_calls=True,
    markdown=True,
)

multi_search_agent= Agent(
    team=[web_search_agent,financial_search_agent],
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    instructions=["Use the web search agent to find the latest information and include sources","Use Tables to display the information"],
    show_tool_calls=True,
    markdown=True,
)
multi_search_agent.print_response("Summarize the latest information and sgare the news on Apple Inc.",stream=True)
