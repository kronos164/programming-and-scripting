import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Check if the dataset exists in the specified path
dataset = os.path.abspath(os.path.join(os.path.dirname(__file__), "../iris-dataset/iris.data"))
images = os.path.abspath(os.path.join(os.path.dirname(__file__), "../images/"))
if not os.path.exists(dataset):
    dataset = os.path.abspath(os.path.join(os.path.dirname(__file__), "../pands-project/iris-dataset/iris.data"))
    images = os.path.abspath(os.path.join(os.path.dirname(__file__), "../pands-project/images/"))
    if not os.path.exists(dataset):
        print("Dataset not found. Please check the path.")
        exit(1)
    else:
        print("Dataset found. Proceeding with the analysis.")
        # read the dataset into a pandas dataframe
        df = pd.read_csv(dataset, header=None, names=["sepal_length", "sepal_width", "petal_length", "petal_width", "species"])
else:   
    print("Dataset found. Proceeding with the analysis.")
    # read the dataset into a pandas dataframe
    df = pd.read_csv(dataset, header=None, names=["sepal_length", "sepal_width", "petal_length", "petal_width", "species"])
    
# Group the data by species and calculate the mean of each feature
df_grouped = df.groupby("species").mean()
print(df_grouped)

# Sumary statistics all 3 species
df_summary = df.describe()
print("Summary Statistics:")
print(df_summary)

# Sumary of iris-setosa
df_setosa = df[df["species"] == "Iris-setosa"]
df_setosa_summary = df_setosa.describe()
print("\n\nSummary Statistics for Iris-setosa:")
print(df_setosa_summary)

# Sumary of iris-versicolor
df_versicolor = df[df["species"] == "Iris-versicolor"]
df_versicolor_summary = df_versicolor.describe()
print("\n\nSummary Statistics for Iris-versicolor:")
print(df_versicolor_summary)

# Sumary of iris-virginica
df_virginica = df[df["species"] == "Iris-virginica"]
df_virginica_summary = df_virginica.describe()
print("\n\nSummary Statistics for Iris-virginica:")
print(df_virginica_summary)

# Convert species to numeric codes for correlation analysis
df["species"] = df["species"].astype("category").cat.codes

# Calculate correlation matrix
correlation_matrix = df.corr()
print("Correlation Matrix:")
print(correlation_matrix)

#Export the summaries to a text file
with open("iris_summary.txt", "w") as f:
    f.write("Grouped Data:\n")
    f.write(str(df_grouped))
    f.write("\n\nSummary Statistics of all 3 species:\n")
    f.write(str(df_summary))
    f.write("\n\nSummary Statistics of Iris-setosa:\n")
    f.write(str(df_setosa_summary))
    f.write("\n\nSummary Statistics of Iris-versicolor:\n")
    f.write(str(df_versicolor_summary))
    f.write("\n\nSummary Statistics of Iris-virginica:\n")
    f.write(str(df_virginica_summary))
    f.write("\n\nCorrelation Matrix:\n")
    f.write(str(correlation_matrix))
    
# Map numeric species codes back to their original names for plotting
species_mapping = {0: "Iris-setosa", 1: "Iris-versicolor", 2: "Iris-virginica"}
df["species_name"] = df["species"].map(species_mapping)

# Plot histograms of each feature per species
plt.figure(figsize=(10, 10))
plt.suptitle("Iris Dataset", fontsize=20)

colors = {"Iris-setosa": "darkblue", "Iris-versicolor": "pink", "Iris-virginica": "yellow"}

plt.subplot(2, 2, 1)
plt.hist(df[df["species_name"] == "Iris-setosa"]["sepal_length"], alpha=0.5, label="Iris-setosa", color=colors["Iris-setosa"])
plt.hist(df[df["species_name"] == "Iris-versicolor"]["sepal_length"], alpha=0.5, label="Iris-versicolor", color=colors["Iris-versicolor"])
plt.hist(df[df["species_name"] == "Iris-virginica"]["sepal_length"], alpha=0.5, label="Iris-virginica", color=colors["Iris-virginica"])
plt.title("Sepal Length")
plt.xlabel("Length (cm)")
plt.ylabel("Frequency")
plt.ylim(0, 20)
plt.xticks(np.arange(df["sepal_length"].min(), df["sepal_length"].max() + 0.2, 0.2), rotation=45)
plt.legend()

plt.subplot(2, 2, 2)
plt.hist(df[df["species_name"] == "Iris-setosa"]["sepal_width"], alpha=0.5, label="Iris-setosa", color=colors["Iris-setosa"])
plt.hist(df[df["species_name"] == "Iris-versicolor"]["sepal_width"], alpha=0.5, label="Iris-versicolor", color=colors["Iris-versicolor"])
plt.hist(df[df["species_name"] == "Iris-virginica"]["sepal_width"], alpha=0.5, label="Iris-virginica", color=colors["Iris-virginica"])
plt.title("Sepal Width")
plt.xlabel("Width (cm)")
plt.ylabel("Frequency")
plt.ylim(0, 20)
plt.xticks(np.arange(df["sepal_width"].min(), df["sepal_width"].max() + 0.2, 0.1), rotation=45)
plt.legend()

