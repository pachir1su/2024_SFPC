# Pre_B1
def main() :
    import sys
    input = sys.stdin.readline

    n = int(input().strip())
    farms = []
    for _ in range(n) :
        data = input().split()
        name = data[0]
        weight = float(data[1])
        farms.append((name, weight))

    sorted_farms = sorted(farms, key=lambda x: x[1], reverse=True)

    rank_dict = {}
    for rank, (name, _) in enumerate(sorted_farms, start=1) :
        rank_dict[name] = rank

    for name, _ in farms:
        print(name, rank_dict[name])

if __name__ == "__main__" :
    main()