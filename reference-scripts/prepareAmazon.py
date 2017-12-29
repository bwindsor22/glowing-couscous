#Script used to help prepare these datasets from raw sources. Not needed for the exercise.

import pandas as pd
import time
import datetime

# initialize data frames
df = pd.DataFrame(
    columns=('ASIN', 'TITLE', 'GROUP', 'SALES_RANK', 'TIMES_REVIEWED', 'TIMES_DOWNLOADED', 'AVERAGE_RATING'))
cdf = pd.DataFrame(columns=('ASIN', 'MAIN_CATEGORY', 'SUB_CATEGORIES'))
rdf = pd.DataFrame(columns=('ASIN', 'DATE', 'CUSTOMER', 'RATING', 'VOTES', 'HELPFUL'))

# initialize everything to blanks
asin = ''
title = ''
group = ''
salesrank = ''
reviewTotal = 0
downloaded = 0
reviewAvgRating = 0

counter = -1
cdfc = -1
revc = -1

with open('amazon-meta.txt', 'r')as fp:
    for line in fp:
        if line.find("Id:   ") != -1:
            # append all variables to data frame
            if (group == 'Music'):
                counter += 1
                df.loc[counter] = [asin, title, group, salesrank, reviewTotal, downloaded, reviewAvgRating]

            # reset everything
            asin = ''
            title = ''
            group = ''
            salesrank = ''
            reviewTotal = 0
            downloaded = 0
            reviewAvgRating = 0
        if line.find("ASIN: ") != -1:
            asin = line[6:].strip()
        if line.find("  title: ") != -1:
            title = line[8:].strip()
        if line.find("  group: ") != -1:
            group = line[8:].strip()
        if group == 'Music':
            if line.find("  salesrank:") != -1:
                salesrank = line[12:].strip()
            if line.find("   |Music[5174]|Styles[301668]|") != -1:
                c = line[31:].strip()
                c = c.split('|')
                cdfc += 1
                cdf.loc[cdfc] = [asin, c[0], c[1]]
            if line.find("  reviews:") != -1:
                r = line[18:].strip()
                r = r.split(' ')
                reviewTotal = r[0]
                downloaded = r[3]
                reviewAvgRating = r[7]
            if line[0:4] == '    ':
                revc += 1
                rev = line.split(' ')
                rev = list(filter(None, rev))
                rdf.loc[revc] = [asin, rev[0], rev[2], rev[4], rev[6], rev[8].strip()]

                if revc % 10000 == 0:
                    print('Processing review .. ' + str(revc) + ' and item ' + str(
                        counter) + ' at time ' + datetime.datetime.fromtimestamp(time.time()).strftime(
                        '%Y-%m-%d %H:%M:%S'))

# Attach category information to summary table
pivotTable = pd.pivot_table(cdf, index=['ASIN'], columns=['MAIN_CATEGORY'], aggfunc=lambda x: len(x) > 0)
df = df.join(pivotTable, on='ASIN')

# Write to file
df.to_csv('reviews_summary_full.csv')
rdf.to_csv('all_reviews_full.csv')
