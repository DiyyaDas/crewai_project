# src/my_project/crew.py
from crewai import Agent, Crew, Process, Task,LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
import os
import yaml
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load YAML configs
with open(os.path.join('config', 'agents.yaml')) as f:
    agents_config = yaml.safe_load(f)

with open(os.path.join('config', 'tasks.yaml')) as f:
    tasks_config = yaml.safe_load(f)

llm = LLM(
    model="groq/llama-3.1-8b-instant",
    temperature=0.3
)


@CrewBase
class LatestAiDevelopmentCrew():
    """LatestAiDevelopment crew"""
    agents: List[BaseAgent]
    tasks: List[Task]
    

    @agent
    def researcher(self) -> Agent:
        self.agents_config['researcher']['llm']=llm# assign first

        return Agent(
    config=self.agents_config['researcher'],
    verbose=True,
    llm=llm
)

        # return Agent(
        #     **self.agents_config['researcher']['llm'] = llm
        #     verbose=True,
        #     llm=llm
        #     # tools=[SerperDevTool()]
        # )

    @agent
    def reporting_analyst(self) -> Agent:
        self.agents_config['reporting_analyst']['llm']=llm
        return Agent(
            config = self.agents_config['reporting_analyst'],
            verbose=True,
            llm=llm
        )

    @task
    def research_task(self) -> Task:
        return Task(
            **self.tasks_config['research_task'],
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            **self.tasks_config['reporting_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the LatestAiDevelopment crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            llm=llm
        )