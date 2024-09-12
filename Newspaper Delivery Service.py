def main():
    #Initialize variables (newspaperPrice = 1.50, commissionRate = 2%, totalPapersDelivered, weeklySalary, tips, totalPay = 0)
    newspaperPrice = 1.50 #Price of newspaper for each customer
    commissionRate = .02 #2% commission earned for each delivered newspaper

    #Display welcome message
    print("\nWelcome to Alex's newspaper delivery service program") 
    print("\nThis program will calculate the amount earned from delivering newspapers, including any tips")

    #Prompt user for inputs for calculation
    dailyPapersDelivered = int(input("\nHow many newspapers delivered per day? ")) #Prompt user to enter # of newspapers delivered each day
    daysperWeek = int(input("\nHow many days per week did you deliver newspapers? ")) #Prompt user to enter # of days worked in the week
    tips = int(input("\nHow much did you recieve in tips this week? ")) #Prompt user to enter any tips earned for the week

    #Calculate and display 
    totalPapersDelivered = dailyPapersDelivered * daysperWeek #Calculates the weeks total of newspapers delivered
    weeklySalary = totalPapersDelivered * (newspaperPrice * commissionRate) #Calculates the weeks salary in commissions 
    totalPay = weeklySalary + tips #Calculates the total earned including commissions and tips
    
    print('\nTotal number of papers delivered per week:', totalPapersDelivered) #Displays total newspapers delivered
    print('Weekly salary from commissions: $', weeklySalary) #Displays the weeks salary in commissions
    print('\nTotal earned this week: $', totalPay)  #Displays the total dollar amount earned for the week delivering newspapers, including tips



main()
