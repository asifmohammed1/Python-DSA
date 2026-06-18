# for input use:
# inputString = input()

# (A[0]+A[1]+……+A[i-1]) =  (A[i+1]+A[i+2]+……..+A[n-1])

# A[1]+A[2]+…….+A[n-1] = 0  (0)
# A[0]+A[1]+…….+A[n-2] = 0 (n-1)

# A[0] + A[1] + A[2] .... + A[n] == A[-1] + A[-2] + ....+ A[-n]


# inpu = input() # "3,-4, 2, -1,-3, 2, 1"
# B = inpu.split(",")
# A = []
# for i in B:
#    z = i.replace(" ", "")
#    A.append(int(z))

# A = [int(i) for i in input().split(",")]
A = list(map(int, input().split(",")))

sumofA = sum(A)  # 0
left_side = 0  # 3,-4, 2, -1,-3, 2, 1
eq = -1

for i in range(len(A)):
    right_side = - left_side - A[i]  # - A[i-1] - A[i]
    if left_side == right_side:
        eq = A[i]
        break
    left_side += A[i]

print(eq)  # 2
