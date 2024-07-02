# Laptop Price Prediction

This project involves analyzing a dataset of laptop prices and specifications from various companies. The goal is to predict the price of a laptop based on its specifications using machine learning models.

## Project Description

### Exploratory Data Analysis (EDA)

1. **Data Cleaning**:
    - Handled missing values and outliers.
    - Standardized column names and data formats.

2. **Descriptive Statistics**:
    - Calculated mean, median, mode, and other statistical measures for each column.
    - Identified distribution patterns and summary statistics.

3. **Visualization**:
    - Plotted histograms, box plots, and scatter plots to visualize the distribution of data.
    - Created correlation matrices and heatmaps to understand relationships between variables.

### Key Findings from EDA

- **Distribution of Data**:
    - Found that laptop prices follow a right-skewed distribution.
    - Identified significant variation in specifications like RAM, storage, and processor type across different price ranges.

- **Correlation Analysis**:
    - Discovered strong positive correlations between laptop prices and certain specifications, such as processor type, RAM size, and storage capacity.

### Model Building and Evaluation

1. **Data Preprocessing**:
    - Used pipelines and column transformers for efficient data preprocessing.
    - Applied techniques like one-hot encoding for categorical variables and scaling for numerical variables.

2. **Modeling**:
    - Implemented two machine learning algorithms: Linear Regression and XGBoost.
    - Split the data into training and testing sets to evaluate model performance.

3. **Evaluation Metrics**:
    - Used R-squared and Mean Absolute Error (MAE) to assess model accuracy.
    - Compared model performance to identify the best algorithm for price prediction.

### Results

- **Linear Regression**:
    - Achieved an accuracy of 79.7%.
    - R-squared: 0.797
    - MAE: (calculated value)

- **XGBoost**:
    - Achieved an accuracy of 86.5%.
    - R-squared: 0.865
    - MAE: (calculated value)

### Conclusion

- **Performance Comparison**:
    - XGBoost outperformed Linear Regression, providing a better fit for the data with higher accuracy and lower error rates.
    - This indicates that XGBoost is more suitable for this dataset due to its ability to handle complex relationships between features.
