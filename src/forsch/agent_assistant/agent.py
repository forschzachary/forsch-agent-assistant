"""assistant agent definition."""

from google.adk import Agent

agent = Agent(
    name="assistant_agent",
    model="gemini-2.5-flash",
    instruction="You are the assistant team lead for Forsch.",
)
