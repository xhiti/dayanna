print('Welcome to PowerLifting Data Collector! \n')


print('Available action:')
print('a - Add new lifter!')
print('r - Remove lifter!')
print('u - Update lifter!')
print('v - View all lifters!')
print('x - Exit the program!')

counter = 0
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

        if action == 'v':
            if len(lifters) == 0:
                print('No lifters added yet!')

        if action != 'a':
            if action == 'x':
                print('Exit!')

            if action == 'v':
                if len(lifters) == 0:
                    print('No lifters added yet!')

            print('\n\nAvailable action:')
            print('a - Add new lifter!')
            print('r - Remove lifter!')
            print('u - Update lifter!')
            print('v - View all lifters!')
            print('x - Exit the program!')

            newAction = str(input('\nPlease enter action!\t'))
            action = newAction

        if newAction == 'a':
            lifterToAdd = input("Enter new lifter name:\t")
            # lifterToAdd = str(lifterToAdd).lower().capitalize()

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
            newAction = not 'a'

        elif newAction == 'u':
            lifterToUpdate = input("Enter lifter name to update:\t")
            # lifterToUpdate = str(lifterToUpdate).lower().capitalize()

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
                                if liftType == 'squat':
                                    lifter['squat'].append(float(weight))
                                if liftType == 'benchpress':
                                    lifter['benchpress'].append(float(weight))
                                if liftType == 'deadlift':
                                    lifter['deadlift'].append(float(weight))
                            else:
                                print("Weights given aren't float numbers!")
                                break
            if not exists:
                print("Lifter '" + lifterToUpdate + "' doesn't exists!")

            action = "!u"
            newAction = not 'u'

        elif newAction == 'r':
            lifterToRemove = input("Enter lifter name to remove:\t")
            # lifterToRemove = str(lifterToRemove).lower().capitalize()

            position = 0
            index = 0
            for lifter in lifters:
                if lifter['name'] == lifterToRemove:
                    position = index
                else:
                    print("Lifter '" + lifterToRemove + "' doesn't exists!")
                index += 1

            lifters.pop(position)
            action = "!r"
            newAction = not 'r'

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

        elif newAction == 'x':
            print("Exit!")
            break
