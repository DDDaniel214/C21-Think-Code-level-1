#Message at the end of the game commenting on your achievement list


def reward(achievements):
    if (achievements == 1, 2, 3):
        print("You can do better.")
        

    if (achievements == 4, 5, 6):
        print("Good job, you got most of them.")
        
    if (achievements == 7, 8):
        print("Wow, you almost did everything!")

    if (achievements == 9):
         print("Nice, you got them all!")


reward(9)
