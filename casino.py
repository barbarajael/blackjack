from game import Game
from player import Player
from randomplayer import RandomPlayer
from student import StudentPlayer

if __name__ == '__main__':
    '''
    players = [StudentPlayer("Human",100000)]

    for i in range(500):
        for j in range(10000):
            print(players)
            g = Game(players, min_bet=1, max_bet=25) 
            #g = Game(players, debug=True)
            g.run()

    print("OVERALL: ", players)


    '''
    players = [StudentPlayer("Human",100), RandomPlayer("Bot", 100)]
    counter = 0

    for j in range(5000):
        print(players)
        g = Game(players, min_bet=1, max_bet=5) 
        #g = Game(players, debug=True)
        g.run()
        if str(g.winner) == "[Human]":
            counter += 1

    print("OVERALL: ", players)
    print("Games won: ", counter)
    