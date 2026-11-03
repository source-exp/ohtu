"""PlayerStats-yksikkötestit."""

from player import Player
from player_stats import PlayerStats


class PlayerReaderStub:
    """Palauta testipelaajat ilman verkkoyhteyttä."""

    def get_players(self):
        """Palauta kiinteä testipelaajalista."""
        return [
            Player({
                "name": "Finnish Star",
                "nationality": "FIN",
                "team": "AAA, BBB",
                "goals": 20,
                "assists": 30,
            }),
            Player({
                "name": "Finnish Scorer",
                "nationality": "FIN",
                "team": "CCC",
                "goals": 25,
                "assists": 10,
            }),
            Player({
                "name": "American Player",
                "nationality": "USA",
                "team": "AAA",
                "goals": 30,
                "assists": 25,
            }),
        ]


def create_stats():
    """Luo PlayerStats stub-lukijalla."""
    return PlayerStats(PlayerReaderStub())


def test_top_scorers_by_nationality():
    """Kansalaisuuden pelaajat järjestetään pisteiden mukaan."""
    players = create_stats().top_scorers_by_nationality("FIN")

    assert [player.name for player in players] == [
        "Finnish Star",
        "Finnish Scorer",
    ]


def test_top_scorers_by_team_includes_players_with_multiple_teams():
    """Monen joukkueen pelaaja löytyy kummankin joukkueen haulla."""
    players = create_stats().top_scorers_by_team("AAA")

    assert [player.name for player in players] == [
        "American Player",
        "Finnish Star",
    ]


def test_top_goal_scorers_limits_result():
    """Maalintekijöiden tulos rajoitetaan pyydettyyn määrään."""
    players = create_stats().top_goal_scorers(2)

    assert [player.name for player in players] == [
        "American Player",
        "Finnish Scorer",
    ]
