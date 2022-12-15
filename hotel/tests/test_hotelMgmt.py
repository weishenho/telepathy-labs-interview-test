import unittest
from status import Status
from hotelMgmt import HotelMgmt


class TestHotelMgmt(unittest.TestCase):
    def setUp(self):
        self.rooms_per_floor = 5
        self.floors = 4
        self.hotel = HotelMgmt(4, 5)

    def test_object_instance(self):
        self.assertIsInstance(self.hotel, HotelMgmt,
                              "Object is not an instance of HotelMgmt")

    def test_available_rooms(self):
        result = self.hotel.get_available_rooms()
        self.assertEqual(len(result), self.rooms_per_floor *
                         self.floors, "total available rooms should be same as total rooms as no rooms are checked in yet")
        self.hotel.check_in()
        result = self.hotel.get_available_rooms()
        self.assertEqual(len(result), self.rooms_per_floor *
                         self.floors -1, "should n-1 available rooms as a room had checked in ")

    def test_set_status_raise_exception(self):
        #  Should raise exception if the status assigned conflicts with the workflow
        room = self.hotel.check_in()
        with self.assertRaises(Exception):
            self.hotel.room_cleaned(room.room_no)

    def test_status_transition(self):
        #  Should raise exception if the status assigned conflicts with the workflow
        room = self.hotel.check_in()
        self.assertEqual(room.status, Status.Occupied)
        room = self.hotel.check_out(room.room_no)
        self.assertEqual(room.status, Status.Vacant)
        room = self.hotel.room_cleaned(room.room_no)
        self.assertEqual(room.status, Status.Available)
        
        # out of service flow
        room = self.hotel.check_in()
        room = self.hotel.check_out(room.room_no)
        room = self.hotel.room_out_of_service(room.room_no)
        self.assertEqual(room.status, Status.Repair)
        room = self.hotel.room_repaired(room.room_no)
        self.assertEqual(room.status, Status.Vacant)
        room = self.hotel.room_cleaned(room.room_no)
        self.assertEqual(room.status, Status.Available)



if __name__ == '__main__':
    unittest.main()
