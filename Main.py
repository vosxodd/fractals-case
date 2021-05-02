# Case-study #9
# Developers:   Aksenov A. (35%),
#               Soloveychik D. (40%),
#               Labuzov A. (46%)

from turtle import *
import math

def ice(order, size): # ледяной фрактал
    if order == 0:          
        forward(size)
    else:
        ice(order-1, size/2)   
        left(90)
        ice(order-1, size/4)
        left(180)
        ice(order-1, size/4)
        left(90)
        ice(order-1, size/2)
        
        
def branch(n, size): # ветка
    if n == 0:
        left(180)
        return
    x = size/(n+1)
    for i in range(n):
        forward(x)
        left(45)
        branch(n-i-1, 0.5*x*(n-i-1))
        left(90)
        branch(n-i-1, 0.5*x*(n-i-1))
        right(135)
    forward(x)
    left(180)
    forward(size)
    
    
def levi(order, size): # фрактал Леви
    if order == 0:          
        forward(size)
    else:
        left(45)
        levi(order-1, size)   
        right(90)
        levi(order-1, size)
        left(45)
        
        
def mincovski(order, size): # Кривая Минковского
    if order == 0:
        forward(size)
    else:
        mincovski(order - 1, size / 4)
        left(90)
        mincovski(order - 1, size / 4)
        right(90)
        mincovski(order - 1, size / 4)
        right(90)
        mincovski(order - 1, size / 4)
        mincovski(order - 1, size / 4)
        left(90)
        mincovski(order - 1, size / 4)
        left(90)
        mincovski(order - 1, size / 4)
        right(90)
        mincovski(order - 1, size / 4)

        

def draw_tree(height, angle): #Двоичное дерево
    left(90)
    draw_branch(height, angle)


def draw_branch(height, angle): #Вспомогательная функция для двоичного дерева
    if height == 0:
        return
    length = 200 * (height / 10)
    rat = math.cos(math.radians(angle))
    print(rat)
    fd(length)
    rt(angle)
    draw_brach(height - 1, angle)
    lt(angle * 2)
    draw_brach(height - 1, -angle)
    rt(angle)
    fd(-length)
    
    
def koch(order, size):
    if order == 0:
        forward(size)
    else:
        koch(order-1, size/3)
        left(60)
        koch(order-1, size/3)
        right(120)
        koch(order-1, size/3)
        left(60)
        koch(order-1, size/3)    
    
    
def main():
    speed(500)
    up()
    goto(0,0)
    down()
    choice = input('Выберите фрактал для рисования из следующих:\n1) ледяной фрактал  2) бинарное дерево  3) ветка  4) кривая Коха  5) кривая Минковского  6) кривая Леви\n').lower()
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    if choice == 'ледяной фрактал':
        ice(n, a)
    elif choice == 'бинарное дерево':
        draw_tree(n, a)
    elif choice == 'ветка':
        branch(n, a)
    elif choice == 'кривая коха':
        koch(n, a)
    elif choice == 'кривая минковского':
        mincovski(n, a)
    elif choice == 'кривая леви':
        levi(n, a)
    mainloop()

main()
