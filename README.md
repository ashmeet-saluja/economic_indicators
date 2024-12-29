# economic_indicators
Macroeconomic Indicators Analysis
# Macroeconomic Indicators Analysis (2010-2023)

## 📊 Project Overview
This project analyzes the impact of macroeconomic indicators such as GDP growth rate, inflation rate, unemployment rate, and interest rate on stock market performance. The dataset covers data from 2010 to 2023 across multiple countries, providing insights into trends, relationships, and correlations.

## 🗂 Dataset
**Filename:** `economic_indicators_dataset_2010_2023.csv`  
**Description:**  
The dataset contains information on key economic indicators and stock market performance for multiple countries over the period of 2010 to 2023.

### **Columns:**
1. **Date:** Time of data collection (monthly intervals).
2. **Country:** Country of observation.
3. **Inflation Rate (%):** Monthly inflation rate.
4. **GDP Growth Rate (%):** Monthly GDP growth rate.
5. **Unemployment Rate (%):** Monthly unemployment rate.
6. **Interest Rate (%):** Monthly interest rate.
7. **Stock Index Value:** Stock market index value for the respective country.

## 🔍 Exploratory Data Analysis (EDA)
### Key Analyses:
1. **Trend Analysis:**
   - Visualized time series trends for GDP growth, inflation, and unemployment rates.
   - Compared stock market performance with macroeconomic indicators.

2. **Country-Specific Insights:**
   - Focused on specific countries like the USA, Brazil, and France to identify localized trends.

3. **Correlation Analysis:**
   - Created a heatmap to reveal relationships between indicators and stock indices.
   - Identified significant correlations between economic indicators.

4. **Scatter Plot Analysis:**
   - Examined pairwise relationships between key indicators to understand their interactions.

## 🛠️ Tools and Libraries
- **Programming Language:** Python
- **Libraries:** 
  - `pandas` for data manipulation.
  - `matplotlib` and `seaborn` for visualization.
  - `numpy` for numerical computations.

## 📈 Visualizations
Key visualizations include:
- Time series plots for GDP growth, inflation, and unemployment.
- Line charts comparing stock indices and macroeconomic indicators.
- Heatmaps for correlation analysis.
- Pairwise scatter plots for relationships between variables.

## 📂 File Structure
├── economic_indicators_dataset_2010_2023.csv # Dataset file ├── eda_macroeconomic_indicators.ipynb # Jupyter notebook for EDA ├── README.md # Project description └── requirements.txt # Python dependencies


## 🚀 How to Run the Project
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/macroeconomic-analysis.git
Navigate to the project folder:
bash
Copy code
cd macroeconomic-analysis
Install required dependencies:
bash
Copy code
pip install -r requirements.txt
Open the Jupyter notebook to explore the analysis:
bash
Copy code
jupyter notebook eda_macroeconomic_indicators.ipynb
