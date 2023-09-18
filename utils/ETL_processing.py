# for data ETL
import sys, os
import pandas as pd

# import modules
import etl_utils 

raw_data = pd.read_csv('raw_data.csv')

filter_data = raw_data.loc[raw_data['目前國內政黨當中，請問您是否偏向哪一個政黨？'].isin(['沒有特定支持', '都不支持'])]
filter_data.drop(['您有絶對的權力決定是否要參與本研究。若您願意參與，請務必勾選下列選項：', '請填寫您的電子信箱，以利後續抽獎聯繫使用'], axis=1, inplace=True)

ml_df = etl_utils.data_cleaning(filter_data)
ml_df = ml_df.reset_index(drop=True)
ml_df = etl_utils.feature_engineering(ml_df)
ml_df = etl_utils.DV_feature(ml_df)
ml_df = etl_utils.anti_party_feature(ml_df)
print(ml_df.shape)
print(ml_df.columns)

ml_df.to_csv('/Users/wen/Desktop/github/media_political/modeling_data.csv', index = False)