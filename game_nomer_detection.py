from random import randint

def game():
    input("Assalomu alaykum! \n 1 dan 10 gacha son o'ylang!\n"
          "Men siz o'ylagan sonni topish uchun harakat qilaman. \n"
          "Uning uchun men aytgan amallarni bajaring oxirida natijani aytaman !")
    player = 0
    index = 5
    i = 0
    while i<=index:

        if i%2==0:
            add = randint(5,10)
            input(f"Siz o'ylagan soningizga {add} ni qo'shing !")
            player += add
        else:
            sub = randint(1,5)
            input(f"Siz o'ylagan soningizga {sub} ni ayiring !")
            player -= sub
        i += 1
    input(f"Endi dastlab o'ylagan soningizni ayirib tashlang !")

    print(f"Natija = {player} ga teng.")

game()
