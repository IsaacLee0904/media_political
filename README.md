![banner](https://github.com/IsaacLee0904/media_political/assets/54140164/18e35fac-7be2-4a8f-8ee8-3342094f5946)

![Python version](https://img.shields.io/badge/Python%20Version-3.9+-lightgrey)
![GitHub last commit](https://img.shields.io/badge/last%20commit-Jul-green)
![GitHub last commit](https://img.shields.io/badge/Repo%20Size-2.3M-blue)
![GitHub last commit](https://img.shields.io/badge/Project%20Type-Analytical%20Project-red)

Badge [source](https://shields.io/)

# media_political

## Authors
- [@IsaacLee0904](https://github.com/IsaacLee0904)

## Table of Contents
  - [Data Source](#data-source)
  - [Repository structure](#repository-structure)
  - [Workflow](#workflow)


## Data Source
  - Survey data

## Repository structure
```
├── ETL.py                            <- Python code for data ETL.
├── ETL_function.py                   <- Python code with all function for ETL.
├── Factor_Analysis.py                <- Python code with all function for factor analysis.
├── DV_FAC.ipynb                      <- notebook with dependent variable factor analysis.
├── anti_party_FAC.ipynb              <- notebook with independent variable factor analysis.
├── Reliability_testing.ipynb         <- notebook with reliability testing for all index.
├── media_political_analysis.ipynb    <- modeling.
└── raw_data.csv
```

## Workflow 
### Step1. Cleaning Data
* Reshape raw data as a dataframe named ml_df 
* Filter out dependent variable as a dataframe named IV_df
* Filter out independent variable as a dataframe named IV_df
### Step2. Factor analysis
  #### Independent Variable
  * Result of Bartlett’s test 
    * Chi-square value : 358.638 
    * p-value          : 0.0
      * The Bartlett test produces a p-value that is less than 0.05. It means, we reject the null hypothesis or in this case, at least two     population variances are different.
  * Result of Kaiser-Meyer-Olkin(KMO)
    * KMO value : 0.675
      *  The KMO test produces a KMO value 0.675 which is great than the standard 0.5
  * Communality testing
    
    ![IV_communality_testing](assets/IV_communality_testing.png)
    * Result 
      * The yellow color indicates that the communality values meet the criteria — greater than 0.5. Eliminated Variable below 0.5 .
      * Also according to the Kaiser criteria, the number of factors generated is 2. It means that the 5 columns or well-known variables will be grouped and interpreted into 2 indicators.
        
    ![IV_scree_plot](assets/IV_scree_plot.png)
    * Result 
      * According to the scree plot we will get the elbow at 2 groups .
     
    ![IV_result](assets/IV_result.png)
    * Result
      * According to the result above and reference can extract 2 indicators from 6 varaibles
        1. 極化現象(political_polarization) : anti_1
        2. 政黨形象(party_image) : anti_3 / anti_4 / anti_5

  #### Dependent Variable
  * Result of Bartlett’s test 
    * Chi-square value : 2616.18
    * p-value          : 0.0
      * The Bartlett test produces a p-value that is less than 0.05. It means, we reject the null hypothesis or in this case, at least two     population variances are different.
  * Result of Kaiser-Meyer-Olkin(KMO)
    * KMO value : 0.771
      *  The KMO test produces a KMO value 0.675 which is great than the standard 0.5
  * Communality testing
    
    ![DV_communality_testing](assets/DV_communality_testing.png)
    * Result 
      * The yellow color indicates that the communality values meet the criteria — greater than 0.5. Eliminated Variable below 0.5 .
      * Also according to the Kaiser criteria, the number of factors generated is 4. It means that the 5 columns or well-known variables will be grouped and interpreted into 4 indicators.
        
    ![DV_scree_plot](assets/DV_scree_plot.png)
    * Result 
      * According to the scree plot we will get the elbow at 4 groups .
     
    ![DV_result](assets/DV_result.png)
    * Result
      * According to the result above and reference can extract 4 indicators from 16 varaibles
        1. 線上媒體政治參與(online_media_pp) : read_media / like_media / share_media / comment_media
            -> reference : 劉嘉薇，2019
        2. 投票參與(voting) : election_mayor / election_18
            -> reference : Barnes and Kaase (1979)
        3. 線下媒體政治參與(offline_media_pp) : read_election_news / read_election_leaflet
            -> reference : 徐火炎，2001
        4. 競選工作式政治參與(campaign_worker_pp) : campaign / volunteer
            -> reference : Mibrath and Goel，1977
    
### Step3. Establish Index with result of factor analysis
1. Method1 : Get factors's mean after factor analysis(因素分析 -> 根據構面取平均)
  #### independent variable
```python
political_polarization_vars = ['anti_1']
party_image_vars = ['anti_3', 'anti_4', 'anti_5']
ml_df['political_polarization_mean'] = ml_df[political_polarization_vars].mean(axis=1)
ml_df['party_image_mean'] = ml_df[party_image_vars].mean(axis=1)
```
  #### dependent variable
```python
ml_df['online_media_pp_mean'] = ml_df[online_media_pp_vars].mean(axis=1)
ml_df['voting_mean'] = ml_df[voting_vars].mean(axis=1)
ml_df['offline_media_pp_mean'] = ml_df[offline_media_pp_vars].mean(axis=1)
ml_df['campaign_worker_pp_mean'] = ml_df[campaign_worker_pp_vars].mean(axis=1)
```
2. 
   
* 
