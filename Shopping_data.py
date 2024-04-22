import statistics
import pandas

#Read the entire CSV file into a pandas DataFrame
df = pandas.read_csv('Shopping_data.csv')
#Filter out the column, Amt-Online
Amt1 = df['Amt-Online']