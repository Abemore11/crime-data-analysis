import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# -------------------------------
# Loads dataset into variable
# for use in all charts.
# -------------------------------
df = pd.read_csv("crime_data.csv")


# ---------------------------------------------
# 1st Chart
# Crimes by Month of the Year (Male & Female)
# ---------------------------------------------

# Ensures DATE OCC is a datetime.
df["DATE OCC"] = pd.to_datetime(df["DATE OCC"], errors="coerce")

# Extracts month name.
df["Month"] = df["DATE OCC"].dt.month_name()

# Define month order (Jan–Dec).
months_order = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Group by month and victim sex.
# DR_NO is used to count occurences.
month_mf_counts = df.groupby(["Month", "Vict Sex"])["DR_NO"].count().unstack(fill_value=0)

# Reindex so all months appear in order.
month_mf_counts = month_mf_counts.reindex(months_order, fill_value=0)

# Plot side-by-side bars (M&F)
x = np.arange(len(months_order))   # positions for bars
width = 0.4

plt.figure(figsize=(12, 6))

# Plot bars for men and women (Vict Sex "M" and "F").
plt.bar(x - width/2, month_mf_counts.get("M", 0), width=width, label="Male", color="blue")
plt.bar(x + width/2, month_mf_counts.get("F", 0), width=width, label="Female", color="#FF67F5")

# Chart details.
plt.xlabel("Month of the Year")
plt.ylabel("Number of Reported Crimes")
plt.title("Crimes by Month of the Year and Victim (Male & Female)\nU.S. Crime Data (Jan. 2020 - Sept. 2024)")
plt.xticks(x, months_order, rotation=45, ha="right")
plt.legend()
plt.tight_layout()
plt.show()


# ------------------------------------------
# 2nd Chart
# Crimes by Day of the Week (Male vs Female)
# ------------------------------------------

# Converts DATE OCC to datetime.
df["DATE OCC"] = pd.to_datetime(df["DATE OCC"], errors="coerce")

# Extracts the day of the week.
df["Day of Week"] = df["DATE OCC"].dt.day_name()

# Reorders days of the week to appear in natural order.
days_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Groups by Day of Week and Victim Sex - then DR_NO counts crimes.
day_mf_counts = df.groupby(["Day of Week", "Vict Sex"])["DR_NO"].count().unstack(fill_value=0)

# Reindex so all days appear in order - even if empty.
day_mf_counts = day_mf_counts.reindex(days_order, fill_value=0)

# Plots side-by-side bars for Male and Female.
# Positions for bars.
x = np.arange(len(days_order))
width = 0.4

plt.figure(figsize=(10, 6))

# Plots bars for men and women (Vict Sex "M" and "F").
plt.bar(x - width/2, day_mf_counts.get("M", 0), width=width, label="Male", color="blue")
plt.bar(x + width/2, day_mf_counts.get("F", 0), width=width, label="Female", color="#FF67F5")

# Chart details.
plt.title("Crimes by Day of the Week and Victim (Male & Female)\nU.S. Crime Data (Jan. 2020 - Sept. 2024)", fontsize=14)
plt.xlabel("Day of the Week", fontsize=12)
plt.ylabel("Number of Reported Crimes", fontsize=12)
plt.xticks(x, days_order, rotation=45, ha="right")
plt.legend()
plt.tight_layout()
plt.show()


# ---------------------------------------------
# 3rd Chart
# Crimes per hour (Male vs Female)
# ---------------------------------------------

# Filters out non-numerical data from TIME OCCURENCE,
# replaces it with NaN.
df["TIME OCC"] = pd.to_numeric(df["TIME OCC"], errors="coerce")

# Convert TIME OCC to hour of day in 0-23 format,
# Will help group/plot crimes by hour.
df["Hour"] = df["TIME OCC"] // 100

# DR_NO column is used for counting crimes each hour.
# Sorts hours in ascending order.
hour_mf_counts = df.groupby(["Hour", "Vict Sex"])["DR_NO"].count().unstack(fill_value=0)

# Makes sure all hours 0-23 exist - even if some have 0 counts.
hour_mf_counts = hour_mf_counts.reindex(range(0, 24), fill_value=0)

