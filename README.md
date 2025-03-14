# Assignment Title

Assignment 2: Web Scraping and Text Analysis
presented by Juan Carlos Katigbak 300366535 to Nikhil Bhardwaj CSIS4260 Special Topics in Data Analytics Section 001

## About the Assignment

The purpose of this assignment is to combine research, benchmarking, and practical coding to perform web scraping from publicly available sources, followed by comprehensive text analysis. The assignment is divided into two parts, each incorporating research and coding elements.

Objectives
Part 1: Web Scraping
Research and Benchmarking:
- Compare two popular web scraping libraries
- Evaluate libraries based on ease of use and performance
- Scrape at least 100 articles/pages from a subreddit/news website about a topic of your choice

Part 2: Text Analysis
Text Analysis:
- Load the data obtained from Part 1
- Apply two text analysis algorithms LSD and LLM
- Generate a directional importance score (+1 for positive, -1 for negative) based on article content characteristics (e.g., length, summarization quality)
- Present the final analysis results clearly in a CSV file


### Prerequisites

- Python (>=3.8)
- Jupyter Notebook (for running notebooks)

## Assignment Structure (if extracted using Github)

Katigbak_300366535_Assignment2
│── beautifulsoup_subreddit_canada_tariffs.ipynb   # Benchmarked BeautifulSoup scraper
│── scrapy_subreddit_canada_tariffs.py             # Benchmarked Scrapy scraper
│── part1.ipynb                                    # Chosen BeautifulSoup scraper used to scrape 100 Reddit                                                        posts
│── part2.ipynb                                    # Text analysis with LSD & Hugging Face algorithms
│── webscraped.csv                                 # Output CSV from Part 1 (created by running part1.ipynb)
│── webscraped.txt                                 # Output TXT from Part 1 (optional, also created                                                                part1.ipynb)
│── textanalysis.csv                               # Final text analysis output from Part 2 (created by                                                            running part2.ipynb)
│── README.md                                      # Assignment documentation (this file)




### Installing (using either macOS/Linux's Terminal or Windows' Command Prompt)

1. Extraction of Katigbak_300366535_Assignment2 folder

If getting it from OneDrive:
Just simply download the Katigbak_300366535_Assignment2.zip folder and extract the folder which will have the files.                           

If getting it from Github:
Extract Katigbak_300366535_Assignment2.zip and make sure that the extracted folder will have the files because there is a tendency that the extracted folder will have another folder before you are able to get the files. You also have to make sure when you run the virtual environment, you are able to locate the exact location of the Katigbak_300366535_Assignment2 folder otherwise it will not run properly.

2. Set Up a Virtual Environment (Optional but Recommended)
   
For macOS/Linux (Terminal):
python -m venv env
source env/bin/activate

For Windows (Command Prompt):
python -m venv env
env\Scripts\activate

3. Install Dependencies

* Make sure to proactively do this in both Terminal/Command Prompt and Jupyter Notebook just to be sure so that there is no interruption with running the assignment!

For macOS/Linux (Terminal)/For Windows (Command Prompt):
pip install beautifulsoup4 requests pandas numpy lxml transformers torch sentencepiece scipy scikit-learn tqdm ipywidgets scrapy


For Jupyter Notebook:
!pip install beautifulsoup4 requests pandas numpy lxml transformers torch sentencepiece scipy scikit-learn tqdm ipywidgets scrapy


## Running each part of the assignment
**Best to run Part 1 and 2 in sequence to ensure that the whole assignment runs

Part 1: Web Scraping
First, we are going to be comparing 2 web scraper libraries to use. In my case, I chose BeautifulSoup and Scrapy.

(1) BeautifulSoup
using either macOS/Linux's Terminal or Windows' Command Prompt, run:

jupyter notebook

this will then open Jupyter Notebook in your web browser and once inside Jupyter Notebook, open beautifulsoup_subreddit_canada_tariffs.ipynb in the Katigbak_300366535_Assignment2 folder wherever it is located in the Jupyter Notebook and run each code using shift + enter

