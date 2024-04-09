def calculate_chocolate_bars(total_money, price_per_bar):
    bars_affordable = int(total_money/price_per_bar)
    change_left_over = total_money - bars_affordable*price_per_bar
    return bars_affordable, change_left_over

# 函数调用示例
total_money = 100
price_per_bar = 7
bars, change = calculate_chocolate_bars(total_money, price_per_bar)
print(f"You can buy {bars} bars, with {change} left.")