class Hotel:
    def __init__(self, hotel_id, name, rooms):
        self.hotel_id = hotel_id
        self.name = name
        self.rooms = rooms  # Podría ser un diccionario con el número de habitación como clave

    def create_hotel(self):
        pass

    def delete_hotel(self):
        pass

    def display_hotel_info(self):
        pass

    def modify_hotel_info(self, **kwargs):
        pass

    def reserve_room(self, room_number, customer_id):
        pass

    def cancel_reservation(self, reservation_id):
        pass



