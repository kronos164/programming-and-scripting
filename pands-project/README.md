# Iris Dataset Analysis

## About This Project

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

## How to use this script

   - Open the python file called `analysis.py` and execute the code. The script will generate a text file with the summary of the dataset, as well as plots in the folder `images/`.
   - In the directory of the python file, it will be exported the text file `iris_summary.txt`. Open to see the dataset summary.
   - In the same directory, in the folder `images/`, it will be exported the generated plots in png files. Open `iris_histograms.png` to see the histograms plots; `iris_scatter_plots.png` to see the scatter plots; and `iris_correlation_matrix.png` to see all the correlations between the features.

## Technical Requirements

```
python = 3.12.7
pandas = 1.5.0
matplotlib = 3.6.0
numpy = 1.23.0
```

## Repository Structure

```
programming-and-scripting/pands-project/
|
├── images/                                           # Folder with images
├── iris-dataset/                                     # Folder with Iris dataset
├── analysis.py/                                      # Python script to analyse iris dataset
├── iris_summary.txt                                  # Text file with summary of Iris dataset
|
```

## Author

***

#### About me:

My name is Cainã Oliveira. I hold a Master's degree in Psychology from the [University of Porto](https://www.up.pt/portal/en/) and am currently advancing my education in data analytics through a postgraduate course at the [Atlantic Technological University: ATU](https://www.atu.ie/). Simultaneously, I am pursuing a Master's in Artificial Intelligence at the [International University of Applied Sciences](https://www.iu.org/). My academic journey reflects a strong commitment to integrating the insights of human behavior with the cutting-edge technologies of AI and data science, aiming to harness these disciplines in innovative and impactful ways.

![IT](https://erp.today/wp-content/uploads/2022/12/Artificial_Intelligence-2048x1024.jpg)