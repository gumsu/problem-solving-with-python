import turtle as t
import random as r

class Brick():
    def __init__(self):
        self.y = 0
        self.x = 6
        self.color = r.randint(1,6)

def draw_grid(black, grid):
    top = 250
    left = -150
    colors = ['black', 'red', 'blue', 'orange', 'yellow', 'green', 'purple', 'white']
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            sc_x = left+(x*22)
            sc_y = top-(y*22)
            block.goto(sc_x,sc_y)
            block.color(colors[grid[y][x]]) # 벽을 7로 생성했으므로 colors[7] 색으로 나타남
            block.stamp()

if __name__ == "__main__":
    sc = t.Screen()
    sc.bgcolor("black")
    sc.setup(width=600, height=700)
    grid = [[0]*12 for _ in range(24)]
    for i in range(24):
        grid[i].insert(0,7)
        grid[i].append(7)
    grid.append([7]*14)
    for y in range(23, 20, -1):
        for x in range(1, 13):
            grid[y][x] = r.randint(1,6)

    block = t.Turtle()
    block.penup() # 줄 삭제
    block.speed(0)
    block.shape("square")
    block.color("red")

    brick = Brick()
    grid[brick.y][brick.x] = brick.color

    draw_grid(block, grid)

    for x in grid:
        print(x)

    sc.mainloop()