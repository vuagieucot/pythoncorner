class RPS:
    def __init__(self, gameId):
        self.id = gameId
        self.move1 = False
        self.move2 = False
        self.ready = False
        self._moves = [None, None]
        self.wins = [0,0]
        self.ties = 0

    def get_player_move(self, p):
        return self._moves[p]

    def play(self, player, move):
        self._moves[player] = move
        if player == 0:
            self.move1 = True
        else:
            self.move2 = True

    def connected(self):
        return self.ready

    def bothPick(self):
        return self.move1 and self.move2

    def winner(self):
        p1 = self._moves[0].upper()[0]
        p2 = self._moves[1].upper()[0]

        if p1 == 'R' and p2 == 'S':
            winner = 0
        elif p1 == 'S' and p2 == 'R':
            winner = 1
        elif p1 == 'P' and  p2 == 'R':
            winner = 0
        elif p1 == 'R' and p2 == 'P':
            winner = 1
        elif p1 == 'S' and p2 == 'P':
            winner = 0
        elif p1 == 'P' and p2 == 'S':
            winner = 1
        else: winner = -1

        return winner

    def resetMove(self):
        self.move1 = False
        self.move2 = False