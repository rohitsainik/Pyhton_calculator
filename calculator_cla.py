import re
print("                   welcome to the equation calculator           ")
print("                              1 2 3\n                              4 5 6\n                              7 8 9\n                              c % /\n                              + - * ")
num = 0
run = True

def perform_math():
    global run
    global num

    equation = input("enter the equation")
    e = str((equation))


    if equation == "c":
        run= False
    else:
        equation=re.sub('[a-zA-z()&$@#:,]', '', equation)
        num=eval(equation)
        print(num)


while run:
    perform_math()











