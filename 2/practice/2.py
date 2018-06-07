points = 0
wins = 0
for i in range(30):
    score = input()
    score = int(score)
    points = score + points
    if score == 3:
        wins = wins + 1
print(points, wins)