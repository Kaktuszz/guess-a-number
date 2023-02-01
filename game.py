import random

def game():
    # Array creator
    a = [0, 0, 0]
    i = 0
    while i != 3:
        a[i] = random.randrange(0,10)
        i += 1
        
    a = random_checker(a)

    print("WELCOME TO THE GREAT GAME! I guessed a three-digit number, guess it and get a reward!")
    # print(a)
    b = []
    while b != a:
        b = []
        x = input("Print number: ")
        # string_checker(x)
        g = 0
        for num in x:
            b += x[g]
            g +=1
            b = list(map(int,b))
        print(b)
        if helper(a,b) == False:
            print("Very cold!")
            
       
    print("Cake is a lie!!")


# Wadahellll
# def helper(guard,suspect):
#     if guard == suspect:
#         print("Nice! But")
#     elif guard[0] == suspect[0] or guard[0] == suspect[1] or guard[0] == suspect[2] or guard[1] == suspect[0] or guard[1] == suspect[1] or guard[1] == suspect[2] or guard[2] == suspect[0] or guard[2] == suspect[1] or guard[2] == suspect[2]:
#         print("Warmer...")
#     else: 
#         print("Very cold")


# Checks array a and b
def helper(guard,suspect):
    g = 0
    s = 0
    f = 0
    if guard == suspect:
        print("Nice! But")
        return True
    else:
        while s!=3:
            g=0
            while g!=3:
                if guard[g] == suspect[s]:
                    print("Warmer...")
                    f+=1
                g+=1
            s+=1
    if f == 0:
        return False


# random numbers generator (if 0 on first position 0+=1)
def random_checker(a):
    if a[0] == 0:
        a[0] += 1
    if a[0] == a[1] or a[0] == a[2] or a[1] == a[2]:
        while a[0] == a[1]:
            a[1] = random.randrange(0,10)
        while a[0] == a[2]:
            a[2] = random.randrange(0,10)
        while a[0] == a[2] or a[1] == a[2]:
            a[2] = random.randrange(0,10)
    return a

# def string_checker(x):
#     while isinstance(x, str) == True:
#         print("I guessed a number not a word!")
#         x = input("Print number:")
#     return x


game()
