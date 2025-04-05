import pandas as pd
import numpy as np

# 1. Read in the original CSV
df = pd.read_csv("data\lung_cancer_prediction.csv")

# 2. Filter out rows with Second_Hand_Smoke == 'Yes'
shs_mask = df["Second_Hand_Smoke"] == "Yes"
sub_df = df.loc[shs_mask].copy()

# 3. Define the stage distribution
stages = ["I", "II", "III", "IV"]
probs = [0.10, 0.40, 0.30, 0.20]  # The desired distribution

# 4. Randomly reassign the Stage_at_Diagnosis for those with second-hand smoke
sub_df["Stage_at_Diagnosis"] = np.random.choice(stages, size=len(sub_df), p=probs)

# 5. Place the updated stages back into the main DataFrame
df.loc[shs_mask, "Stage_at_Diagnosis"] = sub_df["Stage_at_Diagnosis"]

# 6. Write out the modified CSV
df.to_csv("data\lung_cancer_prediction.csv", index=False)

print("Successfully updated stages for second-hand smokers in 'lung_cancer_data_modified.csv'.")
