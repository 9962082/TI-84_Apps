import math

def main():

    #start message
    print("Quadratic Solver")

    # input
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    # processing
    discriminate = math.sqrt((b ** 2)-4*a*c)

    if discriminate < 0:
        print("no solution")
    elif discriminate == 0:
        x = -b / (2*a)
        print("one solution: ", x)
    else:
        plus_answer = (-b + discriminate)/2*a
        minus_answer = (-b - discriminate)/2*a
        print("x = ", plus_answer, " ", minus_answer)

main()