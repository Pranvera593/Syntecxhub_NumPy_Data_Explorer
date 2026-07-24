import random
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# 1. Generate Synthetic Data using standard Python
random.seed(42)
start_date = datetime(2023, 1, 1)
categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books']

monthly_sales = {m: 0 for m in range(1, 13)}
quarterly_sales = {f'Q{q}': 0 for q in range(1, 5)}
category_sales = {cat: 0 for cat in categories}
total_sales = 0

current_date = start_date
while current_date.year == 2023:
    m = current_date.month
    q = f'Q{(m - 1) // 3 + 1}'
    
    for cat in categories:
        sale = random.randint(100, 1000) + (m * 20)
        monthly_sales[m] += sale
        quarterly_sales[q] += sale
        category_sales[cat] += sale
        total_sales += sale
        
    current_date += timedelta(days=1)

month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
m_keys = list(monthly_sales.keys())
m_values = [monthly_sales[m] for m in m_keys]

q_keys = list(quarterly_sales.keys())
q_values = [quarterly_sales[q] for q in q_keys]

# ---------------------------------------------------------
# GRAPH 1: Time Series (Monthly & Quarterly Line Charts)
# ---------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Monthly
ax1.plot(month_names, m_values, marker='o', color='#1f77b4', linewidth=2)
ax1.set_title('Total Sales Trend by Month (2023)', fontweight='bold')
ax1.set_xlabel('Month')
ax1.set_ylabel('Sales ($)')
ax1.grid(True, linestyle='--', alpha=0.6)

# Quarterly
ax2.plot(q_keys, q_values, marker='s', color='#ff7f0e', linewidth=2)
ax2.set_title('Total Sales Trend by Quarter (2023)', fontweight='bold')
ax2.set_xlabel('Quarter')
ax2.set_ylabel('Sales ($)')
ax2.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.savefig('time_series_sales.png', dpi=300)
plt.close()

# ---------------------------------------------------------
# GRAPH 2: Bar Chart - Category Comparison
# ---------------------------------------------------------
sorted_cats = sorted(category_sales.items(), key=lambda x: x[1], reverse=True)
cats, sales_vals = zip(*sorted_cats)

plt.figure(figsize=(8, 5))
bars = plt.bar(cats, sales_vals, color='#2ca02c')
plt.title('Total Sales by Product Category', fontweight='bold')
plt.xlabel('Category')
plt.ylabel('Total Sales ($)')
plt.grid(axis='y', linestyle='--', alpha=0.6)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 5000, f'${yval:,.0f}', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('category_bar_chart.png', dpi=300)
plt.close()

# ---------------------------------------------------------
# GRAPH 3: Pie Chart - Market Share
# ---------------------------------------------------------
plt.figure(figsize=(6, 6))
plt.pie(sales_vals, labels=cats, autopct='%1.1f%%', startangle=140, explode=(0.05, 0, 0, 0))
plt.title('Market Share by Product Category', fontweight='bold')
plt.tight_layout()
plt.savefig('category_pie_chart.png', dpi=300)
plt.close()

# ---------------------------------------------------------
# Export Summary Text File
# ---------------------------------------------------------
summary = f"""==================================================
PROJECT 1 SUMMARY & DISCUSSION
==================================================

1. KEY METRICS:
- Total Annual Revenue: ${total_sales:,.2f}
- Top Category: {cats[0]} (${sales_vals[0]:,.2f})
- Lowest Category: {cats[-1]} (${sales_vals[-1]:,.2f})

2. CHART SELECTION & FORMATTING DISCUSSION:
- Line Charts: Selected for time series data to show continuous trend lines across months and quarters.
- Bar Chart: Chosen to compare discrete category values directly, complete with top data labels.
- Pie Chart: Used to highlight relative market share percentages per category relative to the whole.
"""

with open("project_1_summary.txt", "w") as f:
    f.write(summary)

print("Project 1 completed successfully! PNG images and summary txt file created.")