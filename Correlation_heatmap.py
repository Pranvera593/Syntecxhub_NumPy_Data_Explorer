import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_theme(style="white")

# 1. Generate Synthetic Dataset
np.random.seed(42)
n = 300

marketing_spend = np.random.uniform(1000, 10000, n)
sales = marketing_spend * 2.5 + np.random.normal(0, 1500, n)
customer_visits = sales * 0.05 + np.random.normal(50, 20, n)
discount_rate = np.random.uniform(0.05, 0.35, n)
profit = sales * 0.4 - (discount_rate * 2000) + np.random.normal(0, 500, n)

df = pd.DataFrame({
    'Marketing_Spend': marketing_spend,
    'Sales': sales,
    'Customer_Visits': customer_visits,
    'Discount_Rate': discount_rate,
    'Profit': profit
})

# 2. Pearson Correlation & Masked Heatmap
corr_matrix = df.corr(method='pearson')
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, mask=mask, annot=True, fmt=".2f", cmap='coolwarm', 
            vmax=1.0, vmin=-1.0, square=True, linewidths=.5)
plt.title('Correlation Heatmap (Lower Triangle)')
plt.tight_layout()
plt.savefig('correlation_heatmap.png', dpi=300)
plt.close()

# 3. Pairplot / Scatter Matrix
g = sns.pairplot(df, corner=True, diag_kind='kde', plot_kws={'alpha': 0.6, 's': 25})
g.fig.suptitle('Pairwise Relationships Matrix', y=1.02)
plt.savefig('pairwise_relationships.png', dpi=300, bbox_inches='tight')
plt.close()

# 4. Export Summary Report
summary = f"""PROJECT 3: CORRELATION HEATMAP & PAIRWISE RELATIONSHIPS
============================================================

1. PEARSON CORRELATION MATRIX:
{corr_matrix.round(2).to_string()}

2. KEY RELATIONSHIPS SUMMARY:
- Strongest Positive Relationship: Sales & Customer_Visits (r = 1.00), Marketing_Spend & Sales (r = 0.98), Sales & Profit (r = 0.98).
- Strongest Negative Relationship: Discount_Rate & Profit (r = -0.09).

3. INTERPRETATION:
The correlation matrix reveals a strong positive linear dependency between Marketing Spend and Sales (r = 0.98), indicating that increased ad spend directly expands revenue. Sales and Profitability also move together very closely (r = 0.98). Conversely, Discount Rate shows a slight negative correlation with Profit (r = -0.09), highlighting that higher discounting slightly dampens profit margins.
"""

with open("project_3_summary.txt", "w") as f:
    f.write(summary)

print("Project 3 files generated successfully.")