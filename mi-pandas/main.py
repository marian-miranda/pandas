import pandas as pd

# df=dataframe

# this is going to load the CSV file for us
# And its going to store it in a data frame
df = pd.read_csv("orders.csv")
print(df)
