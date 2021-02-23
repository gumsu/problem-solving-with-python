import turtle as t
import random as r
import time

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

class Brick():
    def __init__(self):
        self.y = 0
        self.x = 6
        self.color = r.randint(1,6)
    
    def move_left(self, grid):
        if grid[self.y][self.x-1] == 0 and grid[self.y+1][self.x-1] == 0:
            grid[self.y][self.x] = 0
            self.x-=1
    def move_right(self, grid):
        if grid[self.y][self.x+1] == 0 and grid[self.y+1][self.x+1] == 0:
            grid[self.y][self.x] = 0
            self.x+=1

def draw_grid(block, grid):
    block.clear()
    top = 250
    left = -150
    colors = ['black', 'red', 'blue', 'orange', 'yellow', 'green', 'purple', 'white']
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            sc_x = left+(x*22)
            sc_y = top-(y*22)
            block.goto(sc_x,sc_y)
            if y == 15 and grid[y][x] == 7:
                block.color("red")
            else:
                block.color(colors[grid[y][x]]) # 벽을 7로 생성했으므로 colors[7] 색으로 나타남
            block.stamp()

def DFS(y, x, grid, color):
    global check, blank
    check[y][x] = 1
    blank.append((y, x))
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 < xx < 13 and 0 < yy < 24:
            if grid[yy][xx] == color and check[yy][xx] == 0:
                DFS(yy, xx, grid, color)

# 블록이 가장 높이 쌓인 값
def max_height(grid):
    for y in range(1, 24):
        for x in range(1, 13):
            if grid[y][x] != 0: # 처음 블록 발견하면 리턴
                # print(y,x)
                return y

def grid_update(grid, blank):
    for y, x in blank:
        grid[y][x] = 0

    height = max_height(grid)

    for y in range(23, height, -1):
        for x in range(1, 13):
            if grid[y][x] == 0:
                tmp_y = y
                while grid[tmp_y-1][x] == 0 and tmp_y-1 > 0:
                    tmp_y -= 1
                grid[y][x] = grid[tmp_y-1][x]
                grid[tmp_y-1][x] = 0

def game_over():
    pen.up()
    pen.goto(-120, 100)
    pen.write("GAME OVER", font=("courier", 30))

def you_win():
    pen.up()
    pen.goto(-100, 100)
    pen.write("YOU WIN", font=("courier", 30))

if __name__ == "__main__":
    sc = t.Screen()
    sc.tracer(False)
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
    block.setundobuffer(None)

    brick = Brick()
    grid[brick.y][brick.x] = brick.color
    draw_grid(block, grid)

    pen = t.Turtle()
    pen.ht()
    pen.goto(-80, 290)
    pen.color("white")
    pen.write("Block Game", font=('courier', 20, 'normal'))

    sc.onkeypress(lambda: brick.move_left(grid), "Left")
    sc.onkeypress(lambda: brick.move_right(grid), "Right")
    sc.listen()

    while True:
        sc.update()
        if grid[brick.y+1][brick.x] == 0:
            grid[brick.y][brick.x] = 0
            brick.y += 1
            grid[brick.y][brick.x] = brick.color
        else:
            check = [[0]*14 for _ in range(25)]
            blank = []
            DFS(brick.y, brick.x, grid, brick.color)
            
            if len(blank) >= 4:
                grid_update(grid, blank)

            height = max_height(grid)

            if height <= 15:
                game_over()
                break

            elif height >= 22:
                draw_grid(block, grid)
                you_win()
                break

            brick=Brick()
    
        # for x in grid:
        #     print(x)
        # print()

        draw_grid(block, grid)
        time.sleep(0.05)

    sc.mainloop()