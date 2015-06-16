# ------------------------------------------- Counting Sundays ------------------------------------------------ #
#                                                                                                               #
#       You are given the following information, but you may prefer to do some research for yourself.           #
#                                                                                                               #
#           1 Jan 1900 was a Monday.                                                                            #
#           Thirty days has September,                                                                          #
#           April, June and November.                                                                           #
#           All the rest have thirty-one,                                                                       #
#           Saving February alone,                                                                              #
#           Which has twenty-eight, rain or shine.                                                              #
#           And on leap years, twenty-nine.                                                                     #
#           A leap year occurs on any year evenly divisible by 4, but not on a century unless it is             #
#           divisible by 400.                                                                                   #
#                                                                                                               #
#           How many Sundays fell on the first of the month during the twentieth century                        #
#           (1 Jan 1901 to 31 Dec 2000)?                                                                        #
# ------------------------------------------------------------------------------------------------------------- #
import time
import datetime

def eu19():
    BEGIN   = datetime.datetime(1901, 1, 1)
    END     = datetime.datetime(2000, 12, 31)
    SUNDAY  = 6
    
    cur = BEGIN
    count = 0

    while (cur < END):
        if (cur.weekday() == SUNDAY):
            count += 1

        if (cur.month == 12):
            cur = datetime.datetime(cur.year + 1, 1, 1)
        else:
            cur = datetime.datetime(cur.year, cur.month + 1, 1)

    return count
            

startTime = time.clock()
print (eu19())
elapsedTime = time.clock() - startTime
print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
