import numpy as np
import string
from itertools import islice

#Lowercase item types a through z have priorities 1 through 26.
#Uppercase item types A through Z have priorities 27 through 52.
#Task 1: matching char from first and second half of line, 
#then priority = ? then sum up all priorities.
#Task2: group lines in bathces of 3. Find shared char in each batch, then return sum of 
#priorities of each batch. 

# Use a list comprehension to create the lists in one line
lowercase_letters_list = [ch for ch in string.ascii_lowercase]
uppercase_letters_list = [ch for ch in string.ascii_uppercase]



def get_priority(input_letter): #input will be shared_letter
	if input_letter.islower():
		#check to see which letter it lines up with
		#get (index+1) to get the priority
		index = lowercase_letters_list.index(input_letter)
		points = index + 1
	
	else:
		index = uppercase_letters_list.index(input_letter)
		points = index + 27

	return points


def return_priority_sum(input_file):
	with open(input_file, "r") as file:

		priority_sum = 0

		for line in file: 
			line = line.strip()
			line_length = len(line)  #number of letters in each line
			mid = line_length // 2

			first_half = line[:mid]
			second_half = line[mid:]

			#convert to a set to use intersection()
			first_half = set(first_half)
			second_half = set(second_half)

			shared_letter = first_half.intersection(second_half)

			#convert to list
			shared_letter = list(shared_letter)
			# Use the join method to concatenate the elements of the list into a string
			shared_letter_as_string = "".join(shared_letter)
			#print(shared_letter_as_string)

			#now to calculate priorities (aka points) 
			priority = get_priority(str(shared_letter_as_string))
			#print(priority)

			priority_sum = priority_sum + priority

	return priority_sum



def return_badge_sum(input_file):
	with open(input_file, "r") as file:

		counter = 0
		three_lines = []
		badge_sum = 0
		priority_sum = 0

		lines = [line.strip() for line in file]

		for line in lines:
			#print(line)

			line_as_set = set(line)
			#print(line_as_set)

			three_lines.append(line_as_set)

			counter += 1

			#once we have our three lines as sets in a list 
			#compare them and return the char that is in common
			#get the priority of the char and add it to sum 
			#reset the counter to 0 and list to empty once we read 3 lines  
			if counter == 3:
				#print(three_lines)
				line1 = three_lines[0]
				line2 = three_lines[1]
				line3 = three_lines[2]

				shared_letter = line1.intersection(line2, line3)
				#print(shared_letter)

				#convert to list
				shared_letter = list(shared_letter)
				# Use the join method to concatenate the elements of the list into a string
				shared_letter_as_string = "".join(shared_letter)
				#print(shared_letter_as_string)

				#now to calculate badge priorities (aka points) 
				priority = get_priority(str(shared_letter_as_string))
				#print(priority)

				badge_sum = badge_sum + priority

				counter = 0
				three_lines = []

	return badge_sum



data = './data3.txt'


#task1
final_priority_sum = return_priority_sum(data)
print(final_priority_sum)

#task2
final_badge_sum = return_badge_sum(data)
print(final_badge_sum)


