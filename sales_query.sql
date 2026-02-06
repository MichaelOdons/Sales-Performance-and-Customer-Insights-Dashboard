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
