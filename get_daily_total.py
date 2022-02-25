# sales_data_history:
# - transaction_id (PK)
# - item_id
# - transaction_timestamp
# - item_price
# - item_quantity

# item_id | transaction_timestamp | item_price | item_quantity
# 1         2022-01-01 10:00AM      25           11

# For each day, report the item_id which has the maximum total quantity (across all transactions)

sales_data_history = [
    (1, '2022-01-01 10:00AM', 25, 11), (1, '2022-01-01 11:00AM', 10, 100), (1, '2022-01-02 10:00AM', 17, 35), 
    (2, '2022-01-01 10:00AM', 13, 50), (2, '2022-01-02 12:00PM', 75, 200), (2, '2022-01-02 2:00PM', 10, 150), 
    (2, '2022-01-03 11:00AM', 12, 60), (3, '2022-01-01 9:00AM', 13, 65), (3, '2022-01-02 11:30AM', 110, 70)
]

def get_daily_total(data):
    print(sales_data_history[0])

daily_total = get_daily_total(sales_data_history)
print(daily_total)