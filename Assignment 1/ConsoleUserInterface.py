print('Welcome to Data Statistics! \n')
print('Available action:')
print('a - Add numbers!')
print('v - View statistics!')
print('x - Exit!')

action = str(input('Please enter action! '))
if action not in 'avx':
    print("Invalid input, '" + str(action) + "' please try again!")
else:
    if action == 'x':
        print("Exit!")
        action = not 'a'

    if action == 'v':
        if counter == 0:
            print("No numbers given!")
        action = not 'a'

    # Variables for stats
    counter = 0
    max = -9999
    min = 9999
    sum = 0

    while action:
        newAction = action

        # VIEW
        if action == 'v':
            if counter == 0:
                print('No numbers have been added yet!')

        # NOT ADD
        if action != 'a':
            if action == 'x':
                print("Exit!")
                # break
            if action == 'v':
                print("No numbers given!")

            print('\nAvailable action:')
            print('a - Add numbers!')
            print('v - View statistics!')
            print('x - Exit!')
            newAction = str(input('Please enter action! '))
            action = newAction

        # ADD
        if newAction == 'a':
            number = input("Enter number or 'x' when you are done! ")

            if number == '':
                print("Invalid input, please try to give a number or 'x' when you are done!")

            if number == 'x':
                if counter == 0:
                    print('No numbers have been added yet!')
                action = '!a'
                newAction = not "a"
            else:
                intNumber = int(number)
                if intNumber > max:
                    max = intNumber
                if intNumber < min:
                    min = intNumber
                sum += intNumber
                counter += 1

        # VIEW
        elif newAction == 'v':
            if counter == 0:
                print('No numbers have been added yet!')
            else:
                avg = sum / counter
                print("COUNT: ", counter)
                print("SUM: ", sum)
                print("AVG: ", avg)
                print("MIN: ", min)
                print("MAX: ", max)

        # EXIT
        elif newAction == 'x':
            print("Exit!")
            break
