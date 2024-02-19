import unittest
from customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer(customer_id="1", name="John Doe", contact_info="john@example.com")

    def test_customer_creation(self):
        self.assertEqual(self.customer.customer_id, "1")
        self.assertEqual(self.customer.name, "John Doe")
        self.assertEqual(self.customer.contact_info, "john@example.com")

    # Añade más tests para otros métodos que desarrolles

if __name__ == '__main__':
    unittest.main()
