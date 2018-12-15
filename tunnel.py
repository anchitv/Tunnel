import os.path
import sys
from collections import deque

# Code for inputs and checking inputs are correct.
input_file = input('Please enter the name of the file you want to get data from: ')
if not os.path.exists(input_file):
    print(f'Sorry, there is no such file.')
    sys.exit()

value = open(input_file).read().strip().split('\n')

ceil = value[0].split()
floor = value[-1].split()
ceil_len = len(ceil)
floor_len = len(floor)


try:
    ceil = [int(ceil[i]) for i in range(ceil_len)]
    floor = [int(floor[i]) for i in range(floor_len)]

except ValueError:
    print('Sorry, input file does not store valid data.')
    sys.exit()

if ceil_len < 2 or floor_len < 2 or ceil_len != floor_len or len(value) > 3:
    print('Sorry, input file does not store valid data.')
    sys.exit()


# Initializing variables.
distance_from_west = 1
max_distance = 0
initial_value = -1
ceil_list = deque([(ceil[0], 0)])
floor_list = deque([(floor[0], 0)])

# For loop to iterate over each element of ceiling and floor.
for i in range(1,len(ceil)):

    # If loop to check for valid input.
    if ceil[i] <= floor[i]:
        print('Sorry, input file does not store valid data.')
        sys.exit()

    # If loop to check if current ceiling element is less than the smallest ceiling element till now.
    if ceil[i] <= ceil_list[0][0]:
        ceil_list.clear()
        ceil_list.append([ceil[i], i])
        floor_list.append([floor[i], i])
        while ceil_list[0][0] <= floor_list[0][0]:
            initial_value = floor_list[0][1]
            floor_list.popleft()

    else:
        ceil_list.append([ceil[i], i])

    # If loop to check if current floor element is larger than the largest floor element till now.
    if floor[i] >= floor_list[0][0]:
        floor_list.clear()
        ceil_list.append([ceil[i], i])
        floor_list.append([floor[i], i])
        while ceil_list[0][0] <= floor_list[0][0]:
            initial_value = ceil_list[0][1]
            ceil_list.popleft()

    else:
        floor_list.append([floor[i], i])

    # Max Distance travelled by the ray.
    max_distance = max(max_distance, (i - initial_value))

    # If loop for the distance from west.
    if initial_value == -1:
        distance_from_west = i - initial_value

# Print statements.
print(f'From the west, one can see into the tunnel over a distance of {distance_from_west}.')
print(f'Inside the tunnel, one can see into the tunnel over a maximum distance of {max_distance}.')
