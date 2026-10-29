
import os.path
import sys

sys.path.append(os.path.abspath(os.path.join(os.getcwd(),  "src/")))

from MAS.agents.core.Agents.CAgent import CAgent



if __name__ == "__main__":
    pass
    agent = CAgent()
    agent.call_api()