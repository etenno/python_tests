import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

complete_data_set = pd.read_csv (r'suicide-rates-overview-1985-to-2016/master.csv')


countries = []
for row in complete_data_set.itertuples():
  if not (row.country in countries):
    countries.append(row.country)

def gender_proportion():
  no_of_males = 0
  no_of_females = 0

  #calculates male/female proportion and creates stores countries
  for row in complete_data_set.itertuples():
    if row.sex == 'male':
      no_of_males += 1
    else:
      no_of_females += 1

  total = no_of_males + no_of_females
  percentage_of_males = (no_of_males / total)*100
  percentage_of_females = (no_of_females / total)*100

  print("males: " + str(percentage_of_males) + '%', "Number of females: " + str(percentage_of_females) + '%')



def highest_suicide_rates():
  suicides_no = []
  suicide_totals = pd.DataFrame(columns=['country', 'total'])

  year = input("Input a year: ")
  num = input("How many top contries: ")

  i = 0

  for country in countries:
    data_for_given_year = complete_data_set[complete_data_set.year == int(year)]
    #filter by year input by user

    filtered_data = data_for_given_year[data_for_given_year.country == country]
    #filter by each country in the array

    amount = 0 # accumulator for suicides in year and country

    for row in filtered_data.itertuples(): #sums amount of suicides in one country
      amount += row.suicides_no

    suicide_totals.loc[i] = [country, amount] #should add new row to suicide_totals
    i += 1

  ordered_data = suicide_totals.sort_values('total', ascending=False).head(int(num))

  fig = plt.figure()
  ax = fig.add_axes([0,0,1,1])
  ax.pie(ordered_data.total, labels = ordered_data.country)
  plt.show()


highest_suicide_rates()



def generation_proportion():
  print("g")
