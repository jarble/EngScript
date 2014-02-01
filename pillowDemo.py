#Use webcolors to convert color names to RGB values, and vice-versa.

'''
http://stackoverflow.com/questions/9694165/convert-rgb-color-to-english-color-name-like-green
'''


from PIL import Image
import webcolors
import numpy

#This is implemented
def magnify1DArray(theArray, scaleFactor):
	theNewArray = []
	for current in range(0, len(theArray)):
		for current1 in range(0, scaleFactor):
			theNewArray += [theArray[current]]
	return theNewArray

print(magnify1DArray([1,3,2,2], 3))

def magnify2DArray(theArray, scaleFactor):
	theNewArray = []
	for current in theArray:
		print(current)
		print(magnify1DArray(current, scaleFactor))
		for current1 in range(0, len(theArray)+1):
			theNewArray += [magnify1DArray(current, scaleFactor)]
	return theNewArray

print(magnify2DArray([[0,1],[9,2]], 3))

def makeImage(my_list, imageName):
	listDimensions = numpy.array(my_list).shape
	for i in range(0, len(my_list)):
		for j in range(0, len(my_list[i])):
			my_list[i][j] = webcolors.name_to_rgb(my_list[i][j])
	new_list = []
	for current in my_list:
		new_list += current

	img = Image.new('RGB', (listDimensions[1], listDimensions[0]))
	img.putdata(new_list)
	img.save(imageName)

makeImage([["green", "blue", "orange"], ["blue", "green", "orange"]], "my_image1.png")

newArray = []
for current in range(0, 10):
	newArray += [[]]
	for current1 in range(0, 10):
		theColor = "red"
		theNumber = (current*3 ** current1*5)%2
		if(theNumber == 0):
			theColor = "blue"
		newArray[current] += [theColor]
makeImage(newArray, "checkerboardPattern.png")
