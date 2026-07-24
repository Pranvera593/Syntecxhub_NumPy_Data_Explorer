import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_theme(style="whitegrid")

# 1. Generate Dataset
np.random.seed(42)
region_a = np.append(np.random.gamma(shape=2.5, scale=120, size=300) + 100, [1250, 1380, 1450])
region_b = np.random.normal(loc=450, scale=110, size=300)

df_a = pd.DataFrame({'Sales': region_a, 'Region': 'Region A'})
df_b = pd.DataFrame({'Sales': region_b, 'Region': 'Region B'})
df = pd.concat([df_a, df_b], ignore_index=True)

# 2. Histograms & KDE (Distribution Comparison)
plt.figure(figsize=(9, 4.5))
sns.histplot(data=df, x='Sales', hue='Region', kde=True, bins=30, palette=['#1f77b4', '#ff7f0e'], alpha=0.5)
plt.title('Sales Distribution & KDE: Region A vs Region B')
plt.xlabel('Sales ($)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('distribution_histogram_kde.png', dpi=300)
plt.close()

# 3. Boxplots (Outliers & Spread)
plt.figure(figsize=(7, 4.5))
sns.boxplot(data=df, x='Region', y='Sales', hue='Region', legend=False, palette=['#1f77b4', '#ff7f0e'], width=0.4,
            flierprops=dict(marker='o', markerfacecolor='red', markersize=6))
plt.title('Boxplot & Outlier Detection')
plt.xlabel('Region')
plt.ylabel('Sales ($)')
plt.tight_layout()
plt.savefig('distribution_boxplot.png', dpi=300)
plt.close()

# 4. Export One-Paragraph Interpretation
skew_a = df[df['Region'] == 'Region A']['Sales'].skew()
skew_b = df[df['Region'] == 'Region B']['Sales'].skew()
med_a = df[df['Region'] == 'Region A']['Sales'].median()
med_b = df[df['Region'] == 'Region B']['Sales'].median()

interpretation = f"""PROJECT 2 INTERPRETATION:
Region A exhibits a right-skewed distribution (skewness = {skew_a:.2f}) with a median sales value of ${med_a:.2f} and several high-value outliers exceeding $1,200 as detected in the boxplot. In contrast, Region B shows a symmetric, bell-shaped distribution (skewness = {skew_b:.2f}) centered around a median of ${med_b:.2f} with lower overall spread and no extreme anomalies. Overall, Region B demonstrates predictable, consistent performance, whereas Region A has higher variance driven by infrequent large sales.
"""

with open("project_2_interpretation.txt", "w") as f:
    f.write(interpretation)

print("Project 2 files generated successfully.")