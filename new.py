import random
import time
r=random.randint(1,10)
while True:
    number=int(input("Enter your Number :"))
    r=str(number)
    with open("number.txt","a") as f:
        f.write(f"{r}\n")
        time.sleep(2)
    w=random.randint(1,3)
    print("RESULT : ",w)
    if w==number:
        print("you won")
    else:
        print("loose")


