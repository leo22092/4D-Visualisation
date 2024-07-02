import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_excel("C:\\Users\\shitosu\\Desktop\\prog\\GANN\\Ram\\Al.xlsx")
# print(data.head(5))

def map_values(value_list, new_min, new_max):
    # Find the minimum and maximum values in the original list
    min_val = min(value_list)
    max_val = max(value_list)

    # Map each value to the new range
    mapped_values = [((value - min_val) / (max_val - min_val)) * (new_max - new_min) + new_min for value in value_list]

    return mapped_values
def normalize_list(input_list):
    # Find the minimum and maximum values in the list
    min_val = min(input_list)
    max_val = max(input_list)

    # Normalize each value in the list
    normalized_list = [(x - min_val) / (max_val - min_val) for x in input_list]

    return normalized_list

########################
# AL
x=[300,300,300,400,400,400,600,600,600]
y=[300,400,600,300,400,600,300,400,600]
z=[0.2,0.4,0.6,0.4,0.6,0.2,0.6,0.2,0.4]
s=[1.648,1.121,1.061,1.305,1.497,0.115,0.268,1.435,1.361]
#######################
# SS
x=[300,300,300,400,400,400,600,600,600]
y=[300,400,600,300,400,600,300,400,600]
z=[0.2,0.4,0.6,0.4,0.6,0.2,0.6,0.2,0.4]
s=[1.824,1.503,2.053,2.271,5.134,0.061,1.492,0.687,0.479]
##############################
# CU
x=[300,300,300,400,400,400,600,600,600]
y=[300,400,600,300,400,600,300,400,600]
z=[0.2,0.4,0.6,0.4,0.6,0.2,0.6,0.2,0.4]
s=[0.475,0.186,1.526,1.583,0.512,1.757,1.021,1.358,0.567]

x=normalize_list(x)
y=normalize_list(y)

# size=result = [x * 20 for x in s]
size=map_values(s,10,80)


# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]
# z = [3, 6, 9, 12, 15]
# j=[8, 12, 8, 17, 19]
#

plt.plot(s, x, label='Train Accuracy')
plt.plot(s, y, label='Validation Accuracy')
plt.plot(s, z, label='Validation Accuracy')

# plt.xlabel('Epochs')
# plt.ylabel('Accuracy')
# plt.legend()
# plt.title('Training and Validation Accuracy')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Sample data

# Create a 3D figure
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# # Plot the scatter points
# ax.scatter(x, y, z)
#
# # Add labels and title
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# ax.set_title('3D Scatter Plot')
#
# # Show the plot
# plt.show()


####################
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]
# z = [3, 6, 9, 12, 15]
# s = [10, 20, 30, 40, 50]  # Fourth variable represented by marker size

# Create a 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the scatter points with varying marker size
ax.scatter(x, y, z, s=size)

# Add labels and title
ax.set_xlabel('Cutting Speed',color='green')
ax.set_ylabel('Feed',color='red')
ax.set_zlabel('Vertical step depth',color='blue')
ax.set_title('3D Scatter Plot for Spring Back(Cu)', fontweight='bold')

# Show the plot
plt.show()