class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = []

    def drive(self):
        return "Brum brum"
    
    def passenger_count(self):
        return len(self.passengers)
    
    def pick_up(self, person):
        self.passengers.append(person)

    def drop_off(self, person):
        self.passengers.remove(person)

    def empty_bus(self):
        while len(self.passengers) > 0:
            self.passengers.pop()

    def pick_up_from_stop(self, bus_stop):
        for person in bus_stop.queue:
            self.passengers.append(person)
            