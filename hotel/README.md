##### Programming lanaguage: python3

## Installation
Only python and it's standard library is needed

## Usage
Edit main.py
Create HotelMgmt 

The object expose the following methods:
is_room_exist(<room_no>) - Check if room exist
get_available_rooms() - show all available rooms
get_available_room() - show closest available room
check_in() - check in the closest available room and transition room to occupied
check_in_specific_room(<room_no>) - check in a specific room of your choosing, can disregard the closest available room
check_out(<room_no>) - check out the room, transition room to vacant
room_cleaned(<room_no>) - transition a vacant room to available
room_out_of_service(<room_no>) - transition a vacant room to repair
room_repaired(<room_no>) - transition a room under repair to vacant

Example:

```
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

```


#### To Run Test cases
    python -m unittest discover tests/