import random
from decimal import Decimal
import datetime

from Agents import Investor, Specialist, Rule
from Market import MarketInfo
from Simulation import Simulation
import numpy as np

param = {"genetic_param": 0.9,
         "param": "valor_do_param"}

# number_agents = 100
# a = Simulation(25, 20)
# a.initialiaze_agents()
# pri = a.MainSimulation(progress=True, price_setting='clearing')


if __name__ == '__main__':
    for k, name in enumerate(["All Tehcnical", "All Fundamental"]):
        agent_0 = []
        others = []
        for i in range(10):
            random.seed(i)
            sim = Simulation(5, 1000)
            a, o = sim.MainSimulation(progress=1, price_setting='auction', new_agents=True, mode=k)
            agent_0.append(a)
            others.append(o)
        agent_0, others = np.array(agent_0), np.array(others)
        agent_0_mu, agent_0_sig, others_mu, others_sig = np.mean(agent_0, axis=0), np.std(agent_0, axis=0), np.mean(others, axis=0), np.std(others, axis=0)
        print(name)
        print(f"Agent 0 returns: {agent_0_mu} {agent_0_sig}")
        print(f"Others returns: {others_mu} {others_sig}")
        print("----------------------")
        print("")



        



