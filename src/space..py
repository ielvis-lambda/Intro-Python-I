#Declaring a class, sorta like a template or a model for objects of this type
class Space: f.y = y

		#TODO: name, character



class Space: 
	def __init__(self, width, height):
		# TODO: allocated 2D lists to hold space

		#Going to contain all the rows
		self.space = []

		# making rows
		for i in range(height):
			row = ['.'] * width
			self.space.append(row)

		# print(self.space)

		# making stars
		for i in range(10):
			rowNum = random.randint(0, height - 1)
			colNum = random.randint(0, width -1)

			self.space[rowNum][colNum] = '*'

		# TODO: add random stars
	
	#TODO methods
	def print_map(self, player):
		print(f'Player is at {player.x}, {player.y}')

		for rowNum in range(len(self.space)):
			for colNum in range(len(self.space[rowNum])):

				if player.x == colNum and player.y == rowNum:
					char = 'Y'
				else: 
					char = self.space[rowNum][colNum]

				#ends the row with nothing
				print(f'{char} ', end='')
			print()

	#override the str method to print a nice string... what? 
	def __str__(self):
		s = ""	

		for row in self.space:
			s+= " ".join(row) + "\n"

		return s	

# instantiating or creating the object, self is automatically populated
s = Space(15, 10)

# print(s)

# the double slash is an integer divide which returns and integer after it divides (to start in the middle of the map)
p = Player(15 // 2, 10 // 2)

# passing in the player
while True: 

	s.print_map(p)
	dir = input(">> ")
	# print(dir)

	if dir == 'n':
		p.y -= 1
	elif dir == 's':
		p.y += 1
	elif dir == 'w':
		p.x -= 1
	elif dir == 'e':
		p.x += 1	

		