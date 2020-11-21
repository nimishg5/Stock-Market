from emailMessageResultModel import setEmailMessage
from patterns import *

def crossovers_analyzer(df, key1, key2, interval, ticker):
    crossover = ''
    closedPriceLowerThanDma = False
    counter = 0
    emailMessage = ''
    print_stars()
    print_startEndPattern_to_distinguish('start', key1, key2)
    for index in df.index:
        if counter == 0:
            closedPriceLowerThanDma = df[key1][index] < df[key2][index]

        if df[key1][index] > df[key2][index] and closedPriceLowerThanDma:
            closedPriceLowerThanDma = not closedPriceLowerThanDma
            crossover = 'Last Golden Cross Over occoured on ' + str(df['timestamp'][index])
        elif df[key1][index] < df[key2][index] and (not closedPriceLowerThanDma):
            closedPriceLowerThanDma = not closedPriceLowerThanDma
            crossover = 'Last Death Cross Over occoured on ' + str(df['timestamp'][index])
        counter = counter + 1
 
    print('crossover value is : ' + str(crossover))
    if bool(crossover):
        emailMessage +=  crossover + ' for Script :' + ticker + ' on ' + key1 + ' vs ' + key2 + ' with interval as ' + interval
        print('Cross Over Occoured for Script :' + ticker + ' on ' + key1 + ' vs ' + key2 + '  : '+ str(crossover) + ' on interval : ' + interval)

    print_startEndPattern_to_distinguish('end', key1, key2)
    print_stars()
    setEmailMessage(emailMessage)