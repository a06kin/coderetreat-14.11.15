import unittest

arr = [[]]

def setUp():
	return [[0,0,0],
	[0,16,0],
	[0,0,0]]

[[1,0,0],
	[0,0],
	[0,0,0]]

arr = setUp()
print arr

def checkBorders(i, j, arr):
	if (i < 0 or j < 0 or len(arr) >= i or len(arr[0]) >= j):
		return 1
	else:
		return 0

def addOne(i, j, arr):
	if checkBorders(i, j, arr):
		arr[i][j] += 1

for i, iVal in enumerate(arr):
	for j, jVal in enumerate(iVal):
		if jVal == 16:
			addOne(i-1, j-1, arr)
			addOne(i-1, j, arr)
			addOne(i-1, j+1, arr)

			addOne(i, j+1, arr)
			addOne(i, j-1, arr)

			addOne(i+1, j-1, arr)
			addOne(i+1, j, arr)
			addOne(i+1, j+1, arr)

print arr

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.a = [[0,0,0],
			[0,16,0],
			[0,0,0]]
