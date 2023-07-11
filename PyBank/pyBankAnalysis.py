#Financial Analysis of PyBank budget_data.csv

#import dependencies
import os
import csv

#import data
budgetData = os.path.join("Resources", "budget_data.csv")

#read csv file
with open(budgetData) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip the header
    csvheader = next(csvreader)

    #set baseline variables
    totalMonths = []
    totalProfit = 0.00
    totalMonthlyChange = []
    grIncProfit = 0.00
    grIncDate = ""
    grDecProfit = 0.00
    grDecDate = ""
    prevProfit = 0.00

    for row in csvreader:

        #find the total months
        date = row[0]
        month = date.split("-") #find the month in each date. Dates are listed in a year-month format within csv
        totalMonths.append(month) #add each month to the list of total months

        #find the total profit from all months
        profit = float(row[1])
        totalProfit += profit

         # Calculate the increase or decrease in profits compared to the previous month
         # excluding the first month because there is no previous data to compare to
        if prevProfit != 0.0:
            monthlyChange = profit - prevProfit
            totalMonthlyChange.append(monthlyChange) #save the monthly change to calculate the average later
            if monthlyChange > grIncProfit:
                grIncProfit = monthlyChange
                grIncDate = row[0]
            if monthlyChange < grDecProfit:
                grDecProfit = monthlyChange
                grDecDate = row[0]

        prevProfit = profit  # Store the current month's profit for the next iteration

    #calculate average monthly change based on saved list of all monthly changes
    averageMonthlyChange = sum(totalMonthlyChange)/len(totalMonthlyChange)

#Format analysis
analysisSummary = f"""Financial Analysis
----------------------------
Total Months: {len(totalMonths)}
Total: ${totalProfit:.0f}
Average Change: ${averageMonthlyChange:.2f}
Greatest Increase in Profits: {grIncDate} ${grIncProfit:.0f}
Greatest Decrease in Profits: {grDecDate} ${grDecProfit:.0f}"""
#print analysis to terminal
print(analysisSummary)

#create text file for analysis summary
with open("pyBankAnalysis.txt","w") as summaryfile:
    summaryfile.write(analysisSummary)