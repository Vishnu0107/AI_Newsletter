# To know more about the Task class, visit: https://docs.crewai.com/concepts/tasks
from crewai import Task
from textwrap import dedent
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")

"""
Creating Tasks Cheat Sheet
- Begin with the end in mind. Identify the specific outcomes your tasks are aiming to achieve.
- Break down the outcome into actionable tasks, assigning each task to the appropriate agent.
- Ensure tasks are descriptive, providing clear instructions and expected deliverables.

Goal: 
- Develop a detailed itinerary , including city selection, attractions, and practical travel advice.

Key Steps for Task Creation:
1. Identify the desired outcome: Define what success looks like for your project.
    - A detailed 7-day travel itinerary 

2. Task Breakdown: Divide the goal into smaller, manageable tasks that agents can execute.
    - Itenerary Planning: develop a detailed plan for each day of the trip.
    - City Selection: Analyze and pick the best cities to visit.
    - Local Tour Guie: Find a local expert to provide insights ad recommendations.

3. Assign Tasks to Agents: Match tasks with agents based on their roles and expertise.

4.Task Description Template:
    - Use this template as a guide to define each task in your CrewI application.
    - This template helps ensure that each task is clearly defined, actionable, and aligned with the specific goals of your project.

Template:
---------

def [task_name](self, agent, parameters):
    return Task(description = dedent(f'''
    **Task**: [Provide a concise name or summary of the task.]
    **Description**: [Provide a detailed description of the task, including any specific instructions or requirements.]

    **Paramters**:
    - [Parameter 1]: [Description]
    - [Parameter 2]: [Description]
    ... [Add more parameters as needed.]

    **Note**: [Optional section for incentives or encouragement for high-quality work. This can include tips, bonuses, or other rewards.]
    '''), agent = agent)

"""

class AINewsLetterTasks:
    def fetch_news_task(self, agent):
        return Task(
        description = f'Fetch top AI news stories and technical AI news stories like updates in new AI packages and forums from the past 24 hours. The current time is {datetime.now()}',
        agent = agent,
        async_execution = True,
        expected_output = """
        A list of top AI news story titles, URLs, and a brief summary for each story 
        Example Output:
        [
            {
                'title' : 'AI takes spotlight in food commercials',
                'url' : 'https://example.com/story1',
                'summary' : 'AI made a splash in this year\'s flight commercials ...'
            },
            {{...}}
        ]
        """
    )

    def analyze_news_task(self, agent, context):
        return Task(
            description = f'Analyze each news story and ensure there are atleast 5 well-formatted articles',
            agent = agent,
            async_execution = True,
            context = context,
            expected_output = """
           A markdown-formatted analysis for each news story, including a rundown, detailed bulletins and a "Why it matters" section. There should be atleast 5 articles, each following the proper format.
           Example Output:
           '## AI takes spotlight in food commercials\n\n
           ** The Rundown:
           ** AI made a splash this year\'s food commercials... \n\n
           ** The details:**\n\n
           - Microsoft\'s Copilot spot showcased its AI assistant...\n\n
           **Why it matters:**\n\n
           While AI-related ads have been rampant over the last year, food commercials have started to AI assistants in their ads ...
            """
    )

    def compile_newletter_task(self, agent, context, callback_function):
        return Task(
            description = f'Compile the newsletter',
            agent = agent,
            context = context,
            async_execution = True,
            expected_output = """
            A complete newsletter in markdown format, with a consistent style and layout.
            Example Output:
            ## Top stories in AI today:\\n\\n
            - AI takes spotlight in food commercials\\n
            - Altman seeks TRILLIONS for global AI chip initiatives\\n\\n

            ## AI takes spotlight in food commercials\\n\\n
            **The Rundown:** AI made a splash in this year\'s food commercials...\\n\\n
            **The details:** ...\\n\\n
            **Why it matters:** ...\\n\\n

            ## Altman seeks TRILLIONS for global AI chip initiatives\\n\\n
            **The Rundown:** OpenAI CEO Sam Altman is reportedly angling to raise TRILLIONS of dollars...\\n\\n
            **The details:** ...\\n\\n
            **Why it matters:** ...\\n\\n
            """,
            callback_function = callback_function
    )
    
