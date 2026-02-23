import math
def runQuadratic():

    print("welcome! Enter a quadratic in ax^2 + bx + c form.")
    # input
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    def roots():
        # processing
        discriminate = math.sqrt((b ** 2)-4*a*c)

        if discriminate < 0:
            print("no real roots")
        elif discriminate == 0:
            x = -b / (2*a)
            print("one root: ", x)
        else:
            plus_answer = (-b + discriminate)/2*a
            minus_answer = (-b - discriminate)/2*a
            print("x = ", plus_answer, " ", minus_answer)
        
    def vertex_form():
        v_form = ""
        h = b/(2*a)
        k = (4*a*c - b**2)/(4*a)
        v_form += "y = a(x "
        if h > 0:
            v_form += "+ " + str(h) + ")^2"
        else:
            v_form += str(h) + ")^2"
        if k > 0:
            v_form += "+ " + str(k)
        else:
            v_form += str(k)
        print("Vertex form: ", v_form)
        

    def output():
        axis_sym = -b/(2*a)

        print("Properties")
        vertex_form()
        roots()
        print("y-int: (0,", c, ")")
        print()
        #axis of symmetry and vertex
        print("axis of symmetry: x = ", axis_sym)

        print("vertex: ", ( axis_sym), ",", (4*a*c - b**2)/(4*a), ")")
        if a < 0:
            print("max: ", axis_sym)
            print("Concave down")
        else: 
            print("min: ", axis_sym)
            print("Concave up.")
    output()
    
while(True):
    runQuadratic()
    clear = input("Press ENTER to clear")
    if clear == "":
        for i in range(10):
            print()
        continue
    else:
        break

    

    

