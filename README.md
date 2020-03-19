## What is it?

This is literally, a housing price estimator for houses sold in the GTA. Well, rather than estimating, the program draws in the cluttered data and breaks it down, house by house. The user, however, will need to modify the code and the data taken to be able to use the program for their needs. In the end, the program spits out, into a CSV file, the date sold and the sold price. This is then used, utilizing Microsoft Excel, to plot a scatterplot which then draws a trendline. 

## Background

Due to the recent housing bubble in the GTA, my parents were adamant about selling their house in Richmond Hill. Rather than guess using prices they saw nearby, this program was built for their needs to accurately see the best time to sell it.


## How it works

Firstly, the data is all compiled and then using Inspect Element, taken as code and copied into a text edit file. Then, the program extracts it from the file and begins to separate the cluttered code line by line. These new houses are then appended to a list. The houses, now dictionaries, contain four values, being the date it was sold, the sold price, the type of the house, and the style of the house. Finally, the program filters through and uses only the data of houses that are only a certain type and a certain style, and outputs the sold price and sold date into a CSV.