hours = np.arange(24)  # 0-23 hours
width = 0.4            # width of each bar

plt.figure(figsize=(12, 6))

# Plot bars for men and women (Vict Sex "M" and "F")
plt.bar(hours - width/2, hour_mf_counts.get("M", 0), width=width, label="Male", color="blue")
plt.bar(hours + width/2, hour_mf_counts.get("F", 0), width=width, label="Female", color="#FF67F5")

# Chart details.
plt.xlabel("Hour of Day (0-23)")
plt.ylabel("Number of Reported Crimes")
plt.title("Crimes by Hour of Day and Victim (Male & Female)\nU.S. Crime Data from Jan. 2020 to Sept. 2024")
plt.xticks(hours)
plt.legend()
plt.show()


# ---------------------------------------
# 4th Chart
# Crime Description Counts
# ---------------------------------------

# Drops rows where Crime Code Description is empty/NaN.
# Converts every value in series to str type.
crime_desc_series = df["Crm Cd Desc"].dropna().astype(str)

# Creates a series of the 10 most common crimes and their counts.
top_crimes = crime_desc_series.value_counts().head(10)

# Creates the bar chart.
plt.bar(top_crimes.index, top_crimes.values, color="#FF9933", edgecolor="black")

# Chart description.
plt.xlabel("Crime Description")
plt.ylabel("Number of Reported Crimes")
plt.title("Top 10 Most Frequent Crimes in U.S.\n(Jan. 2020 to Sept. 2024)")
plt.xticks(rotation=45, ha="right", fontsize=8)
plt.show()


# -----------------------------------
# 5th Chart
# Crime Premises Counts
# -----------------------------------

# Drops rows where Premis Desc is empty/NaN.
# Converts every value in series to str type.
crime_premis_series = df["Premis Desc"].dropna().astype(str)

# Creates a series of the 10 most common crime premises and their counts.
top_crimes_premise = crime_premis_series.value_counts().head(10)

# Creates the bar chart.
plt.bar(top_crimes_premise.index, top_crimes_premise.values, color="#33FF55", edgecolor="black")

# Chart description
plt.xlabel("Premise Description")
plt.ylabel("Number of Reported Crimes")
plt.title("Top 10 Most Frequent Crime Locations in U.S.\n(Jan. 2020 to Sept. 2024)")
plt.xticks(rotation=45, ha="right", fontsize=8)
plt.show()


# ---------------------------------------------
# Summary Report: Most & Least Dangerous Times
# ---------------------------------------------

print("\n===== CRIME DATA SUMMARY REPORT =====\n")

# --- Month of Year ---
# Combines male and female counts into one total per time period.
month_totals = month_mf_counts.sum(axis=1)

# .idxmax() / .idxmin() gives index (“Friday,” “July,” or "1pm") for the highest and lowest totals.
most_dangerous_month = month_totals.idxmax()
least_dangerous_month = month_totals.idxmin()

# Console Output
print(f"Most Dangerous Month: {most_dangerous_month} ({month_totals.max():,} crimes)")
print(f"Least Dangerous Month: {least_dangerous_month} ({month_totals.min():,} crimes)")


# --- Day of Week ---
day_totals = day_mf_counts.sum(axis=1)
most_dangerous_day = day_totals.idxmax()
least_dangerous_day = day_totals.idxmin()
print(f"\nMost Dangerous Day: {most_dangerous_day} ({day_totals.max():,} crimes)")
print(f"Least Dangerous Day: {least_dangerous_day} ({day_totals.min():,} crimes)")

# --- Hour of Day ---
hour_totals = hour_mf_counts.sum(axis=1)
most_dangerous_hour = int(hour_totals.idxmax())
least_dangerous_hour = int(hour_totals.idxmin())
print(f"\nMost Dangerous Hour: {most_dangerous_hour:02d}:00 ({hour_totals.max():,} crimes)")
print(f"Least Dangerous Hour: {least_dangerous_hour:02d}:00 ({hour_totals.min():,} crimes)")

print("\n=====================================\n")