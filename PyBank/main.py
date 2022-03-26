
# reading in the budget_data.csv file

#import packages needed to read csv file
import os
import csv
print(os.path.abspath('.'))

csvpath = os.path.join('', 'Resources', 'budget_data.csv')

profit=[]
monthly_changes=[]
date=[]

count=0
total=0
total_change_profit=0
initial_profit=0


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")



    for row in csvreader:
        count+=1
        date.append([0])

        profit.append([1])
        total+=int(row[1])

        final_profit=int(row[1])
       
    for i in range(1,count):
        monthly_changes.append(count[i]-count[i-1])

        average=sum(monthly_changes)/len(monthly_changes)

    print(monthly_changes)

  