# Sales-Performance-and-Customer-Insights-Dashboard

## Table of Contents
-[Project Overview](#project-overview)

-[Data Source](#data-source)

-[Tools](#tools)

-[Data Cleaning and Preparation](#data-cleaning-and-preparation)

-[Exploratory Data Analysis](#exploratory-data-analysis)

-[Data Analysis](#data-analysis)

-[Results and Findings](#results-and-findings)

-[Recommendations](#recommendations)

-[Limitations](#limitations)

-[Reference](#reference)

### Project Overview
This project focuses on analyzing a company’s sales data to uncover actionable insights that drive business growth. By building a Sales Performance Analysis and Customer Insights Dashboard, you will explore critical aspects of sales, customer behavior, and profitability—areas that every company prioritizes.

The goal of this project is to help decision-makers answer key business questions, such as:

• Revenue Analysis: Which products generate the most revenue?

• Regional Performance: Which regions or markets perform the best?

• Customer Insights: Who are the top customers contributing to revenue?

• Sales Trends: How do sales fluctuate month over month?

• Profit Optimization: What strategies can the business use to increase profitability?

Through this project, you will demonstrate your ability to clean and analyze data, visualize trends, and create dashboards that summarize complex information into actionable insights.

### Data Source
Sales Data: The primary dataset used for this analysis is the 'Sample_Superstore.csv' file containing retail sales data covering customer details, product information, order and shipping records, and financial metrics such as sales, quantity, discount, and profit. It captures transactions across different regions, customer segments, and product categories, making it ideal for analyzing sales performance, customer behavior, regional trends, and profitability.

### Tools
- Excel ( used for data cleaning and formatting raw data, pivot tables for summaries)
- SQL Server ( used for analysis, querying dataset from databases, filtering, sorting and aggregating data)
- Tableau ( Building interactive dashboards, visualizing trends, KPIs, and patterns, sharing insihts with stakeholders)
- Python (cleaning and transforming data(pandas), performing statistical analsysis, building predicticve models and machine learning)

### Data Cleaning and Preparation
• Removed duplicate records to ensure data accuracy

• Handled missing values by correcting, removing, or validating incomplete entries

• Standardized date formats for consistent time-based analysis

• Cleaned and corrected inconsistent text values (e.g., product names, regions, categories)

• Converted data types (text to numbers, dates, currency) for proper analysis

• Checked and corrected calculation errors in sales, profit, and quantity fields

• Created new calculated fields (e.g., profit margin, total revenue, monthly sales)

• Filtered out irrelevant or invalid records (e.g., negative or zero sales where inappropriate)

• Validated data integrity across tables and columns

• Prepared the dataset for analysis and visualization in Excel, SQL, Tableau, and Python

### Exploratory Data Analysis

EDA involves exploring sales data to answer key questions, such as:

1. Which products generate the most revenue?

2. Which regions or markets perform the best?

3. Who are the top products contributing to revenue?

4. How do sales fluctuate month over month?

5. What strategies can the business use to increase profitability?

### Data Analysis 
```sql
CREATE DATABASE Sales_Analysis;
USE Sales_Analysis;

CREATE TABLE sales_data (
	 Row_ID INT,
	 Order_ID VARCHAR(50),
	 Order_Date	DATE,
	 Ship_Date DATE,
	 Ship_Mode	VARCHAR(50),
	 Customer_ID VARCHAR(50),
	 Customer_Name VARCHAR(100),
	 Segment VARCHAR(50),
	 Country VARCHAR(100),
	 City VARCHAR(50),
	 State VARCHAR(50),
	 Postal_Code INT,
	 Region	VARCHAR(50),
	 Product_ID	VARCHAR(50),
	 Category VARCHAR(100),
	 Sub_Category VARCHAR(100),
	 Product_Name VARCHAR(100),
	 Sales DECIMAL(10,2),
	 Quantity INT,
	 Discount DECIMAL(10,2),
	 Profit DECIMAL(10,2)
)

--REMOVE DUPLICATES
select * from [dbo].[cleaned_sales_data.csv]

WITH CTE AS (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY order_id   -- duplicates are checked here
               ORDER BY row_id         -- keep the first row inserted
           ) AS rn
    FROM [dbo].[cleaned_sales_data.csv]

)
DELETE FROM CTE
WHERE rn > 1;


--HANDLING MISSING VALUES
DELETE FROM [dbo].[cleaned_sales_data.csv]
WHERE sales IS NULL
   OR profit IS NULL
   OR region IS NULL;


--VALIDATE DATA
SELECT TOP 10 *
FROM [dbo].[cleaned_sales_data.csv];

--Total Sales & Profit
SELECT 
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM [dbo].[cleaned_sales_data.csv]


--Sales by Region
SELECT 
    region,
    SUM(sales) AS total_sales
FROM [dbo].[cleaned_sales_data.csv]
GROUP BY region
ORDER BY total_sales DESC;

--Top Products
SELECT 
    Product_Name,
    SUM(sales) AS total_sales
FROM [dbo].[cleaned_sales_data.csv]
GROUP BY Product_Name
ORDER BY total_sales DESC;

--Sales Trend (Monthly)
SELECT 
    FORMAT(order_date, 'yyyy-MM') AS month,  -- formats as 2026-02
    SUM(sales) AS monthly_sales
FROM [dbo].[cleaned_sales_data.csv]
GROUP BY FORMAT(order_date, 'yyyy-MM')
ORDER BY month;
```

### Results and Findings
• Strong overall business performance with total sales of $2.29M and total profit of $286K across 5,009 orders, indicating healthy revenue generation with room for profit optimization. 

• West region is the top-performing region, contributing the highest share of sales compared to East, Central, and South regions, making it the strongest market for revenue growth. 

• Technology products dominate sales, outperforming Furniture and Office Supplies, showing that high-tech items are the main revenue drivers for the business. 

• High-value products drive significant revenue, with items like Canon imageCLASS Copiers and Cisco TelePresence Systems emerging as top-selling products, indicating strong demand for premium products. 

• Consistent sales growth over time, with sales increasing steadily from 2014 to 2017, reflecting business expansion and improved market penetration. 

• Product category mix shows opportunity for profit improvement, as Furniture and Office Supplies contribute to sales but lag behind Technology, suggesting pricing or cost optimization opportunities. 

• Customer purchasing behavior favors fewer high-revenue items, meaning a small number of top products account for a large portion of sales, highlighting the importance of inventory and supply chain focus on best sellers. 

### Recommendations
• Focus marketing and sales efforts on the West region to maximize returns

• Expand and promote high-performing Technology products

• Review discount and pricing strategies for Furniture and Office Supplies to improve profit margins

• Leverage sales trend growth to forecast demand and plan inventory more effectively

### Limitations
As I share the insights from our Sales Performance and Customer Insights Dashboard, I also want to highlight a few important limitations to keep in mind:

1. Historical Data Focus:
Our analysis covers 2014 to 2017, so these insights reflect past trends and may not fully capture current or future market dynamics.

2. Limited External Factors:
We didn’t include variables like competitor activity, market conditions, or customer sentiment, which could influence sales and profit outcomes.

3. Data Granularity Constraints:
While we have detailed sales and product information, more granular data like individual customer demographics or product attributes would allow for deeper segmentation and targeted strategies.

4. Preliminary Profit Insights:
Although the dashboard highlights high- and low-performing products, we haven’t conducted a detailed cost or margin analysis, so recommendations around profit optimization are indicative rather than definitive.

5. Descriptive Analysis Only:
This dashboard primarily describes patterns and trends. We haven’t explored predictive modeling or causal relationships, so it guides decision-making but doesn’t predict future performance.

### Reference
- SQL - The Complete Reference

|Heading1|Heading2|
|--------|--------|
|Content1|Content2|
|Python|SQL|
|Excel|Tableau|
