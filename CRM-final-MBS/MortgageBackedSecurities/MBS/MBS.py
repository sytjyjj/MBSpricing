import pandas as pd
import math
import MonteCarloSimulators.Vasicek.vasicekMCSim

class MBS(object):
    def __init__(self, datelist,refinanccost,t_step,principle,mortrate,maturity):
        self.datelist = datelist
        minDay = min(datelist)
        maxDay = max(datelist)
        self.datelistlong = pd.date_range(minDay, maxDay).tolist()
        self.datelistlong = [x.date() for x in self.datelistlong]
        self.ntimes = len(self.datelistlong)
        self.prepay = []
        self.cashflow = []
        self.UPB = [] #unpaid balance
        # these three dataframes' datelist are monthly based, instead of daily
        self.principle = principle
        self.mortrate = mortrate
        self.maturity = maturity
        self.refinanccost = refinanccost



    def getPrepayment(self):
        self.datelist
        #from the datelist find out all the dates that are the end of month


        #get the corresponding libor for the specific date, output:dataframe of interest rate and date:rt


        #prepayment rate deciding function
        if rt > self.mortrate - self.refinanccost:
            prepay = 0
        elif rt < self.mortrate - self.refinanccost < rt_1:
            prepay = 0.05*(self.mortrate - self.refinanccost - rt)
        elif rt < rt_1 < self.mortrate - self.refinanccost:
            prepay = prepay_1 + 0.04*(self.mortrate - self.refinanccost - rt)
        else: prepay = 0

        return prepay

    def setCashFlow(self):
        # get cashflow without prepayment  cashflow is a dataframe
        n = math.pow((1+self.mortrate),self.maturity*12)
        monthpay = self.principle*self.mortrate*n/(n-1)
        for date in schedule:
            cashflow[date] = monthpay
            UPB[date] = self.principle # how to calculate the remaining principle
        return self.cashflow

    def getCashFlow(self):
        # update cashflow based on prepayment rate
        for date in prepay:
            if prepay[date] != 0:
                cashflow[date] = cashflow[date] +　prepay[date]*UPB[date-1]
                UPB[date] = self.principle
        
    
    
        




