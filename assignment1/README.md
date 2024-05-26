# assignment1 - intro to scikit-learn




Load the wine dataset. Use the following documentation, and run preliminary data
analysis on it (features, samples, ranges, scales, variance, and any other information
that you find relevant).

• Use sklearn function test train split to split the data to test-set and train-set, for
each test-size ratio r ∈ [0.1, 0.2, 0.3, ..., 0.9], and use skleran LogisticRegression to
train a logistic regressor on the train-set and evaluate the accuracy on the test-set. Use
matplotlib.pyplot to plot the accuracy of each r (using r as x axis and accuracy as
y axis).

• The 178 samples dataset is unbalanced (each label has different number of samples).

• Implement code for label balancing to take your new dataset and generate a new dataset
with label balancing. Use the the following pseudo code:

        First, find lmin: the number corresponding to the label that appears the least in the data.
        Then, for each label in the dataset, randomly select only lmin samples and add them to the new dataset.

For the same values of r that you used in the previous part, split the balanced dataset
that you created into test-set and train-set, train a logistic regressor on the train-set,
and print the accuracy of the fitted (trained) logistic regressor on the test-set.

• Run a na¨ıve k-features selection algorithm that for each set of k features from the data
trains a classifier on the train-set, and selects the set of k features that achieved the
best accuracy on the test-set. Implement a function that gets train-set, test-set,
and k and returns the best k features from the dataset and the accuracy achieved on
the test-set. Run the function with k = 2, test-size ratio r = 0.1 and print the results
