import turtle
import math


# Функція для малювання гілки дерева
def draw_pythagoras_tree(t, length, level):
    if level == 0:
        t.forward(length)
        t.backward(length)
        return

    t.forward(length)
    new_length = length * math.sqrt(2) / 2

    t.left(45)
    draw_pythagoras_tree(t, new_length, level - 1)
    t.right(45)

    t.right(45)
    draw_pythagoras_tree(t, new_length, level - 1)
    t.left(45)

    t.backward(length)


def main(level):
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.left(90)

    t.penup()
    t.goto(0, -200)
    t.pendown()

    draw_pythagoras_tree(t, 100, level)

    t.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    level = int(input("Введіть рівень рекурсії: "))
    main(level)
