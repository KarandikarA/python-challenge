# import library
import os
import csv

# join path
budget_data = os.path.join('PyBank','Resources', "budget_data.csv")

# opens and reads the csv
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")
    
    # finds the net amount of loss and profit
    P = []
    months = []

    # code reads each row of data  
    for rows in csvreader:
        P.append(int(rows[1]))
        months.append(rows[0])

    # finds the revenue change
    revenue_change =[]

    for x in range(1, len(P)):
        revenue_change.append((int(P[x]) - int(P[x-1])))

    # calculates the average revenue change
    revenue_average_change = sum(revenue_change) / len(revenue_change)
    revenue_average = round(revenue_average_change, 2)

    # calculates the length of months
    total_months = len(months)

    # finds the greatest increase in revenue
    greatest_increase = max(revenue_change)

    # finds the greatest decrease in revenue
    greatest_decrease = min(revenue_change)


    # prints the Results
    print ("Financial Analysis")

    print("....................................................................................")

    print ("Total Months:" + str(total_months))

    print("Total:" + "$" + str(sum(P)))

    print ("Average Change:" + "$" + str(revenue_average))

    print("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "($" + str(greatest_increase) + ")")

    print("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "($" + str(greatest_decrease) + ")")


    # sends the output to a txt file
    file = open("output1.txt","w")

    file.write("Financial Analysis" + "\n")

    file.write("...................................................................................." + "\n")

    file.write("total months: " + str(total_months) + "\n")

    file.write("Total: " + "$" + str(sum(P)) + "\n")

    file.write("Average change: " + "$" + str(revenue_average) + "\n")

    file.write("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "($" + str(greatest_increase) + ")\n")

    file.write("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "($" + str(greatest_decrease) + ")\n")

    file.close()