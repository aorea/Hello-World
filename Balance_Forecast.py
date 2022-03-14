from datetime import date, timedelta

#bill links the name of the bill to the amount
#bill_day links the day of the payment to the bill name
bill = {"Rent+Phone":845,"Prime":100,"Electric":60,"Freedom":700,"CarInsurance":75}
bill_day = {1:"Rent+Phone",2:"Prime",15:"Electric",19:"Freedom",21:"CarInsurance"}
pay = 1850 #standard pay per payday
save = 1050 #amount going in to the savings account
first_pay = date(2022,1,7)
s_pay = first_pay #initializing start of the period
months = {s_pay.month:1} #initializing the dictionary with the first month
start = 1000 #initial balance
costs = []
balance = []
mgs = []

while True:
    cost = 0 #initialize the cost for every period
    n_pay = s_pay+timedelta(weeks = 2)

    if n_pay.year > s_pay.year: #don't add to months if the last period goes into the next year
        pass
    elif n_pay.month in months: #searches if the month and adds 1 or starts at 1
        months[n_pay.month] += 1 
    else:
        months[n_pay.month]=1
        
    if n_pay.month == s_pay.month: #for periods within a calendar month
        for i in bill_day:
            if i > s_pay.day and i <= n_pay.day:
                cost += bill[bill_day[i]]
    else: #for periods between two calendar months
        for i in bill_day:
            if i > s_pay.day:
                cost += bill[bill_day[i]]
            if i <= n_pay.day:
                cost += bill[bill_day[i]]
                
    if months[n_pay.month] < 3: #Only adds to savings twice a month
##        cost += save
        s = save
        mgs.append(save)
    else:
        s = 0
        mgs.append(0)
        
    costs.append(cost)
    print(str(s_pay) + " to " + str(n_pay) + " : " + str(cost) + " : " + str(s))
    if n_pay.year > s_pay.year: # Only does one year
        break
    s_pay = n_pay #Reinitialize the new starting day

prev = start
##for j in costs,mgs:
for j in range(0,len(costs)):
##    period_balance = prev - j - + pay
    period_balance = prev - costs[j] - mgs[j] + pay
    balance.append(period_balance)
    prev = period_balance
##    print(str(s_pay) + " to " + str(n_pay) + " : " + str(period_balance))\
