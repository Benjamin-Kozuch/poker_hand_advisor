import unittest
from poker import Card, Hand, PokerHandAdvisor

class UserModelCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_given_cases(self):

        p = PokerHandAdvisor('TH JH QC QD QS QH KH AH 2S 6S')
        self.assertEqual(p.best_hand(), 'Hand: TH JH QC QD QS Deck: QH KH AH 2S 6S Best hand: royal-flush')
        print(p.best_hand())
        
        p = PokerHandAdvisor('2H 2S 3H 3S 3C 2D 3D 6C 9C TH')
        self.assertEqual(p.best_hand(), 'Hand: 2H 2S 3H 3S 3C Deck: 2D 3D 6C 9C TH Best hand: four-of-a-kind')
        print(p.best_hand())

        p = PokerHandAdvisor('2H 2S 3H 3S 3C 2D 9C 3D 6C TH')
        self.assertEqual(p.best_hand(), 'Hand: 2H 2S 3H 3S 3C Deck: 2D 9C 3D 6C TH Best hand: full-house')
        print(p.best_hand())

        p = PokerHandAdvisor('2H AD 5H AC 7H AH 6H 9H 4H 3C')
        self.assertEqual(p.best_hand(), 'Hand: 2H AD 5H AC 7H Deck: AH 6H 9H 4H 3C Best hand: flush')
        print(p.best_hand())

        p = PokerHandAdvisor('AC 2D 9C 3S KD 5S 4D KS AS 4C')
        self.assertEqual(p.best_hand(), 'Hand: AC 2D 9C 3S KD Deck: 5S 4D KS AS 4C Best hand: straight')
        print(p.best_hand())

        p = PokerHandAdvisor('KS AH 2H 3C 4H KC 2C TC 2D AS')
        self.assertEqual(p.best_hand(), 'Hand: KS AH 2H 3C 4H Deck: KC 2C TC 2D AS Best hand: three-of-a-kind')
        print(p.best_hand())

        p = PokerHandAdvisor('AH 2C 9S AD 3C QH KS JS JD KD')
        self.assertEqual(p.best_hand(), 'Hand: AH 2C 9S AD 3C Deck: QH KS JS JD KD Best hand: two-pairs')
        print(p.best_hand())

        p = PokerHandAdvisor('6C 9C 8C 2D 7C 2H TC 4C 9S AH')
        self.assertEqual(p.best_hand(), 'Hand: 6C 9C 8C 2D 7C Deck: 2H TC 4C 9S AH Best hand: one-pair')
        print(p.best_hand())

        p = PokerHandAdvisor('3D 5S 2H QD TD 6S KH 9H AD QH')
        self.assertEqual(p.best_hand(), 'Hand: 3D 5S 2H QD TD Deck: 6S KH 9H AD QH Best hand: highest-card')
        print(p.best_hand())



if __name__ == '__main__':
    unittest.main()