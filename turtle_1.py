from turtle import *
color('blue', 'green')
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break 
done()