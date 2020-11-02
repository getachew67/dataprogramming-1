"""
Name: Michael Shieh
CSE 163 AB

This file contains all the required functions for hw3.
"""
import cse163_utils  # noqa: F401
# This is a hacky workaround to an unfortunate bug on macs that causes an
# issue with seaborn, the graphing library we want you to use on this
# assignment.  You can just ignore the above line or delete it if you are
# not using a mac!

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor


def compare_bachelors_1980(data):
    """
    This function takes on a pandas dataframe
    and returns a pandas dataframe that includes
    the percentage of male and female who have a bachelor's degree in 1980

    If no required data existed,
    this function should return a empty dataframe
    """
    is_male = data['Sex'] == 'M'
    is_female = data['Sex'] == 'F'
    in_1980 = data['Year'] == 1980
    is_bachelors = data['Min degree'] == 'bachelor\'s'

    bachlors_in_1980 = data[in_1980 & is_bachelors & (is_male | is_female)]
    return bachlors_in_1980.loc[:, ['Sex', 'Total']]


def top_2_2000s(data):
    """
    This function takes on a pandas dataframe
    and returns a panda series that shows
    the top 2 percentage of the minimum degree received for the population

    If no required data existed,
    this function should return a empty series
    """
    for_all_sex = data['Sex'] == 'A'
    later_than_2000 = data['Year'] >= 2000
    earlier_than_2010 = data['Year'] <= 2010

    new_data = data[for_all_sex & later_than_2000 & earlier_than_2010]
    return new_data.groupby('Min degree')['Total'].mean().nlargest(2)


def percent_change_bachelors_2000s(data, sex='A'):
    """
    This function takes on a pandas dataframe and a string.
    The string indicates a specific gender,
    but if it's not specified, it is defaulted as all gender.

    The return of this function should be a number.
    """
    indicate_sex = data['Sex'] == sex
    in_2000 = data['Year'] == 2000
    in_2010 = data['Year'] == 2010
    is_bachelors = data['Min degree'] == 'bachelor\'s'

    new_data = data[is_bachelors & indicate_sex & (in_2000 | in_2010)]
    new_data = new_data.loc[:, 'Total']
    return new_data.diff().dropna().squeeze()


def line_plot_bachelors(data):
    """
    This function takes on a pandas dataframe
    and creates a line plot with seaborn that shows
    the percentage changes of bachelor's degree earned over time.
    This percentage is for all genders.
    """
    is_bachelors = data['Min degree'] == 'bachelor\'s'
    all_sex = data['Sex'] == 'A'

    new_data = data[is_bachelors & all_sex].dropna(subset=['Total'])
    sns.relplot(x='Year', y='Total', data=new_data, kind='line')
    plt.title('Percentage Earning Bachlor\'s over Time')
    plt.xlabel('Year')
    plt.ylabel('Percentage')
    plt.savefig('line_plot_bachelors.png', bbox_inches='tight')
    return None


def bar_chart_high_school(data):
    """
    This function takes on a pandas dataframe
    and creates a bar chart with seaborn that shows
    the percentage of high school graduates in 2009.
    This percentage is for all genders, male, and female.
    """
    complete_high_school = data['Min degree'] == 'high school'
    in_2009 = data['Year'] == 2009
    new_data = data[complete_high_school & in_2009]

    sns.catplot(x='Sex', y='Total', data=new_data, kind='bar')
    plt.title('Percentage Completed High School by Sex')
    plt.xlabel('Sex')
    plt.ylabel('Percentage')
    plt.savefig('bar_chart_high_school.png', bbox_inches='tight')
    return None


def plot_hispanic_min_degree(data):
    """
    This function takes on a pandas dataframe
    and creates a bar chart with seaborn that shows
    the total percentage change of high school graduates
    and bachelor's degrees earned for Hispanics from 1990 to 2010.
    """
    later_than_1990 = data['Year'] >= 1990
    earlier_than_2010 = data['Year'] <= 2010
    complete_high_school = data['Min degree'] == 'high school'
    is_bachelors = data['Min degree'] == 'bachelor\'s'
    all_sex = data['Sex'] == 'A'
    new_data = data[later_than_1990 & earlier_than_2010 & all_sex &
                    (complete_high_school | is_bachelors)]

    sns.catplot(x='Year', y='Hispanic', hue='Min degree',
                data=new_data, kind='bar')
    plt.title('Percentage for Hispanics\' Min. Degree over Time')
    plt.xlabel('Year')
    plt.ylabel('Percentage')
    plt.savefig('plot_hispanic_min_degree.png', bbox_inches='tight')
    return None


def fit_and_predict_degrees(data):
    """
    This function takes on a pandas dataframe
    and runs a machine learning model to predict
    the total percentage of degree earned with features like
    which year, which degree, and which gender.

    It splits the 80 % of the dataset into training set,
    and the rest is testing set.
    This function returns the mean squared error of
    both training set and testing set.
    """
    new_data = data[['Year', 'Min degree', 'Sex', 'Total']].dropna()

    labels = new_data['Total']
    features = new_data.loc[:, new_data.columns != 'Total']
    features = pd.get_dummies(features)
    features_train, features_test, labels_train, labels_test = \
        train_test_split(features, labels, test_size=0.2)

    model = DecisionTreeRegressor()
    model.fit(features_train, labels_train)

    train_prediction = model.predict(features_train)
    test_prediction = model.predict(features_test)

    train_mse = mean_squared_error(labels_train, train_prediction)
    test_mse = mean_squared_error(labels_test, test_prediction)
    return train_mse, test_mse


def main():
    data = pd.read_csv('/home/hw3-nces-ed-attainment.csv', na_values='---')
    compare_bachelors_1980(data)
    top_2_2000s(data)
    percent_change_bachelors_2000s(data)
    line_plot_bachelors(data)
    bar_chart_high_school(data)
    plot_hispanic_min_degree(data)
    train_mse, test_mse = fit_and_predict_degrees(data)


if __name__ == '__main__':
    main()
