import pandas as pd
import glob
import os

files = glob.glob('data/raw/*.csv')
if not files:
    print("Không tìm thấy file CSV trong data/raw/")
dfs = {}
for f in files:
    name = os.path.basename(f).replace('.csv', '')
    try:
        dfs[name] = pd.read_csv(f, low_memory=False)
        print(f"--- Bảng {name.upper()} ({dfs[name].shape[0]} dòng, {dfs[name].shape[1]} cột) ---")
        missing = dfs[name].isnull().sum()
        if missing.sum() > 0:
            print("Missing values:")
            print(missing[missing>0].to_string())
        else:
            print("OK: Không có missing values")
    except Exception as e:
        print(f"Lỗi đọc {name}: {e}")

if 'order_items' in dfs:
    invalid_q = dfs['order_items'][dfs['order_items']['quantity'] <= 0]
    invalid_p = dfs['order_items'][dfs['order_items']['unit_price'] <= 0]
    print(f"\n[ANOMALIES order_items]: {len(invalid_q)} dòng quantity <= 0, {len(invalid_p)} dòng unit_price <= 0")
    
if 'orders' in dfs and 'customers' in dfs:
    diff = set(dfs['orders']['customer_id']) - set(dfs['customers']['customer_id'])
    print(f"[INTEGRITY]: {len(diff)} customer_id trong orders không có ở customers.")

