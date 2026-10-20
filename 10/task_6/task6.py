import csv
import random
from datetime import date, timedelta

PRICES = {
    'Book': 500,
    'Pen': 80,
    'Notebook': 60,
    'Pencil': 30,
    'Backpack': 2500,
    'Calculator': 1200,
}


def make_broken_row():
    day = date(2026, 1, 1).isoformat()
    product = random.choice(list(PRICES))
    kind = random.randint(1, 5)
    if kind == 1:
        return [day, product, 'abc', PRICES[product]]
    if kind == 2:
        return [day, product, 3]
    if kind == 3:
        return [day, product, -2, PRICES[product]]
    if kind == 4:
        return [day, product, 3, '']
    return ['2026-13-45', product, 3, PRICES[product]]


def generate_sales_file(path, count=5000, error_share=0.05, seed=None):
    random.seed(seed)
    start = date(2026, 1, 1)
    broken = 0
    with open(path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['date', 'product', 'quantity', 'price'])
        for _ in range(count):
            day = start + timedelta(days=random.randint(0, 364))
            product = random.choice(list(PRICES))
            quantity = random.randint(1, 20)
            writer.writerow([day.isoformat(), product, quantity, PRICES[product]])
            if random.random() < error_share:
                writer.writerow(make_broken_row())
                broken += 1
    return count, broken


def parse_row(s):
    if len(s) != 4:
        raise ValueError(f'ожидалось 4 поля, получено {len(s)}')
    day, product, quantity_text, price_text = s
    date.fromisoformat(day)
    quantity = int(quantity_text)
    price = float(price_text)
    if not product:
        raise ValueError('пустое название товара')
    if quantity <= 0 or price < 0:
        raise ValueError('количество и цена должны быть положительными')
    return day, product, quantity, price


def analyze_sales(path):
    TotalMoneySpent = 0
    purchases = 0
    skipped = 0
    GoodsSold = {}
    MoneyGained = {}
    BestDay = {}

    with open(path, 'r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        if next(reader, None) is None:
            return None
        for s in reader:
            try:
                day, product, quantity, price = parse_row(s)
            except ValueError:
                skipped += 1
                continue
            money = quantity * price
            TotalMoneySpent += money
            purchases += 1
            GoodsSold[product] = GoodsSold.get(product, 0) + quantity
            MoneyGained[product] = MoneyGained.get(product, 0) + money
            BestDay[day] = BestDay.get(day, 0) + money

    if purchases == 0:
        return {'purchases': 0, 'skipped': skipped}

    maxsold = max(GoodsSold, key=GoodsSold.get)
    MaxMoneyGained = max(MoneyGained, key=MoneyGained.get)
    best_day = max(BestDay, key=BestDay.get)
    return {
        'TotalMoneySpent': TotalMoneySpent,
        'maxsold': (maxsold, GoodsSold[maxsold]),
        'MaxMoneyGained': (MaxMoneyGained, MoneyGained[MaxMoneyGained]),
        'average': TotalMoneySpent / purchases,
        'BestDay': (best_day, BestDay[best_day]),
        'purchases': purchases,
        'skipped': skipped,
    }


def print_report(stats):
    if stats is None:
        print('Файл пуст')
        return
    if stats['purchases'] == 0:
        print(f"Нет корректных записей (пропущено: {stats['skipped']})")
        return
    print(f"Общая сумма продаж: {stats['TotalMoneySpent']:.2f}")
    print(f"Самый продаваемый товар: {stats['maxsold'][0]} ({stats['maxsold'][1]} шт.)")
    print(f"Наибольшая выручка: {stats['MaxMoneyGained'][0]} ({stats['MaxMoneyGained'][1]:.2f})")
    print(f"Средняя стоимость покупки: {stats['average']:.2f}")
    print(f"День с максимальной выручкой: {stats['BestDay'][0]} ({stats['BestDay'][1]:.2f})")
    print(f"Корректных записей: {stats['purchases']}, пропущено: {stats['skipped']}")
