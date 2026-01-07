
# Histogram Exercise – Stress Scores (Python, pandas, matplotlib)

This exercise introduces psychology students to **basic data visualization in Python** using a simple **histogram** of stress scores stored in an Excel file.  
The activity is designed for use in **Jupyter Notebooks** (e.g., GitHub Codespaces).



## 1. Files in this exercise

You should have at least the following files in the same folder:

- `Stress.xlsx`  
  A small Excel file with at least the following columns, for example:

  | participant | stress |
  |------------|--------|
  | 1          | 5      |
  | 2          | 6      |
  | 3          | 4      |
  | 4          | 8      |
  | 5          | 9      |
  | 6          | 7      |

- `exercitiu_histograma.ipynb`  
  A Jupyter notebook where you:
  - load the data from `Stress.xlsx`
  - display the first rows
  - draw a **basic histogram**
  - **customize** the histogram based on the exercise instructions.

---

## 2. Requirements

You will need the following Python packages:

- `pandas`
- `matplotlib`
- `openpyxl` (for reading Excel files)

If you are working in Codespaces or another Jupyter environment, you can install them with:

```python
!pip install pandas matplotlib openpyxl
````

Run this in a notebook cell **before** importing the libraries.

---

## 3. Step-by-step solution

### 3.1. Import the libraries

```python
import pandas as pd
import matplotlib.pyplot as plt

%matplotlib inline
```

`%matplotlib inline` ensures that all plots are shown inside the notebook.

---

### 3.2. Load the Excel file and inspect the data

```python
# Read the data from the Excel file "Stress.xlsx".
# Make sure the file is in the same folder as this notebook.
df = pd.read_excel("Stress.xlsx")

print("First rows of the file:")
df.head()
```

You should see a small table with at least the columns `participant` and `stress`.

---

### 3.3. Extract the stress scores and plot a basic histogram

```python
# Extract the column with stress scores.
stress_values = df["stress"]

# STEP 1: basic histogram (already working)
plt.hist(stress_values)
plt.show()
```

At this stage you already have a **working** histogram, but it is very minimal.

---

## 4. The assignment: customize the histogram

Your task is to **improve** the histogram so it becomes clearer and more informative.
The exercise can be guided in the notebook with comments like:

```python
# EXERCISE: customize the histogram using the instructions below.
#
# 1) Change the number of bins in the histogram.
#    - Hint: use an argument called "bins" in the function plt.hist(...)
#
# 2) Add a meaningful title to the histogram.
#    - Hint: use plt.title("your text here")
#
# 3) Add labels for the X and Y axes.
#    - Hint: plt.xlabel("..."), plt.ylabel("...")
#
# 4) (Optional) Change the color of the bars.
#    - Hint: use the argument "color" in plt.hist(...)
#
# After you make your changes, run the code again and observe the differences.
#
# Write your customized version of the histogram below this comment.
```

---

## 5. Example final solution

Below is one possible solution that satisfies all the requirements.
You do **not** have to use exactly the same text or colors, but the structure should be similar.

```python
import pandas as pd
import matplotlib.pyplot as plt

%matplotlib inline

# Read the data
df = pd.read_excel("Stress.xlsx")
stress_values = df["stress"]

print("First rows of the file:")
print(df.head())

# Customized histogram
plt.hist(
    stress_values,
    bins=5,          # 1) set the number of bins
    color="skyblue"  # 4) optional: change the bar color
)

# 2) title
plt.title("Distribution of Stress Scores")

# 3) axis labels
plt.xlabel("Stress score")
plt.ylabel("Number of participants")

plt.show()
```

You can adjust:

* `bins` (e.g., 5, 10, or other values) to change how detailed the histogram is;
* `color` (e.g., `"skyblue"`, `"lightgreen"`, `"orange"`, etc.);
* the title and labels to match your own wording.

---

## 6. Other example plots you can try

Once you are comfortable with histograms, you can experiment with other simple plots using the same or similar data.

### 6.1. Boxplot (box-and-whisker plot)

Shows the distribution of stress scores (median, quartiles, potential outliers):

```python
plt.boxplot(stress_values)
plt.title("Boxplot of Stress Scores")
plt.ylabel("Stress score")
plt.show()
```

### 6.2. Line plot (e.g., stress by participant index)

Useful if you want to see how scores change across participants:

```python
plt.plot(stress_values)
plt.title("Stress Score by Participant Index")
plt.xlabel("Participant index")
plt.ylabel("Stress score")
plt.show()
```

### 6.3. Scatter plot (if you have a second numeric variable)

If your Excel file also contains, for example, `sleep_hours`, you can show the relationship between stress and sleep:

```python
sleep_values = df["sleep_hours"]

plt.scatter(sleep_values, stress_values)
plt.title("Stress vs. Sleep Hours")
plt.xlabel("Sleep hours")
plt.ylabel("Stress score")
plt.show()
```

---

## 7. Useful links and resources

For students who want to explore more:

* Official Matplotlib tutorials (basic plotting, histograms, etc.):
  [https://matplotlib.org/stable/tutorials/index.html](https://matplotlib.org/stable/tutorials/index.html)

* Matplotlib gallery – many examples of plots with source code:
  [https://matplotlib.org/stable/gallery/index.html](https://matplotlib.org/stable/gallery/index.html)

* pandas visualization overview (plotting directly from DataFrames/Series):
  [https://pandas.pydata.org/docs/user_guide/visualization.html](https://pandas.pydata.org/docs/user_guide/visualization.html)

* A gentle introduction to histograms in data analysis (conceptual explanation):
  [https://en.wikipedia.org/wiki/Histogram](https://en.wikipedia.org/wiki/Histogram)

These resources are optional, but they can help you better understand how to create and customize plots in Python and how to interpret them in psychological research.

---
