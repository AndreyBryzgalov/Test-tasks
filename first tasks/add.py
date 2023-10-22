def min_coins(i):
    coins = [1,9,10]  # Доступные номиналы монет
    dp = [float('inf')] * (i + 1)  # Создаем список для хранения минимального количества монет для каждой суммы
    dp[0] = 0  # Нулевая сдача не требует монет

    prev_coin = [-1] * (i + 1)  # Список для отслеживания предыдущей монеты для каждой суммы

    # Вычисляем минимальное количество монет для каждой суммы от 1 до i
    for j in range(1, i + 1):
        for coin in coins:
            if j >= coin and dp[j - coin] + 1 < dp[j]:
                dp[j] = dp[j - coin] + 1  # Обновляем минимальное количество монет
                prev_coin[j] = coin  # Запоминаем предыдущую монету для данной суммы

    used_coins = []
    while i > 0:
        coin = prev_coin[i]  # Получаем предыдущую монету для текущей суммы
        used_coins.append(coin)  # Добавляем ее в список используемых монет
        i -= coin  # Вычитаем номинал монеты из текущей суммы

    used_coins.reverse()  # Переворачиваем список, чтобы монеты шли в порядке возрастания номинала
    return dp[-1], used_coins  # Возвращаем минимальное количество монет и список используемых монет

# Пример использования:
i = 18  # Пример сдачи, которую нужно вернуть
min_coins_count, used_coins = min_coins(i)
print(f"Минимальное количество монет для возврата сдачи {i}: {min_coins_count}")
print(f"Используемые монеты: {used_coins}")