"""NHL-pelaajien tilastojen käsittely."""


class PlayerStats:
    """Tarjoaa kyselyitä pelaajien tilastoihin."""

    def __init__(self, reader):
        """Alusta tilastot lukijan palauttamilla pelaajilla."""
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        """Palauta kansallisuuden parhaat pistemiehet järjestettynä."""
        players = [
            player for player in self.players
            if player.nationality == nationality
        ]
        return sorted(
            players,
            key=lambda player: player.points,
            reverse=True,
        )
