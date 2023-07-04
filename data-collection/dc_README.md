# Data Collection

This folder contains the scripts used to scrape data from https://www.sports-reference.com/ to produce .csv files locally, the notebook used to join the .csv files produced, as well as the aggregated data after all the .csv files have been joined.

- **conf-rank-scraper.py**:  scraping the conference ranking for each team for each season
- **final-four-champ-scraper.py**:  scraping the "final four" teams and tournament champions for each season
- **sr-scraper.py**:  scraping the "Advanced School Stats" for each team for each season
- **tourn-seed-scraper1.py**:  scraping the tournament seed for each qualifying team for each season
- **joining-data-for-ml.ipynb**:  joins all .csv files produced by the above scrapers and produces d1-baskeball-data-93-23.csv
- **d1-baskeball-data-93-23.csv**:  dataset of all data scraped for each team for each season