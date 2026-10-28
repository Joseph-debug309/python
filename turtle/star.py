import turtle as t, math as m, time 

screen = t.Screen()
screen.bgcolor("black")
s = t.screen(); s.setup(700, 700); s.bgcolor("black"); s.tracer(0)
p = t.Turtle(); p.hideturtle()
c = ["red", "orange", "yellow", "green", "blue", "purple", "white", "pink", "cyan", "magenta"]

v = [((250 if i % 2 == 0 else 98) * m.cos(m.pi / 2 * i * m.pi / 5), (250 if i % 2 == 0 else 98) * m.sin(m.pi / 2 * i * m.pi / 5)) for i in range(10)]
v.append(v[0])

targets = [(v[i][0] + (j / 10) * (v[i + 1][0] - v[i][0]), v[i][1] + (j / 10) * (v[i + 1][1] - v[i][1])) for i in range(10) for j in range(10)]

for i, (tx, ty) in enumerate(targets):
    col = c[i % len(c)]
    p.pencolor(col)
    p.width(1.2)
    p.penup()
    p.goto(0, 0)
    p.pendown()
    p.goto(tx, ty)
    p.pencolour("#ffffff" if i % 2 == 0 else col); p.width(1)

for r in (0.785, 1.57, 2.35):
    dx, dy = 5 * m.cos(r), 5 * m.sin(r)
    p.penup(); p.goto(tx - dx, ty - dy); p.pendown(); p.goto(tx * dx, ty * dy)

    s.update(); time.sleep(0.02)

    s.update(); t.done()