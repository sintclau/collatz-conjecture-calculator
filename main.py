import math
import numpy as np
import matplotlib.pyplot as plt

counter = 0
print("Please enter a natural number:")
n = int(input())
axisX = []
axisY = []
plt.ylabel("Hailstone numbers")
plt.xlabel("Calculations")
plt.title("Collatz Conjecture Graph")

def main():
    global counter
    global n
    axisX.append(n)
    # f(x)=n/2 for n%2=0 and f(x)=3*n+1 for n%2!=0
    highestNumberAchieved = 0
    while n > 1:
        if n % 2 != 0:
            n = (3 * n) + 1
            axisX.append(n)
        else:
            n = n / 2
            axisX.append(n)
        counter += 1
        if n > highestNumberAchieved:
            highestNumberAchieved = n
        print(str(counter) + " -> " + str(n))
    if n == 1:
        print("The total number of calculations: " + str(counter))
        print("The highest number achieved is: " + str(highestNumberAchieved))
        axisY = list(range(1, counter + 2))
        plt.plot(axisY, axisX)
        plt.grid(True)
        plt.show()
    return 0

if __name__ == "__main__":
    main()