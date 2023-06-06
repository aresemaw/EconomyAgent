# Economic Simulation

This is a Python program that simulates an economic scenario using a simple agent-based model. The program consists of three main components:

1. **Agent Class**: The `Agent` class represents an economic agent and has the following attributes:
   - `goods`: The value of goods owned by the agent.
   - `vip`: The balance in the agent's VIP account.
   - `wage`: The monthly wage received by the agent.
   - `rent`: The monthly rent paid by the agent.

   The class also contains methods to simulate agent behavior, such as spending money, paying off debt, paying rent, and receiving wages.

2. **Model Class**: The `Model` class represents the economic model and contains a list of agents. It has the following functionalities:
   - Adding agents to the model.
   - Simulating the economy by iterating over the agents and simulating their behavior.
   - Setting the weekend flag to determine the agent's spending behavior.
   
3. **GUI Class**: The `GUI` class provides a graphical user interface to interact with the economic simulation model. It uses the Tkinter library to create a window and display agent information. The GUI includes the following components:
   - A label to display the title of the agent information section.
   - A text box to display detailed information about each agent.
   - A button to start the simulation.
   
The program creates an instance of the `Model` class, adds multiple agents to the model, and performs a simulation for three months. After the simulation, it prints information about the agents to the console. It then creates an instance of the `GUI` class, passing the model as a parameter, and runs the GUI.

## How to Use

To use this program, follow these steps:

1. Install Python: Make sure you have Python installed on your system.

2. Install Tkinter: If you don't have Tkinter installed, you can install it using the appropriate package manager for your operating system.

3. Set up the environment: Copy the code into a Python file (e.g., `economic_simulation.py`).

4. Run the program: Execute the Python file using the command `python economic_simulation.py` in a terminal or command prompt.

5. GUI Interaction: Once the GUI window appears, click the "Start Simulation" button to run the simulation. After the simulation finishes, the agent information will be displayed in the text box.

Note: You can modify the program by changing the initial agent attributes, adding or removing agents, adjusting simulation parameters, or enhancing the GUI as needed.

## Requirements

This program requires Python and the following libraries:
- `random`
- `decimal`
- `tkinter`

Make sure you have these libraries installed before running the program.
