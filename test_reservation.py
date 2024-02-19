import unittest
from reservation import Reservation

class TestReservation(unittest.TestCase):
    def setUp(self):
        self.reservation = Reservation(reservation_id="1", customer_id="1", hotel_id="1", room_number="101", start_date="2023-01-01", end_date="2023-01-05")

    def test_reservation_creation(self):
        self.assertEqual(self.reservation.reservation_id, "1")
        self.assertEqual(self.reservation.customer_id, "1")
        self.assertEqual(self.reservation.hotel_id, "1")
        self.assertEqual(self.reservation.room_number, "101")
        self.assertEqual(self.reservation.start_date, "2023-01-01")
        self.assertEqual(self.reservation.end_date, "2023-01-05")


if __name__ == '__main__':
    unittest.main()
