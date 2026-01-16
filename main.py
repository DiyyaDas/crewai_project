#!/usr/bin/env python
# src/my_project/main.py
import sys
from  crew import LatestAiDevelopmentCrew,LLM 

from dotenv import load_dotenv
load_dotenv()

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI Agents'
    }
    llm = LLM(
        model="groq/llama3-8b-8192",
        temperature=0.3
    )
    crew = LatestAiDevelopmentCrew().crew()
    crew.kickoff(inputs=inputs)

if __name__ == "__main__":
    print("Starting CrewAI...")
    run()