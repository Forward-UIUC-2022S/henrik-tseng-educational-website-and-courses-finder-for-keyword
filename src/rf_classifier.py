from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.metrics import precision_score, recall_score, roc_auc_score, roc_curve
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix
import itertools

random_seed = 5

data_labeling_path = "/Users/enteilegend/forward_lab/educational-website-and-courses-finder-for-keyword/henrik-tseng-educational-website-and-courses-finder-for-keyword/dataset/data_labeling.xlsx"
modified_data_labeling_path = "/Users/enteilegend/forward_lab/educational-website-and-courses-finder-for-keyword/henrik-tseng-educational-website-and-courses-finder-for-keyword/dataset/data_labeling_modified.xlsx"
new_training_set_path = "/Users/enteilegend/forward_lab/educational-website-and-courses-finder-for-keyword/henrik-tseng-educational-website-and-courses-finder-for-keyword/dataset/data_labeling_new_labels.xlsx"
"""
User service section
"""

'''
Function: predict_for_user

Introduction:
    Input the lists of features collected from the websites, this function apply them to a trained random forest
    classifier and generate prediction for them

Parameters:
    features(list): all features collected from corresponding websites in 'final_results_list' for later classifier prediction

Outputs:
    predictions(list): predicated labels from rf classifier to corresponding websites in input 'features'
'''
def predict_for_user(features):
    predictions = []

    # Load dataset
    # df = pd.read_excel(r'E:\Learning\undergraduate\2021 Fall\CS397\data_labeling.xlsx', sheet_name='dataset')
    # df = pd.read_excel(modified_data_labeling_path, sheet_name='Sheet1')
    df = pd.read_excel(new_training_set_path, sheet_name='Sheet1')
    # 3 is org factor from parsing website url, and continues on until the end label at index 27
    factor_indexes = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
    x = df.iloc[:, factor_indexes].values
    labels = df.iloc[:, 28].values
    
    #print("x")
    #print(x)
    #print("labels")
    #print(labels)

    model = RandomForestClassifier(n_estimators=100,
                                   random_state=random_seed,
                                   max_features='sqrt')

    # Fit on training data
    model.fit(x, labels)

    new_feature = []
    # Evaluation dataset predictions (to evaluate the trained model)
    
    
    #predictions.append(model.predict(new_feature))
    #print("Full features")
    #print(features)
    #print("length")
    #print(len(features))
    for i in range(len(features)):
        print(features[i])
        # skip the first string that has the URL
        feature = features[i]
        new_feature.append(feature[1:])

    # Evaluation dataset predictions (to evaluate the trained model)
    #print("new features")
    #print(new_feature)
    predictions.append(model.predict(new_feature))
    #print("prediction")
    #print(predictions)
    return predictions

"""
Train-test-evaluate section
"""

# Load modified path dataset. NOTE: Currently only checks accuracy on a 80% training 20% testing split.
# Needs to be improved to account for additional statistics.
def training():
    # old dataframes not used anymore
    # df = pd.read_excel(r'E:\Learning\undergraduate\2021 Fall\CS397\data_labeling.xlsx', sheet_name='dataset')
    # df = pd.read_excel(data_labeling_path, sheet_name='dataset')
    df = pd.read_excel(modified_data_labeling_path, sheet_name='Sheet1')
    x = df.iloc[:, [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]].values
    labels = df.iloc[:, 28].values

    train, test, train_labels, test_labels = train_test_split(x, labels, stratify = labels, test_size=0.3, random_state = random_seed)

    print('format is:',test)

    model = RandomForestClassifier(n_estimators = 100,
                               random_state = random_seed,
                               max_features = 'sqrt')

    # Fit on training data
    model.fit(train, train_labels)

    # Training predictions (to demonstrate overfitting)
    train_rf_predictions = model.predict(train)
    train_rf_probs = model.predict_proba(train)[:, 1]

    # Testing predictions (to determine performance)
    rf_predictions = model.predict(test)
    rf_probs = model.predict_proba(test)[:, 1]
    
    print("-----------------Training Part----------------")
    print('Test Accuracy:',accuracy_score(test_labels, rf_predictions))

    # # Load evaluation dataset
    # df_eval = pd.read_excel(r'E:\Learning\undergraduate\2021 Fall\CS397\data_labeling.xlsx', sheet_name='evaluateset')
    # eval_x = df_eval.iloc[:, [0, 7]].values
    # eval_labels = df_eval.iloc[:, 8].values

    # # Evaluation dataset predictions (to evaluate the trained model)
    # rf_eval_predictions = model.predict(eval_x)
    # rf_eval_probs = model.predict_proba(eval_x)[:, 1]

    # # Plot formatting
    # plt.style.use('fivethirtyeight')
    # plt.rcParams['font.size'] = 18

