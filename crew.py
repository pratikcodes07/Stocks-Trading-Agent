from crewai import Crew
from Tasks.analyze_task import get_stock_analysis
from Tasks.trade_task import trade_decision
from Agents.analyst_agent import analyst_agent
from Agents.trader_agent import trader_agent

stock_crew = Crew(
    agents=[analyst_agent,trader_agent],
    tasks=[get_stock_analysis,trade_decision],
    verbose=True
)