(2) Scrapy
using either macOS/Linux's Terminal or Windows' Command Prompt, open a new tab for the Shell and run:

if using macOS/Linux's Terminal:

cd ~/Desktop/Katigbak_300366535_Assignment2
scrapy runspider scrapy_subreddit_canada_tariffs.py

if using Windows' Command Prompt:

cd %USERPROFILE%\Desktop\Katigbak_300366535_Assignment2
(e.g. cd OneDrive\Desktop\Katigbak_300366535_Assignment2) #since Katigbak_300366535_Assignment2 is the folder with the file

scrapy runspider scrapy_subreddit_canada_tariffs.py


Second, since I decided with BeautifulSoup we continue using part1.ipynb in the Katigbak_300366535_Assignment2 folder wherever it is located in the Jupyter Notebook and run each code using shift + enter. Once you run everything, it will create the webscraped.csv and webscraped.txt files in the same Katigbak_300366535_Assignment2 folder with webscraped.csv being the file to be able to do Part 2: Text Analysis (just the same, the webscraped.csv and webscraped.txt files are also available in the Katigbak_300366535_Assignment2 folder and will be overwritten once part1.ipynb is run).


Part 2: Text Analysis
In the same Jupyter Notebook wherever Katigbak_300366535_Assignment2 folder is located, open part2.ipynb and run each code using shift + enter which will then create textanalysis.csv in the samen folder which contains a summary of each article with corresponding importance score. (just the same, textanalysis.csv is also available in the Katigbak_300366535_Assignment2 folder and will be overwritten once part2.ipynb is run).

You can also skip Part 1 and go straight to Part 2 using either macOS/Linux's Terminal or Windows' Command Prompt, run:

jupyter notebook

this will then open Jupyter Notebook in your web browser and once inside Jupyter Notebook, open part2.ipynb and run each code using shift + enter.


## Explanation of Each Part

Part 1: Web Scraping with BeautifulSoup
The goal of Part 1 was to evaluate popular web scraping libraries (Scrapy, BeautifulSoup, and Playwright) for retrieving data from websites, focusing primarily on ease of use, reliability, and beginner friendliness. After researching and benchmarking these libraries:

Scrapy:

Pros: Highly efficient and scalable, built-in support for asynchronous scraping.
Cons: Higher complexity, less beginner-friendly due to the steep learning curve.
BeautifulSoup (selected library):

Pros: Easy to use and beginner-friendly. Simple syntax for parsing HTML content.
Cons: Slightly slower compared to Scrapy, not designed for large-scale scraping tasks.
Playwright (browser automation):

Pros: Supports dynamic web pages that use JavaScript.
Cons: Slower than Scrapy and BeautifulSoup due to full browser automation overhead.
Why BeautifulSoup?
BeautifulSoup was chosen due to ease of use, readability of the code, and excellent suitability for beginners learning web scraping.

Implementation
Scraped the r/canada subreddit for 100 posts containing the topic "tariffs".
Collected and parsed the Reddit titles, direct Reddit URLs, external links (if provided), and retrieved up to 50 comments per post.
Implemented retry logic to handle Reddit API limitations (HTTP 429 rate limits).
Generated two files (webscraped.csv and webscraped.txt) containing the retrieved posts and associated comments.
Output Example:


[1/100] Retrieved: 'Only Works as a State': Trump Vows Not 'To Bend' On Tariffs
Reddit URL: [reddit link]
External URL: [external link]
...
Collected 100 posts in 150.25 seconds.
Scraping complete!

Key Findings for Part 1:
BeautifulSoup effectively retrieved data with minimal complexity.
Error handling was necessary due to occasional retrieval issues (rate limits or unavailable content).
Adding delays (time.sleep()) was necessary to avoid overwhelming Reddit servers and getting rate-limited (HTTP 429 errors).
Proceeding to Part 2
After generating webscraped.csv and webscraped.txt, you're ready to perform text analysis on the scraped comments.










