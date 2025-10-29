# csv-cleaner

A simple Python tool for cleaning and formatting CSV data



\# CSV Cleaner



A minimal Python script to clean messy CSV files (Excel exports, Japanese encodings, etc.).



\## Features

\- Auto-detect encoding (tries `utf-8-sig`, then `cp932`)

\- Normalize column names (strip spaces, replace `/ \\` with `\_`, lowercase)

\- Trim string columns

\- Convert amount columns (¥, $, commas) to numeric

\- Convert date columns to datetime

\- Drop duplicates and save as `cleaned.csv` (UTF-8-SIG, Excel-friendly)



\## Usage

1\. Put your input file as `data.csv` in the same folder.

2\. Run:



```bash

python clean\_csv.py



