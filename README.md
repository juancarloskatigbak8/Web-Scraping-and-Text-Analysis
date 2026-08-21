# Web Scraping and Text Analysis

Benchmarking BeautifulSoup vs Scrapy for Reddit scraping, followed by dual-algorithm text analysis comparing a custom LSA summarizer against HuggingFace Transformers. Applied to 100 r/canada posts on the topic of US-Canada tariffs.

---

## What This Project Does

Two-part pipeline: scrape Reddit at scale, then analyze the collected text using two different summarization approaches side by side.

**Part 1** benchmarks BeautifulSoup and Scrapy on the same scraping task: same subreddit, same topic, same volume, measuring fetch time and total scraping time to evaluate speed and usability tradeoffs.

**Part 2** applies two summarization algorithms to the scraped content: a custom word-frequency LSA summarizer and HuggingFace's `facebook/bart-large-cnn` model. Each post gets an extractive summary, an abstractive summary, and an importance score. Results are written to a structured CSV for comparison.

---

## Part 1 — Web Scraping

**Target:** r/canada subreddit, keyword: `tariffs`
**Volume:** 100 posts, up to 50 comments per post
**Output:** `webscraped.csv`, `webscraped.txt`

### Library Benchmarking

Both libraries were tested on the same 10-post scraping task to measure raw performance:

| Library | Fetch Time | Total Time |
|---------|------------|------------|
| BeautifulSoup | 26.21s | 26.79s |
| Scrapy | 3.13s | 4.47s |

**Scrapy is ~6x faster** on this task due to its asynchronous architecture.

**BeautifulSoup selected** for the full 100-post scrape: simpler syntax, easier retry logic implementation, and more readable code for a task at this scale. Scrapy's speed advantage is more meaningful at larger volumes where asynchronous scraping compounds.

### Implementation

- Paginated Reddit's search API (25 posts per page) to collect 100 posts
- Fetched up to 50 comments per post via Reddit's `.json` endpoint
- Implemented retry logic with 10-second backoff for HTTP 429 rate limit responses
- 1-second delay between requests throughout

---

## Part 2 — Text Analysis

**Input:** `webscraped.csv` (100 posts + comments)
**Output:** `textanalysis.csv` (100 rows, 7 columns)

### Algorithm 1 — Custom LSA Summarizer

A word-frequency extractive summarizer built from scratch:
- Tokenizes text into sentences
- Scores each sentence by summing the frequency of its constituent words across the full document
- Returns the top 3 highest-scoring sentences in original order

Importance score: `+1` if comment text exceeds 50 words, `-1` if below.

### Algorithm 2 — HuggingFace Transformers

Abstractive summarization using `facebook/bart-large-cnn`:
- Input truncated to 512 tokens to stay within model limits
- Output: 50–150 token abstractive summary
- Known limitation: posts with very short or poorly structured text occasionally returned summarization errors

Importance score: assigned based on word count parity (odd/even) - a deliberate design choice to produce a mixed directional distribution for comparison purposes.

### Output Structure

Each row in `textanalysis.csv` contains:

| Column | Description |
|--------|-------------|
| `title` | Reddit post title |
| `lsd_summary` | Extractive summary (custom LSA) |
| `lsd_importance_score` | +1 or -1 |
| `lsd_direction` | Positive or Negative |
| `hf_summary` | Abstractive summary (BART) |
| `hf_importance_score` | +1 or -1 |
| `hf_direction` | Positive or Negative |

---

## Repository Structure

```
Web-Scraping-and-Text-Analysis/
├── beautifulsoup_subreddit_canada_tariffs.ipynb  # BeautifulSoup benchmark (10 posts)
├── scrapy_subreddit_canada_tariffs.py            # Scrapy benchmark (10 posts)
├── part1.ipynb                                   # Full 100-post BeautifulSoup scraper
├── part2.ipynb                                   # Dual-algorithm text analysis
├── webscraped.csv                                # Scraped posts and comments
├── webscraped.txt                                # Plain text version of scraped data
├── textanalysis.csv                              # Final analysis output (100 rows)
└── README.md
```

---

## Tech Stack

- **Scraping:** BeautifulSoup, Scrapy, requests
- **NLP:** HuggingFace Transformers (`facebook/bart-large-cnn`)
- **Summarization:** Custom word-frequency LSA implementation
- **Data:** pandas, csv

---

## Key Findings

**Scraping:** Scrapy significantly outperforms BeautifulSoup on raw speed (~6x faster on the benchmark task), but BeautifulSoup's simpler control flow made retry logic and rate limit handling more straightforward to implement at the 100-post scale used here.

**Summarization:** The custom LSA summarizer consistently produced output for all 100 posts. The HuggingFace BART model produced richer, more coherent abstractive summaries but encountered failures on posts with very short or fragmented comment text due to token length constraints.

**Honest limitations:**
- Reddit's API returns a maximum of 25 posts per page: pagination was required to reach 100 posts
- Rate limiting (HTTP 429) required retry logic and delays, extending total scrape time
- HuggingFace summarization is not fully reproducible without a GPU; CPU inference is slow and may vary

---

## Author

**Juan Carlos Katigbak**
[LinkedIn](https://linkedin.com/in/juan-carlos-katigbak) | [GitHub](https://github.com/juancarloskatigbak8)
