#The number of shares that Joe purchased was 2,000.
#When Joe purchased the stock, he paid $40.00 per share.
#Joe paid his stockbroker a commission that amounted to 3% of the amount Joe paid for the stock.
#Two weeks later Joe sold that stock. Here are the details of the sale.
#The number of shares that Joe sold was 2,000
#He sold the stock for $42.75 per share.
#He paid his stockbroker another commission that amounted for 3% of the amount Joe received for the stock.
#moneyperstock
#buyingcommissiontobroker
#stocksellprice
#sellingcomissiontobroker
#displaymoneyjoesbalance

numberofsharespurchased = 2000
amountpaidpershare = 40.00
amountpaidforstock = numberofsharespurchased * amountpaidpershare
commissionforbuying = 0.03 * amountpaidforstock
numberofsharessold = 2000
amountsoldpershare = 42.75 
amountstocksoldfor = numberofsharessold * amountsoldpershare
commissionforselling = 0.03 * amountstocksoldfor
profit = (amountstocksoldfor - commissionforselling) - (amountpaidforstock - commissionforbuying)

print("Amount Paid for Stock: $" + format(amountpaidforstock, ",.2f"),\
     "Commission for buying: $" + format(commissionforbuying, ",.2f"),\
     "Amount recieved for stock: $" + format(amountstocksoldfor, ",.2"),\
      "Commission for selling: $" + format(commissionforselling, ",.2f"), \
     "profit: $" + format(profit, ",.2f"),\
      sep= "\n")
