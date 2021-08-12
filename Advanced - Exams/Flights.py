def flights(*args):
    flights_info = {}

    if "Finish" not in args:
        return flights_info

    for index in range(0, len(args), 2):
        if args[index] == "Finish":
            return flights_info

        if flights_info.get(args[index]):
            flights_info[args[index]] += args[index + 1]
        else:
            flights_info[args[index]] = args[index + 1]

    return flights_info


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
