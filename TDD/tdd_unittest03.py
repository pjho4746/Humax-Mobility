import unittest
import calendar
year=int(input("year : "))

def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

class TestIsYearFunction(unittest.TestCase):
    def test_leap_year(self):
        self.assertEqual(leap_year(year), calendar.isleap(year))

    def test_non_leap_year(self):
        self.assertEqual(leap_year(year), calendar.isleap(year))

if __name__ == '__main__':
    unittest.main()
