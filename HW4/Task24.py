# A farm in Karelia grows blueberries. It grows on a round, and the bushes are planted only around the circumference.
# Thus, each bush has exactly two neighbors. In total, N bushes grow in the garden.
# These bushes have different yields, so by the time they are harvested, they have grown a different number of berries — ai berries have grown on the i-th bush.
# This farm has introduced an automatic blueberry picking system.
# This system consists of a control module and several collecting modules.
# The picking module in one run, being directly in front of a certain bush, collects berries from this bush and from two neighboring ones.
# Write a program to find the maximum number of berries that the picking module can collect in one run, being in front of some bush of the garden bed specified in the input file.

import random

array = []
max = 0
sum = 0
for i in range(5):
    array.append(random.randint(1, 10))

print(array)
for i in range(len(array)):
    sum = array[i - 2] + array[i - 1] + array[i]
    if (sum > max):
        max = sum

print(max)
