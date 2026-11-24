class TennisGame:
    SCORE_NAMES = ("Love", "Fifteen", "Thirty", "Forty")
    DEUCE_SCORE = 3
    WINNING_SCORE = 4
    ADVANTAGE_MARGIN = 1
    WIN_MARGIN = 2

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        if self._is_tied():
            return self._tied_score()
        if self._is_decided():
            return self._decided_score()
        return self._regular_score()

    def _is_tied(self):
        return self.player1_score == self.player2_score

    def _tied_score(self):
        if self.player1_score < self.DEUCE_SCORE:
            return f"{self._score_name(self.player1_score)}-All"
        return "Deuce"

    def _is_decided(self):
        return (
            self.player1_score >= self.WINNING_SCORE
            or self.player2_score >= self.WINNING_SCORE
        )

    def _decided_score(self):
        score_difference = self.player1_score - self.player2_score
        if score_difference == self.ADVANTAGE_MARGIN:
            return f"Advantage {self.player1_name}"
        if score_difference == -self.ADVANTAGE_MARGIN:
            return f"Advantage {self.player2_name}"
        if score_difference >= self.WIN_MARGIN:
            return f"Win for {self.player1_name}"
        return f"Win for {self.player2_name}"

    def _regular_score(self):
        player1_score = self._score_name(self.player1_score)
        player2_score = self._score_name(self.player2_score)
        return f"{player1_score}-{player2_score}"

    def _score_name(self, score):
        return self.SCORE_NAMES[score]
