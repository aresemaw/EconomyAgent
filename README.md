# Economy Agent

## Background

This Python program creates a simulated economy with agents that represent shoppers, a shop owner, and a wage. The shop owner is responsible for paying rent, which is a fixed cost, and a wage, which represents a tax on the shop's profits. The shoppers are classified as VIPs, and they receive a 10% credit on their purchases. The output of the program shows the wage and rent expenses, as well as the total amount spent by the shoppers.

To use the program, the user creates a Model object and adds Agent objects to it using the add_agent method. The Agent objects represent the shop owner and the VIP shoppers. The user can then simulate the economy by calling the simulate method on the Model object. If desired, the user can set the weekend to True using the set_weekend method, which will cause the simulate method to increase the amount spent by the shoppers. Finally, the user can access the attributes of the Agent objects in the Model object to see the wage and rent expenses, as well as the total amount spent by the shoppers.

 The Agent class represents a person who has certain attributes such as goods, a VIP account, rent, and a wage. It also has methods for spending money on the VIP account, paying off debt on the VIP account, and paying rent and wage.

The Model class represents a model of an economy, and it has a list of Agent objects. It has a method for adding an Agent object to the list, a method for simulating the economy by having each Agent object spend and pay off debt, and a method for setting whether the current day is a weekend. The simulate method calls the spend and pay_debt methods of each Agent object, and the amount spent or paid off is determined by a random value generated using the random.uniform function.

Finally, the code creates a Model object and adds three Agent objects to it. It then simulates the economy and sets the weekend to True, simulating the economy again. It then iterates over the Agent objects in the Model and prints their attributes.
