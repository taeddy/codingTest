sleep = int(input())
wake = int(input())

sleeping_hours = wake-sleep if wake > sleep else wake-sleep+24
print(sleeping_hours)