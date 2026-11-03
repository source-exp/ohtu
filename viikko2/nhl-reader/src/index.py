"""NHL-pelaajatilastojen komentorivikäyttöliittymä."""

from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

from player_reader import PlayerReader
from player_stats import PlayerStats


console = Console()
SEASONS = [
    "2018-19",
    "2019-20",
    "2020-21",
    "2021-22",
    "2022-23",
    "2023-24",
    "2024-25",
    "2025-26",
]
NATIONALITIES = [
    "USA", "FIN", "CAN", "SWE", "CZE", "RUS", "SLO", "FRA",
    "GBR", "SVK", "DEN", "NED", "AUT", "BLR", "GER", "SUI",
    "NOR", "UZB", "LAT", "AUS",
]


def print_players(players, season, nationality):
    """Tulosta pelaajat Rich-taulukkona."""
    table = Table(title=f"Season {season} players from {nationality}")
    table.add_column("Player")
    table.add_column("Teams")
    table.add_column("Goals", justify="right")
    table.add_column("Assists", justify="right")
    table.add_column("Points", justify="right")

    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.points),
        )

    console.print(table)


def get_players_for_selection(stats, selection):
    """Hae pelaajat kansalaisuuden tai joukkueen perusteella."""
    if selection in NATIONALITIES:
        return stats.top_scorers_by_nationality(selection), f"nationality {selection}"

    team = Prompt.ask("Team code").upper()
    return stats.top_scorers_by_team(team), f"team {team}"


def main():
    """Käynnistä komentorivikäyttöliittymä."""
    season = Prompt.ask("Season", choices=SEASONS, default="2024-25")
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    stats = PlayerStats(PlayerReader(url))

    while True:
        selection = Prompt.ask(
            "Nationality or team",
            choices=NATIONALITIES + ["team code", "QUIT"],
            default="FIN",
            show_choices=True,
        ).upper()
        if selection == "QUIT":
            break

        players, label = get_players_for_selection(stats, selection)
        print_players(players, season, label)


if __name__ == "__main__":
    main()
