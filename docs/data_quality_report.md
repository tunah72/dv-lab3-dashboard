# Data Quality Report

- Data directory: `D:\School\DV\dv-lab3-dashboard\data\cleaned`
- Overall status: **PASS**

## Tables

| Table | Rows | Columns | Primary key | Duplicate PK rows | Blank PK rows | Null columns | Date errors | Numeric errors |
|---|---:|---:|---|---:|---:|---|---|---|
| categories | 30 | 2 | category_id | 0 | 0 | - | - | - |
| customers | 50000 | 4 | customer_id | 0 | 0 | - | signup_date: 0 | - |
| employees | 1000 | 3 | employee_id | 0 | 0 | - | - | salary >= 0: 0 |
| orders | 300000 | 5 | order_id | 0 | 0 | - | order_date: 0 | - |
| order_items | 600000 | 5 | order_item_id | 0 | 0 | - | - | qty > 0: 0, price > 0: 0 |
| payments | 300000 | 3 | payment_id | 0 | 0 | - | - | amount >= 0: 0 |
| products | 10000 | 4 | product_id | 0 | 0 | - | - | price > 0: 0 |
| promotions | 50 | 2 | promotion_id | 0 | 0 | - | - | discount >= 0: 0 |
| returns | 30000 | 3 | return_id | 0 | 0 | - | - | refund >= 0: 0 |
| shipments | 300000 | 3 | shipment_id | 0 | 0 | - | - | - |
| stores | 100 | 2 | store_id | 0 | 0 | - | - | - |
| suppliers | 200 | 2 | supplier_id | 0 | 0 | - | - | - |

## Relationships

| Child | Parent | Missing parent keys | Sample missing keys |
|---|---|---:|---|
| orders.customer_id | customers.customer_id | 0 | - |
| orders.store_id | stores.store_id | 0 | - |
| orders.promotion_id | promotions.promotion_id | 0 | - |
| order_items.order_id | orders.order_id | 0 | - |
| order_items.product_id | products.product_id | 0 | - |
| products.category_id | categories.category_id | 0 | - |
| products.supplier_id | suppliers.supplier_id | 0 | - |
| payments.order_id | orders.order_id | 0 | - |
| returns.order_item_id | order_items.order_item_id | 0 | - |
| shipments.order_id | orders.order_id | 0 | - |
| employees.store_id | stores.store_id | 0 | - |
