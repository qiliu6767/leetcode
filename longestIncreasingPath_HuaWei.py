import operator

def longestIncreasingPath(matrix):
	'''
	Args:
		matrix: List[List[int]]

	Return:
		an integer representing the longest increasing path
	'''
	# Number of rows of matrix
	h = len(matrix)
	if h == 0:
		return 0
	# Number of columns of matrix
	w = len(matrix[0])

	# A sorted list with element (i, j, val)
	# where (i, j) represents the location
	# and val represents the corresponding number
	slist = sorted([(i, j, val)
					 for i, row in enumerate(matrix)
					 for j, val in enumerate(row)],
					key = operator.itemgetter(2))
	print(slist)

	# Initialize a helper List[List[int]]
	# with the same shape of matrix
	dp = [[1]*w for _ in range(h)]

	for x, y, val in slist:
		for dx, dy in zip([1, 0, -1, 0], [0, 1, 0, -1]):
			nx, ny = x+dx, y+dy # Loop over moving right, up, left and down
			if 0 <= nx < h and 0 <= ny < w and matrix[nx][ny] > matrix[x][y]:
				dp[nx][ny] = max(dp[nx][ny], dp[x][y]+1)

	return max([max(x) for x in dp])



# Test
matrix = [[3, 4, 5],
		  [3, 2, 6],
		  [2, 2, 1]]
print(longestIncreasingPath(matrix))
