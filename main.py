from front import Game
from back import Rule

print("Enter rule number: ")
#rule = Rule(int(input()))
rule = Rule(487378)
print("Enter field size: ")
input_got = False
m, n = 0, 0
while not input_got:
    try:
        m, n = [int(i) for i in input().split()]
        if m > 0 and n > 0:
            input_got = True
        else:
            print('Invalid size, please try again: ')
    except ValueError:
        print('Invalid format, please try again: ')

print("Choose way to fill the field:\n1)manually\n2)random")
ans = int(input())
#ans = 2
game = Game(m, n, rule)
if ans != 1 and ans != 2:
    print("Couldn't recognise your answer, assuming random generation")
if ans == 1:
    game.run(True)
else:
    game.run(False)
