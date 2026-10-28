import unittest

from player import Player
from statistics_service import SortBy, StatisticsService


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),   #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54),  # 45+54 = 99
            Player("Kurri", "EDM", 37, 53),    # 37+53 = 90
            Player("Yzerman", "DET", 42, 56),  # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)   # 35+89 = 124
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(PlayerReaderStub())

    def test_sort_by_enum_has_expected_values(self):
        self.assertEqual(SortBy.POINTS.value, 1)
        self.assertEqual(SortBy.GOALS.value, 2)
        self.assertEqual(SortBy.ASSISTS.value, 3)

    def test_search_returns_player_when_name_is_found(self):
        player = self.stats.search("Kurri")

        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Kurri")

    def test_search_returns_none_when_name_is_not_found(self):
        player = self.stats.search("Selänne")

        self.assertIsNone(player)

    def test_team_returns_only_players_of_given_team(self):
        players = self.stats.team("EDM")

        self.assertEqual(len(players), 3)
        self.assertEqual(
            [player.name for player in players],
            ["Semenko", "Kurri", "Gretzky"]
        )

    def test_team_returns_empty_list_when_team_has_no_players(self):
        players = self.stats.team("PHI")

        self.assertEqual(players, [])

    def test_top_returns_players_in_descending_points_order_by_default(self):
        players = self.stats.top(5)

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Lemieux", "Yzerman", "Kurri", "Semenko"]
        )
        self.assertEqual(
            [player.points for player in players],
            [124, 99, 98, 90, 16]
        )

    def test_top_with_points_sort_by(self):
        players = self.stats.top(5, SortBy.POINTS)

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Lemieux", "Yzerman", "Kurri", "Semenko"]
        )

    def test_top_without_sort_by_behaves_like_points_sort_by(self):
        default_players = self.stats.top(5)
        points_players = self.stats.top(5, SortBy.POINTS)

        self.assertEqual(default_players, points_players)

    def test_top_with_goals_sort_by(self):
        players = self.stats.top(3, SortBy.GOALS)

        self.assertEqual(
            [player.name for player in players],
            ["Lemieux", "Yzerman", "Kurri"]
        )

    def test_top_with_assists_sort_by(self):
        players = self.stats.top(3, SortBy.ASSISTS)

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Yzerman", "Lemieux"]
        )

    def test_top_returns_only_how_many_players(self):
        players = self.stats.top(2)

        self.assertEqual(len(players), 2)
        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Lemieux")
