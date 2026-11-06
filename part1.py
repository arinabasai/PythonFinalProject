#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Arina Basai 

"""

""""
In the fast-paced world of finance, hedge funds serve as a cornerstone for those seeking to grow wealth while sharing risks with experienced professionals. 
With countless options available, the challenge lies in choosing the right hedge fund.
By analysing the 2020 hedge fund database, this programme helps uncover trends, evaluate performance metrics, and provide insights into average returns by country and fund.
This empowers investors to make informed decisions and navigate the competitive landscape of hedge fund investments.
I used a part of the dataset other than one of those provided during the course. 
The dataset used can be found by using the following link: https://www.kaggle.com/datasets/ironbatshashank/top-100-global-hedge-funds-2020
"""

import numpy as np
import database as mymod
import os

def sum_returns(returns: list):
    """
    Calculates the sum of the returns.
    
    Parameters
    ----------
    returns : list
        List representing the returns of various hedge funds.

    Returns
    -------
    head + sum_returns(tail) : float
        The total sum of returns, calculated recursively.
        
    """

    if len(returns) > 0:
        head = returns[0]
        tail = returns[1:]
        return head + sum_returns(tail)
    elif len(returns) == 0:
        return 0
    
def average_returns_by_country(hedge_funds: dict):
    """
    Calculates the average returns of funds grouped by country.
    
    Parameters
    ----------
    hedge_funds : dict
        Dictionary with fund names as keys and a tuple as values. Each tuple contains:
            1) city_name: str
            2) country: str
            3) total assets: int
            4) return: float.

    Returns
    -------
    av_returns_coutry: dict
    A dictionary with countries as keys and their respective average returns.

    """
    country_data = {}
    for k, v in hedge_funds.items():
        country = v[1]
        returns = v[3]
        if country not in country_data.keys():
            country_data[country] = []
        country_data[country].append(returns)
    av_returns_country = {country: sum_returns(returns)/len(returns) for country, returns in country_data.items()}
    return av_returns_country

def sorted_returns(hedge_funds: dict):
    """
    Sorts the returns using Quicksort algorithm.
    
    Parameters
    ----------
    hedge_funds : dict
        Dictionary with fund names as keys and a tuple as values. Each tuple contains:
            1) city_name: str
            2) country: str
            3) total assets: int
            4) return: float.

    Returns
    -------
    np.array
        Sorted returns in ascending order.

    """
    returns_arr = np.array([v[3] for v in hedge_funds.values()], dtype = 'float64')
    if len(returns_arr) <= 1:
        return returns_arr
    pivot = returns_arr[-1]
    first_half = returns_arr[returns_arr < pivot]
    pivot_if_repetition = returns_arr[returns_arr == pivot]
    second_half = returns_arr[returns_arr > pivot]
    return np.concatenate((sorted_returns({k: v for k, v in hedge_funds.items() if v[3] in first_half}), pivot_if_repetition, sorted_returns({k: v for k, v in hedge_funds.items() if v[3] in second_half})))

def top_performing_funds(hedge_funds: dict, n: int):
    """
    Rearranges the hedge funds dictionary to reflect the top n funds based on returns.

    Parameters
    ----------
    hedge_funds : dict
        Dictionary with fund names as keys and a tuple as values. Each tuple contains:
            1) city_name: str
            2) country: str
            3) total assets: int
            4) return: float.
    n : int
        Number of top-performing funds to include.

    Returns
    -------
    top_funds: dict
        Dictionary of top n funds based on performance.

    """
    ranked_returns = sorted_returns(hedge_funds)[::-1]
    top_fund_names = []
    for r in ranked_returns:
        for k, v in hedge_funds.items():
            if v[3] == r and k not in top_fund_names:
                top_fund_names.append(k)
                break
    top_funds = {k: hedge_funds[k] for k in top_fund_names[:n]}
    return top_funds
    
def funds_in_profit_or_loss(hedge_funds: dict):
    """
    Separates funds into two groups (those with positive and negative returns).

    Parameters
    ----------
    hedge_funds : dict
        Dictionary with fund names as keys and a tuple as values. Each tuple contains:
            1) city_name: str
            2) country: str
            3) total assets: int
            4) return: float.

    Returns
    -------
    tuple of lists
       A tuple containing two lists:
           1) funds with positive returns
           2) funds with negative returns.
       Each list contains tuples of fund_name and return.
       
    """
    positive = [(k, v[3]) for k, v in hedge_funds.items() if v[3] > 0]
    negative = [(k, v[3]) for k, v in hedge_funds.items() if v[3] < 0]
    return (positive, negative)

def returned_assets(hedge_funds: dict):
    """
    Computes how many total assets were returned by each fund.

    Parameters
    ----------
    hedge_funds : dict
        Dictionary with fund names as keys and a tuple as values. Each tuple contains:
            1) city_name: str
            2) country: str
            3) total assets: int
            4) return: float.

    Returns
    -------
    np.ndarray
        An array of returned assets (total assets multiplied by returns) for each fund.
    """ 
    re_assets = np.array([v[2]*v[3] for v in hedge_funds.values()], dtype = 'float64')
    return re_assets
    
def main():
    #To ensure that the manually written module opens in Terminal:
    directory = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(directory, "hedge_funds_database.txt")
    hedge_funds = mymod.read_file(path)
    #Visible portion of the project:
    print("\nWelcome to hedge fund database analysis! Using the top 33 funds from the year 2020, we provide the help to choose the best funds for your needs")
    #Infinite "while" loops with try-except statements are used to ensure that the programme runs in case of a user mistake:
    while True:
           print(" ", "Choose an option:", " ", "1: Calculate the average return for each country listed in the database", "2: Display the top performing funds", "3: Display funds with positive/negative returns", "4: Calculate returned assets", "5: Exit programme", " ", sep = "\n")
           try:
               choice_1 = int(input("I choose the option:\n"))
               if choice_1 == 1:
                  print("\nWhen investing multinationally, it is important to understand overall characteristics of the foreign and domestic markets")
                  print("\nLet's see the results obtained from the 2020 data: ")
                  #calling the function to obtain the average return based on the performance of funds in each country used in the database:
                  av_returns_country = (average_returns_by_country(hedge_funds))
                  for k, v in av_returns_country.items():
                      #Since there is no "the" before the word "France", two different formatted string constructions are used:
                      if k == "US" or k == "UK":
                           print(f"The average return of hedge funds in the {k} reached {v} in 2020")
                      else:
                           print(f"The average return of hedge funds in {k} reached {v} in 2020\n")
               elif choice_1 == 2:
                  print("\nAn obvious first step of choosing a hedge fund is to see the top performers")
                  while True:
                         try:
                              n = int(input("How many top funds do you wish to see?\n"))
                              #calling the function to provide the user with n top performing funds with the name of the fund and corresponding place it holds:
                              top_funds = top_performing_funds(hedge_funds, n)
                              if n <= 33:
                                   rank = 1
                                   for top_funds in top_funds.items():
                                       print(f" The fund {top_funds[0]} was on position {rank} in the year 2020")
                                       rank += 1
                                   break
                              else:
                                   print("Please, use a whole number between 1 and 33") 
                         except:
                                 print("Please, choose a valid option") 
               elif choice_1 == 3:
                  print("\nHedge funds with both positive and negative returns can be interesting for investors using different portfolio techniques\n")
                  #calling the function to generate tuples with fund names and corresponding positive/negative returns:
                  pos_neg_r_funds = funds_in_profit_or_loss(hedge_funds)
                  while True:
                         try:
                             choice_2 = int(input("Do you want to see positive or negative returning funds?(1 - positive, 2 - negative)\n"))
                             if choice_2 == 1:
                                 #Index 0 stands for the "positive" part of the function output tuple
                                 for f in pos_neg_r_funds[0]:
                                     print(f" The fund {f[0]} had a positive return of {f[1]} in the year 2020")
                                 break
                             elif choice_2 == 2:
                                 #Index 1 stands for the "negative" part of the function output tuple
                                 for f in pos_neg_r_funds[1]:
                                     print(f" The fund {f[0]} had a negative return of {f[1]} in the year 2020")
                                 break
                             else:
                                print("Please, choose 1 or 2")
                         except:
                                 print("Please, choose a valid option h") 
               elif choice_1 == 4: 
                  print("\nFor further analysis, you may need various more advanced performance metrics. For instance, let's see the the fund returns in terms of assets\n")
                  while True:
                         try:
                             n = int(input("How many funds do you wish to see?\n"))
                             #calling the function to compute the funds' numerical returns in terns of assets:
                             r_a = returned_assets(hedge_funds)
                             hedge_funds_keys = list(hedge_funds.keys())
                             if n <= 33:
                                  for i in range(n):
                                        print(f" The fund {hedge_funds_keys[i]} returned {r_a[i]} assets in the year 2020")
                                  break
                             else:
                                print("Please, use a whole number between 1 and 33") 
                         except:
                                 print("Please, choose a valid option")     
               elif choice_1 == 5:
                  #Exit option:
                  print("\nThanks for using this programme!")
                  break
               else:
                  print("Please, choose a whole number from 1 to 5")
           except:
                   print("Please, choose a valid option")         
    return

if __name__ == "__main__":
    main()






