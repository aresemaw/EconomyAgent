import random
from decimal import Decimal, ROUND_DOWN , ROUND_HALF_UP
import tkinter as tk

class Agent:
    def __init__(self, goods, vip, rent, wage):
        self.goods = max(Decimal(goods).quantize(Decimal('0.01'), rounding=ROUND_DOWN), Decimal('0.00'))
        self.vip = max(Decimal(vip).quantize(Decimal('0.01'), rounding=ROUND_DOWN), Decimal('0.00'))
        self.wage = max(Decimal(wage).quantize(Decimal('0.01'), rounding=ROUND_DOWN), Decimal('0.00'))
        self.rent = max(Decimal(rent).quantize(Decimal('0.01'), rounding=ROUND_DOWN), Decimal('0.00'))

    def spend(self, amount):
        # Simulate agent spending by deducting money from VIP balance with a chance of overspending
        overspend = Decimal(random.uniform(1.0, 1.2)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        self.vip -= Decimal(amount) * overspend

    def pay_debt(self, amount):
        # Simulate agent paying off credit card debt with a chance of getting a discount
        discount = Decimal(random.uniform(0.9, 1.0)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        self.vip -= Decimal(amount) * discount

    def pay_rent(self, amount):
        # Simulate agent paying monthly rent with a chance of late payment and additional fee
        late_fee = Decimal(random.uniform(1.1, 1.2)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        self.vip -= Decimal(amount) * late_fee

    def receive_wage(self, amount):
        # Simulate agent receiving monthly wage with a chance of bonus
        bonus = Decimal(random.uniform(1.0, 1.1)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        self.vip += Decimal(amount) * bonus


class Model:
    def __init__(self):
        self.agents = []
        self.weekend = False

    def add_agent(self, agent):
        self.agents.append(agent)

    def simulate(self):
        for agent in self.agents:
            # Simulate agent spending
            if self.weekend:
                # Agents spend more on weekends, randomly determined within a range
                agent.spend(random.uniform(100, 200))
            else:
                agent.spend(random.uniform(50, 100))

            # Simulate agent paying off debt, randomly determined within a range
            agent.pay_debt(random.uniform(10, 50))

            # Simulate agent paying monthly rent
            agent.pay_rent(agent.rent)

            # Simulate agent receiving monthly wage
            agent.receive_wage(agent.wage)

    def set_weekend(self, value):
        self.weekend = value

# Create model and add agents
model = Model()

model.add_agent(Agent(goods=5000, vip=500, rent=500, wage=200))
model.add_agent(Agent(goods=6000, vip=600, rent=500, wage=200))
model.add_agent(Agent(goods=7000, vip=700, rent=500, wage=200))

# Simulate economy for multiple months
for month in range(3):
    # Set weekend and simulate
    model.set_weekend(True)
    model.simulate()

    # Set weekday and simulate
    model.set_weekend(False)
    model.simulate()

# Print information about agents
for i, agent in enumerate(model.agents):
    print(f"Agent {i+1}:")
    print(f"  VIP balance: ${agent.vip}")
    print(f"  Goods value: ${agent.goods}")
    print(f"  Rent value: ${agent.rent}")
    print(f"  Wage value: ${agent.wage}")

# GUI class
class GUI:
    def __init__(self, model):
        self.model = model

        # Create the main window
        self.root = tk.Tk()
        self.root.title("Economic Simulation")

        # Create and configure the GUI elements
        self.agent_info_label = tk.Label(self.root, text="Agent Information", font=("Helvetica", 20, "bold"))
        self.agent_info_label.pack()

        self.agent_info_text = tk.Text(self.root, width=60, height=20, font=("Helvetica", 14))
        self.agent_info_text.pack()

        self.start_button = tk.Button(self.root, text="Start Simulation", font=("Helvetica", 16), command=self.start_simulation)
        self.start_button.pack()

    def start_simulation(self):
        # Perform the simulation
        for month in range(3):
            self.model.set_weekend(True)
            self.model.simulate()

            self.model.set_weekend(False)
            self.model.simulate()

        # Update the GUI elements with simulation results
        self.update_agent_info()

    def update_agent_info(self):
        self.agent_info_text.delete(1.0, tk.END)
        self.agent_info_text.insert(tk.END, "Agent Information:\n\n")
        for i, agent in enumerate(self.model.agents):
            self.agent_info_text.insert(tk.END, f"Agent {i+1}:\n")
            self.agent_info_text.insert(tk.END, f"  VIP balance: ${agent.vip:.2f}\n")
            self.agent_info_text.insert(tk.END, f"  Goods value: ${agent.goods:.2f}\n")
            self.agent_info_text.insert(tk.END, f"  Rent value: ${agent.rent:.2f}\n")
            self.agent_info_text.insert(tk.END, f"  Wage value: ${agent.wage:.2f}\n")
            self.agent_info_text.insert(tk.END, "\n")

    def run(self):
        # Start the GUI main loop
        self.root.mainloop()

# Create model and add agents
model = Model()
model.add_agent(Agent(goods=5000, vip=500, rent=500, wage=200))
model.add_agent(Agent(goods=6000, vip=600, rent=500, wage=200))
model.add_agent(Agent(goods=7000, vip=700, rent=500, wage=200))

# Create the GUI instance
gui = GUI(model)

# Run the GUI
gui.run()
