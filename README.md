# Credit Card Customer Intelligence Platform

## Overview

The Credit Card Customer Intelligence Platform is an end-to-end analytics and AI solution designed to help financial institutions understand customer behavior, identify high-value customers, and generate personalized business recommendations.

The project combines Customer Analytics, Machine Learning, Data Visualization, and Generative AI to transform raw transaction data into actionable business insights.

---

## Business Problem

Financial institutions manage millions of customers with diverse spending habits and transaction behaviors. Understanding these customers is essential for improving retention, increasing engagement, and maximizing revenue.

This project addresses the following business challenges:

* Identifying high-value customers
* Understanding spending behavior
* Creating meaningful customer segments
* Generating personalized recommendations
* Providing business-friendly customer insights

---

## Project Architecture

Raw Transaction Data

↓

Feature Engineering

↓

Customer 360 Dataset

↓

├── Customer Segmentation (K-Means)

├── High-Value Customer Classification (Random Forest)

└── Recommendation Engine

↓

Streamlit Dashboard

↓

AI Customer Analyst (Groq + Llama 3.3)

---

## Dataset

The project uses credit card transaction data containing:

* Customer information
* Merchant information
* Transaction details
* Spending behavior
* Transaction channels

### Customer 360 Features Created

Examples include:

* Total Spend
* Average Spend
* Median Spend
* Transaction Count
* Unique Merchant Categories
* Unique Merchants
* Unique Cities
* Online Transaction Percentage
* Fraud Rate
* Refund Rate
* Customer Tenure

---

## Methodology

### 1. Customer 360 Creation

Raw transaction records were aggregated at the customer level to create a comprehensive customer profile.

### 2. Customer Segmentation

K-Means clustering was applied to identify distinct customer groups based on spending and behavioral characteristics.

Final customer segments:

* Stable Everyday Customers
* Loyal Mid-Tier Customers
* Premium Power Users
* Retail-Focused Customers
* Digital First Customers

### 3. High-Value Customer Classification

A Random Forest classifier was trained to identify high-value customers.

High-value customers were defined as customers belonging to the top 20% spending group.

### 4. Feature Importance Analysis

Feature importance was analyzed to identify the strongest drivers of customer value.

Top drivers included:

* Transaction Count
* Customer Segment
* Merchant Diversity
* Merchant Category Diversity
* Geographic Diversity

### 5. AI Customer Analyst

A Generative AI layer was integrated using Groq and Llama 3.3.

The AI analyst generates:

* Executive Summary
* Behavioral Analysis
* Business Opportunities
* Risk Assessment
* Recommended Actions

for any selected customer.

---

## Dashboard Features

### Project Summary

Provides an executive overview of:

* Total Customers
* Customer Segments
* High-Value Customers
* Key Business Findings

### Overview

Displays:

* Customer KPIs
* Segment Distribution
* Business Insights

### Customer Search

Allows users to:

* Search by Customer ID
* View Customer Profile
* View Segment Information
* View Recommendations

### Segment Explorer

Provides:

* Segment Characteristics
* Behavioral Patterns
* Segment-Level Analysis

### Feature Importance

Displays:

* Feature Importance Rankings
* Business Interpretation of Model Drivers

### AI Customer Analyst

Generates AI-powered customer reports including:

* Executive Summary
* Behavioral Analysis
* Opportunities
* Risks
* Recommended Actions

---

## Technology Stack

### Programming

* Python

### Data Analytics

* Pandas
* NumPy

### Machine Learning

* Scikit-Learn
* K-Means Clustering
* Random Forest Classification

### Visualization

* Matplotlib
* Streamlit

### Generative AI

* Groq API
* Llama 3.3

### Deployment

* GitHub
* Streamlit Community Cloud

---

## Key Insights

* Transaction Count is the strongest predictor of customer value.
* Merchant diversity is highly correlated with customer engagement.
* Digital First Customers exhibit significantly higher online transaction activity.
* Premium Power Users generate the highest spending levels.
* Segment-based personalization can improve customer retention and engagement.

---

## Results

* Built a Customer 360 dataset from raw transaction data.
* Identified 5 distinct customer segments.
* Developed a High-Value Customer Classification model.
* Created an interactive Streamlit dashboard.
* Integrated Generative AI for automated customer analysis.
* Successfully deployed the application on Streamlit Cloud.

---

## Future Improvements

Potential enhancements include:

* Customer Lifetime Value (CLV) Prediction
* Churn Prediction
* Real-Time Customer Monitoring
* Retrieval-Augmented Generation (RAG)
* Personalized Offer Recommendation Engine
* Multi-LLM Customer Analytics

---

## Deployment

### Live Application

https://credit-card-customer-intelligence.streamlit.app/

## Screenshots

Add screenshots of:
<img width="1919" height="910" alt="image" src="https://github.com/user-attachments/assets/9575a4bd-fbac-41a7-a462-29766029a47f" />
<img width="929" height="825" alt="image" src="https://github.com/user-attachments/assets/99260905-2bc2-4bd2-ab0b-805d70bd93fb" />
<img width="1125" height="891" alt="image" src="https://github.com/user-attachments/assets/78a8cda3-d05b-4d22-ab1d-6aa21015dacf" />
<img width="1014" height="845" alt="image" src="https://github.com/user-attachments/assets/c4a6acaf-bc7d-49aa-b401-c1a45a085328" />

## Author

Mayan Kalal

Data Analytics | Machine Learning | Generative AI | Customer Intelligence
