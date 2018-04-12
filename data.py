#encoding: utf8

'''
 Bárbara Jael (73241)
 Catarina Fonseca (75719)
 Miriam Cardoso (72181)
'''

# all data gathered + populate matriz data + save in file
class Data:
    def __init__(self):
        # making a matrix 22x22 <- range(23) goes from 0 to 22 points; anything >= 22 is "busted"
        self.data = [[EachPlay() for i in range(23)] for j in range(23)]

    # read file and populate matrix with data
    def readData(self):
        f = open('dataMatrix.txt', 'r')
        dataList = f.read()
        lines = dataList.split('\n')

        r = 0
        for i in range(23):
            for j in range(23):
                tokens = lines[r].split(' ')
                self.data[i][j] = EachPlay(int(tokens[1]), int(tokens[2]), int(tokens[3]))
                r += 1

    	f.close()


    # save populated matrix (data) into a file
    def writeData(self):
        newData = ""

        for i in range(23):
            for j in range(23):
                # construct new dataList with data that populated the matrix (data)
                newData += "[" + str(i) + "," + str(j) + "] " + str(self.data[i][j]) + "\n"

        f = open('dataMatrix.txt', 'w')
        f.write(newData)
        f.close()


# each element - what is learnt in each play
class EachPlay:
    def __init__ (self, h=0, s=0, u=0):
        self.hit = int(h)
        self.stand = int(s)
        self.surrender = int(u)

    def __str__ (self):
        return str(self.hit) + " " + str(self.stand) + " " + str(self.surrender)
