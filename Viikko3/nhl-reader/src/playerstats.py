class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        top_scorers = []
        players = [player for player in self.reader.get_players() if player.nationality == nationality]
        for player in sorted(players, key=lambda player: player.goals, reverse=True):
            top_scorers.append(player.__str__())

        return top_scorers