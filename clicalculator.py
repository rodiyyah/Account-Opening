startcalculator = False
while startcalculator == False:

    firstvalue = int(input('enter a firstvalue \n'))
    secondvalue = int(input('enter a secondvalue \n'))

    print('These are the available options')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Modulus operations')
    isvalidoptionselected = False

    while isvalidoptionselected == False:

        selectedoptions = int(input('please select an option \n'))

        if(selectedoptions == 1):
            isvalidoptionselected = True
            print('You selcted option %s'%selectedoptions)
            print(firstvalue + secondvalue)
        elif(selectedoptions == 2):
            isvalidoptionselected = True
            print('You selcted option %s'%selectedoptions)
            print(firstvalue - secondvalue)
        elif(selectedoptions == 3):
            isvalidoptionselected = True
            print('You selcted option %s'%selectedoptions)
            print(firstvalue * secondvalue)
        elif(selectedoptions == 4):
            isvalidoptionselected = True
            print('You selcted option %s'%selectedoptions)
            print(firstvalue / secondvalue)
        elif(selectedoptions == 5):
             isvalidoptionselected = True
             print('You selcted option %s'%selectedoptions)
             print(firstvalue % secondvalue)
        else:
            print('Kindly choose an available option')

    continuecalculations =int(input('Do you wnt to calculate again 1. yes 2. no \n'))
    if(continuecalculations == 1):
        startcalculator = False
    elif(continuecalculations ==2):
       startcalculator = True
    else:
        print('kindly chhose an available option')

