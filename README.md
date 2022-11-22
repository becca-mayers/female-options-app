# 🤹‍♀️ Female Options Calculator
*The accurate alternative to the Female Delusion Calculator.*


![Calculator Home](https://github.com/becca-mayers/female-options-app/blob/36f51dd7d86f141eca107a0ca5787434190ca6a0/imgs/app-hero.png)

![Calculator Widgets](https://github.com/becca-mayers/female-options-app/blob/1e977dc8ba25cab42cb4e7f2a69c082374a49cb9/imgs/app-widgets.png)


# The Data
All variables came from the [2020 CDC National Health Interview Survey (NHIS)](https://www.cdc.gov/nchs/nhis/2020nhis.htm) data. 

## Data Wrangling process
1. Filter dataset for 18+ years of age
2. Categorize marital status categories as either married or single:
    - Codes 1-4 are categorized as married
    - Codes 5-7 are categorized as single
4. Convert hispanic codes into Yes/No flags
5. Clean race types (White, Black, Asian, or Other):
    - Codes 01, 06, 07, 08 and 09 are flagged as White
    - Codes 2, 10, 11, and 12 are flagged as Black
    - Codes 3, 4, 5, 13, 14, and 15 are flagged as Asian
    - All remaining codes are flagged as Other

##### Widgets
+ Age ranges from 18 to 85
+ Height range dependent on partner's gender preference  
+ (Annual) income ranges from $0,000.00 to $250,000.00+  
+ Race multiselect options are Asian, Black, Hispanic, Other, and/or White  
+ Exclude obesity checkbox is not default selected
+ Exclude married checkbox is default selected  
+ Ranges defaulted to 25th and 75th deciles  
