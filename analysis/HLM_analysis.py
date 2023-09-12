import pandas as pd
import statsmodels.api as sm
from scipy.stats import f

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

def calculate_sig_f_change(model_old, model_new):
    """
    Calculate the significance of the F change for hierarchical regression.
    
    Parameters:
    - model_old: The regression model result object for the previous step.
    - model_new: The regression model result object for the current step.
    
    Returns:
    - ΔF and its p-value.
    """
    df_diff = model_old.df_resid - model_new.df_resid
    r2_diff = model_new.rsquared - model_old.rsquared
    
    delta_f = (r2_diff / df_diff) / ((1 - model_new.rsquared) / model_new.df_resid)
    p_value = 1 - f.cdf(delta_f, df_diff, model_new.df_resid)
    
    return delta_f, p_value

def save_all_results_to_txt(results_list, delta_f_values, p_values, file_path="/mnt/data/offline_media_pp_mean_result.txt"):
    """
    Save the hierarchical regression results along with ΔF and its significance to a .txt file.
    
    Parameters:
    - results_list: List of lists of hierarchical regression result objects.
    - delta_f_values: List of ΔF values for each model group.
    - p_values: List of p-values for ΔF for each model group.
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
            file.write(f"ΔF for Model Group {idx}: {delta_f_values[idx-1]:.4f}\n")
            file.write(f"p-value for ΔF for Model Group {idx}: {p_values[idx-1]:.4e}\n")
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

# Calculate Sig F change for each group
delta_f_1, p_value_1 = calculate_sig_f_change(results_1[0], results_1[1])
delta_f_2, p_value_2 = calculate_sig_f_change(results_2[0], results_2[1])
delta_f_3, p_value_3 = calculate_sig_f_change(results_3[0], results_3[1])

print(delta_f_1, p_value_1, delta_f_2, p_value_2, delta_f_3, p_value_3)

# Saving all the results using the modified function
# confirmation_message_offline = save_all_results_to_txt(
#     [results_1_offline, results_2_offline, results_3_offline],
#     [delta_f_1_offline, delta_f_2_offline, delta_f_3_offline],
#     [p_value_1_offline, p_value_2_offline, p_value_3_offline]
# )
# confirmation_message_offline