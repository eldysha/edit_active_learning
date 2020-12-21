from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
import numpy as np
from filter_evaluation import *
from sklearn.model_selection import train_test_split

#Logistic Regression / SVC
def regression(X_list_scores, y_list_labels, list_labels_ok):
    '''Given a list of scores of features and a list of labels for the candidates (0/1) as returned by
    calculate_scores_labels method in filter_builder.py, it computes LogisticRegression on them and returns the
    coefficientes of the regression, that represent the weights of the filters (features), old and predicted labels,
    predict_proba'''
    lr = LogisticRegression(solver='lbfgs', max_iter=1000, random_state=42, class_weight='balanced')
    #lr = SVC(kernel='linear')
    lr.fit(np.array(X_list_scores), np.array(y_list_labels))
    predicted_labels = lr.predict(X_list_scores)
    predict_proba = lr.predict_proba(X_list_scores)
    coef = lr.coef_
    print("list scores before", X_list_scores)
    print("list labels before", y_list_labels)
    #print("new predicted labels", predicted_labels)
    #print("coef", lr.coef_)
    print("predict_proba", predict_proba.tolist())
    #print("regression score", lr.score(np.array(list_scores_labels[0]), np.array(list_scores_labels[1])))
    print("regression score y predicted labels / labels ok", lr.score(np.array(X_list_scores), np.array(list_labels_ok)))
    #print("regression score y data /labels ok", lr.score(np.array(predicted_labels), np.array(list_labels_ok)))
    zip_label = list(zip(*[y_list_labels, predicted_labels, list_labels_ok]))
    print("zip labels before, predicted, right", zip_label)
    return [zip_label, coef, predict_proba, predicted_labels]










# With training and test
def regression_1(X_train, y_train, X_test, y_test):
    '''Given a list of scores of features and a list of labels for the candidates (0/1) as returned by
    calculate_scores_labels method in filter_builder.py, it computes LogisticRegression on them and returns the
    coefficientes of the regrssion, that represent the weights of the filters (features)'''
    lr = LogisticRegression(solver='lbfgs', max_iter=1000, random_state=42, class_weight='balanced')
    #lr = SVC(kernel='linear')
    lr.fit(np.array(X_train), np.array(y_train))
    y_pred = lr.predict(X_test)
    print("accuracy score", accuracy_score(y_test, y_pred))
    coef = lr.coef_
    print("X_train", X_train)
    print("y_train", y_train)
    print("X_train", X_test)
    print("y_train", y_test)
    print("coef", lr.coef_)
    print("y_pred", y_pred)
    #print("regression score", lr.score(np.array(list_scores_labels[0]), np.array(list_scores_labels[1])))
    #print("zip labels before and later", list(zip(list_scores_labels[1], predicted_labels)))
    '''lr.fit(np.array(list_scores_labels[0]), np.array(list_scores_labels[1]))
    predicted_labels_2 = lr.predict(list_scores_labels[0])
    print("list scores_2", list_scores_labels[0])
    print("list labels_2", list_scores_labels[1])
    print("coef_2", lr.coef_)
    print("new predicted labels_2", predicted_labels_2)
    print("regression score_2", lr.score(np.array(list_scores_labels[0]), np.array(list_scores_labels[1])))
    print("zip labels before and later_2", list(zip(list_scores_labels[1], predicted_labels_2)))'''
    return coef




#Decision Tree
def regression_2(list_scores_labels):
    '''Given a list of scores of features and a list of labels for the candidates (0/1) as returned by
    calculate_scores_labels method in filter_builder.py, it computes LogisticRegression on them and returns the
    coefficientes of the regrssion, that represent the weights of the filters (features)'''
    lr = DecisionTreeClassifier(random_state=0)
    lr.fit(np.array(list_scores_labels[0]), np.array(list_scores_labels[1]))
    predicted_labels = lr.predict(list_scores_labels[0])
    print("list scores", list_scores_labels[0])
    print("list labels", list_scores_labels[1])
    print("new predicted labels", predicted_labels)
    print("regression score", lr.score(np.array(list_scores_labels[0]), np.array(list_scores_labels[1])))
    print("zip labels before and later", list(zip(list_scores_labels[1], predicted_labels)))
    return 0






# INUTILI

# lr = LogisticRegression(solver='lbfgs', max_iter=1000, random_state=42)
# lr.fit(np.array([[0.5, 0.6], [0.2, 0.7], [0.5, 0.7], [0.6, 0.2], [0.1, 0.8], [0.4, 0.3]]), np.array([1, 0, 0, 1, 0, 0]))
es = ESLookup()

'''def calculate_list_reults(json_input_user_list):
    evaluator = Evaluation()
    list_scores = []
    list_labels = []
    i = 0
    for x in json_input_user_list:
        sorted_reults = evaluator.evaluate(x)
        print(sorted_reults)
        if i == 0:
            for key in sorted_reults:
                j = 0
                for x in sorted_reults[key]:
                    list_scores.append([x[1]])
                    if j == 0:
                        list_labels.append(1)
                    else:
                        list_labels.append(0)
                    j += 1
            print("list", list_scores)
        else:
            y = 0
            for key in sorted_reults:
                for x in sorted_reults[key]:
                    list_scores[y].append(x[1])
                    y += 1
        i += 1
    return [list_scores, list_labels]'''

