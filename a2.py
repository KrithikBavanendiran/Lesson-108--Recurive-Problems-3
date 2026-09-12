def Hanoi(n, a, b, c):
    if n == 1:
        print("Move disc 1 from rod", a,"to rod", b)
        return
    
    Hanoi(n-1, a, c, b)
    print("Move disc", n, "from rod", a,"to rod", b)
    Hanoi(n-1,c, b, a)

Hanoi(3, 'A', 'C', 'B')
