import unittest
from unittest.mock import Mock, call

from kauppa import Kauppa
from tuote import Tuote


class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.viitegeneraattori_mock.uusi.return_value = 42
        self.varasto_mock = Mock()

        self.tuotteet = {
            1: Tuote(1, "maito", 5),
            2: Tuote(2, "leipa", 7),
        }
        self.saldot = {1: 10, 2: 10}
        self.varasto_mock.saldo.side_effect = lambda tuote_id: self.saldot.get(
            tuote_id, 0
        )
        self.varasto_mock.hae_tuote.side_effect = lambda tuote_id: self.tuotteet.get(
            tuote_id
        )

        self.kauppa = Kauppa(
            self.varasto_mock,
            self.pankki_mock,
            self.viitegeneraattori_mock,
        )

    def test_maksettaessa_ostos_pankin_metodia_tilisiirto_kutsutaan(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called()

    def test_tilisiirto_kutsutaan_oikeilla_parametreilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 5
        )

    def test_kahden_eri_tuotteen_hinnat_lasketaan(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 12
        )

    def test_saman_tuotteen_hinta_lasketaan_useamman_kerran(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 10
        )

    def test_loppuunmyytya_tuotetta_ei_lisata_koriin(self):
        self.saldot[2] = 0

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 5
        )

    def test_aloita_asiointi_nollaa_edellisen_ostoksen(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.kauppa.aloita_asiointi()
        self.kauppa.tilimaksu("anna", "54321")

        self.assertEqual(
            self.pankki_mock.tilisiirto.call_args_list,
            [
                call("pekka", 42, "12345", "33333-44455", 5),
                call("anna", 42, "54321", "33333-44455", 0),
            ],
        )

    def test_uusi_viite_kysytaan_jokaiselle_maksulle(self):
        self.viitegeneraattori_mock.uusi.side_effect = [10, 11]

        self.kauppa.aloita_asiointi()
        self.kauppa.tilimaksu("pekka", "12345")
        self.kauppa.aloita_asiointi()
        self.kauppa.tilimaksu("anna", "54321")

        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 2)

    def test_ostos_poistetaan_korista(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.poista_korista(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 0
        )
