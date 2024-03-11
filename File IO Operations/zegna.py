import pandas as pd
import seaborn as sns
sns.set_theme(style="ticks")


# Replace 'your_local_file.csv' with the path to your local file
data = pd.read_csv("zegna_results.txt")

# Now you can use this data for visualization with Seaborn
import seaborn as sns
sns.lineplot(x='column_x', y='column_y', data=data)

# Show the results of a linear regression within each dataset
sns.lmplot(
    data=df, x="x", y="y", col="dataset", hue="dataset",
    col_wrap=2, palette="muted", ci=None,
    height=4, scatter_kws={"s": 50, "alpha": 1}
)



