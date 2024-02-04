# NYC Dark Kitchen Sales Data Analysis Project with Advanced Analytics
## Overview
Welcome to the Dark Kitchen Sales Data Analysis Project with Advanced Analytics! This project is an exciting opportunity to dive deep into the sales data of dark kitchen operations in New York City from 2020 to 2021. Task is to uncover insights into customer behavior, sales trends, and operational efficiency using both traditional analysis and advanced analytical techniques.

Objective
The main goal is to create a comprehensive visual narrative that showcases key insights from the dataset. This includes not just identifying patterns and trends but also applying advanced algorithms and machine learning models to predict future trends, detect anomalies, and understand customer churn.

The dataset contains sales data with the following fields:

* ID: Unique identifier for each order.
* Order Timestamp: Date and time when the order was placed.
* Brand: Brand associated with the order.
* Kitchen: Kitchen where the order was prepared.
* Total amount: Total sales amount of the order.
* Channel: The channel through which the order was received.
* destination_lat: Latitude of the order's destination.
* destination_lng: Longitude of the order's destination.
* Customer Name: Name of the customer.
* Order_delivery_type: Type of delivery (e.g., 3rd party service, Pickup).

## Key Performance Indicators (KPIs)

* Top 100 Customers
* Average Revenue Trend
* Metrics by Kitchen
* Total Revenue by Kitchen
* Delivery Type Distribution
* Metrics by Channels
* Total Revenue and Orders
* Sales Insights
* Brand Insights
* Geographic Distribution of Orders within NYC
* Kitchen and Brand Performance
* Kitchen Insights
* Channel Insights

# Advanced Analytical Techniques

## Anomaly Detection
Objective: Detect unusual patterns or outliers in sales data.
Method: Set a threshold value for the 'Total amount'. Any value above this threshold is flagged as an anomaly.
Tools: Pandas for data manipulation, Plotly for visualization.
Process:
Read the data and convert the 'Order Timestamp' to a datetime format.
Sort data by 'Order Timestamp'.
Define a threshold value to identify anomalies.
Visualize the total amount over time and highlight anomalies with red markers.

## Churn Rate Analysis
Objective: Identify the rate at which customers stop ordering.
Method: Calculate the difference in days between the last order timestamp and the maximum timestamp in the dataset for each customer. If this difference is greater than a defined threshold, the customer is considered churned.
Tools: Pandas for data manipulation, Plotly for visualization.
Process:
Read and preprocess the data.
Compute the 'Order Difference' for each customer.
Define a churn threshold (e.g., 60 days).
Determine the churn status of each customer and visualize the churn rate.

## Monthly Sales Prediction
Objective: Predict sales for each month.
Method: Use a Gradient Boosting Regressor to predict monthly sales.
Tools: Pandas for data manipulation, Scikit-Learn for the regression model, Plotly for visualization.
Process:
Read the data and extract the month from the 'Order Timestamp'.
Split the data into training and testing sets.
Train the Gradient Boosting Regressor.
Make predictions for each month and compare them with actual average sales.

## Weekly Sales Prediction
Objective: Forecast weekly sales amounts.
Method: Apply Gradient Boosting Regressor for predicting sales based on the day of the week.
Tools: Pandas, Scikit-Learn, Plotly.
Process:
Extract the day of the week from the 'Order Timestamp'.
Train the Gradient Boosting Regressor on the day of the week.
Predict sales for each day of the week and compare with actual data.

## Trend Analysis
Objective: Analyze trends in total sales over time.
Method: Visualize daily total sales and observe patterns.
Tools: Pandas for data manipulation, Matplotlib for visualization.
Process:
Read the data and group it by 'Order Date'.
Calculate total sales for each date.
Visualize the trend of sales over time using a color-coded scatter plot, where the color intensity represents the sales amount.
Each of these models serves a specific purpose and will provide a comprehensive understanding of the sales dynamics in the dataset. The combination of anomaly detection, churn analysis, predictive modeling, and trend analysis offers a robust approach to understanding and forecasting business performance.

## Tools
Python (matplotlip, plotly,sklearn, GradientBoostingRegressor), Bigquery, SQL, Looker Studio, PowerPoint. 

## Final outcome

These hypotheses, derived from our data-driven analysis, reveal significant insights into customer behaviors, sales trends, and operational efficiencies. They not only provide clear-cut findings but also uncover curious anomalies and unexplained trends. These insights are invaluable in fine-tuning our business strategies, enhancing customer engagement, and optimizing our operational practices to better align with market dynamics and customer preferences

## Deliverables
* A detailed report with your analysis and findings - Looker Studio
* Visual representations (graphs/charts) of key insights - Looker Studio.
* Any hypotheses , algorithm, ML models and conclusions drawn from the data - PowerPoint file.
