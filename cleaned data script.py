# Step 1: Import necessary libraries
import pandas as pd

# Step 2: Load the dataset
df = pd.read_csv('netflix_titles.csv')  # Make sure the CSV file is in your working directory

# Step 3: Initial inspection
print("Initial dataset info:")
print(df.info())
print("\nMissing values:\n", df.isnull().sum())

# Step 4: Handle missing values
df['director'].fillna('Unknown', inplace=True)
df['cast'].fillna('Not Specified', inplace=True)
df['country'].fillna('Unknown', inplace=True)
df['date_added'].fillna(df['date_added'].mode()[0], inplace=True)

# Step 5: Remove duplicates
df.drop_duplicates(inplace=True)

# Step 6: Standardize text data
string_columns = df.select_dtypes(include='object').columns
df[string_columns] = df[string_columns].apply(lambda x: x.str.strip().str.lower())

# Step 7: Convert date formats
df['date_added'] = pd.to_datetime(df['date_added'])

# Step 8: Rename columns (lowercase, underscores)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Step 9: Extract numeric duration
# Splitting 'duration' into duration_int and duration_type
df[['duration_int', 'duration_type']] = df['duration'].str.extract(r'(\d+)\s*(\w+)')
df['duration_int'] = pd.to_numeric(df['duration_int'], errors='coerce')

# Step 10: Final check and save cleaned dataset
print("\nCleaned dataset info:")
print(df.info())

df.to_csv('netflix_cleaned.csv', index=False)
print("\n✅ Cleaned dataset saved as 'netflix_cleaned.csv'")
