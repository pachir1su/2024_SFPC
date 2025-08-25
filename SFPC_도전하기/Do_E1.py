# Do_E1
def solve() :
    import sys

    input_data = sys.stdin.read().split()
    if len(input_data) < 2 :
        return

    k = int(input_data[0])
    a = int(input_data[1])

    peppers = [0] * k
    peppers[0] = a
    peppers[1] = a

    for i in range(2, k) :
        amount = peppers[i-1] + peppers[i-2]
        if amount >= 30 :
            peppers[i] = 1
        else:
            peppers[i] = amount
    
    print(peppers[k-1])

if __name__ == "__main__" :
    solve()