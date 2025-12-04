import pandas as pd
import io

filename = "25_26"

with open(filename + ".txt", 'r') as file:
    data = file.read()

print("First 50 characters repr:", repr(data[:50]))

try:
    df = pd.read_csv(io.StringIO(data), sep='\t')
    
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    # Function to format values:
    # 1. Replace NaNs or empty strings with '_'
    # 2. Convert numbers to integers (removes decimals like 2.0 -> 2)
    def clean_value(x):
        if pd.isna(x) or str(x).strip() == '':
            return '_'
        try:
            return str(int(float(x)))
        except ValueError:
            return str(x)

    # Apply the function to the entire DataFrame
    df_filled = df.applymap(clean_value)

    print("\nShape:", df_filled.shape)
    print("Columns:", df_filled.columns.tolist())
    
    output_filename = filename + '.csv'
    df_filled.to_csv(output_filename, index=False)

    # Display the first 10 rows
    print(df_filled.head(10).to_markdown(index=False, numalign="left", stralign="left"))

except Exception as e:
    print("Error:", e)