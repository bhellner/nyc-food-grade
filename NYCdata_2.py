import pandas
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import descartes
import geopandas as gpd
from shapely.geometry import Point, Polygon

df = pandas.read_csv('/Users/Brittney/Desktop/NYCdata.csv')
boro = df['BORO'].value_counts()
print(boro)

#making a dataframe only with Manhattan Restaurants and plotting
manhattan_df = df[df['BORO'] == 'Manhattan']

sns.countplot(x='GRADE',data=manhattan_df)
#add labels
plt.show()

#organizing data frame by zipcodes and binning from zipcodes

print(manhattan_df['ZIPCODE'].nunique())
print(manhattan_df['ZIPCODE'].value_counts())
print(len(manhattan_df))

#Central Harlem
# zipcodes 10026, 10027, 10030, 10037, 10039
central_harlem_df = manhattan_df[(manhattan_df['ZIPCODE'] == 10026)|(manhattan_df['ZIPCODE'].isin([10027,10030,10037,10039]))]

#Chelsea and Clinton
# zipcodes 10001, 10011, 10018, 10019, 10020, 10036
chelsea_clinton_df = manhattan_df[(manhattan_df['ZIPCODE'] == 10001)|(manhattan_df['ZIPCODE'].isin([10011,10018,10019,10020,10036]))]

#East Harlem
# zipcodes 10029, 10035
east_harlem_df = manhattan_df[(manhattan_df['ZIPCODE'] == 10029)|(manhattan_df['ZIPCODE']== 10035)]
east_harlem_grade = east_harlem_df[(east_harlem_df['GRADE']=='A')| (east_harlem_df['GRADE']=='B')|(east_harlem_df['GRADE']=='C')]
c = east_harlem_grade['GRADE'].value_counts(normalize = True)*100
c.plot.bar()
plt.show()

#Gramercy Park and Murray Hill
# zipcodes 10010, 10016, 10017, 10022
gramercy_murray_df = manhattan_df[(manhattan_df['ZIPCODE'] == 10010)|(manhattan_df['ZIPCODE'].isin([10016,10017,10022]))]
print(len(gramercy_murray_df))

#Greenwich Village and Soho
# zip codes 10012, 10013, 10014
greenwich_soho_df = manhattan_df[(manhattan_df['ZIPCODE'] == 10012)|(manhattan_df['ZIPCODE'].isin([10013,10014]))]
print(len(greenwich_soho_df))

#Lower Manhattan
# 10004, 10005, 10006, 10007, 10038, 10280
lower_manhattan_df = manhattan_df[(manhattan_df['ZIPCODE'] == 10004)|(manhattan_df['ZIPCODE'].isin([10005,10006,10007,10038,10280]))]
print(len(lower_manhattan_df))

#Lower East Side
# 10002, 10003, 10009
lower_eastside_df = manhattan_df[(manhattan_df['ZIPCODE'] == 10002)|(manhattan_df['ZIPCODE'].isin([10003,10009]))]
print(len(lower_eastside_df))

#Upper East Side
# Zipcodes 10021, 10028, 10044, 10065, 10075, 10128
upper_eastside_df = manhattan_df[(manhattan_df['ZIPCODE'] == 10021)|(manhattan_df['ZIPCODE'].isin([10028,10044, 10065, 10075, 10128]))]
print(len(upper_eastside_df))

#Upper West side
# 10023, 10024, 10025
upper_westside_df = manhattan_df[(manhattan_df['ZIPCODE'] == 10023)|(manhattan_df['ZIPCODE'].isin([10024,10025]))]
print(len(upper_westside_df))

#inwood and washington heights
#10031, 10032, 10033, 100034, 10040
inwood_df = manhattan_df[(manhattan_df['ZIPCODE'] == 10031)|(manhattan_df['ZIPCODE'].isin([10032, 10033, 100034, 10040]))]
print(len(inwood_df))

#ax = plt.subplot(111)
#ax.bar(c-0.2, y, width=0.2, color='b', align='center')
#ax.bar(c, z, width=0.2, color='g', align='center')
#ax.bar(c+0.2, k, width=0.2, color='r', align='center')
#plt.show(ax)