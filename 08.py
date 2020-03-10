user1=input("Player One Choose Rock(R),Paper(P),Scissors(S)")
user2=input("Player Two Choose Rock(R),Paper(P),Scissors(S)")

while user1 == 'R':
    if user2 == 'P':
        print("Player 2 hat gewonnen")
        break
    if user2 == 'S':
        print("Player 1 hat gewonnen")
        break
    if user2 == 'R':
        print("Unentschieden")
        break

while user1 == 'S':
    if user2 == 'R':
        print("Player 2 hat gewonnen")
        break
    if user2 == 'P':
        print("Player 1 hat gewonnen")
        break
    if user2 == 'S':
        print("Unentschieden")
        break

while user1 == 'P':
    if user2 == 'S':
        print("Player 2 hat gewonnen")
        break
    if user2 == 'R':
        print("Player 1 hat gewonnen")
        break
    if user2 == 'P':
        print("Unentschieden")
        break
