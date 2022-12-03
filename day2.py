import numpy as np

# Opening file
data = open('./data2.txt', 'r')

#score for the shape you selected:
#(1 Rock, 2 Paper, 3  Scissors)
#plus the score for the outcome of the round:
#(0 lost, 3 draw, 6  won)

#A = rock 
#B = paper 
#C = scissors 

#A rock -draw  
#A paper -win 
#A scissors -lost  

#B rock -lose
#B paper -draw
#B scissors -win

#C rock -win
#C paper -lose
#C scissors -draw

#X means need to lose
#Y means need to draw 
#Z means need to win

rock_points = 1
paper_points = 2
scissor_points = 3

lose_points = 0
draw_points = 3
win_points = 6

#10835
#11164

def calculate_points(a,b):
	score = 0
	if a =='A' and b =='X': #need lose
		score = scissor_points + lose_points
	elif a =='A' and b =='Y': #need to draw
		score = rock_points + draw_points
	elif a =='A' and b =='Z': #need to win
		score = paper_points + win_points

	elif a =='B' and b =='X': #need to lose
		score = rock_points + lose_points
	elif a =='B' and b =='Y': #need to draw
		score = paper_points + draw_points
	elif a =='B' and b =='Z': #need to win
		score = scissor_points + win_points

	elif a =='C' and b =='X': #need to lose 
		score = paper_points + lose_points
	elif a =='C' and b =='Y': #need to draw
		score = scissor_points + draw_points
	elif a =='C' and b =='Z': #need to win
		score = rock_points + win_points
	else:
		print('something went wrong')

	return score #returns array of points 

all_letters = []
total_points = 0

for line in data: 
	line = line.strip().split(' ')
	print(line[0],line[1])
	point = calculate_points(line[0],line[1])
	print(point)
	total_points = total_points + point


print(total_points)
	


	
#print(total_points)     

data.close()


'''
	for letter in line:
		if line == '/n':
			print('empty line')
		else:
			print('letter: ' + letter)

	elf_hand = data.read(1)
	my_hand = data.read(2)
	#print(my_hand)
	#if elf_hand =='A':
		#print(elf_hand)
	#if my_hand == ' X':
		#print(my_hand)
'''

