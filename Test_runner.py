# CSV-datase
#Test runner according to 2nd week plan

#pandas is excel toolkit
#setting up pandas as shortform "pd"
import pandas as pd
# The file name works directly because it is in the same folder
file_name = "mock_market.csv" #state out the file name

try: #attempt to run this code
    #df = a variable name
    df = pd.read_csv(file_name) #using pd to read
    #read_csv = Read the file using csv format
    #set the data in a table according to the comma

    print("-"*20+ ' Successfully Loaded Market Data '+ "-"*20)
    # Print only the first 5 rows
    print(df.head(6))

except FileNotFoundError: #exemption if didn't find the file (except)
    print(f"Error: Could not find '{file_name}'. Make sure it's in the same directory.")