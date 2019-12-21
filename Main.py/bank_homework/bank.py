import os
import csv
Python_bank_homework_csv = os.path.join('..', 'bank_homework', 'budget_data.csv')

total_months = 0
total_profit = 0
value = 0
change = 0

months = []
profits = []

with open(Python_bank_homework_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    first_row = next(csvreader)
    total_months = 1
    total_profit = int(first_row[1])
    value = int(first_row[1])

    for row in csvreader:
        months.append(row[0])

        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])

        total_months = total_months + 1

        total_profit = total_profit + value

    greatest_inc = max(profits)
    increase_index = profits.index(greatest_inc)
    best_date = months[increase_index]

    greatest_dec = min(profits)
    decrease_index = profits.index(greatest_dec)
    worst_date = months[decrease_index]

    avg_date = sum(profits)/len(profits)

    print("Financial Analysis")
    print("---------------------")
    print("Total Months: " + str(total_months))
    print("Total: " + "$" + str(total_profit))
    print("Average Change: " +  "$" + str(round(avg_date,2)))
    print("Greatest Increase: " + (best_date) +" " + "$" + str(greatest_inc))
    print("Greatest Decrease: " + (worst_date) + " " + "$" + str(greatest_dec))