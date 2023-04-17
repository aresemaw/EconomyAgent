# Agent-Based Economic Simulation

## Background

This program simulates an economy with multiple agents. Each agent has a starting amount of goods and a VIP balance (which can be thought of as a credit card balance). Agents spend money randomly on each simulation step, and also pay off a random amount of debt.
 
  ## Usage
The Agent class represents an economic agent in the model, and has the following attributes:

goods: the value of goods owned by the agent
vip: the balance of the agent's virtual credit card
rent: the cost of the agent's rent
wage: the agent's weekly wage
The Model class represents the economic model, and has the following methods:

add_agent(agent): adds an Agent object to the model
simulate(): simulates the economy for one week
set_weekend(value): sets whether the current day is a weekend or not

 ## How to Use
To run the simulation, run the agent.py file in Python. You can adjust the parameters of the simulation by modifying the Agent class and the Model class in the code.

To add agents, create an instance of the Agent class and pass in the starting values for goods, VIP balance, rent, and wage. Then add the agent to the Model class using the add_agent method.

To run the simulation, call the simulate method of the Model class. You can also set the weekend property of the Model class to True to simulate higher spending on weekends.

After running the simulation, information about each agent's VIP balance, goods value, rent value, and wage value will be printed to the console.
To run the Python file, open a terminal or command prompt and navigate to the directory where the file is located. Then, run the following command:

### *python agent.py*


