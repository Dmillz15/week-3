import seaborn as sns
import pandas as pd


# update/add code below ...
#Question 1
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

fibonacci(15)

#Question 2
def to_binary(x):
    x=bin(x)
    return x[2:]

to_binary(12)

#Question 3
import pandas as pd
 


url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'

df_bellevue = pd.read_csv(url)

def task_1():
    """
    Return a list of all column names sorted by missing values (least to most).
    Handle the gender column issue.
    """
    df = df_bellevue.copy()

    print("Gender column values before cleaning:")
    print(df['gender'].value_counts())
    print()
    

    df['gender'] = df['gender'].str.strip().str.lower()
    
    gender_mapping = {
        'm': 'male',
        'male': 'male',
        'f': 'female', 
        'female': 'female',
        'unknown': 'unknown',
        '': 'unknown',
        'nan': 'unknown',
        'none': 'unknown'
    }
    
    df['gender'] = df['gender'].map(gender_mapping).fillna('unknown')
    
    print("Gender column values after cleaning:")
    print(df['gender'].value_counts())
    print()
    
    missing_counts = df.isnull().sum()
    
    sorted_columns = missing_counts.sort_values().index.tolist()
    
    print(f"Columns sorted by missing values (least to most): {sorted_columns}")
    return sorted_columns

task_1()

#Task 2
def task_2():
    """
    Return a data frame with year and total number of entries for each year.
    """
    df = df_bellevue.copy()
    
    # Check for issues with the date column
    print("Checking date column for data issues...")
    
    # Convert date column to datetime, handling potential format issues
    df['date_in'] = pd.to_datetime(df['date_in'], errors='coerce')
    
    # Extract year from date
    df['year'] = df['date_in'].dt.year
    
    # Check for missing or invalid years
    missing_years = df['year'].isnull().sum()
    if missing_years > 0:
        print(f"Warning: {missing_years} entries have missing or invalid dates")
    
    # Group by year and count admissions
    yearly_admissions = df.groupby('year').size().reset_index(name='total_admissions')
    
    # Rename columns for clarity
    yearly_admissions.columns = ['year', 'total_admissions']
    
    print(f"Yearly admissions data frame created with {len(yearly_admissions)} years")
    return yearly_admissions

task_2()

#Task 3
def task_3():
    """
    Return a series with gender as index and average age as values.
    """
    df = df_bellevue.copy()
    
    # Clean the gender column first (similar to task_1)
    df['gender'] = df['gender'].str.strip().str.lower()
    gender_mapping = {
        'male': 'male',
        'female': 'female',
        'm': 'male',
        'f': 'female'
    }
    df['gender'] = df['gender'].map(gender_mapping).fillna(df['gender'])
    
    # Check for age data issues
    print("Checking age column for data issues...")
    
    # Convert age to numeric, handling non-numeric values
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    
    # Check for missing or invalid ages
    missing_ages = df['age'].isnull().sum()
    if missing_ages > 0:
        print(f"Warning: {missing_ages} entries have missing or invalid ages")
    
    # Calculate average age by gender
    avg_age_by_gender = df.groupby('gender')['age'].mean()
    
    print(f"Average ages calculated for {len(avg_age_by_gender)} gender categories")
    return avg_age_by_gender
task_3()

#Task 4
def task_4():
    df = df_bellevue.copy()
    
    print("Checking profession column for data issues...")
    df['profession'] = df['profession'].fillna('Unknown')
    df['profession'] = df['profession'].str.strip().str.title()
    
    profession_counts = df['profession'].value_counts()
    top_5_professions = profession_counts.head(5).index.tolist()
    
    print(f"Top 5 professions: {top_5_professions}")
    print(f"Total unique professions: {len(profession_counts)}")
    
    return top_5_professions

task_4()