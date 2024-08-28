import matplotlib.pyplot as plt

# Example data
data = [1, 2, 3, 3, 4, 5, 5, 5, 6, 7, 7, 8, 8, 8, 8]

# Create histogram
plt.hist(data, bins=range(1, 10), edgecolor='black')

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')

# Show plot
plt.show()
