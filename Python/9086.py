for i in range(int(input())):
    inputtext = input()

    if len(inputtext) == 1:
        print(inputtext*2)
    else:
        print(inputtext[0]+inputtext[-1])