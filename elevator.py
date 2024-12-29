import random

"""You are an engineer working with an architect who is designing a new
building. The architect has expressed frustration that every time he works
on a new building he has to do a lot of repetitive calculations to decide on
the number of elevators that will be required to meet the building capacity.

He has asked you to write a program that can take various variables, such as
building size, number of floors, occupancy, staff work times and other such
data and build a simulation to identify how many elevators will need to be
installed."""
SECONDS_PER_HOUR = 60 * 60
ELEVATOR_TRIP_TIME_SECONDS = random.randint(100, 140)
scenario1 = {"number_of_floor": 12, "occupancy_per_floor": 60,
    "elevator_busy_times": [7, 8, 11, 12, 13, 17, 18]}


def is_busy(time):
    return time in scenario1["elevator_busy_times"]


def get_occupancy(time):
    if is_busy(time):
        pass


total_occupancy = scenario1["number_of_floor"] * scenario1[
    "occupancy_per_floor"]
length_of_trip = scenario1[
                     "number_of_floor"] * SECONDS_PER_HOUR / ELEVATOR_TRIP_TIME_SECONDS
with open("elevators.txt", "a") as f:
    clock = range(7, 20)
    for hour in clock:
        number_of_people_in_the_elevator = random.randrange(1, 9)
        if is_busy(hour):
            number_of_occupants = total_occupancy * 0.45
            number_of_trips = total_occupancy * 0.45 / number_of_people_in_the_elevator
            print(hour, "busy: number of occupants using elevator =",
                  int(number_of_occupants), "number_of_trips ",
                  int(number_of_trips), "taking",
                  int(number_of_trips * length_of_trip), "hours")
            f.write(
                f"{hour} busy: number of occupants using elevator =\
                    {int(number_of_occupants)} number_of_trips\
                    {int(number_of_trips)} taking {int(number_of_trips * length_of_trip)} hours\n")
        else:
            number_of_occupants = total_occupancy * 0.10
            number_of_trips = total_occupancy * 0.10 / number_of_people_in_the_elevator
            print(hour, "not busy: number of occupants using elevator=",
                  int(number_of_occupants), "number_of_trips ",
                  int(number_of_trips), "taking",
                  int(number_of_trips * length_of_trip), "hours")
            f. (
                f"{hour} busy: number of occupants using elevator =\
                {int(number_of_occupants)} number_of_trips\
                {int(number_of_trips)} taking {int(number_of_trips * length_of_trip)} hours\n")

"""
        print(hour, "busy",number of occupants)
    else:
        print(hour,number of occupants)"""

"If it is busy. Assume that 45% of the people are going to use the elevator. If it is not busy. Assume 10% is going to use the elevator. Work out number of occupants"
