import pandas as pd
import numpy as np

# Optional: set a random seed for reproducibility
np.random.seed(123)

# 1. Read the CSV file
df = pd.read_csv('CSC316-Final-Project\data\lung_cancer_prediction.csv')  # Replace 'your_data.csv' with your CSV file's name

# 2. Define the distributions for each smoking status.
# Ensure that the keys match exactly how they appear in your 'Smoking_Status' column.
distributions = {
    'Non-Smoker': [0.4, 0.3, 0.2, 0.1],      # Stage I, II, III, IV
    'Former Smoker': [0.2, 0.3, 0.3, 0.2],     # Stage I, II, III, IV
    'Smoker': [0.1, 0.2, 0.3, 0.4]             # Stage I, II, III, IV
}

# List of possible stages in the same order as in the distributions
stages = ['I', 'II', 'III', 'IV']

# 3. Create a function to assign a stage based on smoking status
def reassign_stage(smoking_status):
    """
    Returns a randomly chosen stage (I, II, III, IV)
    according to the distribution of the given smoking status.
    """
    # Check if the smoking_status is present in our dictionary
    if smoking_status not in distributions:
        # Handle missing or unexpected values as needed
        # For example, you could return the original stage or set as NaN:
        return np.nan  
    # Get the probability list for the given smoking status
    probs = distributions[smoking_status]
    # Choose a stage according to the probability distribution
    return np.random.choice(stages, p=probs)

# 4. Apply the function to create/modify the 'Stage_at_Diagnosis' column
#    Here, we assume your DataFrame has a column called 'Smoking_Status'
df['Stage_at_Diagnosis'] = df['Smoking_Status'].apply(reassign_stage)

# 5. Save the modified DataFrame to a new CSV file
df.to_csv('CSC316-Final-Project\data\lung_cancer_prediction.csv', index=False)

print("The data has been modified and saved to 'modified_data.csv'.")
