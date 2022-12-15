import unittest
from status import Status
from room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room =  Room("1D", Status.Available, 1)

    def test_object_instance(self):
        self.assertIsInstance(self.room, Room, "Object is not an instance of Room")
        
    def test_status_instance(self):
        self.assertIsInstance(self.room.status, Status, "Object is not an instance of Status")

    def test_set_status(self):
        self.room.set_status(Status.Occupied)
        self.assertEqual(self.room.status, Status.Occupied)

    def test_set_status_raise_exception(self):
        # Should raise exception if the status assigned conflicts with the workflow
        with self.assertRaises(Exception):
            self.room.set_status(Status.Repair)

if __name__ == '__main__':
    unittest.main()