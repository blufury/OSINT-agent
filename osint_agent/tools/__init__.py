from osint_agent.tools.tavily_tool import tavily_search
from osint_agent.tools.github_tool import github_lookup
from osint_agent.tools.news_tool import news_search
from osint_agent.tools.whois_tool import whois_lookup

ALL_TOOLS = [tavily_search, github_lookup, news_search, whois_lookup]
