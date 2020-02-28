import pandas
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

df = pandas.read_csv('/Users/Brittney/Desktop/NYCdata.csv')

print(df.info())

#Part 1
#Dividing restaurants by borough and plotting
boro_percent = df['BORO'].value_counts(normalize=True) * 100
print(boro_percent)

boro_percent.plot.bar()
plt.title('Percentage of Restaurants in each Borough')
plt.ylabel('Percentage')
plt.show()

#Part 2
# Dividing restaurants by grade and boro
A_B_C_df = df[(df['GRADE'] == 'A')|(df['GRADE'].isin(['B','C']))]

print('Only '+ str(len(A_B_C_df)) + ' have letter grades out of ' + str(len(df)) + ' entries. ')

queens_boro = A_B_C_df[A_B_C_df['BORO'] == 'Queens']['GRADE'].value_counts()
brooklyn_boro = A_B_C_df[A_B_C_df['BORO'] == 'Brooklyn']['GRADE'].value_counts()
manhattan_boro = A_B_C_df[A_B_C_df['BORO'] == 'Manhattan']['GRADE'].value_counts()
bronx_boro = A_B_C_df[A_B_C_df['BORO'] == 'Bronx']['GRADE'].value_counts()
staten_island = A_B_C_df[A_B_C_df['BORO'] == 'Staten Island']['GRADE'].value_counts()

#combining the data to plot
combined = pandas.DataFrame({'Queens': queens_boro, 'Brooklyn': brooklyn_boro, 'Manhattan':manhattan_boro,'Bronx':bronx_boro,'Staten Island':staten_island})
transpose_combined = combined.transpose()

transpose_combined.plot.bar()
plt.title('Restaurant Grade Distribution for each Borough')
plt.show()

#want to compare percentages to see if there is a significant difference in grade distribution for the different boroughs


queens_percent = A_B_C_df[A_B_C_df['BORO'] == 'Queens']['GRADE'].value_counts(normalize = True, dropna=False) *100
brooklyn_percent= A_B_C_df[A_B_C_df['BORO'] == 'Brooklyn']['GRADE'].value_counts(normalize = True, dropna=False) *100
manhattan_percent = A_B_C_df[A_B_C_df['BORO'] == 'Manhattan']['GRADE'].value_counts(normalize = True, dropna=False) *100
bronx_percent = A_B_C_df[A_B_C_df['BORO'] == 'Bronx']['GRADE'].value_counts(normalize = True, dropna=False) *100
staten_percent = A_B_C_df[A_B_C_df['BORO'] == 'Staten Island']['GRADE'].value_counts(normalize = True, dropna=False) *100



#counting the A, B, C grades for each borough
#queens_boro = queens_boro_df['GRADE'].value_counts()
#brooklyn_boro = brooklyn_boro_df['GRADE'].value_counts()
#manhattan_boro = manhattan_boro_df['GRADE'].value_counts()
#bronx_boro = bronx_boro_df['GRADE'].value_counts()
#staten_island = staten_island_df['GRADE'].value_counts()

#combining the data to plot percentage data
percent_combined = pandas.DataFrame({'Queens': queens_percent, 'Brooklyn': brooklyn_percent, 'Manhattan':manhattan_percent,'Bronx':bronx_percent,'Staten Island':staten_percent})
transpose_percent_combined = percent_combined.transpose()

transpose_percent_combined.plot.bar()
plt.title('Restaurant Grade Distribution for each Borough by percent')
plt.show()

#Part 3 separating inspection grade by type of food for 10 most common restaurants
print(df['CUISINE DESCRIPTION'].value_counts().head(20))

American = A_B_C_df[A_B_C_df['CUISINE DESCRIPTION'] == 'American']['GRADE'].value_counts(normalize = True, dropna=False) *100
Chinese = A_B_C_df[A_B_C_df['CUISINE DESCRIPTION'] == 'Chinese']['GRADE'].value_counts(normalize = True, dropna=False) *100
Cafe_Coffee_Tea = A_B_C_df[A_B_C_df['CUISINE DESCRIPTION'] == 'Café/Coffee/Tea']['GRADE'].value_counts(normalize = True, dropna=False) *100
Latin = A_B_C_df[A_B_C_df['CUISINE DESCRIPTION'] == 'Latin (Cuban, Dominican, Puerto Rican, South & Central American)']['GRADE'].value_counts(normalize = True, dropna=False) *100
Pizza = A_B_C_df[A_B_C_df['CUISINE DESCRIPTION'] == 'Pizza']['GRADE'].value_counts(normalize = True, dropna=False) *100
Mexican = A_B_C_df[A_B_C_df['CUISINE DESCRIPTION'] == 'Mexican']['GRADE'].value_counts(normalize = True, dropna=False) *100
Italian = A_B_C_df[A_B_C_df['CUISINE DESCRIPTION'] == 'Italian']['GRADE'].value_counts(normalize = True, dropna=False) *100
Caribbean = A_B_C_df[A_B_C_df['CUISINE DESCRIPTION'] == 'Caribbean']['GRADE'].value_counts(normalize = True, dropna=False) *100
Japanese = A_B_C_df[A_B_C_df['CUISINE DESCRIPTION'] == 'Japanese']['GRADE'].value_counts(normalize = True, dropna=False) *100
Spanish = A_B_C_df[A_B_C_df['CUISINE DESCRIPTION'] == 'Spanish']['GRADE'].value_counts(normalize = True, dropna=False) *100

#combining
grade_combo = pandas.DataFrame({'American': American, 'Chinese': Chinese, 'Cafe/Coffee/Tea': Cafe_Coffee_Tea,'Latin': Latin,'Pizza':Pizza,'Mexican':Mexican,'Italian':Italian,'Caribbean':Caribbean, 'Japanese':Japanese,'Spanish': Spanish})
transpose_grade_combo = grade_combo.transpose()


transpose_grade_combo.plot.barh()
plt.title('Percentage of Grades by Top 10 Cuisines')
plt.ylabel('Percentage')
plt.show()

#Part 4
#Most common violation code
print(df['VIOLATION CODE'].value_counts().head(1))


#looking at critical flag and at inspection type
# to get an idea of which restaurants might be close to closing

#unique things written in Critical flag column
#print(df['CRITICAL FLAG'].value_counts())
#Most common violation code

