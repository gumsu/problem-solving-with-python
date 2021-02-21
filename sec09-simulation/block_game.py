import turtle as t
import random as r

if __name__ == "__main__":
    sc = t.Screen()
    sc.bgcolor("black")
    sc.setup(width=600, height=700)
    grid = [[0]*12 for _ in range(24)]
    for i in range(24):
        grid[i].insert(0,7)
        grid[i].append(7)
    grid.append([7]*14)

    block = t.Turtle()
    block.penup() # 줄 삭제
    block.speed(0)
    block.shape("square")
    block.color("red")

    for x in grid:
        print(x)

    sc.mainloop()