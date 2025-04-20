# Iris Dataset Analysis

The Iris dataset is a well-known dataset in the field of machine learning and statistics. It was introduced by the British statistician and biologist Ronald A. Fisher in 1936 as part of his work on linear discriminant analysis. The dataset contains 150 entries of iris flowers, divided into three species: Iris-setosa, Iris-versicolor, and Iris-virginica. Each species has 50 entries.

The dataset includes four features for each entry:
- Sepal length (in cm)
- Sepal width (in cm)
- Petal length (in cm)
- Petal width (in cm)

These features are used to classify the samples into their respective species. This dataset is a very popular data dataset for students in machine learning and data analysis due to its simplicity and being well esctrutered.

Each feature has different means values and distribution, mostly based on each species. Which makes easier to visualize this differences in plots.

This follow image helps to understand each feature and the three flower species.

![Iris Species](images/iris_species.svg)

### How to use this script

   - Open the python file called `analysis.py` and execute the code. The script will generate a text file with the summary of the dataset, as well as plots.
   - In the directory of the python file, it will be exported the text file `iris_summary.txt`. Open to see the dataset summary.
   - In the same directory, it will be exported the generated plots in png files. Open `iris_histograms.png` to see the histograms plots; `iris_scatter_plots.png` to see the scatter plots; and `iris_correlation_matrix.png` to see all the correlations between the features.
   