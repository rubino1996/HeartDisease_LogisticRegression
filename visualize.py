import matplotlib.pyplot as plt

def plot_distribution(y, title='Class Distribution', colors=None):
    """
    Plot the class distribution of the target variable.

    Args:
        y (pd.Series): Target variable.
        title (str): Title of the plot.
        colors (list): Colors for the bars.
    """
    colors = colors or ['skyblue', 'orange']
    counts = y.value_counts()
    plt.figure(figsize=(8, 6))
    bars = counts.plot(kind='bar', color=colors)
    plt.title(title, fontsize=16)
    plt.xlabel('Class (0: No CHD, 1: CHD)', fontsize=14)
    plt.ylabel('Count', fontsize=14)
    plt.xticks(rotation=0)
    for bar in bars.patches:
        plt.text(bar.get_x() + bar.get_width() / 2,
                 bar.get_height() - 20,
                 f'{int(bar.get_height())}',
                 ha='center', va='bottom', fontsize=12, color='black')
    plt.show()
