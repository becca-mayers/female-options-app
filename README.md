# 🤹‍♀️ Female Options Calculator
The accurate alternative to the Female Delusion Calculator.
---

![Calculator Home](https://github.com/becca-mayers/female-options-app/blob/main/imgs/app-hero.png)

![Calculator Widgets](https://github.com/becca-mayers/female-options-app/blob/main/imgs/app-widgets.png)

# The Data
The marital status, age, race type, hispanic flag, and income variables came from the 2020 [US Census Annual Social and Economic Supplement (ASEC)](https://www.census.gov/data/datasets/time-series/demo/cps/cps-asec.2020.html#list-tab-YY1CQJF340IKCHJEXH)  data. 
The obesity metric came from the 2011-2020 year start [Center for Disease Control and Prevention (CDC) Behavioral Risk Factor Surveillance System](https://chronicdata.cdc.gov/Nutrition-Physical-Activity-and-Obesity/Nutrition-Physical-Activity-and-Obesity-Behavioral/hn4x-zwk7).


## ASEC Variables
Data dictionary, including variable descriptions, available [here](https://www2.census.gov/programs-surveys/cps/datasets/2020/march/ASEC2020ddl_pub_full.pdf).
+ A_AGE: Age
    - 00-79 corresponds to 0-79 years of age
    - 80 corresponds to 80-84 years of age
    - 85 corresponds to 85+ years of age
+ A_MARITL: Marital status
    - 1, 2 and 3 are variations on married respondents
    - 4 is coded for widowers
    - 5 is coded for divorcees
    - 6 is coded for separated individuals
        * Note separated individuals are flagged as "Single"
    - 7 is coded for single (never married) respondents
+ A_SEX: Sex
    - 1 is coded for males
    - 2 is coded for females
+ PEHSPNON: Are you Spanish, Hispanic, or Latino?
    - 1 is coded for Yes
    - 2 is coded for No
+ PRDTRACE: Race
    - 01 is coded for White only
    - 02 is coded for Black only
    - 03 is coded for American Indian, Alaskan Native only (AI)
    - 04 is coded for Asian only
    - 05 is coded for Hawaiian/Pacific Islander only (HP)
    - 06 is coded for White-Black
    - 07 is coded for White-AI
    - 08 is coded for White-Asian
    - 09 is coded for White-HP
    - 10 is coded for Black-AI
    - 11 is coded for Black-Asian
    - 12 is coded for Black-HP
    - 13 is coded for AI-Asian
    - 14 is coded for AI-HP
    - 15 is coded for Asian-HP
    - 16 is coded for White-Black-AI
    - 17 is coded for White-Black-Asian
    - 18 is coded for White-Black-HP
    - 19 is coded for White-AI-Asian
    - 20 is coded for White-AI-HP
    - 21 is coded for White-Asian-HP
    - 22 is coded for Black-AI-Asian
    - 23 is coded for White-Black-AI-Asian
    - 24 is coded for White-AI-Asian-HP
    - 25 is coded for Other 3 race comb.
    - 26 is coded for Other 4 or 5 race comb.
+ PTOT_R: Income
    - 0 is coded for NO INCOME
    - 1 is coded for UNDER $2,500 OR LOSS
    - 2 is coded for $2,500 TO $4,999
    - 3 is coded for $5,000 TO $7,499
    - 4 is coded for $7,500 TO $9,999
    - 5 is coded for $10,000 TO $12,499
    - 6 is coded for $12,500 TO $14,999
    - 7 is coded for $15,000 TO $17,499
    - 8 is coded for $17,500 TO $19,999
    - 9 is coded for $20,000 TO $22,499
    - 10 is coded for $22,500 to $24,999
    - 11 is coded for $25,000 to $27,499
    - 12 is coded for $27,500 to $29,999
    - 13 is coded for $30,000 to $32,499
    - 14 is coded for $32,500 to $34,999
    - 15 is coded for $35,000 to $37,499
    - 16 is coded for $37,500 to $39,999
    - 17 is coded for $40,000 to $42,499
    - 18 is coded for $42,500 to $44,999
    - 19 is coded for $45,000 to $47,499
    - 20 is coded for $47,500 to $49,999
    - 21 is coded for $50,000 to $52,499
    - 22 is coded for $52,500 to $54,999
    - 23 is coded for $55,000 to $57,499
    - 24 is coded for $57,500 to $59,999
    - 25 is coded for $60,000 to $62,499
    - 26 is coded for $62,500 to $64,999
    - 27 is coded for $65,000 to $67,499
    - 28 is coded for $67,500 to $69,999
    - 29 is coded for $70,000 to $72,499
    - 30 is coded for $72,500 to $74,999
    - 31 is coded for $75,000 to $77,499
    - 32 is coded for $77,500 to $79,999
    - 33 is coded for $80,000 to $82,499
    - 34 is coded for $82,500 to $84,999
    - 35 is coded for $85,000 to $87,499
    - 36 is coded for $87,500 to $89,999
    - 37 is coded for $90,000 to $92,499
    - 38 is coded for $92,500 to $94,999
    - 39 is coded for $95,000 to $97,499
    - 40 is coded for $97,500 to $99,999
    - 41 is coded for $100,000 and over

## ASEC Data Wrangling process
1. Filter dataset for males 18+ years of age
2. Categorize marital status categories as either married or single:
    - Codes 1-4 are categorized as married
    - Codes 5-7 are categorized as single
4. Convert hispanic codes into Yes/No flags
5. Clean race types (White, Black, Asian, or Other):
    - Codes 01, 06, 07, 08 and 09 are flagged as White
    - Codes 2, 10, 11, and 12 are flagged as Black
    - Codes 3, 4, 5, 13, 14, and 15 are flagged as Asian
    - All remaining codes are flagged as Other
6. Convert income codes into income values
    - Every other code is paired together (ex., 3 & 4, 5 & 6, etc.) with the maximum income for the lesser code (ex., both codes 3 & 4 are indicated as $7,499, both codes 5 & 6 are indicated as $12,499, etc.)

# Nutrition, Physical Activity, and Obesity - Behavioral Risk Factor Surveillance System
This dataset includes data on adult's diet, physical activity, and weight status from Behavioral Risk Factor Surveillance System. This data is used for DNPAO's Data, Trends, and Maps database, which provides national and state specific data on obesity, nutrition, physical activity, and breastfeeding.

## Obesity Variables
+ YearStart
+ LocationAbbr
+ Question
+ Data_Value_Type
+ Data_Value
+ Data_Value_Alt
+ Low_Confidence_Limit
+ High_Confidence_Limit
+ Sample_Size
+ Total
+ Gender

## Obesity Data Wrangling Process
1. Filter dataset for year starting 2020, US location
2. Filter questions for "Percent of adults aged 18 years and older who have obesity"
3. Filter dataset for the male gender
4. Index the remaining Data_Value variable for percentage obesity (31.7%)

##### Widgets
+ Age ranges from 18 to 85; Default range is 33-42
+ Height ranges from 4'1" to 6'12"; Default range is 5'9" to 6'3"
+ (Annual) income ranges from $0,000.00 to $100,000.00+; Default range is up to $82,500.00
+ Race multiselect options are Asian, Black, Other, and/or White; All are default selections
+ Exclude obesity checkbox is not default selected
+ Exclude married checkbox is default selected
