import pandas as pd
import statsmodels.api as sm

# Load data
ml_df = pd.read_csv(r'C:\Users\GTW_User\Desktop\media_political\modeling_data.csv')

# Perform One-Hot Encoding on the specified categorical variables
data_encoded = pd.get_dummies(ml_df, columns=["ethnic", "Negative_1", "Negative_2", "Negative_3"], drop_first=True)

def hierarchical_regression(ml_df, dependent_var, blocks):
    results = []
    y = ml_df[dependent_var]
    included_vars = []
    
    for block in blocks:
        included_vars.extend(block)
        X = sm.add_constant(ml_df[included_vars]) # add an intercept (beta_0) to our model
        model = sm.OLS(y, X).fit()
        results.append(model)
    return results

def save_regression_results_to_txt(results_list, file_path=r"C:\Users\GTW_User\Desktop\media_political\results\online_media_pp_mean_result.txt"):
    """
    Save the hierarchical regression results to a .txt file.
    
    Parameters:
    - results_list: List of lists of hierarchical regression result objects.
    - file_path: Path to the file where the results should be saved.
    
    Returns:
    - Confirmation message with the file path.
    """
    with open(file_path, 'w') as file:
        for idx, results in enumerate(results_list, 1):
            for i, result in enumerate(results, 1):
                file.write(f"Model Group {idx} - Level {i}:\n")
                file.write(result.summary().as_text())
                file.write("\n\n")
            file.write("-" * 80 + "\n\n")
    return f"Results saved to {file_path}"

# Define the blocks for the first analysis
blocks_1 = [
    ["sex", "edu", "income"] + [col for col in data_encoded.columns if "ethnic" in col],
    ["political_knowledge", "TC_issue"]
]

# Perform the first hierarchical regression
results_1 = hierarchical_regression(data_encoded, "online_media_pp_mean", blocks_1)
print(results_1[0].summary(), results_1[1].summary())

# Define the blocks for the second analysis
blocks_2 = [
    ["sex", "edu", "income"] + [col for col in data_encoded.columns if "ethnic" in col],
    ["political_knowledge"] + [col for col in data_encoded.columns if "Negative_" in col]
]

# Perform the second hierarchical regression
results_2 = hierarchical_regression(data_encoded, "online_media_pp_mean", blocks_2)
print(results_2[0].summary(), results_2[1].summary())

# Define the blocks for the third analysis
blocks_3 = [
    ["sex", "edu", "income"] + [col for col in data_encoded.columns if "ethnic" in col],
    ["political_knowledge", "political_polarization_mean", "party_image_mean"]
]

# Perform the third hierarchical regression
results_3 = hierarchical_regression(data_encoded, "online_media_pp_mean", blocks_3)
print(results_3[0].summary(), results_3[1].summary())

# Saving all the results using the modified function
confirmation_message = save_regression_results_to_txt([results_1, results_2, results_3])
confirmation_message