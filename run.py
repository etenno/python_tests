# Simple Univariate linear regression for US election demography by county
# Kaggle link for dataset: https://www.kaggle.com/etsc9287/2020-general-election-polls

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

################### FUNCTIONS ######################################

#TO DO - find more rigorous way of selecting datapoint to calc beta10
def regression(variable):
  # beta1 = regression gradient, beta0 = intercept
  beta1 = data[variable].cov(data.percentage20_Donald_Trump) / data[variable].var() #= cov(x,y) / var(x)
  beta0 = data.percentage20_Donald_Trump[1] - beta1 * data[variable][1]        #= y - beta1*x
  return beta0, beta1

def plot(variables,betas):
  # plot regression line with sample data points

  # set up axes
  x = np.linspace(0, 400000, 1000000)
  fig = plt.figure()
  ax = plt.axes()
  plt.ylim(0, 1)
  plt.xlim(0, 350000)
  ax.set_ylabel('Percentage of Trump Votes')

  def axisplot(pair): # plot regression lines for each variable
    ax.plot(x, pair[1]*x+pair[0]);

  def scatterplot(variables): # plot sample data sets
    plt.scatter(data[variables],data.percentage20_Donald_Trump)

  [axisplot(i) for i in betas]
  [scatterplot(i) for i in variables]
  ax.legend(variables, prop={'size': 15})
  plt.show()


def init(variables):
  #input list of variables to plot against % trump votes
  #eg. ['Income','cases','deaths']]
  betas = [regression(i) for i in variables]
  plot(variables,betas)

############################################################################


# obtain and filter training data
data = pd.read_csv (r'data/election_demography/county_statistics.csv')

init(['Men','Women'])