plt.subplot(2, 2, 3)
plt.hist(df[df["species_name"] == "Iris-setosa"]["petal_length"], alpha=0.5, label="Iris-setosa", color=colors["Iris-setosa"])
plt.hist(df[df["species_name"] == "Iris-versicolor"]["petal_length"], alpha=0.5, label="Iris-versicolor", color=colors["Iris-versicolor"])
plt.hist(df[df["species_name"] == "Iris-virginica"]["petal_length"], alpha=0.5, label="Iris-virginica", color=colors["Iris-virginica"])
plt.title("Petal Length")
plt.xlabel("Length (cm)")
plt.ylabel("Frequency")
plt.ylim(0, 30)
plt.xticks(np.arange(df["petal_length"].min(), df["petal_length"].max() + 0.2, 0.3), rotation=45)
plt.legend()

plt.subplot(2, 2, 4)
plt.hist(df[df["species_name"] == "Iris-setosa"]["petal_width"], alpha=0.5, label="Iris-setosa", color=colors["Iris-setosa"])
plt.hist(df[df["species_name"] == "Iris-versicolor"]["petal_width"], alpha=0.5, label="Iris-versicolor", color=colors["Iris-versicolor"])
plt.hist(df[df["species_name"] == "Iris-virginica"]["petal_width"], alpha=0.5, label="Iris-virginica", color=colors["Iris-virginica"])
plt.title("Petal Width")
plt.xlabel("Width (cm)")
plt.ylabel("Frequency")
plt.ylim(0, 30)
plt.xticks(np.arange(0, 3, 0.1), rotation=45)
plt.legend()

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(os.path.join(images, "iris_histograms.png"))
plt.show()

# Scatter plot distribution of each feature for each species
plt.figure(figsize=(10, 10))
plt.suptitle("Iris Dataset Feature Distributions", fontsize=20)

plt.subplot(3, 2, 1)
plt.scatter(df["sepal_length"], df["sepal_width"], c=df["species"].astype("category").cat.codes, cmap="plasma", alpha=0.5)
plt.title("Sepal Length vs Width")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")

plt.subplot(3, 2, 2)
plt.scatter(df["petal_length"], df["petal_width"], c=df["species"].astype("category").cat.codes, cmap="plasma", alpha=0.5)
plt.title("Petal Length vs Width")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")

plt.subplot(3, 2, 3)
plt.scatter(df["sepal_length"], df["petal_length"], c=df["species"].astype("category").cat.codes, cmap="plasma", alpha=0.5)
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")

plt.subplot(3, 2, 4)
plt.scatter(df["sepal_width"], df["petal_width"], c=df["species"].astype("category").cat.codes, cmap="plasma", alpha=0.5)
plt.title("Sepal Width vs Petal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Petal Width (cm)")

plt.subplot(3, 2, 5)
plt.scatter(df["sepal_length"], df["petal_width"], c=df["species"].astype("category").cat.codes, cmap="plasma", alpha=0.5)
plt.title("Sepal Length vs Petal Width")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Width (cm)")

plt.subplot(3, 2, 6)
plt.scatter(df["sepal_width"], df["petal_length"], c=df["species"].astype("category").cat.codes, cmap="plasma", alpha=0.5)
plt.title("Sepal Width vs Petal Length")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Petal Length (cm)")

plt.tight_layout()
plt.savefig(os.path.join(images, "iris_scatter_plots.png"))
plt.show()

# Plot correlation matrix with values displayed
plt.figure(figsize=(10, 8))
plt.title("Correlation Matrix")
plt.imshow(correlation_matrix, cmap="coolwarm", interpolation="nearest")
plt.colorbar()

# Add text annotations for each square (this feature was generated by an AI model Copilot, the prompt was "add the value in the centre of each square representing its correlation")
for i in range(len(correlation_matrix)):
    for j in range(len(correlation_matrix)):
        plt.text(j, i, f"{correlation_matrix.iloc[i, j]:.2f}", ha="center", va="center", color="black")

plt.xticks(range(len(df.columns)), df.columns, rotation=45)
plt.yticks(range(len(df.columns)), df.columns)
plt.tight_layout()
plt.savefig(os.path.join(images, "iris_correlation_matrix.png"))
plt.show()

# References:
# https://www.kaggle.com/datasets/uciml/iris
# https://matplotlib.org/stable/gallery/statistics/histogram_features.html
# https://matplotlib.org/stable/gallery/images_contours_and_fields/interpolation_methods.html
# https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html
# https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html
# https://pandas.pydata.org/pandas-docs/stable/user_guide/categorical.html
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter.html
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.astype.html
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Categorical.cat.codes.html
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.corr.html