Part 2: Data Storage and Retrieval
In this section, the goal was to compare the performance of Pandas vs. Polars for data manipulation and analysis. Additionally, I implemented four technical indicators to enhance the dataset and trained two machine learning models (Linear Regression & Random Forest) to predict stock prices.

Step 1 - Loading and Filtering Data
First, I checked if the CSV dataset exists before loading it to avoid file errors.

import os
import pandas as pd

csv_file = "all_stocks_5yr.csv"

if not os.path.exists(csv_file):
    raise FileNotFoundError(f"Error: {csv_file} not found. Please place the CSV file in the same folder as this script.")

df = pd.read_csv(csv_file)
print("Dataset loaded successfully.")

Ensures the script runs on any computer without assuming the dataset is present. After loading, I filtered stocks where the closing price was greater than $100, a simple example of data filtering.

filtered_df = df[df['close'] > 100]
print(filtered_df.head())

Then, I did the same filtering operation using Polars, since it’s known for its speed.

import polars as pl
df_polars = pl.read_csv(csv_file)

filtered_df_polars = df_polars.filter(pl.col("close") > 100)
print(filtered_df_polars.head())

This demonstrates how Pandas and Polars handle filtering differently.

Performance Benchmark:

%timeit pd.read_csv(csv_file)
%timeit pl.read_csv(csv_file)

Pandas: 329 ms
Polars: 20.5 ms

Polars was significantly faster at reading CSV files (16x speedup).

Step 2 - Enhancing the Dataset with 4 Technical Indicators
Since raw data isn’t always useful for predictions, I enhanced the dataset by adding four key technical indicators using both Pandas and Polars.

(1) Simple & Exponential Moving Averages (SMA & EMA)
SMA and EMA help smooth price trends by averaging past values.

Pandas Implementation:

df["SMA_20"] = df["close"].rolling(window=20).mean()
df["EMA_20"] = df["close"].ewm(span=20, adjust=False).mean()

Polars Implementation:

df_polars = df_polars.with_columns([
    df_polars["close"].rolling_mean(window_size=20).alias("SMA_20"),
    df_polars["close"].ewm_mean(span=20).alias("EMA_20"),
])

(2) Moving Average Convergence Divergence (MACD)
MACD measures the momentum of price movements.

Pandas Implementation:

import ta
macd = ta.trend.MACD(df["close"])
df["MACD"] = macd.macd()
df["MACD_Signal"] = macd.macd_signal()

Polars Implementation:

def compute_macd(df, column="close"):
    short_ema = df[column].ewm_mean(span=12)
    long_ema = df[column].ewm_mean(span=26)
    macd = short_ema - long_ema
    macd_signal = macd.ewm_mean(span=9)
    return macd, macd_signal

macd, macd_signal = compute_macd(df_polars, "close")
df_polars = df_polars.with_columns(macd.alias("MACD"), macd_signal.alias("MACD_Signal"))

(3) Bollinger Bands
Measures volatility by plotting an upper and lower band around the price.

Pandas Implementation:

bb = ta.volatility.BollingerBands(df["close"], window=20)
df["BB_High"] = bb.bollinger_hband()
df["BB_Low"] = bb.bollinger_lband()

Polars Implementation:

def compute_bollinger_bands(df, column="close", window=20):
    sma = df[column].rolling_mean(window_size=window)
    std_dev = df[column].rolling_std(window_size=window)
    upper_band = sma + (2 * std_dev)
    lower_band = sma - (2 * std_dev)
    return upper_band, lower_band

bb_high, bb_low = compute_bollinger_bands(df_polars, "close", 20)
df_polars = df_polars.with_columns(bb_high.alias("BB_High"), bb_low.alias("BB_Low"))

(4) Stochastic Oscillator
Measures the stock’s closing price relative to its price range over time.

Pandas Implementation:

