'''
Aditya Chakraborty
8/22
Age Calc
'''

running = True

while running:
    n = input("Enter an age, or q to quit: ")
    if n == "q":
        print("Goodbye!")
        running = False
        break
    hours = 8760*float(n)
    mins = hours*60
    secs = mins*60
    print(f"You have been alive for {hours}")
    print(f"That's {mins} minutes")
    print(f"That's {secs} seconds")
