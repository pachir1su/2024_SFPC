# Do_B1
def solve() :
    import sys
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return

    h = int(input_data[0])   
    w = int(input_data[1])   
    x = int(input_data[2])  
    y = int(input_data[3])  
    n = int(input_data[4])  

    current = [[False]*w for _ in range(h)]
    current[x][y] = True

    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    for _day in range(n) :
        next_day = [[False]*w for _ in range(h)]
        
        for i in range(h) :
            for j in range(w) :
                if current[i][j] :
                    can_breed = False
                    for dx, dy in directions :
                        nx, ny = i+dx, j+dy
                        if 0 <= nx < h and 0 <= ny < w :
                            if not current[nx][ny] :
                                can_breed = True
                                next_day[nx][ny] = True
                    if can_breed :
                        next_day[i][j] = True
        
        current = next_day
    answer = 0
    for i in range(h) :
        for j in range(w) :
            if current[i][j] :
                answer += 1

    print(answer)

if __name__ == "__main__" :
    solve()