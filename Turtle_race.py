# Coded by Yashowardhan Shinde
import turtle
import random

print('''
This is a game of Turtle Race you can bet your Money on any of the four Turtles.
Along with you 3 more people will place their bets on the turtle they want.
The people placing the bets is the computer and not a real person.
Depending on the winner or the Race the people who had placed their money 
on the winning turtle will split the pot between them.
The Turtle Codes are:
1> Red(1)
2> Purple(2)
3> Blue(3)
4> Yellow(4)
The catch in this betting is that that you can bet very little and win a fortune or 
bet a huge amount and lose it all there is no middle ground.
''')
a = input('Enter your name:')
turtle_ = int(input('Enter the code of turtle you want to bet on : '))
if turtle_ > 4:
    print('The code that u have entered does not exist, Plaese enter a valid code')
    turtle_ = int(input('Enter the code of turtle you want to bet on : '))
money = int(input('Enter the amount of money you want to bet on the turtle'))

# Initializing the game window and the turtles
def race(a, turtle_, money):
    window = turtle.Screen()
    window.bgcolor('green')
    window.setup(600, 600)
    window.title('TURTLE RACE')

    t1 = turtle.Turtle()
    t1.speed(100)
    t1.hideturtle()
    t1.penup()
    t1.goto(0, 200)
    t1.pendown()
    t1.write('TURTLE RACE', False, 'center', ('Arial', 25, 'bold'))
    t1.penup()
    t1.goto(215, 150)
    t1.right(90)
    t1.pensize(20)
    t1.pendown()
    for i in range(5):
        t1.color('black')
        t1.forward(25)
        t1.color('white')
        t1.forward(25)
    t1.penup()
    t1.goto(235, 150)
    t1.pendown()
    for i in range(5):
        t1.color('white')
        t1.forward(25)
        t1.color('black')
        t1.forward(25)

    t2 = turtle.Turtle()
    t2.hideturtle()
    t2.penup()
    t2.goto(-300, -150)
    t2.pensize(1)
    t2.pendown()
    t2.fillcolor('brown')
    t2.speed(500)
    t2.begin_fill()
    for j in range(2):
        t2.forward(600)
        t2.right(90)
        t2.forward(250)
        t2.right(90)
    t2.end_fill()

    turtle1 = turtle.Turtle()
    turtle1.shape('turtle')
    turtle1.color('red')
    turtle1.speed(0)
    turtle1.penup()
    turtle1.goto(-250, 100)
    turtle1.pendown()

    turtle2 = turtle.Turtle()
    turtle2.shape('turtle')
    turtle2.color('purple')
    turtle2.speed(0)
    turtle2.penup()
    turtle2.goto(-250, 50)
    turtle2.pendown()

    turtle3 = turtle.Turtle()
    turtle3.shape('turtle')
    turtle3.color('blue')
    turtle3.speed(0)
    turtle3.penup()
    turtle3.goto(-250, 0)
    turtle3.pendown()

    turtle4 = turtle.Turtle()
    turtle4.shape('turtle')
    turtle4.color('yellow')
    turtle4.speed(0)
    turtle4.penup()
    turtle4.goto(-250, -50)
    turtle4.pendown()

    window.delay(10)

    for i in range(147):
        turtle1.forward(random.randint(1, 5))
        turtle2.forward(random.randint(1, 5))
        turtle3.forward(random.randint(1, 5))
        turtle4.forward(random.randint(1, 5))
    
    # Determining the winner of the race and printing the result
    x = turtle1.xcor()
    y = turtle2.xcor()
    z = turtle3.xcor()
    w = turtle4.xcor()
    winner = [x, y, z, w].index(max([x, y, z, w]))
    t3 = turtle.Turtle()
    t3.hideturtle()
    t3.penup()
    t3.goto(0, -200)
    t3.write('RESULTS', False, 'center', ('Arial', 16, 'bold'))
    t3.goto(0, -230)
    t3.write(f'Turtle1 :{x}, Turtle2 :{y}, Turtle3: {z}, Turtle4 :{w}', False, 'center', ('Arial', 14, 'bold'))
    t3.goto(0, -260)
    t3.write(f'The Winner of the Race is: Turtle{winner+1}', False, 'center', ('Arial', 16, 'underline'))
    window.exitonclick()
    
    # Initializing the betters and calculating the winners of the betting 
    b = 'Tim'
    c = 'Leonerd'
    d = 'Sheldon'
    turtle_b = random.randint(1, 4)
    turtle_c = random.randint(1, 4)
    turtle_d = random.randint(1, 4)
    pool = [turtle_, turtle_b, turtle_c, turtle_d]
    money_b = random.randint(1000, 100000)
    money_c = random.randint(1000, 100000)
    money_d = random.randint(1000, 100000)
    total_money_pool = money + money_b + money_c + money_d
    count_winners = 0
    win = [a, b, c, d]
    losers = []
    for k in range(len(pool)):
        if pool[k] == winner + 1:
            count_winners += 1
        else:
            losers.append(win[k])
            win[k] = 0
    win = [m for m in win if m != 0]
    if count_winners == 0:
        print('All the betters have lost their money')
    else:
        prize = total_money_pool / count_winners
        for l in win:
            print(f'Congratulations {l} you won {prize} Rs.')
        for _ in losers:
            print(f'Sorry {_} you lost all your money')


# Function call
race(a, turtle_, money)

