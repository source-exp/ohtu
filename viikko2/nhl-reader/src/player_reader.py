"""NHL-pelaajien lukeminen verkko-API:sta."""

import requests

from player import Player


class PlayerReader:
    """Lukee pelaajat annetusta NHL-tilastopalvelun URL-osoitteesta."""

    def __init__(self, url):
        """Alusta lukija URL-osoitteella."""
        self.url = url

    def get_players(self):
        """Palauta URL-osoitteen JSON-datan pelaajaolioina."""
        response = requests.get(self.url, timeout=30)
        response.raise_for_status()
        return [Player(player_data) for player_data in response.json()]
