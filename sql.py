import pandas as pd

# Replace 'your_csv_file.csv' with the path to your CSV file
csv_file_path = './Cancer Death - Data.csv'


# Read the CSV file into a pandas DataFrame
data = pd.read_csv(csv_file_path)

# Function to map pandas data types to SQL data types
def map_data_types(dtype):
    if dtype == 'object':
        return 'TEXT'
    elif dtype in ['int64', 'int32']:
        return 'INTEGER'
    elif dtype in ['float64', 'float32']:
        return 'REAL'
    elif 'datetime' in str(dtype).lower():
        return 'DATE'  # Assuming datetime columns should be mapped to DATE in SQL
    else:
        return 'TEXT'  # Default to TEXT for other data types

# Function to generate SQL create table statement
def generate_create_table_sql(data, table_name):
    create_table_sql = f"CREATE TABLE {table_name} (\n"

    for column_name, dtype in zip(data.columns, data.dtypes):
        sql_type = map_data_types(dtype)
        create_table_sql += f"    {column_name} {sql_type},\n"

    create_table_sql = create_table_sql.rstrip(",\n")  # Remove the trailing comma and newline
    create_table_sql += "\n);"

    return create_table_sql

# Replace 'your_table_name' with the desired table name
table_name = 'your_table_name'

# Generate the SQL create table statement
sql_statement = generate_create_table_sql(data, table_name)

# Print the SQL statement
print(sql_statement)
