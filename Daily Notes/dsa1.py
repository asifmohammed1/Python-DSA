
class cl1:
    def func1():
        t = 4

        for x in range(t):
            S = input()
            samlist = S
            samlistoutput = [samlist[0]]
            for i in range(1, len(samlist)):
                if samlist[i] != samlist[i-1]:
                    samlistoutput.append(samlist[i])
        return samlistoutput









