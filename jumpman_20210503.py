# jumpman
def jumpman(word):
    wrong = 0
    stages = ["",
             "   (ﾟ∀ﾟ)/　 　",
             "   / |       ",
             "    //       ",
             " 　｜｜｜    　",
             " ________    "
             ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ジャンプマンへようこそ！")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "１文字を予想してね"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print("".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("YOU WIN!")
            print("".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("YOU LOSE...The correct answer is {}.".format(word))

import random
wl = ["cat","dog","pig"]
r = random.randint(0,2)
jumpman(wl[r])
