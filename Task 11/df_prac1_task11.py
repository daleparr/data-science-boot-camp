import pandas as pd

# Load your dataset
df = pd.read_csv('Dataset Task.ipynb')  # Example for loading a dataset

# Task 1a: Select the 'Limit' and 'Rating' columns of the first five observations
task_1a = df[['Limit', 'Rating']].head(5)

# Task 1b: Select the first five observations with 4 cards
task_1b = df[df['Cards'] == 4].head(5)

# Task 1c: Sort the observations by 'Education' in descending order
task_1c = df.sort_values('Education', ascending=False)

# Explanations for the lines of code:
# a. df.iloc[:,:]: This line selects all rows and columns in the DataFrame.
# b. df.iloc[5:,5:]: This selects rows from index 5 to the end and columns from index 5 to the end of the DataFrame.
# c. df.iloc[:,0]: This selects all rows and only the first column of the DataFrame.
# d. df.iloc[9,:]: This selects the tenth row (index starts at 0) and all columns in that row.