df["Lowest_Low"] = df["low"].rolling(window=14).min()
df["Highest_High"] = df["high"].rolling(window=14).max()
df["Stoch"] = 100 * ((df["close"] - df["Lowest_Low"]) / (df["Highest_High"] - df["Lowest_Low"]))

Polars Implementation:

df_polars = df_polars.with_columns([
    df_polars["low"].rolling_min(window_size=14).alias("Lowest_Low"),
    df_polars["high"].rolling_max(window_size=14).alias("Highest_High"),
])
df_polars = df_polars.with_columns(
    ((df_polars["close"] - df_polars["Lowest_Low"]) / 
     (df_polars["Highest_High"] - df_polars["Lowest_Low"]) * 100).alias("Stoch")
)

Forward and backward filled missing values to avoid gaps in calculations.

df.ffill(inplace=True)
df.bfill(inplace=True)
df_polars = df_polars.fill_null(strategy="forward").fill_null(strategy="backward")

Step 3 - Training Machine Learning Models
After enriching the dataset, I trained Linear Regression and Random Forest models to predict the next day’s closing price.

Defining Features & Target

features = ["SMA_20", "EMA_20", "MACD", "MACD_Signal", "BB_High", "BB_Low", "Stoch"]
df_pandas["target"] = df_pandas["close"].shift(-1)
df_polars = df_polars.with_columns(df_polars["close"].shift(-1).alias("target"))

Splitting Data for Training & Testing

X_train_pandas, X_test_pandas, y_train_pandas, y_test_pandas = train_test_split(
    df_pandas[features], df_pandas["target"], test_size=0.2, random_state=42, shuffle=False
)

X_train_polars, X_test_polars, y_train_polars, y_test_polars = train_test_split(
    df_polars.select(features).to_pandas(), df_polars.select("target").to_pandas(), 
    test_size=0.2, random_state=42, shuffle=False
)

Training Models

(1) Linear Regression

lr_model_pandas = LinearRegression().fit(X_train_pandas, y_train_pandas)
lr_model_polars = LinearRegression().fit(X_train_polars, y_train_polars)

(2) Random Forest

rf_model_pandas = RandomForestRegressor(n_estimators=100).fit(X_train_pandas, y_train_pandas)
rf_model_polars = RandomForestRegressor(n_estimators=100).fit(X_train_polars, y_train_polars)

Evaluating Models

print("MAE:", mean_absolute_error(y_test_pandas, y_pred_lr_pandas))
print("R2 Score:", r2_score(y_test_pandas, y_pred_lr_pandas))

Findings:
1. Polars models performed slightly worse than Pandas.
2. Pandas and Polars both showed similar MAE, but Polars had slower training.

Final Takeaways:
1. Polars is faster than Pandas for data manipulation, but it’s less optimized for ML tasks.
2. Random Forest outperformed Linear Regression for stock price predictions.
3. All four technical indicators were useful in improving model accuracy.


Part 3: Visual Dashboard for Benchmarking & Predictions
In this final section, the goal was to create an interactive dashboard to display:

Benchmarking results from Part 1 (CSV vs. Parquet, Pandas vs. Polars, ML model performance)
Stock price predictions from Part 2, including actual & predicted prices and technical indicators

For this, I chose Streamlit as the dashboarding framework because: (1) It provides an interactive and user-friendly interface, (2) it allows real-time updates for selected stock tickers, (3) it integrates well with Plotly for data visualization, and (4) it is good for beginners.

Step 1 - Loading & Caching Data
To improve performance, I cached the benchmark data and stock dataset using @st.cache_data, ensuring data is only loaded once unless the script is restarted.
    
Caching the data prevents unnecessary reloading, making the dashboard faster and is useful when switching between different stock tickers.

Step 2 - Creating the Dashboard Layout
The dashboard has two sections, controlled via a sidebar navigation menu.

This allows users to switch between:

1. Benchmark Results
2. Stock Price Predictions
   
Step 3 - Displaying Benchmark Results (Dashboard A)
This section visualizes machine learning model performance and CSV vs. Parquet storage performance.

