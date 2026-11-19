from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._tavaroita = 0
        self._hinta = 0
        self._ostokset = []

    def tavaroita_korissa(self):
        return self._tavaroita

    def hinta(self):
        return self._hinta

    def _paivita_korin_tila(self, tuote: Tuote, muutos: int):
        self._tavaroita += muutos
        self._hinta += muutos * tuote.hinta()

    def lisaa_tuote(self, lisattava: Tuote):
        self._paivita_korin_tila(lisattava, 1)
        for ostos in self._ostokset:
            if ostos.tuote == lisattava:
                ostos.muuta_lukumaaraa(1)
                return
        self._ostokset.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        for ostos in self._ostokset:
            if ostos.tuote == poistettava:
                ostos.muuta_lukumaaraa(-1)
                self._paivita_korin_tila(poistettava, -1)
                if ostos.lukumaara() == 0:
                    self._ostokset.remove(ostos)
                return

    def tyhjenna(self):
        self._tavaroita = 0
        self._hinta = 0
        self._ostokset = []

    def ostokset(self):
        return self._ostokset
