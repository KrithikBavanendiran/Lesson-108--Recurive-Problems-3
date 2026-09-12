def hanoi(n):
    if n==0:
        return 0
    return 2 * hanoi(n-1)+1

input("hanoi(n) is a function that coutns the no of moces required to move no of discs from peg A to peg C using peg B as auxiliary. Press Enter")
print("hanoi(1) = ", hanoi(1))
print("hanoi(2) = ", hanoi(2))

n=int(input("Enter the number of discs: "))
guess=int(input("What is hanoi(" + str(n) + ")? "))
input("hanoi(n) = 2 * hanoi(n-1)+1 move the stack twice plus the big disc once. Press Enter")
print("hanoi(" + str(n) + ")? ", hanoi(n), "your guess: ", guess)
if guess==hanoi(n):
    print("Correct!")
else:
    print("Incorrect! The correct answer is: ", hanoi(n))
