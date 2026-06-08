import json
import os

def create_notebook(filename, cells):
    nb = {
        "cells": [],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.10"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    
    for cell_type, source in cells:
        nb["cells"].append({
            "cell_type": cell_type,
            "metadata": {},
            "source": source if isinstance(source, list) else [source],
            **({"execution_count": None, "outputs": []} if cell_type == "code" else {})
        })
        
    with open(filename, 'w') as f:
        json.dump(nb, f, indent=1)

os.makedirs('notebooks', exist_ok=True)

# 1. EDA Notebook
eda_cells = [
    ("markdown", ["# Khám phá Dữ liệu (EDA)\n", "Notebook này đọc 12 files từ `data/raw/` để phát hiện lỗi."]),
    ("code", [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "import os\n",
        "import glob\n\n",
        "raw_path = '../data/raw/'\n",
        "csv_files = glob.glob(os.path.join(raw_path, '*.csv'))\n",
        "print(f'Tìm thấy {len(csv_files)} files CSV.')"
    ]),
    ("code", [
        "dfs = {}\n",
        "for f in csv_files:\n",
        "    name = os.path.basename(f).replace('.csv', '')\n",
        "    dfs[name] = pd.read_csv(f)\n",
        "    print(f'Bảng {name.upper()}: {dfs[name].shape[0]} dòng, {dfs[name].shape[1]} cột')"
    ]),
    ("markdown", ["## 1. Phát hiện Missing Values"]),
    ("code", [
        "for name, df in dfs.items():\n",
        "    missing = df.isnull().sum()\n",
        "    missing = missing[missing > 0]\n",
        "    if not missing.empty:\n",
        "        print(f'\\n--- Bảng {name.upper()} ---')\n",
        "        print(missing)"
    ]),
    ("markdown", ["## 2. Tìm kiếm Outliers và Anomalies"]),
    ("code", [
        "if 'order_items' in dfs:\n",
        "    display(dfs['order_items'].describe())\n",
        "    invalid_qty = dfs['order_items'][dfs['order_items']['qty'] <= 0]\n",
        "    print(f'Phát hiện {len(invalid_qty)} dòng có số lượng <= 0.')\n",
        "    invalid_price = dfs['order_items'][dfs['order_items']['price'] <= 0]\n",
        "    print(f'Phát hiện {len(invalid_price)} dòng có đơn giá <= 0.')"
    ])
]
create_notebook('notebooks/eda.ipynb', eda_cells)

# 2. Preprocessing Notebook
pre_cells = [
    ("markdown", ["# Tiền xử lý dữ liệu (Preprocessing)\n", "Khắc phục lỗi tìm thấy ở bước EDA và lưu vào `data/cleaned/`."]),
    ("code", [
        "import pandas as pd\n",
        "import os\n",
        "import glob\n\n",
        "raw_path = '../data/raw/'\n",
        "clean_path = '../data/cleaned/'\n",
        "os.makedirs(clean_path, exist_ok=True)\n",
        "csv_files = glob.glob(os.path.join(raw_path, '*.csv'))\n",
        "dfs = {os.path.basename(f).replace('.csv', ''): pd.read_csv(f) for f in csv_files}"
    ]),
    ("markdown", ["## 1. Sửa lỗi Dữ liệu bất thường (Anomalies)"]),
    ("code", [
        "if 'order_items' in dfs:\n",
        "    # Xóa các dòng có giá trị âm hoặc 0\n",
        "    df_oi = dfs['order_items']\n",
        "    dfs['order_items'] = df_oi[(df_oi['qty'] > 0) & (df_oi['price'] > 0)].copy()\n",
        "    print('Đã làm sạch bảng order_items.')"
    ]),
    ("markdown", ["## 2. Đồng bộ kiểu dữ liệu (Date & String IDs)"]),
    ("code", [
        "for name, df in dfs.items():\n",
        "    for col in df.columns:\n",
        "        if 'date' in col.lower():\n",
        "            df[col] = pd.to_datetime(df[col], errors='coerce')\n",
        "        elif col.endswith('_id'):\n",
        "            df[col] = df[col].astype(str)\n",
        "    print(f'Đã đồng bộ kiểu dữ liệu cho bảng {name}.')"
    ]),
    ("markdown", ["## 3. Lưu dữ liệu đã làm sạch"]),
    ("code", [
        "for name, df in dfs.items():\n",
        "    save_path = os.path.join(clean_path, f'{name}.csv')\n",
        "    df.to_csv(save_path, index=False)\n",
        "    print(f'Đã lưu: {save_path}')"
    ])
]
create_notebook('notebooks/preprocessing.ipynb', pre_cells)

# 3. Machine Learning Notebook
ml_cells = [
    ("markdown", ["# Machine Learning: Phân cụm Khách hàng (K-Means)\n", "Sử dụng dữ liệu sạch để tạo cụm RFM."]),
    ("code", [
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "from sklearn.preprocessing import StandardScaler\n",
        "from sklearn.cluster import KMeans\n\n",
        "clean_path = '../data/cleaned/'\n",
        "df_orders = pd.read_csv(f'{clean_path}orders.csv')\n",
        "df_payments = pd.read_csv(f'{clean_path}payments.csv')\n",
        "df_customers = pd.read_csv(f'{clean_path}customers.csv')"
    ]),
    ("markdown", ["## 1. Tính toán ma trận RFM"]),
    ("code", [
        "df_orders['order_date'] = pd.to_datetime(df_orders['order_date'])\n",
        "max_date = df_orders['order_date'].max() + pd.Timedelta(days=1)\n\n",
        "rfm = df_orders.groupby('customer_id').agg({\n",
        "    'order_date': lambda x: (max_date - x.max()).days,\n",
        "    'order_id': 'count'\n",
        "}).rename(columns={'order_date': 'Recency', 'order_id': 'Frequency'})\n\n",
        "monetary = df_payments.groupby('order_id')['amount'].sum().reset_index()\n",
        "orders_monetary = df_orders.merge(monetary, on='order_id')\n",
        "monetary_agg = orders_monetary.groupby('customer_id')['amount'].sum().reset_index()\n",
        "monetary_agg.rename(columns={'amount': 'Monetary'}, inplace=True)\n\n",
        "rfm = rfm.reset_index().merge(monetary_agg, on='customer_id', how='left').fillna(0)"
    ]),
    ("markdown", ["## 2. K-Means Clustering"]),
    ("code", [
        "scaler = StandardScaler()\n",
        "rfm_scaled = scaler.fit_transform(rfm[['Recency', 'Frequency', 'Monetary']])\n\n",
        "kmeans = KMeans(n_clusters=4, random_state=42)\n",
        "rfm['Cluster'] = kmeans.fit_predict(rfm_scaled)\n\n",
        "# Ánh xạ tên cụm cho dễ hiểu (ví dụ minh họa)\n",
        "cluster_names = {0: 'At Risk', 1: 'Loyal', 2: 'New', 3: 'VIP'}\n",
        "rfm['Segment'] = rfm['Cluster'].map(cluster_names)\n\n",
        "display(rfm.head())"
    ]),
    ("markdown", ["## 3. Lưu lại kết quả để dùng trong Power BI"]),
    ("code", [
        "if 'Segment' in df_customers.columns:\n",
        "    df_customers = df_customers.drop(columns=['Segment'])\n",
        "df_customers = df_customers.merge(rfm[['customer_id', 'Segment']], on='customer_id', how='left')\n",
        "df_customers['Segment'] = df_customers['Segment'].fillna('Unknown')\n",
        "df_customers.to_csv(f'{clean_path}customers.csv', index=False)\n",
        "print('Đã gán nhãn phân khúc khách hàng và cập nhật customers.csv!')"
    ])
]
create_notebook('notebooks/machine_learning.ipynb', ml_cells)
print('Đã tạo xong 3 file notebook.')
