# Do_D1
def solve() :
    import sys
    data = sys.stdin.read().strip().split()
    if not data :
        return

    n = int(data[0])  
    k = int(data[1])   
    prices = list(map(int, data[2:]))

    total_price = sum(prices)

    if total_price >= k :
        print(-1)
    else :
        print(k - total_price)

if __name__ == "__main__" :
    solve()