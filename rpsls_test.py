# Testing for rpsls
import unittest
import rpsls

class RpslsTestCase(unittest.TestCase):

    # Test calls to name_to_number()
    def test_number_to_name(self):
        self.assertEquals(rpsls.number_to_name(0), 'rock');
        self.assertEquals(rpsls.number_to_name(1), 'Spock');
        self.assertEquals(rpsls.number_to_name(2), 'paper');
        self.assertEquals(rpsls.number_to_name(3), 'lizard');
        self.assertEquals(rpsls.number_to_name(4), 'scissors');

    # Test calls to name_to_number()
    def test_name_to_number(self):
        self.assertEquals(rpsls.name_to_number("rock"),     0);
        self.assertEquals(rpsls.name_to_number("Spock"),    1);
        self.assertEquals(rpsls.name_to_number("paper"),    2);
        self.assertEquals(rpsls.name_to_number("lizard"),   3);
        self.assertEquals(rpsls.name_to_number("scissors"), 4);

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(RpslsTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)