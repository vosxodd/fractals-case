# Case-study #9
# Developers:   Aksenov A. (%),
#               Soloveychik D. (%),
#               Labuzov A. (%)

# нужно сделать следующие фракталы: 1) бинарное дерево, 2) ветка, 3) кривая Коха (сделана в задании), 4) Кривая Минковского, 5) Ледяные фракталы, 
# 6) Кривая Леви, 7) Фрактал Дракон Хартера-Хейтуэя
# ледяной фрактал Андрей Геннадиевич рекомендовал построить каждому
# фрактал дракон это жесть, поэтому ни на кого конкретно одного он не ложится, кто смогёт тот молодец
# один из вариантов улучшения кода - добавление смены цвета во фракталах. Ляпота
# плюсом в работе будет рисование снежинок у некоторых фракталов

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

