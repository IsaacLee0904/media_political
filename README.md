 ![banner]([https://mms.businesswire.com/media/20210608005361/en/883509/5/Stackline-Logo-DarkBlue.jpg?download=1](https://www.bbc.co.uk/news/world-54477523))

![Python version](https://img.shields.io/badge/Python%20Version-3.9+-lightgrey)
![GitHub last commit](https://img.shields.io/badge/last%20commit-Jul-green)
![GitHub last commit](https://img.shields.io/badge/Repo%20Size-210M-blue)
![GitHub last commit](https://img.shields.io/badge/Project%20Type-Teamson%20Project-red)

Badge [source](https://shields.io/)

# media_political

## Authors
- [@IsaacLee0904](https://github.com/IsaacLee0904)

## Table of Contents
  - [Data Source](#Data-Source)
  - [Repository structure](#repository-structure)


## Data Source
  - Stackline：https://www.stackline.com
  - Postman API：https://www.postman.com

## Repository structure
```
├── TWN-Stackline_Integration
│   ├── bin                   
│   │   ├── main.py                              <- main python data pipeline script for download data from Stackline API.
│   │   ├── CreateSqlScript.py                   <- main python script for create SQL temp-table, table and insert data.
│   │   ├── HouseKeeping                         <- python script for backup.
│   │   ├── Utilities                            <- include all other python module.
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── TWN-Stackline_Integration.bat
│   │    
│   ├── config
│   │   ├── Stackline_api_config.toml            <- config for Stackline api.
│   │   ├── Stackline_integration_config.toml    <- config for SQL server.
│   │  
│   ├── Stackline.drawio.html                    <- ER diagram.
│   │  
│   ├── requirements.txt
│   │  
│   ├── stackline_logs.txt
│
├── Stackline_Sales_ETL
│   ├── Sales ETL_Onetimecode.py                 <- python data pipeline script for sales data from 2019-09-14(201937) ~ 2022-06-11(202223).
│   ├── Sales ETL_Regular.py                     <- main python pipeline script for sales data.
│ 
├── Stackline_Reveiw_Rating_Alert
│   ├── Reveiw_Rating_Alert.py                   <- main python script sending email with review rating star under 3 stars excel file.
│   ├── weekly_reveiw_rating_alert.xlsx          
│   ├── Stackline_Review_Rating_Alert.pdf         
│   ├── Work Flow.png         
│ 
```
