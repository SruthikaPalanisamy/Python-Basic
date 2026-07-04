n = 42
cnt=0
while  (cnt!=100):
    cnt+=1
    x = int(input("Guess: "))
    if x>42:
        print("Too High")
    if x<42:
        print("Too Low")
    if x==42:
        print("Correct its 42 guessed in " , cnt , "Attempts")
        break;
