a = int(input())

andrea = []
for _ in range(a):
    andrea.append(int(input()))
m = int(input())
maria = []
for _ in range(m):
    maria.append(int(input()))

event = input("enter event: ").capitalize()
if event == "Even":
    start = 0
else:
    start = 1
score = 0

for i in range(start, len(andrea), 2):
    score += andrea[i] - maria[i]
if score > 0:
    print("Andrea ")
elif score < 0:
    print("Maria ")
else:
    print("Tie")