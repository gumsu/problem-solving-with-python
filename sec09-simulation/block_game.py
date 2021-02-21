import turtle as t
import random as r

if __name__ == "__main__":
    sc = t.Screen()
    sc.bgcolor("black")
    sc.setup(width=600, height=700)
    grid = [[0]*12 for _ in range(24)]
    for x in grid:
        print(x)

    sc.mainloop()