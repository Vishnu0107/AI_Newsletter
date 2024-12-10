from crewai import Agent
from textwrap import dedent
from langchain.chat_models import ChatOpenAI
from search_tools import SearchTools
from dotenv import load_dotenv
import os
import warnings
warnings.filterwarnings("ignore")

load_dotenv()
class AINewsLetterAgent:
    def __init__(self):
        self.miss = ChatOpenAI(model_name="miss_stress", base_url=os.getenv("MISS"), api_key=os.getenv("MISS_KEY"))

    def editor_agent(self):
        return Agent(
            role="Editor",
            backstory=dedent(f"""
                            With a keen eye for detail and a passion for storytelling, you ensuer that the AI newsletter 
                            not only informs but also engages and inspires the readers. 
                            """),
            goal=dedent(f"""
                       Oversee the creation of the AI Newsletter
                        """),
            max_iter = 15,
            verbose=True,
            allow_delegation = True,
            llm=self.miss,
        )

    def news_fetcher_agent(self):
        return Agent(
            role="NewsFetcher",
            backstory=dedent(f"""
                            As a digital sleuth, you scour the internet for the latest and most impactful developments in the world of AI,
                            ensuring that our readers are always in the know.
                            """),
            goal=dedent(f"""
                       Fetch the top AI news stories for the day
                        """),
            tools=[SearchTools.search_internet],
            verbose=True,
            allow_delegation = True,
            llm=self.miss,
        )

    def news_analyzer_agent(self):
        return Agent(
            role="NewsAnalyzer",
            backstory=dedent(f"""
                            With a critical eye and a knack for distilling complex information, your job is to
                                analyze AI news stories and make them accessible and engaging to the audience.
                            """),
            goal=dedent(f"""
                        Analyze each new story and generate a detailed markdown summary   
                        """),
            tools=[SearchTools.search_internet],
            verbose=True,
            allow_delegation = True,
            llm=self.miss,
        )

    def newsletter_compiler_agent(self):
        return Agent(
            role="NewsletterCompiler",
            backstory=dedent(f""" 
                            As the final architect of the newsletter, you meticulously arrange a coherent and visually appealing presentation
                             that captivates our reader. Make sure that the newsletter maintains the consistency.
                            """),
            goal=dedent(f"""
                        Compile the analyzed AI news stories into a final newsletter format
                        """),
            verbose = True,
            llm = self.miss,
        )
    