'''def calculate_list_reults(json_input_user_list):

    Given a list of lists that contain simple filter (first: operator = edit distance, second: operator = jaccard), as
    [[f1_edit, f1_jaccard], [f2_edit, f2_jaccard], ..., [fn_edit, fn_jaccard]], where each couple contains the same
    filter, but with different operator, it returns a list of 2 lists:
    list_scores = each couple contains the local score using edit distance, jaccard
    list_labels = it contains 1 if it is linked to the first entity in the sorted_results, 0 if it is

    evaluator = Evaluation()
    list_scores = []
    list_labels = []
    y = 0
    for x in json_input_user_list:
        sorted_reults_edit = evaluator.evaluate(x[0])
        sorted_reults_jaccard = evaluator.evaluate(x[1])
        #print("sorted_reults_edit", sorted_reults_edit)
        #print("sorted_reults_jaccard", sorted_reults_jaccard)
        for key in sorted_reults_edit:
            j = 0
            for k in sorted_reults_edit[key]:
                list_scores.append([k[1]])
                #print("A", list_scores)
                if j == 0:
                    list_labels.append(1)
                else:
                    list_labels.append(0)
                j += 1
        for key in sorted_reults_jaccard:
            for k in sorted_reults_jaccard[key]:
                list_scores[y].append(k[1])
                #print("B", list_scores)
                y += 1
    #print("list_scores", list_scores)
    #print("list_labels", list_labels)
    return [list_scores, list_labels]'''

'''def calculate_list_reults(json_input_user_list):

    Given a list of lists that contain simple filter (first: operator = edit distance, second: operator = jaccard), as
    [[f1_edit, f1_jaccard], [f2_edit, f2_jaccard], ..., [fn_edit, fn_jaccard]], where each couple contains the same
    filter, but with different operator, it returns a list of 2 lists:
    list_scores = each couple contains the local score using edit distance, jaccard
    list_labels = it contains 1 if it is linked to the first entity in the sorted_results, 0 if it is

    evaluator = Evaluation()
    dict_scores = {}
    list_labels = []
    for x in json_input_user_list:
        y = 0
        sorted_reults_edit = evaluator.evaluate(x[0])
        sorted_reults_jaccard = evaluator.evaluate(x[1])
        print("sorted_reults_edit", sorted_reults_edit)
        print("sorted_reults_jaccard", sorted_reults_jaccard)
        for key in sorted_reults_edit:
            j = 0
            dict_scores[key] = []
            for k in sorted_reults_edit[key]:
                #print(k)
                dict_scores[key].append([k[1]])
                print("A", dict_scores)
                if j == 0:
                    list_labels.append(1)
                else:
                    list_labels.append(0)
                j += 1
        for key in sorted_reults_jaccard:
            for k in sorted_reults_jaccard[key]:
                dict_scores[key][y].append(k[1])
                print("B", dict_scores)
                y += 1
    list_scores = []
    for key in dict_scores:
        list_scores.append(dict_scores[key])
    #print("list_scores", list_scores)
    #print("list_labels", list_labels)
    return [list_scores, list_labels]'''

# LIST LABELS PER ORA CONSIDERANO 1 PER LA PRIMA ENTITà RIDATA DAL PRIMO FILTRO PER OGNI ELEMENTO DA RICONCILIARE
# VEDI ESEMPIO IN examples_filter in cui ci sono 4 filtri per anversa e 2 per milano
# VEDI ESEMPIO IN examples_filter in cui ci sono 1 filtro edit e 1 filtro jaccard per ogni entità
'''def calculate_list_results(json_input_user_list):
    
    Given a list of lists of json simple filters (each minor list contains the filters for a single value to reconcile
    -> es: [filter_edit_dbo:country, filter_jaccard_dbo:country] for each value to reconcile) ->
    [[f1_e, f1_j], [f2_e, f2_j], ..., [fn_e, fn_j]] with n = number of values to reconcile, it returns a list of
    2 lists (to use for the regression):
    - list_scores: list of lists (each minor list contains the local scores of the filters for a single candidate entity,
    candidate entities are all together, even if linked to different values to reconcile -> entity_milan1,
    entity_milan2, ..., entity_paris1, .., ..., entity_antwerp1, ...)
    - list_labels: it does not make sense now, it contains 0/1 if the entity is relevant or not, but now it puts 1 on
    the first entity for each value to reconcile given by the last filter in the minor list (f1_j, f2_j, ...)
    
    evaluator = Evaluation()
    dict_scores = {}
    list_scores = []
    list_labels = []
    dict_sorted_results = {}
    list_sorted_results = []
    counter = 0
    for x in json_input_user_list:
        i = 0
        dict_sorted_results = {}
        for y in x:
            sorted_results = evaluator.evaluate(y)
            print("sorted_results", sorted_results)
            for key in sorted_results:
                if i == 0:
                    j = 0
                    for k in sorted_results[key]:
                        dict_sorted_results[k[0]] = [k[1]]
                        # list_sorted_results.append([k[1]])
                        if j == 0:
                            list_labels.append(1)
                        else:
                            list_labels.append(0)
                        j += 1
                        # print("AAA", dict_sorted_results[k[0]])
                else:
                    for k in sorted_results[key]:
                        dict_sorted_results[k[0]].append(k[1])
                        # list_sorted_results[counter].append(k[1])
                        # print("DDD", dict_sorted_results[k[0]])
                        counter += 1
                i += 1
        for key in dict_sorted_results:
            list_scores.append(dict_sorted_results[key])
    # print("dict_sorted_results", dict_sorted_results)
    print("list_scores", list_scores)
    # print("list_scores", list_scores)
    print("list_labels", list_labels)
    # print("n scores", len(list_scores))
    print("n scores", len(list_scores))
    print("n labels", len(list_labels))
    # return [list_scores, list_labels]
    return [list_scores, list_labels]'''
