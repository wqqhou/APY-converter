import math
#Convert APY (calculated with the assumption of compound) into simple daily interest and actual return 

APY = user_input = float(input("Enter APY in %: "))/100
P = user_input = float(input("Enter Principal: "))
t = user_input = float(input("Enter the time to maturity in days: "))/365
while(True):
    q  = user_input = input("Is the APY caculated based on the assumption of continous compounding? (y/n): ")
    if q == 'y':
        r = math.log((APY)+1)
        print(f'Simple daily interest is: {r/365}')
        print(f'Return will be: {P*math.exp(r*t)-P}')
        break
    elif q == 'n':
        i = user_input = 365.0 / float(input("Enter the interval of compound in days: "))
        r = ((APY + 1) ** (1/i) - 1) * i
        print(f'Simple daily interest is: {r/365}')
        print(f'Return will be: {(P*(1+r/i)**(i*t))}')
        break
    else:
        print("Please enter y or n")