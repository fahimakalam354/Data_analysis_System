# Start
import pandas as pd

# Load the dataframe
df = pd.read_csv(r'C:\\Users\\Chota Zindegi\\Desktop\\Data_Analysis_System\\Backend\\Titanic-Dataset.csv')

# Print the column names
print("Column Names: ", df.columns.tolist())

# Print the number of rows
print("Number of Rows: ", df.shape[0])

# Print the number of people who died
print("Number of People Who Died: ", df[df['Survived'] == 0].shape[0])

# Print the names of the five oldest people
print("Names of the Five Oldest People: ", df.nlargest(5, 'Age')['Name'].tolist())

# End