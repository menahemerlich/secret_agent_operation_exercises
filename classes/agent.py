
class Agent:
    total_agents = 0
    def __init__(self, code_name: str, clearance_level: int):
        self.code_name = code_name
        self._clearance_level = clearance_level
        Agent.total_agents += 1

    def report(self):
        print(f"Agent {self.code_name} reporting. Clearance Level: {self._clearance_level}")

    def getter(self):
        return self._clearance_level

    def setter(self):
        if 1 < self._clearance_level < 10:
            self._clearance_level = self._clearance_level

    @staticmethod
    def get_total_agents():
        print(Agent.total_agents)





