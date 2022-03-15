class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):     
        if player_name == self.player1_name: 
            self.m_score1 += 1
        else:
            self.m_score2 += 1

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self.even_score()
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            return self.advantage_score()
        else:
            return self.player_score(self.m_score1) + "-" + self.player_score(self.m_score2)
    
    def even_score(self):
        if self.m_score1 == 0:
            score = "Love-All"
        elif self.m_score1 == 1:
            score = "Fifteen-All"
        elif self.m_score1 == 2:
            score = "Thirty-All"
        elif self.m_score1 == 3:
            score = "Forty-All"
        else:
            score = "Deuce"
        
        return score
    
    def advantage_score(self):
        difference = self.m_score1 - self.m_score2
        if difference == 1:
            score = "Advantage player1"
        elif difference == -1:
            score = "Advantage player2"
        elif difference >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"
        
        return score
    
    def player_score(self, player_score):
        if player_score == 0:
            score = "Love"
        elif player_score == 1:
            score = "Fifteen"
        elif player_score == 2:
            score = "Thirty"
        elif player_score == 3:
            score = "Forty"
        
        return score