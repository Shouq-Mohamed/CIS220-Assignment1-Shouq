class Passenger:
    """Class to represent a passenger"""

    # Constructor
    def __init__(self, name, ticket_class, from_location, to_location, flight, date, time, gate, boarding_time, seat, arrival_time, terminal, electronic_ticket):
        #initialize passenger attributes
        self.__name = name
        self.__ticket_class = ticket_class
        self.__from_location = from_location
        self.__to_location = to_location
        self.__flight = flight
        self.__date = date
        self.__time = time
        self.__gate = gate
        self.__boarding_time = boarding_time
        self.__seat = seat
        self.__arrival_time = arrival_time
        self.__terminal = terminal
        self.__electronic_ticket = electronic_ticket

    # Setter and Getter methods
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setTicketClass(self, ticket_class):
        self.__ticket_class = ticket_class

    def getTicketClass(self):
        return self.__ticket_class

    def setFromLocation(self, from_location):
        self.__from_location = from_location

    def getFromLocation(self):
        return self.__from_location

    def setToLocation(self, to_location):
        self.__to_location = to_location

    def getToLocation(self):
        return self.__to_location

    def setFlight(self, flight):
        self.__flight = flight

    def getFlight(self):
        return self.__flight

    def setDate(self, date):
        self.__date = date

    def getDate(self):
        return self.__date

    def setTime(self, time):
        self.__time = time

    def getTime(self):
        return self.__time

    def setGate(self, gate):
        self.__gate = gate

    def getGate(self):
        return self.__gate

    def setBoardingTime(self, boarding_time):
        self.__boarding_time = boarding_time

    def getBoardingTime(self):
        return self.__boarding_time

    def setSeat(self, seat):
        self.__seat = seat

    def getSeat(self):
        return self.__seat

    def setArrivalTime(self, arrival_time):
        self.__arrival_time = arrival_time

    def getArrivalTime(self):
        return self.__arrival_time

    def setTerminal(self, terminal):
        self.__terminal = terminal

    def getTerminal(self):
        return self.__terminal

    def setElectronicTicket(self, electronic_ticket):
        self.__electronic_ticket = electronic_ticket

    def getElectronicTicket(self):
        return self.__electronic_ticket

    # Display passenger details
    def displayPassengerInfo(self):
        print("Passenger:", self.getName())
        print("Ticket Class:", self.getTicketClass())
        print("From:", self.getFromLocation())
        print("To:", self.getToLocation())
        print("Flight:", self.getFlight())
        print("Date:", self.getDate())
        print("Time:", self.getTime())
        print("Gate:", self.getGate())
        print("Boarding till:", self.getBoardingTime())
        print("Seat:", self.getSeat())
        print("Arrival time:", self.getArrivalTime())
        print("Terminal:", self.getTerminal())
        print("Electronic Ticket:", self.getElectronicTicket())


class Flight:
    """Class to represent a flight"""

    # Constructor
    def __init__(self, flight_number, departure_time, arrival_time, departure_location, arrival_location):
        #initialize flight details
        self.__flight_number = flight_number
        self.__departure_time = departure_time
        self.__arrival_time = arrival_time
        self.__departure_location = departure_location
        self.__arrival_location = arrival_location

    # Setter and Getter methods
    def setFlightNumber(self, flight_number):
        self.__flight_number = flight_number

    def getFlightNumber(self):
        return self.__flight_number

    def setDepartureTime(self, departure_time):
        self.__departure_time = departure_time

    def getDepartureTime(self):
        return self.__departure_time

    def setArrivalTime(self, arrival_time):
        self.__arrival_time = arrival_time

    def getArrivalTime(self):
        return self.__arrival_time

    def setDepartureLocation(self, departure_location):
        self.__departure_location = departure_location

    def getDepartureLocation(self):
        return self.__departure_location

    def setArrivalLocation(self, arrival_location):
        self.__arrival_location = arrival_location

    def getArrivalLocation(self):
        return self.__arrival_location


class BoardingPass:
    """Class to represent a boarding pass"""

    # Constructor
    def __init__(self, passenger, flight, gate, boarding_time):
        #initialize boarding pass details
        self.__passenger = passenger
        self.__flight = flight
        self.__gate = gate
        self.__boarding_time = boarding_time

    # Setter and Getter methods
    def setPassenger(self, passenger):
        self.__passenger = passenger

    def getPassenger(self):
        return self.__passenger

    def setFlight(self, flight):
        self.__flight = flight

    def getFlight(self):
        return self.__flight

    def setGate(self, gate):
        self.__gate = gate

    def getGate(self):
        return self.__gate

    def setBoardingTime(self, boarding_time):
        self.__boarding_time = boarding_time

    def getBoardingTime(self):
        return self.__boarding_time


class Staff:
    """Class to represent staff members"""

    # Constructor
    def __init__(self, name, ID, role):
        #initialize staff details
        self.__name = name
        self.__ID = ID
        self.__role = role

    # Setter and Getter methods
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setID(self, ID):
        self.__ID = ID

    def getID(self):
        return self.__ID

    def setRole(self, role):
        self.__role = role

    def getRole(self):
        return self.__role


# Create objects and populate boarding pass details
passenger = Passenger("James Smith", "First Class", "Chicago ORD", "New York JFK", "NA4321", "06 Dec 20", "11:40", "03", "11:20", "09A", "13:30", "2", "629")
flight = Flight("NA4321", "11:40", "13:30", "Chicago ORD", "New York JFK")
boarding_pass = BoardingPass(passenger, flight, "03", "11:20")

# Display boarding pass details
boarding_pass.getPassenger().displayPassengerInfo()