Comparison of MAE, MSE, and R² Score for Pandas vs. Polars models.

fig1 = px.bar(benchmark_long, 
              x="Algorithm", 
              y="Value", 
              color="Metric", 
              barmode="group", 
              title="Model Performance Comparison (MAE, MSE, R² Score)")
st.plotly_chart(fig1)

Findings:
1. Random Forest performed slightly better than Linear Regression in Pandas but had slower performance in Polars.

Comparison of CSV vs. Parquet read times across different dataset sizes (1x, 10x, 100x).

fig2 = px.bar(storage_benchmark, 
              x="Scale", 
              y="Read Time (ms)", 
              color="Kind of File", 
              barmode="group",
              title="CSV vs Parquet Read Time Across Different Scales")
st.plotly_chart(fig2)

Findings:
1. Parquet was consistently faster than CSV, especially at 10x and 100x scales.
2. At 100x scale, Parquet was 19.4x faster than CSV.
   
Step 4 - Stock Price Predictions (Dashboard B)
This section visualizes actual vs. predicted stock prices and includes key technical indicators.

Selecting a Stock Ticker

stock_ticker = st.selectbox("Select a stock ticker:", df["name"].unique())
df_stock = df[df["name"] == stock_ticker]

Users can select any stock ticker, and the charts will update dynamically.

Candlestick Chart with Predictions

Displays actual stock price movement with predicted next-day prices.

fig3.add_trace(go.Candlestick(
    x=df_stock["date"],
    open=df_stock["open"],
    high=df_stock["high"],
    low=df_stock["low"],
    close=df_stock["close"],
    name="Actual Price",
    increasing_line_color="green",
    decreasing_line_color="red"
))

fig3.add_trace(go.Scatter(
    x=df_stock["date"], 
    y=df_stock["close"].shift(-1),
    mode="lines",
    name="Predicted Price",
    line=dict(color="black", dash="dot")
))

Users can visually compare actual vs. predicted prices.

Overlaying Technical Indicators

To help analyze trends, I plotted: (1) SMA (20) & EMA (20), (2) Bollinger Bands, (3) MACD & MACD Signal, and (4) Stochastic Oscillator

fig3.add_trace(go.Scatter(x=df_stock["date"], y=df_stock["SMA_20"], 
                          mode="lines", name="SMA (20)", line=dict(color='blue')))
fig3.add_trace(go.Scatter(x=df_stock["date"], y=df_stock["EMA_20"], 
                          mode="lines", name="EMA (20)", line=dict(color='orange', dash='dot')))

fig3.add_trace(go.Scatter(x=df_stock["date"], y=df_stock["BB_High"], 
                          mode="lines", name="Bollinger High", line=dict(color='purple', dash='dot')))
fig3.add_trace(go.Scatter(x=df_stock["date"], y=df_stock["BB_Low"], 
                          mode="lines", name="Bollinger Low", line=dict(color='purple', dash='dot')))

fig3.add_trace(go.Scatter(x=df_stock["date"], y=df_stock["MACD"], 
                          mode="lines", name="MACD", line=dict(color='green')))
fig3.add_trace(go.Scatter(x=df_stock["date"], y=df_stock["MACD_Signal"], 
                          mode="lines", name="MACD Signal", line=dict(color='red')))

fig3.add_trace(go.Scatter(x=df_stock["date"], y=df_stock["Stoch"], 
                          mode="lines", name="Stochastic Oscillator", line=dict(color='brown', dash='dot')))

Users can toggle indicators on/off using the legend.

Final Takeaways:
1. Streamlit provided a fast, interactive way to visualize model results.
2. Dashboard A demonstrated how CSV vs. Parquet and Pandas vs. Polars performed across different benchmarks.
3. Dashboard B allowed users to explore stock price predictions and key technical indicators dynamically.
   

## Author

* **Juan Carlos Katigbak** - *Initial work to Final work* - (https://github.com/juancarloskatigbak8)
