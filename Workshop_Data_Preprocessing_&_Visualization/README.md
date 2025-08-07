🧮 Diamond Price Analysis & Preprocessing
This notebook explores and preprocesses the diamonds dataset, with a focus on analyzing the relationship between price and key features like carat, cut, clarity, color, depth, table, and dimensions (x, y, z). The notebook includes:

🔍 Exploratory Data Analysis (EDA)
- Scatter plots for visualizing price vs. numerical features (carat, depth, table)

- Heatmap to explore multicollinearity, especially between dimensions and carat

- Correlation analysis between volume (x * y * z) and price

🧼 Data Preprocessing
- Handling missing values and outliers (Winsorization & clipping)

- Log transformation of skewed features (e.g. carat)

- Feature scaling (StandardScaler, RobustScaler)

- Label encoding of categorical features (cut, clarity, color)

- Custom scaling strategies for different types of features

- Creation of new features like log_carat and volume

📁 Output
- Cleaned and transformed dataset exported to CSV for future modeling or analysis

*Note:*
- This notebook is a practice exercise in data preprocessing and feature engineering, not model building.