# NOTE: not currently working with current model, could maybe change to apply to current model
def evaluate_model(predictions, train_predictions):
    """Compare machine learning model to baseline performance.
    Computes statistics and shows ROC curve."""

    baseline = {}

    """ Note that the 'baseline' here is set by making all predictions for test_data to be 'useful' """
    baseline['recall'] = recall_score(test_labels,
                                      [1 for _ in range(len(test_labels))],average = 'micro')
    baseline['precision'] = precision_score(test_labels,
                                            [1 for _ in range(len(test_labels))],average = 'micro')
    baseline['roc'] = 0.5

    results = {}

    results['recall'] = recall_score(test_labels, predictions,average = 'micro')
    results['precision'] = precision_score(test_labels, predictions,average = 'micro')
    # results['roc'] = roc_auc_score(test_labels, probs,average = 'micro')

    train_results = {}
    train_results['recall'] = recall_score(train_labels, train_predictions,average = 'micro')
    train_results['precision'] = precision_score(train_labels, train_predictions,average = 'micro')
    # train_results['roc'] = roc_auc_score(train_labels, train_probs)

    for metric in ['recall', 'precision']:
        print(
            f'{metric.capitalize()} Baseline: {round(baseline[metric], 2)} Test: {round(results[metric], 2)} Train: {round(train_results[metric], 2)}')

    # Calculate false positive rates and true positive rates
    # base_fpr, base_tpr, _ = roc_curve(test_labels, [1 for _ in range(len(test_labels))])
    # model_fpr, model_tpr, _ = roc_curve(test_labels, probs)

    # plt.figure(figsize=(8, 6))
    # plt.rcParams['font.size'] = 16
    #
    # # Plot both curves
    # plt.plot(base_fpr, base_tpr, 'b', label='baseline')
    # plt.plot(model_fpr, model_tpr, 'r', label='model')
    # plt.legend()
    # plt.xlabel('False Positive Rate')
    # plt.ylabel('True Positive Rate')
    # plt.title('ROC Curves of Random Forest')
    # plt.show()


# evaluate_model(rf_predictions, train_rf_predictions)
# plt.savefig('roc_auc_curve.png')

# NOTE: May not work with current model, needs to be updated
def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Oranges):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    Source: http://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    # Plot the confusion matrix
    plt.figure(figsize=(10, 10))
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title, size=24)
    plt.colorbar(aspect=4)
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45, size=14)
    plt.yticks(tick_marks, classes, size=14)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.

    # Labeling the plot
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt), fontsize=20,
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.grid(None)
    plt.tight_layout()
    plt.ylabel('True label', size=18)
    plt.xlabel('Predicted label', size=18)
    plt.title('Confusion Matrix of Random Forest')
    plt.show()


# Confusion matrix
# cm = confusion_matrix(test_labels, rf_predictions)
# plot_confusion_matrix(cm, classes=['Not useful', 'Useful','very useful'])
# print('\n')

# plt.savefig('cm.png')

# print("-----------------Evaluation Part----------------")
# print('Evaluation Accuracy:',accuracy_score(eval_labels, rf_eval_predictions))
#
# cm_eval = confusion_matrix(eval_labels, rf_eval_predictions)
# plot_confusion_matrix(cm_eval, classes=['Not useful', 'Useful','very useful'])
#
# print('evaluate label predictions:',rf_eval_predictions)