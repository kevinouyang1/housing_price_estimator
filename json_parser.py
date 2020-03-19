# Taking data, break them down house by house until you are left with data that is only a sold date and a sold price
# Data shows houses sold from 2015-2019 and in the Crosby region of Richmond Hill in the GTA.
import json
from datetime import datetime

# import the data.json string and then read it line by line into a new string
price = []
chart = []


# Extract data and output it into price list, containing a dictionary for each house.
# Each dict contains date sold, sold price, type of the house (i.e. bungalow), and style (i.e. detached).
with open('data.json') as fin:
    for line in fin:
        final = json.loads(line)
        for element in range(len(final['d']['tables'][0]['rows'])) :

            date_epoch = final['d']['tables'][0]['rows'][element][12].replace('/Date(', '')
            date_epoch = date_epoch.replace('-0500)/', '')
            date_epoch = date_epoch.replace('-0400)/', '')
            sold_date = datetime.fromtimestamp(int(date_epoch) / 1000).strftime('%Y-%m-%d')
            house = {'date' : sold_date, 'sold-price' : final['d']['tables'][0]['rows'][element][6], 'type' : final['d']['tables'][0]['rows'][element][16], 'style' : final['d']['tables'][0]['rows'][element][7]}
            price.append(house)


# Output data given into a csv file, only giving date sold and the sold price
# Code below shows all houses filtered for only Bungalow and Detached homes
with open('crosby_filtered_bungalow+detached.csv', 'a') as the_file :
    for house in price :
        if (house['type'] == 'Bungalow') and house['style'] == 'Detached' :
            the_file.write(house['date'])
            the_file.write(',')
            the_file.write(str(house['sold-price']))
            the_file.write('\n')





