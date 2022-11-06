print('Welcome to PowerLifting Data Collector! \n')
print('Available action:')
print('a - Add new lifter!')
print('r - Remove lifter!')
print('u - Update lifter!')
print('v - View all lifters!')
print('x - Exit the program!')

lifters = []
action = str(input('\nPlease enter action!\t'))

if action not in 'aruvx':
    print("Invalid input, '" + str(action) + "' please try again!")
else:
    if action == 'x':
        print("Exit!")
        action = not 'a'

    if action in ['r', 'u', 'v']:
        print("No lifters added, action can't be done!")
        action = not 'a'

    while action:
        newAction = action

        if action != 'a':
            print('\n\nAvailable action:')
            print('a - Add new lifter!')
            print('r - Remove lifter!')
            print('u - Update lifter!')
            print('v - View all lifters!')
            print('x - Exit the program!')

            newAction = str(input('\nPlease enter action!\t'))
            action = newAction

        # 1. ADD Lifter
        if newAction == 'a':
            lifterToAdd = input("Enter new lifter name:\t")

            exists = False
            for lifter in lifters:
                if lifter['name'] == lifterToAdd:
                    exists = True
                    print("Lifter '" + lifterToAdd + "' already exists!")

            if not exists:
                lifter = {
                    "name": lifterToAdd,
                    "squat": [],
                    "benchpress": [],
                    "deadlift": []
                }
                lifters.append(lifter)

            action = "!a"

        # 2. UPDATE Lifter
        elif newAction == 'u':
            lifterToUpdate = input("Enter lifter name to update:\t")

            exists = False
            for lifter in lifters:
                exists = lifter['name'] == lifterToUpdate
                if exists:
                    liftType = input("Enter lift (one of 'squat', 'benchpress' and 'deadlift':\t")
                    if liftType not in ['squat', 'benchpress', 'deadlift']:
                        print("Invalid lift type given!")
                        break
                    else:
                        weights = input("Enter weight(s) separated by one single space:\t")
                        weights = weights.split()

                        for weight in weights:
                            if float(weight):
                                lifter[liftType].append(float(weight))
                            else:
                                print("Weights given aren't float numbers!")
                                break
            if not exists:
                print("Lifter '" + lifterToUpdate + "' doesn't exists!")

            action = "!u"

        # 3. REMOVE Lifter
        elif newAction == 'r':
            lifterToRemove = input("Enter lifter name to remove:\t")

            exists = False
            position = 0
            index = 0
            for lifter in lifters:
                exists = lifter['name'] == lifterToRemove
                if exists:
                    position = index
                    break
                index += 1

            if not exists:
                print("Lifter '" + lifterToRemove + "' doesn't exists!")

            lifters.pop(position)
            action = "!r"

        # 4. VIEW Lifters
        elif newAction == 'v':
            if len(lifters) > 0:
                counter = 0
                for lifter in lifters:
                    counter += 1
                    print("--------------------------")
                    print("Lifter #:\t\t", counter)
                    print("Name:\t\t\t", lifter['name'])
                    print("Squat:\t\t\t", lifter['squat'])
                    print("Bench Press:\t", lifter['benchpress'])
                    print("Deadlift:\t\t", lifter['deadlift'])
                    print("--------------------------")
                    print()
            else:
                print("No lifters added yet!")

            action = "!v"

        # 5. EXIT Program
        elif newAction == 'x':
            print("Exit!")
            break
