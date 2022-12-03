import numpy as np

data = open('./data1.txt', 'r')

#define a loop that goes through each line and sums values 
#add each line until empty line, save a elf_sum = []
#task1: return max value
#Task2: find top three values, what is the sum of those?

calorie_sum = 0
elf_sums = []

for line in data:
    if line!='\n':
        calorie_sum = calorie_sum + int(line)

    else:
        print(calorie_sum)
        elf_sums.append(calorie_sum) #adding current sum to zero
        calorie_sum = 0 #resetting calorie count to zero since we've hit an empty line
  
sorted_elves = np.sort(elf_sums)
print(sorted_elves)

top_three = sorted_elves[-1] + sorted_elves[-2] + sorted_elves[-3]
print(sorted_elves[-1], sorted_elves[-2], sorted_elves[-3])
print('top_three: ')
print(top_three)

# Closing files
data.close()
