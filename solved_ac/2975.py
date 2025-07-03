# Transactions
# https://www.acmicpc.net/problem/2975


def solution():
    while True:
        starting_balance, action, amount = input().split()
        starting_balance = int(starting_balance)
        amount = int(amount)

        # finish condition
        if starting_balance == 0 and action == 'W' and amount == 0:
            break
            
        prediction = starting_balance + amount if action == "D" else starting_balance - amount
        if prediction < -200:
            print("Not allowed")
        else:
            print(prediction)
    
    return

solution()