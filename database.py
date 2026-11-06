#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Arina Basai 

"""

""""
I used a part of the dataset other than one of those provided during the course. 
The dataset used can be found by using the following link: https://www.kaggle.com/datasets/ironbatshashank/top-100-global-hedge-funds-2020
"""

import io
import os

def read_file(filename = 'hedge_funds_database.txt'):
    """
    Reads the hedge funds database from a file and loads it into a dictionary.
    Each fund's name is a key, and its details (city, country, assets, returns) are stored in a tuple.
    
    
    Parameters
    ----------
    filename : str
        the file containing the dataset 'hedge_funds_database.txt'.

    Returns
    -------
    dict: A dictionary of hedge funds with their details.

    """
    
    if os.path.isfile(filename):
        with io.open(filename, 'r') as file:
            hedge_funds = {}
            line = file.readline()
            while line!= '':
                line = line.split("\" ")
                fund_name = line[0][1:]
                city = line[1].split()[:-3]
                if len(city) == 1:
                    city_name = city[0]
                elif len(city) == 2:
                    city_name = f"{city[0]} {city[1]}"
                elif len(city) == 3:
                    city_name = f"{city[0]} {city[1]} {city[2]}"
                country = line[1].split()[-3]
                assets = int(line[1].split()[-2])
                returns = float(line[1].split()[-1])
                if fund_name not in hedge_funds.keys():
                    hedge_funds[fund_name] = (city_name, country, assets, returns)
                line = file.readline() 
            return hedge_funds
    else:
            return None