import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv (r'suicide-rates-overview-1985-to-2016/master.csv')

no_of_males = 0
no_of_females = 0
countries = []

#calculates male/female proportion and creates stores countries
for row in df.itertuples():
  if not (row.country in countries):
    countries.append(row.country)

  if row.sex == 'male':
    no_of_males += 1
  else:
    no_of_females += 1

total = no_of_males + no_of_females
percentage_of_males = (no_of_males / total)*100
percentage_of_females = (no_of_females / total)*100


print("males: " + str(percentage_of_males) + '%', "Number of females: " + str(percentage_of_females) + '%')

################################################
#ALBANIAN EXAMPLE

#filters only albanian suicides into var variable
albanian_data = df[df.country == 'Albania']

x = albanian_data.year
y = albanian_data.suicides_no
#plt.plot(x,y)
#plt.show() this line stops code execution so comment while experimenting

################################################
#filter data by year, see breakdown of total number of suicides over countries in specified year

suicides_no = []
data_store = {}
year = input("Input a year: ")

for country in countries:
  data1 = df[df.year == int(year)]
  #filter by year input by user
  data = data1[data1.country == country]
  #filter by each country in the array

  amount = 0
  for row in data.itertuples():
    amount += row.suicides_no

  suicides_no.append(amount)
  data_store[country] = amount

ordered_data = sorted(data_store)

print(ordered_data)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.set_xlabel('Countries')
ax.set_ylabel('Number')
ax.set_title('Scores by group and gender')
ax.pie(suicides_no,labels = countries)
plt.show()

