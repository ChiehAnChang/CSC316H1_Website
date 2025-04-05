import pandas as pd
import numpy as np

# Optional: set a random seed for reproducibility
np.random.seed(123)

# 1. Read the CSV file that already contains the stage information
df = pd.read_csv('CSC316-Final-Project\data\lung_cancer_prediction.csv')  # Replace with your CSV file's name

# 2. Define mortality risk ranges for each combination of Smoking_Status and Stage_at_Diagnosis.
# The ranges are provided as (lower_bound, upper_bound) in decimals.
mortality_ranges = {
    'Non-Smoker': {
        'I': (0.20, 0.25),
        'II': (0.35, 0.50),
        'III': (0.50, 0.65),
        'IV': (0.75, 0.83)
    },
    'Former Smoker': {
        'I': (0.25, 0.30),
        'II': (0.40, 0.55),
        'III': (0.55, 0.70),
        'IV': (0.80, 0.88)
    },
    'Smoker': {
        'I': (0.35, 0.40),
        'II': (0.50, 0.65),
        'III': (0.65, 0.80),
        'IV': (0.90, 0.98)
    }
}

def assign_mortality_risk(row):
    """
    Given a row, return a mortality risk drawn uniformly
    from the range corresponding to the Smoking_Status and Stage_at_Diagnosis.
    Returns NaN if the combination is not found.
    """
    smoking_status = row['Smoking_Status']
    stage = row['Stage_at_Diagnosis']
    
    if smoking_status in mortality_ranges and stage in mortality_ranges[smoking_status]:
        low, high = mortality_ranges[smoking_status][stage]
        return np.random.uniform(low, high)
    else:
        return np.nan

# 3. Apply the function to each row to create a new Mortality_Risk column
df['Mortality_Risk'] = df.apply(assign_mortality_risk, axis=1)

# Optional: If you prefer the risk as a percentage, uncomment the next line.
# df['Mortality_Risk'] = df['Mortality_Risk'] * 100

# 4. Save the modified DataFrame to a new CSV file
df.to_csv('CSC316-Final-Project\data\lung_cancer_prediction.csv', index=False)

print("Mortality risk has been assigned and saved to 'modified_data_with_mortality.csv'.")
