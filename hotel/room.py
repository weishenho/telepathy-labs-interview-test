from status import Status
 
class Room:
    def __init__(self, room_no: str, status: Status, priority: int) -> None:
        self.room_no = room_no
        self.status = status
        self.priority = priority

    def set_status(self, status: Status):
        if (self.status == status.Available and status == Status.Occupied):
            self.status = status  # Occupied
        elif (self.status == status.Occupied and status == Status.Vacant):
            self.status = status  # Vacant
        elif (self.status == status.Vacant and status == Status.Available):
            self.status = status  # Available
        elif (self.status == status.Vacant and status == Status.Repair):
            self.status = status  # Repair
        elif (self.status == status.Repair and status == Status.Vacant):
            self.status = status  # Vacant
        else:
            raise Exception(
                "Cannot assign status as it conflicts with the status workflow")