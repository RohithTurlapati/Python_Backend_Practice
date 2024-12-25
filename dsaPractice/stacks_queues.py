from collections import deque


# Stack implementation

stk = []

# appending in the end
stk.append(3)
stk.append(5)
stk.append(7)

# popping from the last after checking if the stack is not empty
if stk:
    stk.pop()

# peek
print(stk[-1])
print(stk)

# Queue implementation using deque(double ended queue)

de = deque(stk)

de.appendleft(2)
de.append(8)
de.insert(10,5)
print(de)
print(de.index(5))
de.popleft()
print(de)
de.remove(2)
print(de)
de.reverse()
print(de)
de.rotate(-2)
print(de)
de.rotate(1)
print(de)


