#encoding: utf8

'''
 script to make a matrix 22x22
    - range(23) goes from 0 to 22 points
 it goes 'till 22 because anything >= 22 points is "busted"
 the matrix is initialized with all probabilities at zero
'''

cleanData = ""

for i in range(23):
    for j in range(23):
        cleanData += "[" + str(i) + "," + str(j) + "] 0 0 0 \n"

f = open('dataMatrix.txt', 'w')
f.write(cleanData)
f.close()