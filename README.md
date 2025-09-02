
# Weibo Sentiment Crawler

A crawler tool for collecting Weibo data and performing sentiment analysis.

## Project Description

This project is a Weibo data crawler tool that can:
- Crawl Weibo-related information and data
- Preprocess the collected data
- Perform sentiment analysis

## File Structure

- `collect.py` - Data collection module
- `preprocess.py` - Data preprocessing module
- `chunwan.py` - Spring Festival Gala related data processing
- `getcoockie.py` - Cookie acquisition module
- `cookies.pkl` - Stored cookie file
- `weibo_data.txt` - Weibo raw data
- `weibo_results.txt` - Processing results
- `preprocessed_info` - Preprocessed information
- `春晚.txt` - Spring Festival Gala related data

## Usage

1. Ensure Python and related dependencies are installed
2. Run `python collect.py` to start data collection
3. Run `python preprocess.py` for data preprocessing
4. Run `python chunwan.py` to process Spring Festival Gala related data

## Requirements

Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Notes

- Please comply with Weibo's terms of service and robots.txt
- Control crawling frequency reasonably to avoid server pressure
- Pay attention to user privacy and data security

## License

This project is for learning and research purposes only.
