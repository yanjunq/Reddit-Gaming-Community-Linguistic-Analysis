# Reddit Gaming Community Linguistic Analysis

## Project Overview

This project aims to analyze the linguistic characteristics of posts from two distinct gaming subreddits: PCGaming and MobileGaming. By examining word frequency, sentiment, and readability, this research seeks to understand how communication styles vary between PC and mobile gaming platforms.

## Libraries Used

- **General Libraries**: NumPy, Pandas, re, datetime, collections
- **Progress Bar**: tqdm
- **Visualization**: seaborn, matplotlib, matplotlib_venn, wordcloud
- **Machine Learning**: scikit-learn
- **Natural Language Processing**: NLTK
- **Readability Score**: textstat
- **Statistical Analysis**: scipy
- **Reddit API**: PRAW

## Data Collection

- **Sources**: Posts were collected from the PCGaming and MobileGaming subreddits using the PRAW library.
- **Filtering**: 1,000 top posts from each subreddit over the past year were selected to ensure high engagement.
- **Attributes**: Data collected includes title, selftext, score, ID, URL, comments count, and more.

## Data Cleaning

- **Duplicates**: Posts with duplicate titles were removed.
- **Incomplete Data**: Excluded posts with empty selftext, focusing analysis on titles.
- **Final Dataset**: Resulted in 900 unique top posts from each subreddit.

## Data Processing

- **Text Standardization**: Utilized Python's `re` library for cleaning text data.
- **Stopword Removal**: Applied to refine the word frequency analysis.
- **Sentiment Analysis**: Conducted using the VADER tool.
- **Readability**: Evaluated using the textstat library.

## Data Analysis

- **Word Frequency**: Utilized `CountVectorizer` and Chi-Square tests to identify significant lexical differences.
- **Classification Models**: Tested Logistic Regression, Random Forest, and Multinomial Naive Bayes to predict subreddit based on text data.
- **Sentiment and Readability Scores**: Compared between the two subreddits.

## Results

Differences in word usage and style were found between PCGaming and MobileGaming subreddits.

## Limitations

- **Scope**: Limited to top posts; may not represent the full subreddit spectrum.
- **Tools**: Sentiment analysis tools struggled with nuances like sarcasm.
- **Data Focus**: Analysis primarily based on titles due to the high volume of incomplete selftext entries.

## Contact

For questions or support, please contact yqa32@sfu.ca or yinxuanz@sfu.ca

## Commands to Run Jupyter Notebook

To run the Jupyter Notebook, follow these steps:

```bash
# Step 1: Install Jupyter Notebook
pip install jupyter

# Step 2: Navigate to the directory containing the notebook
cd ~/CMPT353_PROJECT

# Step 3: Run Jupyter Notebook
jupyter notebook

# Step 4: Open the notebook file 'data_analysis.ipynb' from the Jupyter interface.



