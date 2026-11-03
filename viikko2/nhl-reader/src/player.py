"""NHL-pelaajan tietomalli."""


class Player:
    """Edustaa NHL-pelaajaa ja hänen tilastotietojaan."""

    def __init__(self, player_data):
        """Alusta pelaaja API:n palauttamista tiedoista."""
        self.name = player_data["name"]
        self.nationality = player_data["nationality"]
        self.team = player_data["team"]
        self.goals = player_data["goals"]
        self.assists = player_data["assists"]

    @property
    def points(self):
        """Palauta pelaajan maali- ja syöttöpisteiden summa."""
        return self.goals + self.assists

    def __str__(self):
        """Palauta pelaajan muotoiltu merkkijonoesitys."""
        return f"{self.name:20} {self.team:15} {self.goals} + {self.assists} = {self.points}"
