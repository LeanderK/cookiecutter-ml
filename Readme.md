# Cookiecutter Machine Learning
a simple project template for model-centric machine learning

## How To: Set Up Cookiecutter Machine Learning
It's easy!
```python
pip install cookiecutter
cookiecutter https://github.com/LeanderK/cookiecutter-ml
```

## Why Cookiecutter Machine Learning?

Machine learning is a largely experimental science. This means that over the course of a project one has to iterate a lot over different models, hyper-parameters, preprocessing options etc. Not loosing your sanity and keeping the project organized is suprisingly hard. But, as it's usually the case in life, one size doesn't fit all.

## Model-Centric Machine Learning

This template is optimized for a model-centric machine learning project. In contrast to a data-centric machine-learning project ([cookiecutter data-science](https://github.com/drivendata/cookiecutter-data-science) is a fantastic template), the main body of work is spent working with the model and not understanding the data. This is, among other things, often the case with deep learning projects.

## Recommendations
But still, it is not possible to come up with a perfect structure for every project. We recommend to take great care with how to organize the `experiments/` folder. For example, if your project involves evaluating your model on a lot of different datasets, grouping your experiments by dataset is probably a good approach. If your project involves only a single dataset, then grouping by weeks/months could be a good approach. The nature of your project should dictate the approach taken.

# Project Structure

    ├── data               <- Folder for all the datasets used in the machine-learning project
    |
    ├── experiments        <- This folder is used for all the experiments and their results.
    |                         This is not the place for your preprocessing-code or layer-definitions.
    |                         It is recommended to think about a substructure depending on the nature
    |                         of the project. For example, one could groupy the experiments by
    |                         week/month/dataset.
    |                         Additionaly, keeping all the experiment-definitions immutable is
    |                         strongly encouraged. One often wants revisit experiments months later
    |                         and rebuilding them from scratch is not always possible.
    |                         The option to initialize the experiments folder with a date or dataset
    |                         based structure is provided by the cookiecutter.
    |
    ├── notebooks          <- The place for all your jupyter-notebooks. If the project involves a
    |                         lot of notebooks it is recommended to adopt a similiar structure to
    |                         the one used in `/experiments`.
    |
    ├── reports            <- Smaller reports and the code to generate the relevant figures belongs
    |                         here.
    |
    ├── src                <- Source code for the project.
    │   ├── data           <- Downloading, preprocessing and loading the datasets.
    │   ├── models         <- Here belongs all the code that is used to define your models.
    │   ├── training       <- The training and evaluation code.
