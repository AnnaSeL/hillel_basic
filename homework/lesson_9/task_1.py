"""Count amount of points that the team got"""
def count(win, draw, loss):
    return int(win)*3+int(draw)*1-int(loss)*1


win = input("Enter win: ")
draw = input("Enter draw: ")
loss = input("Enter loss: ")
result = list(map(count, win, draw, loss))
print(f"Amount of points: {result}")
