import pandas as pd

titanic = pd.read_csv(r'C:\Users\shiri\Data Engineering Practice\Datasets_Source\titanic.csv')

print(titanic.head())

print(titanic.dtypes)

# let's round Age to 1 decimal and Fare to 2 decimals

titanic_rounded = titanic.round({'Age' : 1, 'Fare' : 2})
print(titanic_rounded)

# Now let's split the Name column, which starts with last name followed by comma and then salutation and first and middle names

titanic[['LastName', 'Name']] = titanic['Name'].str.split(', ', n = 1, expand = True)

print(titanic.head())

# Let's reorder the columns to display both the names next to each other

ordered_titanic = titanic[['PassengerId', 'Survived', 'Pclass', 'Name', 'LastName', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']]

print(ordered_titanic.head())

# Count the no. of nulls or blanks in each column

null_count_titanic = ordered_titanic.isna().sum()

print(null_count_titanic)

# There are 2 nulls in Embarked, 177 in Age and 687 in Cabin

# let find the average age of men and women on board and fill the nulls with the average age

titanic_pivot = ordered_titanic.pivot_table(index = 'Sex', values = 'Age', aggfunc = 'mean')

print(titanic_pivot)

# Average age of women is 27.9 and men is 30.7
# Populating the nulls with these values

ordered_titanic.loc[(ordered_titanic['Sex'] == 'male') & (ordered_titanic['Age'].isnull()), 'Age'] = 30.7

ordered_titanic.loc[(ordered_titanic['Sex'] == 'female') & (ordered_titanic['Age'].isnull()), 'Age'] = 27.9

print(ordered_titanic.isnull().sum())

# Age column has been fully populated

# Checking how many families

pivot_titanic = ordered_titanic.pivot_table(index = 'LastName', aggfunc = 'size').sort_values(ascending = False)

print(pivot_titanic[pivot_titanic > 1])

# 133 different last name are returned, let's filter the data frame to have only records with families

titanic_family = ordered_titanic[ordered_titanic['LastName'].isin(pivot_titanic.index[pivot_titanic > 1])]

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(titanic_family.sort_values(by = 'LastName'))
