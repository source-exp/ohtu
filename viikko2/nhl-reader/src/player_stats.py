"""NHL-pelaajien tilastojen käsittely."""


class PlayerStats:
    """Tarjoaa kyselyitä pelaajien tilastoihin."""

    def __init__(self, reader):
        """Alusta tilastot lukijan palauttamilla pelaajilla."""
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        """Palauta kansallisuuden parhaat pistemiehet järjestettynä."""
        players = [player for player in self.players if player.nationality == nationality]
        return self._sort_by_points(players)

    def top_scorers_by_team(self, team):
        """Palauta joukkueen pelaajat pistejärjestyksessä."""
        players = [
            player for player in self.players
            if team in [player_team.strip() for player_team in player.team.split(",")]
        ]
        return self._sort_by_points(players)

    def top_goal_scorers(self, how_many):
        """Palauta pyydetty määrä maalintekijöitä."""
        return sorted(self.players, key=lambda player: player.goals, reverse=True)[:how_many]

    @staticmethod
    def _sort_by_points(players):
        return sorted(
            players,
            key=lambda player: player.points,
            reverse=True,
        )
