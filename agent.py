import random

class Agent:
  def __init__(self, goods, vip,rent,wage):
    self.goods = goods
    self.vip = vip
    self.wage = wage
    self.rent = rent

  def spend(self, amount):
    # spend money on credit card
    self.vip += amount

  def pay_debt(self, amount):
    # pay off credit card debt
    self.vip -= amount
  def rent(self, amount):
    # spend money on credit card
    self.vip += amount
  def wage(self, amount):
    # pay off credit card debt
    self.vip -= amount

class Model:
  def __init__(self):
    self.agents = []
    self.weekend = False

  def add_agent(self, agent):
    self.agents.append(agent)

  def simulate(self):
    for agent in self.agents:
      # simulate agent spending
      if self.weekend:
        # agents spend more on weekends
        agent.spend(random.uniform(100, 200))
      else:
        agent.spend(random.uniform(50, 100))

      # simulate agent paying off debt
      agent.pay_debt(random.uniform(10, 50))

  def set_weekend(self, value):
    self.weekend = value

# create model and add agents
model = Model()

model.add_agent(Agent(goods=5000, vip=500,rent=500, wage=200))
model.add_agent(Agent(goods=6000, vip=600,rent=500, wage=200))
model.add_agent(Agent(goods=7000, vip=700,rent=500, wage=200))

# simulate economy
model.simulate()

# set weekend and simulate again
model.set_weekend(True)
model.simulate()
for agent in model.agents: