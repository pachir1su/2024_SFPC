# Do_D0
def solve() :
    total_money = 54000
    basket_prices = [4900, 5000, 5100, 5200, 5500, 5500, 6000, 6500, 7000]
    current_sum = sum(basket_prices)

    if current_sum >= total_money :
        print(0)
    else :
        print(total_money - current_sum)

if __name__ == "__main__":
    solve()