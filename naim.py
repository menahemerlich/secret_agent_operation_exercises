from classes.agent import Agent
from classes.field_agent import FieldAgent
from classes.cyber_agent import CyberAgent

agent_1 = Agent("Kodkode", 5)
agent_1.get_total_agents()
agent_2 = FieldAgent("Zamir", 2, "Tel Aviv")
agent_2.get_total_agents()
agent_3 = CyberAgent("Netz", 7, True)
agent_3.get_total_agents()

agent_list = [agent_3, agent_2, agent_1]
for agent in agent_list:
    agent.report()


