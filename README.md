# Introduction
I'm implementing some Machine Learning Algorithms in form of little tools in this repository, some have graphics as well.
Graphical tools are mostly implemented using `Javascript`, `CSS`, `HTML`.
Non-Graphical tools are mostly implemented in `C++` and `Python`.

# Linear Regression
We are trying to fit a linear function (called hypothesis in Machine Learning) which describes our datas the best. This function is defined as:
$$h(X) = \sum^{i=n}_{i=0}\theta_i X_i = \Theta^T X$$
keeping in mind that:
$$X_0 = 1$$
So our task is to find thetas.
## Linear Regression Visualizer
A tool you can see the Gradient Descent Algorithm with your own eyes.

![Linear Regression Visualizer](https://github.com/Danial-Hosseintabar/ML-Algorithms/blob/main/Documents/images/LinearRegressionVisualizer.png)
## General Linear Regression
A C++ program which will find the closest linear function which has the condition : $$f : R^n \rightarrow R \\ \\ \\ \\ \\ ( n \in \mathbb{Z}^+ )$$ for any any and any number of datas. It uses Gradient descent algorithm.

![General Linear Regression](https://github.com/Danial-Hosseintabar/ML-Algorithms/blob/main/Documents/images/GeneralLinearRegression.JPG)

# Logistic Regression
This time we are trying to solve a classification problem. A very nice example for this which was mentioned in CS229 Stanford class by Andrew NG is the breast cancer tumor problem. There are several features for a tumor and you have a set of datas with binary out put (the tumor is either malignant or it is not).
Based on this datas we will be able to predict the chance that a tumor is malignant.
This time we are trying to fit a sigmoid funtion that describes the datas the best. (In Mathematical terms: has the maximum likelihood)
$$h(X) = \frac{1}{1-e^{-\Theta^T X}}$$

## Gradient ascsent
The logic is excatly like gradient descent, but this time we are trying to reach the maximum. Overally simple, but slow algorithm.

## Newton's method
This method converges really fast, but each iteration is expensive because it includes inversing the hessian matrix and multiplying matrices.

