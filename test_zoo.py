import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

# Price invalid when age < 0 --------------------------------------------------
    def test_invalid_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), "invalid")

# Price_ticket 50 students (0 <= age <= 12) ---------------------------------------------------  
    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)
    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(12), 50)

# Price_ticket 100 students (13 <= age <= 20) ---------------------------------------------------
    def test_students_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(13), 100)
    def test_students_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)

# Price_ticket 150 (21 <= age <= 60) -------------------------------------------------------------
    def test_adults_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)
    def test_adults_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(60), 150)  

# Price_ticket 100 (age > 60) -----------------------------------------------------   
    def test_seniors_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)

if __name__ == '__main__':
    unittest.main()