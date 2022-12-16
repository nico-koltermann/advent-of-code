player1 = ['A', 'B', 'C']
player2 = ['X', 'Y', 'Z']


def calculate_score(p1, p2):

    p1_chose = player1.index(p1)
    p2_chose = player2.index(p2)

    if p1_chose == p2_chose:
        return (1 + p2_chose) + 3
    elif (p1_chose + 1) % 3 == p2_chose:
        return (1 + p2_chose) + 6
    else:
        return (1 + p2_chose)


def action_choosed(p1, p2):

    p1_chose = player1.index(p1)
    action = player2.index(p2)

    # Loose
    if action == 0:
        return 1 + (p1_chose - 1) % 3
    elif action == 1:
        return 1 + ((p1_chose) % 3) + 3
    elif action == 2:
        return 1 + ((p1_chose + 1) % 3) + 6


def main():
    # Using readlines()
    file_ = open('data', 'r')
    Lines = file_.readlines()
      
    score = 0
    action_score = 0
    for line in Lines:
        game = line.split()
        score += calculate_score(game[0], game[1])
        action_score += action_choosed(game[0], game[1])

    print(score)
    print(action_score)

if __name__ == '__main__':
    main()
