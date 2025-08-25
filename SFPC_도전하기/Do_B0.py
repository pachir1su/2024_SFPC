# Do_B0
def solve() :
    h, w = 4, 5
    init_x, init_y = 2, 3
    days = 5

    current = [[False]*w for _ in range(h)]
    current[init_x][init_y] = True

    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    for _ in range(days) :
        next_day = [[False]*w for _ in range(h)]
        
        for x in range(h) :
            for y in range(w) :
                if current[x][y] :
                    can_breed = False
                    for dx, dy in directions :
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w :
                            if not current[nx][ny] :
                                can_breed = True
                                next_day[nx][ny] = True
                    if can_breed :
                        next_day[x][y] = True
        
        current = next_day

    answer = sum(sum(1 for cell in row if cell) for row in current)
    print(answer)

if __name__ == "__main__" :
    solve()