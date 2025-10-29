import pandas as pd

# 1) Try reading CSV (utf-8-sig first, fallback to cp932)
try:
    df = pd.read_csv('data.csv', encoding='utf-8-sig')
except UnicodeDecodeError:
    df = pd.read_csv('data.csv', encoding='cp932')

# 2) Normalize column names
df.columns = (df.columns
    .str.strip()
    .str.replace(r'[ \t\u3000/\\]+', '_', regex=True)
    .str.lower())

# 3) Strip leading/trailing spaces in string columns
for c in df.select_dtypes(include=['object','string']).columns:
    df[c] = df[c].astype('string').str.strip()

# 4) Convert amount columns to numeric (adjust list as needed)
for c in ['amount', '金額', '税額']:
    if c in df.columns:
        df[c] = (df[c].astype('string')
                   .str.replace('[¥$,，,\\s]', '', regex=True)
                   .str.replace('−','-'))
        df[c] = pd.to_numeric(df[c], errors='coerce')

# 5) Convert date columns to datetime (adjust list as needed)
for c in ['date', '発生日', '請求日']:
    if c in df.columns:
        df[c] = pd.to_datetime(df[c], errors='coerce')

# 6) Drop duplicates and save as UTF-8-SIG (Excel-friendly)
df = df.drop_duplicates()
df.to_csv('cleaned.csv', index=False, encoding='utf-8-sig')
print("OK -> cleaned.csv")
