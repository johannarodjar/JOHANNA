import unittest
from hotel import Hotel

class TestHotel(unittest.TestCase):
    def setUp(self):
        self.hotel = Hotel(hotel_id="1", name="Hotel Test", rooms={})

    def test_create_hotel(self):
        self.assertEqual(self.hotel.hotel_id, "1")
        self.assertEqual(self.hotel.name, "Hotel Test")
        self.assertDictEqual(self.hotel.rooms, {})

if __name__ == '__main__':
    unittest.main()
