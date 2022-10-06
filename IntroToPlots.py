# importing the required module
import matplotlib.pyplot as plt
  
# x axis values (Voltage V)
x = [9.019,7.96,5.59,3.67,2.51,1.88,0.842]
# corresponding y axis values (Resistance kohms)
y = [9.25,8.33,5.9,3.97,2.83,1.99,0.9]
  
# plotting the points 
plt.plot(x, y)
  
# naming the x axis
plt.xlabel('Voltage (V)')
# naming the y axis
plt.ylabel('Resistance (Ohms)')
  
# giving a title to my graph
plt.title('Voltage vs. Measured Resistance (for the Potentiometer Experiment)')
  
# function to show the plot
plt.show()