import shelve


locations = {0: {"desc": "You are sitting in front of a computer learning Python",
                 "exits": {},
                 "namedExits": {}},
             1: {"desc": "You are standing at the end of a road before a small brick building",
                 "exits": {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
                 "namedExits": {"2": 2, "3": 3, "5": 5, "4": 4, "0": 0}},
             2: {"desc": "You are at the top of a hill",
                 "exits": {"N": 5, "Q": 0},
                 "namedExits": {"5": 5, "0": 0}},
             3: {"desc": "You are inside a building, a well house for a small stream",
                 "exits": {"W": 1, "Q": 0},
                 "namedExits": {"1": 1, "0": 0}},
             4: {"desc": "You are in a valley beside a stream",
                 "exits": {"N": 1, "W": 2, "Q": 0},
                 "namedExits": {"1": 1, "2": 2, "0": 0}},
             5: {"desc": "You are in the forest",
                 "exits": {"W": 2, "S": 1, "Q": 0},
                 "namedExits": {"1": 1, "2": 2, "0": 0}}
             }

loc = 1

while True:

    with shelve.open("locations") as locationShelve:

        availableExits = ", ".join(locationShelve[str(loc)]["exits"].keys())
        print(locationShelve[str(loc)]["desc"])
        if loc == 0:
            break
        direction = input("Available exits are " + availableExits + " " +" or simply ask politely (es: Can i go north?)").upper()

        allExits = locationShelve[str(loc)]["exits"].copy()
        allExits.update(locationShelve[str(loc)]["namedExits"])

    with shelve.open("vocabulary") as vocabularyShelve:
        for vocItems in vocabularyShelve:
            if vocItems in direction:
                direction = vocabularyShelve[vocItems]
                break
        print()

        if direction in allExits:
            loc = allExits[direction]

        else:
            print("You cannot go in that direction")
