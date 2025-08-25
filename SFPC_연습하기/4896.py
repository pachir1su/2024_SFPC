def main() :
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    dx = min(x2, x4) - max(x1, x3)
    dy = min(y2, y4) - max(y1, y3)
    
    if dx < 0 or dy < 0 :
        print("NULL")
        return

    if dx > 0 and dy > 0 :
        print("FACE")
        return

    if dx == 0 and dy == 0 :
        print("POINT")
        return

    print("LINE")


if __name__ == "__main__" :
    main()