import math
#Convert APY (calculated with the assumption of continious compound) into simple daily interest and actual return 
APY = user_input = float(input("Enter APY in %: "))
P = user_input = float(input("Enter Principal: "))
t = user_input = float(input("Enter the time to maturity in days: "))/365
r = math.log((APY/100)+1)
print(f'Simple daily interest is: {r/365}')
print(f'Return will be: {P*math.exp(r*t)-P}')
