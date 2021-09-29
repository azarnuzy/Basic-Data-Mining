vec = [-1,-2,2,3,-3]
l1 = [x for x in vec if x >= 0]
print(l1)

l2 = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(l2)
