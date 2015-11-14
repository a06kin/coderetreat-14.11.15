# '*' array x,y
# 

matrix = []

def main():
	with open('input.in') as f:
		arr = f.read().split('\n')[:-1]
		stars = getAsterixIndex(arr)
		for el in stars:
			matrix.append(buildMatrix(arr, el))
		print output(matrix,stars)

def output(matrix, stars):
	strr = ''
	for line in summMatrix(matrix, stars):
		for sumb in line:
			strr += str(sumb)
		strr+= '\n'
	return strr

def getAsterixIndex(inn):
	arr = []
	for i, line in enumerate(inn):
		for j, _ in enumerate(line):
			if _ == '*':
				arr.append((i,j))
	return arr

def getSize(arr):
	return (len(arr), len(arr[0]))

def buildMatrix(arr, el):
	x, y = el
	res = []
	for i in range(getSize(arr)[0]):
		line = []
		for j in range(getSize(arr)[1]):
			line.append(1 if (i in (x-1, x, x+1)) \
				and (j in (y-1, y, y+1)) else 0)
		res.append(line)
	return res

def summMatrix(arr, stars):
	tmp = arr[0]
	height, width = getSize(tmp)
	for i in range(height):
		for j in range(width):
			for z in range(len(arr)):
				tmp[i][j] += arr[z][i][j]
	for x,y in stars:
		tmp[x][y] = '*'
	return tmp

if __name__ == '__main__':
	main()