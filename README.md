# Overview

As a software engineer and data enthusiast, I wanted to deepen my familiarity with the **Python data analysis** ecosystem, including **Pandas, NumPy,** and **Matpoltlib.** I used this project to explore **data cleaning, transformation,** and **visualization** techniques and to strengthen my understanding of how to extract meaningful insights from large-scale public data.

My purpose for developing this analytical program was to gain hands-on experience with real-world **data pipelines** and to practice **storytelling** through **visualization**. By combining structured programming practices with analytical reasoning, I learned how to transform of raw, messy datasets into clear and actionable insights from resulting **descriptive statistics**.

# Data Analysis Results

The dataset analyzed contains **reported crimes in the United States** from **January 2020 to September 2024**,
including details such as **date and time of occurance, victim sex, crime type, and crime location**, among others. This dataset contains **982,639** reported crimes.

- [Video Walkthrough](https://youtu.be/1f1y0ctI9T8)

### What are the most and least dangerous months, days, and hours based on reported crimes in the U.S.?

- **Most Dangerous Month:** January (80,508 crimes)
- **Least Dangerous Month:** November (61,812 crimes)
- **Most Dangerous Day of the Week:** Friday (128,308 crimes)
- **Least Dangerous Day of the Week:** Tuesday (116,039 crimes)
- **Most Dangerous Hour of the Day:** 12:00 (58,751 crimes)
- **Least Dangerous Hour of the Day:** 05:00 (14,386 crimes)

### How do these crime patterns differ between male and female victims? (demographic differences across time)

- Male victims experience consistently higher and more variable crime rates.
- Female victims show slightly lower, steadier patterns, with small rises in **late-night and noon incidents**.

### Which types of crimes occur most frequently and where?

- **Vehicle-related thefts, simple assaults, and burglaries** were the most frequently reported crimes in the U.S.
- **Property and identity-related offenses** dominate overall crime totals.
- Most incidents occurred in **public and residential areas**, particularly **streets, single-family homes, and multi-unit dwellings** (top 3 designations).

---

# Development Environment

- **Programming Language:** Python 3.13
- **Libraries Used:**
- `Pandas` - data cleaning, manipulation, and aggregation
- `numpy` - numerical operations and array handling
- `matplotlib` - creating visualizations (charts)
- **Development Tools:** VSCode

# Useful Websites

- [Kaggle: U.S. Crime Dataset](https://www.kaggle.com/datasets/arpitsinghaiml/u-s-crime-dataset) — source dataset
- [Pandas Documentation](https://pandas.pydata.org/docs/) — reference for data manipulation
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html) — reference for plotting
- [NumPy Documentation](https://numpy.org/doc/) — reference for numerical operations

# Future Work

- Incorporate **statistical significance testing** for time-based differences (e.g., Chi-square tests for months, days, and hours).
- Develop a **dashboard-style interface** for interactive exploration of trends.
- Explore **crime rates per capita** to normalize for population differences.
