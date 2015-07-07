class BoardManager(object):
	rows = 10
	columns = 10
	all_pieces = {
		'red':{
			'pieces':[],
		},
		'blue':{
			'pieces':[],
		}
	} 

	def __init__(self):
	
		for piece in Pieces.piece_dict.values():	
			for a_piece in xrange(piece['quantity']):
				self.all_pieces['red']['pieces'].append(piece)

		for piece in Pieces.piece_dict.values():
			for a_piece in xrange(piece['quantity']):
				self.all_pieces['blue']['pieces'].append(piece)

		self.build_sequential_board()

	def build_sequential_board(self):
		
		for piece in self.all_pieces['red']['pieces']:
			x, y = 0, 0

			while x <= 9 and y <= 3:
				self.all_pieces['red']['position'] = (x, y)

				if x < 9:
					x += 1
				elif x == 9:
					y += 1
					x = 0

		# for piece in self.all_pieces['blue']['pieces']:
		# 	x, y = 0, 6

		# 	while x <= 9 and y <= 9:
		# 		self.all_pieces['blue']['position']

		# 		if x < 9:
		# 			x += 1
		# 		elif x == 9:
		# 			y += 1
		# 			x = 0


		




class Pieces(object):
	piece_dict = {
	'10':{'name':'Marshal', 'quantity':1},
	'9':{'name':'General', 'quantity':1},
	'8':{'name':'Colonel', 'quantity':2},
	'7':{'name':'Major', 'quantity':3},
	'6':{'name':'Captain', 'quantity':4},
	'5':{'name':'Lieutenant', 'quantity':4},
	'4':{'name':'Sergeant', 'quantity':4},
	'3':{'name':'Miner', 'quantity':5},
	'2':{'name':'Scout', 'quantity':8},
	'S':{'name':'Spy', 'quantity':1},
	'B':{'name':'Bomb', 'quantity':6},
	'F':{'name':'Flag', 'quantity':1}
	}


def print_board():
	bm = BoardManager()
	board = ""
	for x in xrange(11):
		for y in xrange(11):
			#assign a piece
			for piece_id in bm.all_pieces['red']:
				piece = bm.all_pieces['red'][piece_id]
				if piece['position'][0] == x and piece['position'][1] == y:
					board = board + piece_id + " "
				else:
					board = board + "0 "
		print board
		board = ""

if __name__ == '__main__':
    
    print_board()
    
    