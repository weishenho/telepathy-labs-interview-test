import heapq
from status import Status
from room import Room

class HotelMgmt:
    def __init__(self, floors=4, rooms=5) -> None:
        self.floors = floors
        self.rooms = rooms
        self.total_rooms = self.floors * self.rooms
        self.rooms_letter_dict = [chr(ord('A') + x) for x in range(self.rooms)]
        self.heap = []
        self.rooms_dict = {}
        cur_priority = self.total_rooms
        cur_direction = "RL" if self.floors % 2 == 0 else "LR"

        # "Create the rooms, assign priority and add it to priority queue starting from the highest to lowest floor"
        for i in range(self.floors, 0, -1):
            for j in range(self.rooms) if cur_direction == "RL" else range(self.rooms-1, -1, -1):
                room_no = f"{i}{self.rooms_letter_dict[j]}"
                room = Room(
                    room_no, Status.Available, cur_priority)
                self.rooms_dict[room_no] = room
                heapq.heappush(self.heap, (cur_priority, room))
                cur_priority -= 1

            cur_direction = "LR" if cur_direction == "RL" else "RL"

    def is_room_exist(self, room_no):
        try:
            self.rooms_dict[room_no]
            return True
        except:
            return False

    def get_available_rooms(self):
        return [item[1].room_no for item in self.heap]

    def get_available_room(self):
        # Peek at the next available room from the queue
        return self.heap[0].room_no

    def check_in(self):
        _, room = heapq.heappop(self.heap)
        room.set_status(Status.Occupied)
        return room

    def check_in_specific_room(self, room_no):
        self.is_room_exist(room_no)
        room = self.rooms_dict[room_no]
        self.heap.remove((room.priority, room))
        heapq.heapify(self.heap)
        return room

    def check_out(self, room_no):
        self.is_room_exist(room_no)
        room = self.rooms_dict[room_no]
        room.set_status(Status.Vacant)
        return room

    def room_cleaned(self, room_no):
        self.is_room_exist(room_no)
        room = self.rooms_dict[room_no]
        room.set_status(Status.Available)
        heapq.heappush(self.heap, (room.priority, room))
        return room

    def room_out_of_service(self, room_no):
        self.is_room_exist(room_no)
        room = self.rooms_dict[room_no]
        room.set_status(Status.Repair)
        return room
        
    def room_repaired(self, room_no):
        # room = self.rooms_dict[room_no]
        # room.set_status(Status.Vacant)
        return self.check_out(room_no)
