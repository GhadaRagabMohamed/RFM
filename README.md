# RFM Analysis and DataVisualization

Project Overview

This project focuses on analyzing customer data using the RFM (Recency, Frequency, Monetary) model. It includes steps for cleaning the dataset, calculating RFM metrics, segmenting customers into value groups, and visualizing insights through various plots.


---

Key Features

Data Cleaning:

Removed missing and duplicate values.

Filtered out invalid records (e.g., negative quantities or IDs).


RFM Analysis:

Calculated Recency, Frequency, and Monetary metrics.

Segmented customers using quartile-based scoring.

Created an RFM score and labeled customers into "High-Value", "Mid-Value", and "Low-Value" groups.


Visualizations:

Distribution of customer segments.

Top 10 countries by quantity sold.

Weekly transactions trend over time.

Heatmap of top-performing countries by sales quantity.




---

Tools and Libraries Used

Python

pandas

datetime

matplotlib

seaborn

plotly




---

How to Run the Project

1. Clone the repository:

git clone https://github.com/YourUsername/YourRepoName.git


2. Install the required Python libraries:

pip install pandas matplotlib seaborn plotly


3. Run the script:

python rfm.py




---

Project Insights

1. Value Segment Distribution


Shows the distribution of customers across "High-Value", "Mid-Value", and "Low-Value" groups.

2. Top 10 Countries by Total Quantity Sold


Highlights the top-performing countries in terms of sales volume.

3. Weekly Transactions Over Time


Tracks transaction trends over weeks to identify peak periods.


---

Future Improvements

Add a detailed dashboard for interactive visualizations.

Integrate machine learning for predictive customer behavior.

Expand analysis to include time-based trends per product.



---

License

This project is licensed under the MIT License.
