# Pre_A1
# 인삼 밭 초기화
field = [[0] * 10 for _ in range(10)]
total_sales = 0

# 재배 기간 입력
k = int(input())

for n in range(1,k+1):
    c, x1, y1, x2, y2 = map(int, input().split())
    if c == 0:
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if field[i][j] == 0:  # 인삼이 없으면 심기
                    field[i][j] = n  # 인삼 심기 (1년근)

    # 수확
    elif c == 1:
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if field[i][j] > 0:  
                    if n-field[i][j] == 4:
                        total_sales +=62000
                        field[i][j]=0
                    elif n-field[i][j] == 5:
                        total_sales +=68000
                        field[i][j]=0
                    elif n-field[i][j] == 6:
                        total_sales+=72000
                        field[i][j]=0
                    elif n-field[i][j] >= 7:
                        field[i][j]=0
                        pass
                    else:
                        pass

# 총 판매 금액 출력
print(total_sales)