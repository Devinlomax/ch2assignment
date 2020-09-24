# ingredient adjustster
# if 48 = 1.5 cups of sugar 
# then 10 =? 
#if 48 = 1 cup of butter 
# then 10 = ?
#if 48 = 2.75 cups of flour # then 10 = ?
# if 48 = 1.5 cups of sugar 
# then 60 =? 
#if 48 = 1 cup of butter 
# then 60 = ?
#if 48 = 2.75 cups of flour 
# then 60 = ?
# sugarpercookie = 0.03125 or 0.03
#butterpercookie = 0.02
#flourpercookie = 0.06
regularbatchofcookies = 48
cupsofsugarper48cookies = 1.5
cupsofbutterper48cookies = 1
cupsofflourper48cookies = 2.75

numberofcookies = float(input("How many cookies would you like to make?"))

expectedcupsofsugar = (numberofcookies / regularbatchofcookies) * cupsofsugarper48cookies

expectedcupsofbutter = (numberofcookies / regularbatchofcookies) * cupsofbutterper48cookies
expectedcupsofflour = (numberofcookies / regularbatchofcookies) * cupsofflourper48cookies

print("For" +str(numberofcookies) + "cookies"+ "you will need")
print("cups of sugar needed:" + str(expectedcupsofsugar))
print("cups of butter needed:" + str(expectedcupsofbutter))
print("cups of flour:" + str(expectedcupsofflour))