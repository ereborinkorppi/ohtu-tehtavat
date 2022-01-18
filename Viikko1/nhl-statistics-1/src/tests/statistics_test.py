import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    
    def test_pelaajalista_muodostuu_oikein(self):
        
        self.assertAlmostEqual(len(self.statistics._players), 5)
        
    def test_pelaajahaku_toimii(self):
        PRstub = PlayerReaderStub()
        pelaajat = PRstub.get_players()
        for pelaaja in pelaajat:
            self.assertEqual(self.statistics.search(pelaaja.name).__str__(), pelaaja.__str__())
            
    def test_joukkuehaku_toimii(self):
        
        self.assertEqual(self.statistics.team("DET")[0].__str__(), Player("Yzerman", "DET", 42, 56).__str__())
    
    def test_parhaat_maalintekijathaku_toimii(self):
        
        self.assertEqual(self.statistics.top_scorers(1)[0].__str__(), Player("Gretzky", "EDM", 35, 89).__str__())
    
    def test_pelaajahaku_toimii_kun_haettua_ei_loydy(self):

        self.assertEqual(self.statistics.search("Raipe"), None)
