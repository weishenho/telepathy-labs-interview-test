from hotelMgmt import HotelMgmt

if __name__ == "__main__":
    hotel = HotelMgmt()
    result = hotel.check_in_specific_room("4D")
    avail_rooms = hotel.get_available_rooms()
    print(avail_rooms)

    room = hotel.check_in()
    room = hotel.check_out(room.room_no)
    room = hotel.room_out_of_service(room.room_no)
    room = hotel.room_repaired(room.room_no)
    room = hotel.room_cleaned(room.room_no)

    room = hotel.check_in()
    room = hotel.check_out(room.room_no)
    room = hotel.room_out_of_service(room.room_no)
    room = hotel.room_repaired(room.room_no)
    print(room.room_no, room.status)