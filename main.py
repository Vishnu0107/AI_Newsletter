from crewai import Crew, Process
from agents import AINewsLetterAgent
from tasks import AINewsLetterTasks
from dotenv import load_dotenv
from file_io import save_markdown
import warnings
warnings.filterwarnings("ignore")
load_dotenv()
# Install duckduckgo-search for this example:
# !pip install -U duckduckgo-search



# search_tool = DuckDuckGoSearchRun()

# os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")
# os.environ["OPENAI_ORGANIZATION"] = config("OPENAI_ORGANIZATION_ID")

# This is the main class that you will use to define your custom crew.
# You can define as many agents and tasks as you want in agents.py and tasks.py


class AINewsLetterCrew:
    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = AINewsLetterAgent()
        tasks = AINewsLetterTasks()

        # Define your custom agents and tasks here
        editor = agents.editor_agent()
        news_fetcher = agents.news_fetcher_agent()
        news_analyzer = agents.news_analyzer_agent()
        newletter_compiler = agents.newsletter_compiler_agent()

        # Custom tasks include agent name and variables as input
        fetch_news_task = tasks.fetch_news_task(news_fetcher)
        analyzed_news_task = tasks.analyze_news_task(news_analyzer, [fetch_news_task])
        compile_newsletter_task = tasks.compile_newletter_task(newletter_compiler, [analyzed_news_task], save_markdown)


        # Define your custom crew here
        crew = Crew(
            agents=[editor, news_fetcher, news_analyzer, newletter_compiler],
            tasks=[fetch_news_task, analyzed_news_task, compile_newsletter_task],
            process = Process.sequential,
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    results = AINewsLetterCrew()

    print("Crew results:")
    print(results.run())