#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 11:46:52 2020

@author: taylor
"""
#importing random to later draw from a random uniform distribution
import random as ra

#creating class Portfolio() with attributes cash, stock, mf and hist
class Portfolio():    
    def __init__(self, cash = 0, stock = {}, mf = {}, hist = []): #initialize instance of class Portfolio with parameter name
        self.cash = cash
        self.stock = stock
        self.mf = mf
        self.hist = hist
    
    #create function to add cash    
    def addCash(self, addedCash):
        if type(addedCash) in {int, float}:
            self.cash += addedCash #update cash amount
            self.hist.append("Deposited $" + str(addedCash)) #add transaction history
            return self
        else: return print("Please enter a cash amount in the form of a float or integer.")

    #create function to withdraw cash
    def withdrawCash(self, withdrawal):
        if self.cash >= withdrawal:
            self.cash = self.cash - withdrawal #update cash amount
            self.hist.append("Withdrew" + str(withdrawal)) #add transaction history
            return self
        else: return print("There is not enough money in this account to withdraw that amount.")
    
    #create function to buy stock
    def buyStock(self, shares, stock):
        self.cash = self.cash - shares * stock.stockPrice #update cash amount
        self.stock[stock.stockTick] = stock.stockPrice #add stock to portfolio
        self.hist.append("Bought " + str(shares) + " shares of stock " + str(stock.stockTick)) #add transaction history
        return self
    
    #create function to buy mutual fund
    def buyMutualFund(self, mfTick, shares):
        self.cash = self.cash - shares #update cash amount
        self.mf[mfTick.mfTick] = shares #add mutual fund to portfolio
        self.hist.append("Bought " + str(shares) + " shares of mutual fund " + str(mfTick.mfTick)) #add transaction history
        return self
    
    #create function to sell mutual fund
    def sellMutualFund(self, mfTick, mfShares):
        self.cash = self.cash + mfShares * round(ra.uniform(0.9, 1.2),2) #update cash amount
        del self.mf[mfTick.mfTick] #remove mf from portfolio
        self.hist.append("Sold " + str(mfShares) + " shares of mutual fund " + str(mfTick.mfTick)) #add transaction history
        return self
    
    #create function to sell stock
    def sellStock(self, stockPrice, stockTick):
        self.cash = self.cash + stockTick.stockPrice * round(ra.uniform(0.9 * stockPrice, 1.2 * stockPrice),2) #update cash amount
        del self.stock[stockTick.stockTick] #remove stock from portfolio
        self.hist.append("Sold " + str(stockPrice) + " shares of stock " + str(stockTick.stockTick)) #add transaction history
        return self
    
    #create function to print transaction history
    def history(self):   
        print(self.hist)
    
    #defining what prints out when calling print()
    def __str__(self):
        return "Cash: $" + str(round(self.cash, 2)) + "\n" + "Stock: " + str(self.stock) + "\n" + "Mutual Funds: " + str(self.mf)
  
#define class Stock()
class Stock():
    def __init__(self, stockPrice, stockTick):#, stockShares = 0):
      self.stockPrice = stockPrice
      self.stockTick = stockTick
      #self.stockShares = stockShares

#define class MutualFund()
class MutualFund():
    def __init__(self, mfTick, mfShares = 0):
        self.mfTick = mfTick
        self.mfShares = mfShares
        
        
##########################################     
#testing out the required functionalities:
##########################################

#creating a retirement portfolio
retirement = Portfolio(cash = 1000)

#adding money to retirement
retirement.addCash(200.2)

#withdrawing money from portfolio
retirement.withdrawCash(100)

#creating a stock s with a price and ticker
s = Stock(20, "HFH")

#buying 5 shares of stock
retirement.buyStock(shares = 5, stock = s)

#selling stock
retirement.sellStock(1, s)

#creating mutual funds
mf1 = MutualFund("BRT")
mf2 = MutualFund("GHT")

#buying shares of mutual funds with retirement portfolio
retirement.buyMutualFund(mf1, 10.3) #Buys 10.3 shares of "BRT"
retirement.buyMutualFund(mf2, 2) #Buys 2 shares of "GHT"

#selling shares of mutual fund
retirement.sellMutualFund(mf2, 2)

#print out what is left in portfolio
print(retirement)

#print out all successful transactions from this portfolio
retirement.history()