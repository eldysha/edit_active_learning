'''Examples pandas'''

import pandas as pd
import ast

import sklearn

from regression import *
import pickle
import random



'''es_lookup = ESLookup()
df = pd.read_csv("CTRL_DBP_BUS_european_company_high_revenues.csv")

l = df["product"].tolist()
l1 = []
i = 0
for x in l:
    l1.append([x, l.count(x)])
print(l)
print("l1", l1)

list_value = df["company"].tolist()
print(list_value)
print("len list value", len(list_value))
dic = es_lookup.multi_search(list_value)
print(dic)
super_list = []
for x in list_value:
    y = [x, dic[x]]
    super_list.append(y)
print("super list", super_list)
print("len super list", len(super_list))

col_1 = []
col_2 = []
for el in super_list:
    #for y in dic[key]:
    #print(y)
    #print(len(y))
    col_1 += [el[0]] * len(dic[el[0]])
    for x in el[1]:
        col_2.append(x[0])
    #col_2.append(el[1][0][0])
print(col_1)
print(col_2)'''

#dic = {"Algeria": [("url1", [1, 2, 3]), ("url2", [1, 2, 3])], "Uganda": [("url2", [1,2,3])]}

'''for key in dic:
    #for y in dic[key]:
    #print(y)
    #print(len(y))
    col_1 += [key] * len(dic[key]) # [key] * len(dic[key])  alternativa
    for y in dic[key]:
        col_2.append(y[0])
print(col_1)
print(col_2)
print("len col1", len(col_1))
print("len col2", len(col_2))
df_dic = {"product": col_1, "url product lookup": col_2}
new_df = pd.DataFrame(df_dic)'''
#new_df.to_csv(r'C:\Users\veror\PycharmProjects\tesi_vorsanigo\new_df.csv', index = False)
'''
df = pd.read_csv("CTRL_DBP_BUS_european_company_high_revenues.csv")
list = df["product"].tolist()
print("len lsit", len(list))
dataframe = pd.merge(new_df, df, on='product', how='left')'''
#dataframe = df.set_index("product").join(new_df.set_index("product"))
#dataframe_1 = pd.concat([dataframe, new_df], axis=1, sort=False)
#dataframe = pd.merge(df, new_df, on=['key1', 'key2'])

#print(dataframe['product'].tolist())

#print(dataframe)

#dataframe.to_csv(r'C:\Users\veror\PycharmProjects\tesi_vorsanigo\new european companies.csv', index = False)

# FZ AUSILIARIA
def mul_x(list_coeff, list_scores, x):
    for scores in list_scores:
        i = 0
        while i < x:
            scores[i] = scores[i] * list_coeff[i]
            i += 1
    return list_scores

'''es = ESLookup()
#df = pd.read_csv("CTRL_DBP_BUS_european_company_high_revenues.csv")
df1 = pd.read_csv("TOUGH_T2D_BUS_39650055_5_7135804139753401681___brands.csv")
#list_products = df['product'].tolist()
#d = es.multi_search(list_products)
list_brands = df1['Brand'].tolist()
d1 = es.multi_search(list_brands)
#print(d)
print(d1)
print(list_brands)
list_parameters = [('Industry', 'http://dbpedia.org/ontology/industry', 'edit distance', 0, '>=', 1)]
#list_scores_labels = calculate_scores_labels(df, 'Candidate url state', list_parameters, 'Label Lookup')
new_list = []
for key in d1:
    for x in d1[key]:
        new_list.append(x[0])
        print(x[0])
print("new list", new_list)'''


# PROCESSO PER PREPARARE DTI DA PASSARE PER FARE LOGISTIC REGRESSION
'''df = pd.read_csv("CURRENCY DATAFRAME 370.csv") # CAMBIARE NOME DF SE SE NE USA UN ALTRO
list_parameters = [('Capital', 'http://dbpedia.org/ontology/capital', 'edit distance', 0, '>=', 1), ('Official Language', 'http://dbpedia.org/ontology/language', 'edit distance', 0, '>=', 1), ('Name of Currency', 'http://dbpedia.org/ontology/currency', 'edit distance', 0, '>=', 1)]
list_scores_labels = calculate_scores_labels(df, 'Candidate url state', list_parameters, 'Label Lookup')
file = open('pickle_scores_labels_CURRENCY370', 'wb')
pickle.dump(list_scores_labels, file)
file.close()
print("XXXXXXXXXX", list_scores_labels)

file = open('pickle_scores_labels_CURRENCY370', 'rb')
list_scores_labels = pickle.load(file)

scores_no_weights = list_scores_labels[0]
file_1 = open('pickle_scores_no_weights_CURRENCY370', 'wb')
pickle.dump(scores_no_weights, file_1)
file_1.close()
print('scores_no_weights_CURRENCY370', scores_no_weights)

labels_lookup = list_scores_labels[1]
file_2 = open('pickle_labels_lookup_CURRENCY370', 'wb')
pickle.dump(labels_lookup, file_2)
file_2.close()
print('labels_lookup_CURRENCY370', labels_lookup)

labels_ok = df['Label ok'].tolist()
file_3 = open('pickle_labels_ok_CURRENCY370', 'wb')
pickle.dump(labels_ok, file_3)
file_3.close()
print('labels_ok_CURRENC370', labels_ok)'''

'''for x in scores_no_weights:
    x.remove(x[2])
    x.remove(x[0])'''

file_1 = open('pickle_scores_no_weights_CURRENCY560', 'rb')
scores_no_weights = pickle.load(file_1)
print("scores_no_weights_CURRENCY560", scores_no_weights)

file_2 = open('pickle_labels_lookup_CURRENCY560', 'rb')
labels_lookup = pickle.load(file_2)
print('labels_lookup_CURRENCY560', labels_lookup)

file_3 = open('pickle_labels_ok_CURRENCY560', 'rb')
labels_ok = pickle.load(file_3)
print('labels_ok_CURRENCY560', labels_ok)

x = list(zip(scores_no_weights, labels_ok))
i = 0
for y in x:
    #if (y[0][0] != 0 or y[0][1] != 0 or y[0][2] != 0) and y[1] == 0:
    if y[0][2] != 0 and y[0][0] and y[1] == 0:
        print("EEE", i)
        print(y)
    i += 1
print(x)
print("GUINEA", x[270])
print("KOKOTA", x[272])
print("GUINEA BISSAU", x[275])
print("AIKEA", x[278])

num1 = 0
for x in labels_ok:
    if x == 1:
        num1 += 1
print("num1", num1)
i = 0
uguali = 0
diversi = 0
for x in labels_lookup:
    if x == labels_ok[i]:
        uguali += 1
    else:
        diversi += 1
    i += 1
print("uguali", uguali)
print("diversi", diversi)

'''print(len(labels_lookup))
print(len(labels_ok))
print(len(scores_no_weights))'''
# FINE PROCESSO

#TODO inizio BRANDS NON PIù  DA USARE
'''df = pd.read_csv("BRANDS.csv")
print(df)
list_parameters = [('Industry', 'http://dbpedia.org/ontology/industry', 'edit distance', 0, '>=', 1)]
list_scores_labels = calculate_scores_labels(df, 'Brand__URI', list_parameters, 'Label lookup')
file = open('pickle_scores_labels_brands', 'wb')
pickle.dump(list_scores_labels, file)
file.close()
print("XXXXXXXXXX", list_scores_labels)

file = open('pickle_scores_labels_brands', 'rb')
list_scores_labels = pickle.load(file)

scores_no_weights = list_scores_labels[0]
file_1 = open('pickle_scores_no_weights_brands', 'wb')
pickle.dump(scores_no_weights, file_1)
file_1.close()
print('scores_no_weights_brands', scores_no_weights)

file_1 = open('pickle_scores_no_weights_brands', 'rb')
scores_no_weights = pickle.load(file_1)
print("scores_no_weights_brands", scores_no_weights)'''
'''for x in scores_no_weights:
    x.remove(x[2])
    x.remove(x[0])
print(scores_no_weights)'''

'''labels_lookup = list_scores_labels[1]
file_2 = open('pickle_labels_lookup_brands', 'wb')
pickle.dump(labels_lookup, file_2)
file_2.close()
print('labels_lookup_brands', labels_lookup)

file_2 = open('pickle_labels_lookup_brands', 'rb')
labels_lookup = pickle.load(file_2)
print('labels_lookup_brands', labels_lookup)

labels_ok = df['Label ok'].tolist()
file_3 = open('pickle_labels_ok_brands', 'wb')
pickle.dump(labels_ok, file_3)
file_3.close()
print('labels_ok_brands', labels_ok)

file_3 = open('pickle_labels_ok_brands', 'rb')
labels_ok = pickle.load(file_3)
print('labels_ok_brands', labels_ok)'''

#TODO fine BRANDS NON PIù DA USARE

#TODO DA USARE

# DATI SE SI FA SU DF PRUNED (377 EL)
'''file_1 = open('pickle_scores_no_weights_pruned', 'rb')
scores_no_weights = pickle.load(file_1)
print("scores_no_weights_pruned", scores_no_weights)
for x in scores_no_weights:
    x.remove(x[2])
    x.remove(x[0])
print(scores_no_weights)

file_2 = open('pickle_labels_lookup_pruned', 'rb')
labels_lookup = pickle.load(file_2)
print('labels_lookup_pruned', labels_lookup)

file_3 = open('pickle_labels_ok_pruned', 'rb')
labels_ok = pickle.load(file_3)
print('labels_ok_pruned', labels_ok)

print(len(scores_no_weights))
print(len(labels_lookup))
print(len(labels_ok))
#print(len(labels_ok))'''

#FINE DATI 377



# DATI SE SI FA SU DF COMPLETO (727 EL)
#df = pd.read_csv("currency dataframe bello da usare.csv")

# LIST SCORES NO WEIGHTS
'''scores_no_weights = list_scores_labels[0]
file_1 = open('pickle_scores_no_weights', 'wb')
pickle.dump(scores_no_weights, file_1)
file_1.close()
print('scores_no_weights', scores_no_weights)'''
#print(len(scores_no_weights))

#TODO DA DECOMMENTARE PER RUN
'''file_1 = open('pickle_scores_no_weights', 'rb')
scores_no_weights = pickle.load(file_1)
print("scores_no_weights", scores_no_weights)'''

'''for x in scores_no_weights:
    x.remove(x[2])
    x.remove(x[0])
print(scores_no_weights)'''

# LIST LABELS OK
'''labels_ok = list_scores_labels[1]
file_2 = open('pickle_labels_ok', 'wb')
pickle.dump(labels_ok, file_2)
file_2.close()
print('labels_ok', labels_ok)
#print(len(labels_ok))'''

#TODO DA DECOMMENTARE PER RUN
'''file_2 = open('pickle_labels_ok', 'rb')
labels_ok = pickle.load(file_2)
print('labels_ok', labels_ok)'''

# LIST LABELS LOOKUP
'''labels_lookup = df['Label Lookup'].tolist()
file_3 = open('pickle_labels_lookup', 'wb')
pickle.dump(labels_lookup, file_3)
file_3.close()
print('labels_lookup', labels_lookup)'''
#print(len(labels_lookup))

#TODO DA DECOMMENTARE PER RUN
'''file_3 = open('pickle_labels_lookup', 'rb')
labels_lookup = pickle.load(file_3)
print('labels_lookup', labels_lookup)'''

# FINE DATI 727



# esempio piccolo
'''labels_lookup = [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0]
labels_ok = [0, 1, 0, 0, 0, 0, 1 ,1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1]
scores_no_weights = [[0.0, 0.0, 0.0], [1, 1, 0.3571428571428571], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.1428571428571429, 0.0, 0.0], [1, 1, 0.6], [1, 1, 0.4666666666666667], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.3571428571428572, 1, 0.2], [1, 1, 0.375], [0.1428571428571429, 0.0, 0.0], [0.8571428571428572, 1, 0.5], [0.8571428571428572, 0.5, 0.5], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.8888888888888888, 0.0, 0.5], [1, 1, 0.675], [0.0, 0.0, 0.0], [0.8888888888888888, 0.0, 0.5],  [1, 1, 0.8666666666666667]]
'''



print("-------------------------------------------------------------------------------------------------------------")

# LISTA PARAMETRI FILTRI USATI PER CALCOLARE GLO SCORES PASSATI (xX DELLA LOGISTIC REGRESSION)
#list_parameters_2 = [('Capital', 'http://dbpedia.org/ontology/capital', 'edit distance', 0, '>=', coef[0][0]), ('Official Language', 'http://dbpedia.org/ontology/language', 'edit distance', 0, '>=', coef[0][1])] #, ('Name of Currency', 'http://dbpedia.org/ontology/currency', 'edit distance', 0, '>=', 0.33333)

# CODICE PER FARE ITERAZIONI LOGISTIC REGRESSION, USANDO DATI SOPRA

N_filters = 3 # DA CAMBIARE SE NUMERO FILTRI è DIFFERENTE
N_el = 560 # NUMERO EL NEL DATAFRAME, DA CAMBIARE SE è DIFFERENTE
j = 0
#num_iteration = 5
X_scores = scores_no_weights
y_labels = labels_lookup # labels_ok
coef = [[1, 1, 1]]
ran = -1
answer = "n"

while answer == "n":
    print("ITERATION ", j)
    if j > 0:
        if ran != -1:
            #label = input('Insert label of the entity ' + str(ran) + ' :')
            print('Check entities similar to position: ' + str(ran))
            pos = input('Insert index of right entity or -1 if there is no right match:')
            start_pos = input('Insert index of starting position of candidates:')
            last_pos = input('Insert index of last position of candidates:')
            #y_labels[ran] = int(label)
            i = int(start_pos)
            last_position = int(last_pos)
            while i <= last_position:
                y_labels[i] = 0
                i += 1
            right_position = int(pos)
            if right_position >= 0:
                print("hey")
                y_labels[right_position] = 1

        print("NEW", y_labels)
        X_scores = mul_x(coef[0], X_scores, N_filters)
        #print("zipzipzip", zip_label_coef_1[3])

    regression_res = regression(X_scores, y_labels, labels_ok)
    #print("zip labels", regression_res[0])
    #print("coef", regression_res[1])
    predict_proba = regression_res[2]
    #y_labels = regression_res[3]
    coef = regression_res[1]
    #print("new predicted y_labels", y_labels)
    #print("EEEEEEE coef", coef)

    #print("regression_res[3]", regression_res[3])
    pred_labels = list(regression_res[3])
    print("pred labels", pred_labels)
    print("labels ok", labels_ok)
    i = 0
    num_right_1 = 0
    num_right_0 = 0
    num_0_instead_of_1 = 0
    num_1_instead_of_0 = 0
    for x in pred_labels:
        #print(pred_labels[i])
        #print(labels_ok[i])
        if x == 1:
            if x == labels_ok[i]:
                #print("uno")
                num_right_1 += 1
            else:
                #print("due")
                num_1_instead_of_0 += 1
        else:  # x == 0
            if x == labels_ok[i]:
                #print("tre")
                num_right_0 += 1
            else:
                #print("quattro")
                num_0_instead_of_1 += 1
        i += 1
    print("NUM RIGHT 1", num_right_1)
    print("NUM RIGHT 0", num_right_0)
    print("NUM 1 INSTEAD OF 0", num_1_instead_of_0)
    print("NUM 0 INSTEAD OF 1", num_0_instead_of_1)

    confusion_matrix = np.array([[num_right_1, num_1_instead_of_0],
                        [num_0_instead_of_1, num_right_0]])
    print("CONFUSION MATRIX NON AUTOMATICA\n", confusion_matrix)

    con_matr = sklearn.metrics.confusion_matrix(labels_ok, pred_labels)
    print("CONFUSION MATRIX\n", con_matr)

    print("\n")

    # 1) CHOOSE ENTITY TO BE LABELED BY USER -> SCORE NEAR 0.5
    n = 0
    list_entities_1 = []
    list_pos_1 = []

    while n < len(predict_proba):
        y = predict_proba[n]
        if (y[0] >= 0.4 and y[0] <= 0.6) or (y[1] >= 0.4 and y[1] <= 0.6):
            # x = False
            #print("eccolo", y, "in posizione", n)
            #print("labels", regression_res[0][n])
            list_entities_1.append(y.tolist())
            list_pos_1.append(n)
        n += 1

    if len(list_pos_1) != 0:
        ran = random.choice(list_pos_1)
        #print("ENTITY FOR USER TO LABEL", ran)
        print('random pos', ran)
        print("SCORE", X_scores[ran])
        print("PREDICT_PROBA", predict_proba[ran])
        print("LABELS LOOKUP RAN", labels_lookup[ran])
        print("Y_LABELS RAN", y_labels[ran])
        print("LIST ENTITIES", list_entities_1)
        print("LIST POS", list_pos_1)

    # 2) CHOOSE ENTITY TO BE LABELED BY USER -> MORE FREQUENT SCORE
    class_3_4 = []
    pos_3_4 = []
    class_4_5 = []
    pos_4_5 = []
    class_5_6 = []
    pos_5_6 = []
    class_6_7 = []
    pos_6_7 = []
    i = 0
    while i < len(predict_proba):  # and x:
        y = predict_proba[i]
        if (y[0] >= 0.3 and y[0] < 0.4):
            # x = False
            class_3_4.append(y.tolist())
            pos_3_4.append(i)
        elif (y[0] >= 0.4 and y[0] < 0.5):
            class_4_5.append(y.tolist())
            pos_4_5.append(i)
        elif (y[0] >= 0.5 and y[0] < 0.6):
            class_5_6.append(y.tolist())
            pos_5_6.append(i)
        elif (y[0] >= 0.6 and y[0] < 0.7):
            class_6_7.append(y.tolist())
            pos_6_7.append(i)
        i += 1

    print("\n")

    print("class 3 4", class_3_4)
    print("pos 3 4", pos_3_4)
    print("class 4 5", class_4_5)
    print("pos 4 5", pos_4_5)
    print("class 5 6", class_5_6)
    print("pos 5 6 ", pos_5_6)
    print("class 6 7 ", class_6_7)
    print("pos 6 7 ", pos_6_7)

    if not (len(class_3_4) == 0 and len(class_4_5) == 0 and len(class_5_6) == 0 and len(class_6_7) == 0):
        list_len = [len(class_3_4), len(class_4_5), len(class_5_6), len(class_6_7)]
        list_class = [class_3_4, class_4_5, class_5_6, class_6_7]
        list_pos = [pos_3_4, pos_4_5, pos_5_6, pos_6_7]
        index = list_len.index(max(list_len))
        #print('list_pos_labels_one', list_pos_labels_one)
        print('list pos selected', list_pos[index])
        #inters = list(set(list_pos_labels_one) & set(list_pos[index]))
        #print("intersection", inters)
        #if len(inters) != 0: #ran = random.choice(inters) #else:
        ran = random.choice(list_pos[index])
        print('list_len', list_len)
        print('list_class', list_class)
        print('list_pos', list_pos)
        print('i', index)
        print('random pos', ran)
        print("SCORE", X_scores[ran])
        print("PREDICT_PROBA", predict_proba[ran])
        print("LABELS LOOKUP RAN", labels_lookup[ran])
        print("Y_LABELS RAN", y_labels[ran])

    print("\n")

    uguali = 0
    diversi = 0
    uguali_1 = 0
    diversi_1 = 0
    uguali_2 = 0
    diversi_2 = 0
    for x in regression_res[0]:
        if x[1] == x[2]:
            uguali += 1
        else:
            diversi += 1
        if x[1] == x[0]:
            uguali_1 += 1
        else:
            diversi_1 += 1
        if x[0] == x[2]:
            uguali_2 += 1
        else:
            diversi_2 += 1
    print("uguali predicted / label_ok", uguali)
    print("diversi predicted / label_ok", diversi)
    print("uguali y_label / predicted", uguali_1)
    print("diversi y_label / predicted", diversi_1)
    print("uguali y_label / label_ok", uguali_2)
    print("diversi y_label / label_ok", diversi_2)
    print("pred / ok", uguali * 100 / N_el) #377)
    print("pred / y_labels", uguali_1 * 100 / N_el) #377)
    print("y_labels / ok", uguali_2 * 100 /  N_el) #377)

    print("----------------------------------------------")

    answer = input("Do you want to stop? [y/n]")

    j += 1

#FINE CODICE PER FARE REGRESSION


'''
N_filters = 3 # DA CAMBIARE SE NUMERO FILTRI è DIFFERENTE
N_el = 560 # NUMERO EL NEL DATAFRAME, DA CAMBIARE SE è DIFFERENTE
X_scores = scores_no_weights
y_labels = labels_lookup # labels_ok
coef = [[1, 1, 1]]
k = 550

#while k < 560:

print("DECINA", k)

regression_res = regression(X_scores, y_labels, labels_ok)
#print("zip labels", regression_res[0])
print("coef", regression_res[1])
predict_proba = regression_res[2]
#coef = regression_res[1]
#print("new predicted y_labels", y_labels)
#print("EEEEEEE coef", coef)

#print("regression_res[3]", regression_res[3])
pred_labels = list(regression_res[3])
print("pred labels", pred_labels)
print("labels ok", labels_ok)

print("\n")
# 1) CHOOSE ENTITY TO BE LABELED BY USER -> SCORE NEAR 0.5
print("0.5 STRATEGY")
n = k
end = k + 10
list_entities_1 = []
list_pos_1 = []

while n < end:
    print("n", n)
    y = predict_proba[n]
    print("y", y)
    if (y[0] >= 0.4 and y[0] <= 0.6) or (y[1] >= 0.4 and y[1] <= 0.6):
        # x = False
        #print("eccolo", y, "in posizione", n)
        #print("labels", regression_res[0][n])
        list_entities_1.append(y.tolist())
        list_pos_1.append(n)
    n += 1

if len(list_pos_1) != 0:
    ran = random.choice(list_pos_1)
    #print("ENTITY FOR USER TO LABEL", ran)
    print('random pos', ran)
    print("SCORE", X_scores[ran])
    print("PREDICT_PROBA", predict_proba[ran])
    print("LABELS LOOKUP RAN", labels_lookup[ran])
    print("Y_LABELS RAN", y_labels[ran])
    print("LIST ENTITIES", list_entities_1)
    print("LIST POS", list_pos_1)

else:
    print("NO 0.5")
    print("\n")

# 2) CHOOSE ENTITY TO BE LABELED BY USER -> MORE FREQUENT SCORE
print("BIN STRATEGY")
class_3_4 = []
pos_3_4 = []
class_4_5 = []
pos_4_5 = []
class_5_6 = []
pos_5_6 = []
class_6_7 = []
pos_6_7 = []
l = k
end = k + 10
print("l", l)
while l < end:  # and x:
    y = predict_proba[l]
    if (y[0] >= 0.3 and y[0] < 0.4):
        # x = False
        class_3_4.append(y.tolist())
        pos_3_4.append(l)
    elif (y[0] >= 0.4 and y[0] < 0.5):
        class_4_5.append(y.tolist())
        pos_4_5.append(l)
    elif (y[0] >= 0.5 and y[0] < 0.6):
        class_5_6.append(y.tolist())
        pos_5_6.append(l)
    elif (y[0] >= 0.6 and y[0] < 0.7):
        class_6_7.append(y.tolist())
        pos_6_7.append(l)
    l += 1

#print("\n")

print("class 3 4", class_3_4)
print("pos 3 4", pos_3_4)
print("class 4 5", class_4_5)
print("pos 4 5", pos_4_5)
print("class 5 6", class_5_6)
print("pos 5 6 ", pos_5_6)
print("class 6 7 ", class_6_7)
print("pos 6 7 ", pos_6_7)

if not (len(class_3_4) == 0 and len(class_4_5) == 0 and len(class_5_6) == 0 and len(class_6_7) == 0):
    list_len = [len(class_3_4), len(class_4_5), len(class_5_6), len(class_6_7)]
    list_class = [class_3_4, class_4_5, class_5_6, class_6_7]
    list_pos = [pos_3_4, pos_4_5, pos_5_6, pos_6_7]
    index = list_len.index(max(list_len))
    #print('list_pos_labels_one', list_pos_labels_one)
    print('list pos selected', list_pos[index])
    #inters = list(set(list_pos_labels_one) & set(list_pos[index]))
    #print("intersection", inters)
    #if len(inters) != 0: #ran = random.choice(inters) #else:
    ran = random.choice(list_pos[index])
    print('list_len', list_len)
    print('list_class', list_class)
    print('list_pos', list_pos)
    print('i', index)
    print('random pos', ran)
    print("SCORE", X_scores[ran])
    print("PREDICT_PROBA", predict_proba[ran])
    print("LABELS LOOKUP RAN", labels_lookup[ran])
    print("Y_LABELS RAN", y_labels[ran])
    print("LABELS OK", labels_ok[ran])

print("\n")

i = 0
num_right_1 = 0
num_right_0 = 0
num_0_instead_of_1 = 0
num_1_instead_of_0 = 0
for x in pred_labels:
    # print(pred_labels[i])
    # print(labels_ok[i])
    if x == 1:
        if x == labels_ok[i]:
            # print("uno")
            num_right_1 += 1
        else:
            # print("due")
            num_1_instead_of_0 += 1
    else:  # x == 0
        if x == labels_ok[i]:
            # print("tre")
            num_right_0 += 1
        else:
            # print("quattro")
            num_0_instead_of_1 += 1
    i += 1
print("NUM RIGHT 1", num_right_1)
print("NUM RIGHT 0", num_right_0)
print("NUM 1 INSTEAD OF 0", num_1_instead_of_0)
print("NUM 0 INSTEAD OF 1", num_0_instead_of_1)

confusion_matrix = np.array([[num_right_1, num_1_instead_of_0],
                             [num_0_instead_of_1, num_right_0]])
print("CONFUSION MATRIX NON AUTOMATICA\n", confusion_matrix)'''


#BOH
'''X_scores = scores_no_weights
y_labels = labels_lookup  # labels_ok
coef = [[1, 1, 1]]
k = 0
j = 0

print("DECINE CANDIDATE ", k)
while j < 2:

    regression_res = regression(X_scores, y_labels, labels_ok)

    predict_proba = regression_res[2]
    coef = regression_res[1]
    pred_labels = list(regression_res[3])
    print("pred labels", pred_labels)
    print("labels ok", labels_ok)
    print("predict proba", predict_proba)
    print("coef", coef)
    
    i = 0
    num_right_1 = 0
    num_right_0 = 0
    num_0_instead_of_1 = 0
    num_1_instead_of_0 = 0
    for x in pred_labels:
        # print(pred_labels[i])
        # print(labels_ok[i])
        if x == 1:
            if x == labels_ok[i]:
                # print("uno")
                num_right_1 += 1
            else:
                # print("due")
                num_1_instead_of_0 += 1
        else:  # x == 0
            if x == labels_ok[i]:
                # print("tre")
                num_right_0 += 1
            else:
                # print("quattro")
                num_0_instead_of_1 += 1
        i += 1
    print("NUM RIGHT 1", num_right_1)
    print("NUM RIGHT 0", num_right_0)
    print("NUM 1 INSTEAD OF 0", num_1_instead_of_0)
    print("NUM 0 INSTEAD OF 1", num_0_instead_of_1)

    confusion_matrix = np.array([[num_right_1, num_1_instead_of_0],
                                 [num_0_instead_of_1, num_right_0]])
    print("CONFUSION MATRIX NON AUTOMATICA\n", confusion_matrix)

    con_matr = sklearn.metrics.confusion_matrix(labels_ok, pred_labels)
    print("CONFUSION MATRIX\n", con_matr)

    uguali = 0
    diversi = 0
    uguali_1 = 0
    diversi_1 = 0
    uguali_2 = 0
    diversi_2 = 0
    for x in regression_res[0]:
        if x[1] == x[2]:
            uguali += 1
        else:
            diversi += 1
        if x[1] == x[0]:
            uguali_1 += 1
        else:
            diversi_1 += 1
        if x[0] == x[2]:
            uguali_2 += 1
        else:
            diversi_2 += 1
    print("uguali predicted / label_ok", uguali)
    print("diversi predicted / label_ok", diversi)
    print("uguali y_label / predicted", uguali_1)
    print("diversi y_label / predicted", diversi_1)
    print("uguali y_label / label_ok", uguali_2)
    print("diversi y_label / label_ok", diversi_2)
    print("pred / ok", uguali * 100 / N_el)  # 377)
    print("pred / y_labels", uguali_1 * 100 / N_el)  # 377)
    print("y_labels / ok", uguali_2 * 100 / N_el)  # 377)

    X_scores = mul_x(coef[0], X_scores, N_filters)

    if j < 1:
        print('Check entities similar to position: ' + str(k))
        pos = input('Insert index of right entity or -1 if there is no right match:')
        start_position = k
        last_position = k + 9
        while start_position <= last_position:
            y_labels[start_position] = 0
            start_position += 1
        right_position = int(pos)
        if right_position >= 0:
            print("hey")
            y_labels[right_position] = 1
        print("NEW", y_labels)

    j += 1

print("--------------------------------------------------------------------------------------------------------------------------")
k += 10'''
#FINE BOH




# CODICE USATO PER CREARE "DECINE 560 DA USARE"
'''
N_filters = 3 # DA CAMBIARE SE NUMERO FILTRI è DIFFERENTE
N_el = 560 # NUMERO EL NEL DATAFRAME, DA CAMBIARE SE è DIFFERENTE
X_scores = scores_no_weights
y_labels = labels_lookup # labels_ok
coef = [[1, 1, 1]]
k = 0
j = 0
print("DECINE CANDIDATE ", k)
while j < 2:

    regression_res = regression(X_scores, y_labels, labels_ok)

    predict_proba = regression_res[2]
    coef = regression_res[1]
    pred_labels = list(regression_res[3])
    print("pred labels", pred_labels)
    print("labels ok", labels_ok)
    print("predict proba", predict_proba)
    print("coef", coef)
    i = 0
    num_right_1 = 0
    num_right_0 = 0
    num_0_instead_of_1 = 0
    num_1_instead_of_0 = 0
    for x in pred_labels:
        # print(pred_labels[i])
        # print(labels_ok[i])
        if x == 1:
            if x == labels_ok[i]:
                # print("uno")
                num_right_1 += 1
            else:
                # print("due")
                num_1_instead_of_0 += 1
        else:  # x == 0
            if x == labels_ok[i]:
                # print("tre")
                num_right_0 += 1
            else:
                # print("quattro")
                num_0_instead_of_1 += 1
        i += 1
    print("NUM RIGHT 1", num_right_1)
    print("NUM RIGHT 0", num_right_0)
    print("NUM 1 INSTEAD OF 0", num_1_instead_of_0)
    print("NUM 0 INSTEAD OF 1", num_0_instead_of_1)

    confusion_matrix = np.array([[num_right_1, num_1_instead_of_0],
                                 [num_0_instead_of_1, num_right_0]])
    print("CONFUSION MATRIX NON AUTOMATICA\n", confusion_matrix)

    con_matr = sklearn.metrics.confusion_matrix(labels_ok, pred_labels)
    print("CONFUSION MATRIX\n", con_matr)

    uguali = 0
    diversi = 0
    uguali_1 = 0
    diversi_1 = 0
    uguali_2 = 0
    diversi_2 = 0
    for x in regression_res[0]:
        if x[1] == x[2]:
            uguali += 1
        else:
            diversi += 1
        if x[1] == x[0]:
            uguali_1 += 1
        else:
            diversi_1 += 1
        if x[0] == x[2]:
            uguali_2 += 1
        else:
            diversi_2 += 1
    print("uguali predicted / label_ok", uguali)
    print("diversi predicted / label_ok", diversi)
    print("uguali y_label / predicted", uguali_1)
    print("diversi y_label / predicted", diversi_1)
    print("uguali y_label / label_ok", uguali_2)
    print("diversi y_label / label_ok", diversi_2)
    print("pred / ok", uguali * 100 / N_el)  # 377)
    print("pred / y_labels", uguali_1 * 100 / N_el)  # 377)
    print("y_labels / ok", uguali_2 * 100 / N_el)  # 377)

    X_scores = mul_x(coef[0], X_scores, N_filters)

    if j < 1:
        print('Check entities similar to position: ' + str(k))
        pos = input('Insert index of right entity or -1 if there is no right match:')
        start_position = k
        last_position = k + 9
        while start_position <= last_position:
            y_labels[start_position] = 0
            start_position += 1
        right_position = int(pos)
        if right_position >= 0:
            print("hey")
            y_labels[right_position] = 1
        print("NEW", y_labels)

    j += 1'''

print("--------------------------------------------------------------------------------------------------------------------------")

# FINE CODICE USATO PER "DECINE 560 DA USARE"















'''list_pos_labels_one = []
    i = 0
    for x in y_labels:
        if x == 1:
            list_pos_labels_one.append(i)
        i += 1
    print('list_pos_labels_ok', list_pos_labels_one)'''



'''while j < num_iteration:
    print("ITERATION ", j)
    if j > 0:
        if ran != -1:
            label = input('Insert label fo the entity ' + str(ran) + ' :')
            y_labels[ran] = int(label)
        X_scores = mul_x(coef[0], X_scores, N_filters)
        #print("zipzipzip", zip_label_coef_1[3])

    regression_res = regression(X_scores, y_labels, labels_ok)
    #print("zip labels", regression_res[0])
    #print("coef", regression_res[1])
    predict_proba = regression_res[2]
    y_labels = regression_res[3]
    coef = regression_res[1]
    print("new predicted y_labels", y_labels)
    #print("EEEEEEE coef", coef)

    list_pos_labels_one = []
    i = 0
    for x in y_labels:
        if x == 1:
            list_pos_labels_one.append(i)
        i += 1
    print('list_pos_labels_ok', list_pos_labels_one)

    print("\n")

    # 1) CHOOSE ENTITY TO BE LABELED BY USER -> SCORE NEAR 0.5
    n = 0
    list_entities_1 = []
    list_pos_1 = []

    while n < len(predict_proba):
        y = predict_proba[n]
        if (y[0] > 0.4 and y[0] < 0.6) or (y[1] > 0.4 and y[1] < 0.6):
            # x = False
            print("eccolo", y, "in posizione", n)
            print("labels", regression_res[0][n])
            list_entities_1.append(y.tolist())
            list_pos_1.append(n)
        n += 1

    if len(list_pos_1) != 0:
        ran = random.choice(list_pos_1)
        print("ENTITY FOR USER TO LABEL", ran)
        print("LIST ENTITIES", list_entities_1)
        print("LIST POS", list_pos_1)

    # 2) CHOOSE ENTITY TO BE LABELED BY USER -> MORE FREQUENT SCORE
    class_3_4 = []
    pos_3_4 = []
    class_4_5 = []
    pos_4_5 = []
    class_5_6 = []
    pos_5_6 = []
    class_6_7 = []
    pos_6_7 = []
    i = 0
    while i < len(predict_proba):  # and x:
        y = predict_proba[i]
        if (y[0] >= 0.3 and y[0] < 0.4):
            # x = False
            class_3_4.append(y.tolist())
            pos_3_4.append(i)
        elif (y[0] >= 0.4 and y[0] < 0.5):
            class_4_5.append(y.tolist())
            pos_4_5.append(i)
        elif (y[0] >= 0.5 and y[0] < 0.6):
            class_5_6.append(y.tolist())
            pos_5_6.append(i)
        elif (y[0] >= 0.6 and y[0] < 0.7):
            class_6_7.append(y.tolist())
            pos_6_7.append(i)
        i += 1

    print("\n")

    print("class 3 4", class_3_4)
    print("pos 3 4", pos_3_4)
    print("class 4 5", class_4_5)
    print("pos 4 5", pos_4_5)
    print("class 5 6", class_5_6)
    print("pos 5 6 ", pos_5_6)
    print("class 6 7 ", class_6_7)
    print("pos 6 7 ", pos_6_7)

    if not (len(class_3_4) == 0 and len(class_4_5) == 0 and len(class_5_6) == 0 and len(class_6_7) == 0):
        list_len = [len(class_3_4), len(class_4_5), len(class_5_6), len(class_6_7)]
        list_class = [class_3_4, class_4_5, class_5_6, class_6_7]
        list_pos = [pos_3_4, pos_4_5, pos_5_6, pos_6_7]
        index = list_len.index(max(list_len))
        print('list_pos_labels_one', list_pos_labels_one)
        print('list pos selected', list_pos[index])
        inters = list(set(list_pos_labels_one) & set(list_pos[index]))
        print("intersection", inters)
        if len(inters) != 0:
            ran = random.choice(inters)
        else:
            ran = random.choice(list_pos[index])
        print('list_len', list_len)
        print('list_class', list_class)
        print('list_pos', list_pos)
        print('i', index)
        print('random pos', ran)
        print("LABELS LOOKUP RAN", labels_lookup[ran])
        print("Y_LABELS RAN", y_labels[ran])
    print("\n")'''

'''    uguali = 0
    diversi = 0
    uguali_1 = 0
    diversi_1 = 0
    uguali_2 = 0
    diversi_2 = 0
    for x in regression_res[0]:
        if x[1] == x[2]:
            uguali += 1
        else:
            diversi += 1
        if x[1] == x[0]:
            uguali_1 += 1
        else:
            diversi_1 += 1
        if x[0] == x[2]:
            uguali_2 += 1
        else:
            diversi_2 += 1
    print("uguali predicted / label_ok", uguali)
    print("diversi predicted / label_ok", diversi)
    print("uguali y_label / predicted", uguali_1)
    print("diversi y_label / predicted", diversi_1)
    print("uguali y_label / label_ok", uguali_2)
    print("diversi y_label / label_ok", diversi_2)
    print("pred / ok", uguali * 100 / 727) #377)
    print("pred / y_labels", uguali_1 * 100 / 727) #377)
    print("y_labels / ok", uguali_2 * 100 /  727) #377)

    print("----------------------------------------------")
    j += 1'''








# ALTRO NON UTILE ADESSO

'''print("FIRST ITERATION")

zip_label_coef_1 = regression(scores_no_weights, labels_lookup, labels_ok)
print("zip labels", zip_label_coef_1[0])
print(zip_label_coef_1[1])
predict_proba_1 = zip_label_coef_1[2]'''

'''i = 0
x = True
list_entities_1 = []
list_pos_1 = []
while i < len(predict_proba_1): #and x:
    y = predict_proba_1[i]
    if (y[0] > 0.4 and y[0] < 0.6)  or (y[1] > 0.4 and y[1] < 0.6):
        #x = False
        print("eccolo", y, "in posizione", i)
        print("labels", zip_label_coef_1[0][i])
        list_entities_1.append(y.tolist())
        list_pos_1.append(i)
    i += 1

label_index_user = random.choice(list_pos_1)
print("ENTITY FOR USER TO LABEL", label_index_user)
print("LIST ENTITIES", list_entities_1)
print("LIST POS", list_pos_1)'''

'''class_3_4 = []
pos_3_4 = []
class_4_5 = []
pos_4_5 = []
class_5_6 = []
pos_5_6 = []
class_6_7 = []
pos_6_7 = []
i = 0
while i < len(predict_proba_1): #and x:
    y = predict_proba_1[i]
    if (y[0] >= 0.3 and y[0] < 0.4):
        #x = False
        class_3_4.append(y.tolist())
        pos_3_4.append(i)
    elif (y[0] >= 0.4 and y[0] < 0.5):
        class_4_5.append(y.tolist())
        pos_4_5.append(i)
    elif (y[0] >= 0.5 and y[0] < 0.6):
        class_5_6.append(y.tolist())
        pos_5_6.append(i)
    elif (y[0] >= 0.6 and y[0] < 0.7):
        class_6_7.append(y.tolist())
        pos_6_7.append(i)
    i += 1

print("class 3 4", class_3_4)
print("pos 3 4", pos_3_4)
print("class 4 5", class_4_5)
print("pos 4 5", pos_4_5)
print("class 5 6", class_5_6)
print("pos 5 6 ", pos_5_6)
print("class 6 7 ", class_6_7)
print("pos 6 7 ", pos_6_7)

list_len = [len(class_3_4), len(class_4_5), len(class_5_6), len(class_6_7)]
list_class = [class_3_4, class_4_5, class_5_6, class_6_7]
list_pos = [pos_3_4, pos_4_5, pos_5_6, pos_6_7]
i = list_len.index(max(list_len))
ran = random.choice(list_pos[i])
print('list_len', list_len)
print('list_class', list_class)
print('list_pos', list_pos)
print('i', i)
print('ran', ran)


uguali = 0
diversi = 0
uguali_1 = 0
diversi_1 = 0
uguali_2 = 0
diversi_2 = 0
for x in zip_label_coef_1[0]:
    if x[1] == x[2]:
        uguali += 1
    else:
        diversi += 1
    if x[1] == x[0]:
        uguali_1 += 1
    else:
        diversi_1 += 1
    if x[0] == x[2]:
        uguali_2 += 1
    else:
        diversi_2 += 1
print("uguali", uguali)
print("diversi", diversi)
print("uguali_1", uguali_1)
print("diversi_1", diversi_1)
print("uguali_2", uguali_2)
print("diversi_2", diversi_2)
print("pred / ok", uguali * 100 / 727)
print("lookup / pred", uguali_1 * 100 / 727)
print("lookup / ok", uguali_2 * 100 / 727)

print("")
print("ITERATION 2")
label = input('Insert label fo the entity ' + str(ran) + ' :')
zip_label_coef_1[3][ran] = int(label)
scores_weights_1 = mul_x(zip_label_coef_1[1][0], scores_no_weights, N_filters)
print("zipzipzip", zip_label_coef_1[3])
zip_label_coef_2 = regression(scores_weights_1, zip_label_coef_1[3], labels_ok)
predict_proba_2 = zip_label_coef_2[2]

i = 0
x = True
list_entities_1 = []
list_pos_1 = []
while i < len(predict_proba_2): #and x:
    y = predict_proba_2[i]
    if (y[0] > 0.4 and y[0] < 0.6)  or (y[1] > 0.4 and y[1] < 0.6):
        x = False
        print("eccolo", y, "in posizione", i)
        print("labels", zip_label_coef_1[0][i])
        list_entities_1.append(y.tolist())
        list_pos_1.append(i)
    i += 1

if len(list_pos_1) != 0:
    label_index_user = random.choice(list_pos_1)
    print("ENTITY FOR USER TO LABEL", label_index_user)
    print("LIST ENTITIES", list_entities_1)
    print("LIST POS", list_pos_1)

class_3_4 = []
pos_3_4 = []
class_4_5 = []
pos_4_5 = []
class_5_6 = []
pos_5_6 = []
class_6_7 = []
pos_6_7 = []
i = 0
while i < len(predict_proba_2):  # and x:
    y = predict_proba_2[i]
    if (y[0] >= 0.3 and y[0] < 0.4):
        # x = False
        class_3_4.append(y.tolist())
        pos_3_4.append(i)
    elif (y[0] >= 0.4 and y[0] < 0.5):
        class_4_5.append(y.tolist())
        pos_4_5.append(i)
    elif (y[0] >= 0.5 and y[0] < 0.6):
        class_5_6.append(y.tolist())
        pos_5_6.append(i)
    elif (y[0] >= 0.6 and y[0] < 0.7):
        class_6_7.append(y.tolist())
        pos_6_7.append(i)
    i += 1

print("class 3 4", class_3_4)
print("pos 3 4", pos_3_4)
print("class 4 5", class_4_5)
print("pos 4 5", pos_4_5)
print("class 5 6", class_5_6)
print("pos 5 6 ", pos_5_6)
print("class 6 7 ", class_6_7)
print("pos 6 7 ", pos_6_7)

list_len = [len(class_3_4), len(class_4_5), len(class_5_6), len(class_6_7)]
list_class = [class_3_4, class_4_5, class_5_6, class_6_7]
list_pos = [pos_3_4, pos_4_5, pos_5_6, pos_6_7]
i = list_len.index(max(list_len))
ran = random.choice(list_pos[i])
print('list_len', list_len)
print('list_class', list_class)
print('list_pos', list_pos)
print('i', i)
print('ran', ran)

uguali = 0
diversi = 0
uguali_1 = 0
diversi_1 = 0
uguali_2 = 0
diversi_2 = 0
for x in zip_label_coef_2[0]:
    if x[1] == x[2]:
        uguali += 1
    else:
        diversi += 1
    if x[1] == x[0]:
        uguali_1 += 1
    else:
        diversi_1 += 1
    if x[0] == x[2]:
        uguali_2 += 1
    else:
        diversi_2 += 1
print("uguali", uguali)
print("diversi", diversi)
print("uguali_1", uguali_1)
print("diversi_1", diversi_1)
print("uguali_2", uguali_2)
print("diversi_2", diversi_2)
print("pred / ok", uguali * 100 / 727)
print("lookup / pred", uguali_1 * 100 / 727)
print("lookup / ok", uguali_2 * 100 / 727)

print("")
print("ITERATION 3")
label = input('Insert label fo the entity ' + str(ran) + ' :')
print("QQQQQQQQ", zip_label_coef_2[3][ran])
zip_label_coef_2[3][ran] = int(label)
print("EEEEEEEEEEE", zip_label_coef_1[3][ran])
scores_weights_2 = mul_x(zip_label_coef_2[1][0], scores_weights_1, N_filters)
zip_label_coef_3 = regression(scores_weights_2, zip_label_coef_2[3], labels_ok)
predict_proba_3 = zip_label_coef_3[2]

i = 0
x = True
list_entities_1 = []
list_pos_1 = []
while i < len(predict_proba_3): #and x:
    y = predict_proba_3[i]
    if (y[0] > 0.4 and y[0] < 0.6)  or (y[1] > 0.4 and y[1] < 0.6):
        x = False
        print("eccolo", y, "in posizione", i)
        print("labels", zip_label_coef_1[0][i])
        list_entities_1.append(y.tolist())
        list_pos_1.append(i)
    i += 1

if len(list_pos_1) != 0:
    label_index_user = random.choice(list_pos_1)
    print("ENTITY FOR USER TO LABEL", label_index_user)
    print("LIST ENTITIES", list_entities_1)
    print("LIST POS", list_pos_1)

uguali = 0
diversi = 0
uguali_1 = 0
diversi_1 = 0
uguali_2 = 0
diversi_2 = 0
for x in zip_label_coef_3[0]:
    if x[1] == x[2]:
        uguali += 1
    else:
        diversi += 1
    if x[1] == x[0]:
        uguali_1 += 1
    else:
        diversi_1 += 1
    if x[0] == x[2]:
        uguali_2 += 1
    else:
        diversi_2 += 1
print("uguali", uguali)
print("diversi", diversi)
print("uguali_1", uguali_1)
print("diversi_1", diversi_1)
print("uguali_2", uguali_2)
print("diversi_2", diversi_2)
print("pred / ok", uguali * 100 / 727)
print("lookup / pred", uguali_1 * 100 / 727)
print("lookup / ok", uguali_2 * 100 / 727)'''

'''print("")
print("ITERATION 4")
#label = input('Insert label fo the entity ' + str(label_index_user) + ' :')
#labels_lookup[label_index_user] = int(label)
scores_weights_3 = mul_x(zip_label_coef_3[1][0], scores_weights_2, N_filters)
zip_label_coef_4 = regression(scores_weights_3, zip_label_coef_1[3], labels_ok)
predict_proba_4 = zip_label_coef_4[2]

i = 0
x = True
list_entities_1 = []
list_pos_1 = []
while i < len(predict_proba_4): #and x:
    y = predict_proba_4[i]
    if (y[0] > 0.4 and y[0] < 0.6)  or (y[1] > 0.4 and y[1] < 0.6):
        x = False
        print("eccolo", y, "in posizione", i)
        print("labels", zip_label_coef_1[0][i])
        list_entities_1.append(y.tolist())
        list_pos_1.append(i)
    i += 1

label_index_user = random.choice(list_pos_1)
print("ENTITY FOR USER TO LABEL", label_index_user)
print("LIST ENTITIES", list_entities_1)
print("LIST POS", list_pos_1)

uguali = 0
diversi = 0
uguali_1 = 0
diversi_1 = 0
uguali_2 = 0
diversi_2 = 0
for x in zip_label_coef_4[0]:
    if x[1] == x[2]:
        uguali += 1
    else:
        diversi += 1
    if x[1] == x[0]:
        uguali_1 += 1
    else:
        diversi_1 += 1
    if x[0] == x[2]:
        uguali_2 += 1
    else:
        diversi_2 += 1
print("uguali", uguali)
print("diversi", diversi)
print("uguali_1", uguali_1)
print("diversi_1", diversi_1)
print("uguali_2", uguali_2)
print("diversi_2", diversi_2)
print("pred / ok", uguali * 100 / 727)
print("lookup / pred", uguali_1 * 100 / 727)
print("lookup / ok", uguali_2 * 100 / 727)

print("")
print("ITERATION 5")
#label = input('Insert label fo the entity ' + str(label_index_user) + ' :')
#labels_lookup[label_index_user] = int(label)
scores_weights_4 = mul_x(zip_label_coef_4[1][0], scores_weights_3, N_filters)
zip_label_coef_5 = regression(scores_weights_4, zip_label_coef_1[3], labels_ok)
predict_proba_5 = zip_label_coef_5[2]

i = 0
x = True
list_entities_1 = []
list_pos_1 = []
while i < len(predict_proba_5): #and x:
    y = predict_proba_5[i]
    if (y[0] > 0.4 and y[0] < 0.6)  or (y[1] > 0.4 and y[1] < 0.6):
        x = False
        print("eccolo", y, "in posizione", i)
        print("labels", zip_label_coef_1[0][i])
        list_entities_1.append(y.tolist())
        list_pos_1.append(i)
    i += 1

label_index_user = random.choice(list_pos_1)
print("ENTITY FOR USER TO LABEL", label_index_user)
print("LIST ENTITIES", list_entities_1)
print("LIST POS", list_pos_1)

uguali = 0
diversi = 0
uguali_1 = 0
diversi_1 = 0
uguali_2 = 0
diversi_2 = 0
danger = ""
for x in zip_label_coef_5[0]:
    if x[1] == x[2]:
        uguali += 1
    else:
        diversi += 1
    if x[1] == 0 and x[2] == 1:
        danger += " entità giusta non trovata |"
    if x[1] == 1 and x[2] == 0:
        danger += " ridata entità errata |"
    if x[1] == x[0]:
        uguali_1 += 1
    else:
        diversi_1 += 1
    if x[0] == x[2]:
        uguali_2 += 1
    else:
        diversi_2 += 1
print(danger)
print("uguali", uguali)
print("diversi", diversi)
print("uguali_1", uguali_1)
print("diversi_1", diversi_1)
print("uguali_2", uguali_2)
print("diversi_2", diversi_2)
print("pred / ok", uguali * 100 / 727)
print("lookup / pred", uguali_1 * 100 / 727)
print("lookup / ok", uguali_2 * 100 / 727)
'''

'''df = pd.read_csv("currency dataframe bello da usare.csv")
labels_lookup = df['Label Lookup'].tolist()
print('labels_lookup', labels_lookup)
list_scores_labels_lookup = []
list_scores_labels_lookup.append(list_scores_labels[0])
list_scores_labels_lookup.append(labels_lookup)
print("list_scores_labels_lookup", list_scores_labels_lookup)

file_2 = open('pickle_scores_labels_weights_2', 'rb')
list_scores_labels_weights_2 = pickle.load(file_2)
#print(list_scores_labels_weights_2)
print("labels_ok", list_scores_labels_weights_2[1])

coef_lookup = regression(list_scores_labels_lookup[0], list_scores_labels_lookup[1], list_scores_labels_weights_2[1])
print("COEF LOOKUP", coef_lookup)
print("---------------------------------------------------------------")
for y in list_scores_labels_lookup[0]:
    y[0] = y[0] * coef_lookup[0][0]
    y[1] = y[1] * coef_lookup[0][1]
    y[2] = y[2] * coef_lookup[0][2]

list_scores_updated = mul_x(coef_lookup[0], list_scores_labels_lookup[0], 3)
print("list_scores_updated", list_scores_updated)
print("updated list", list_scores_labels_lookup)
coef_updated = regression(list_scores_labels_lookup, list_scores_labels_weights_2[1])
print("COEF UPDATED", coef_updated)
for y in list_scores_labels_lookup[0]:
    y[0] = y[0] * coef_updated[0][0]
    y[1] = y[1] * coef_updated[0][1]
    y[2] = y[2] * coef_updated[0][2]
print("updated list", list_scores_labels_lookup)
coef_updated_ = regression(list_scores_labels_lookup, list_scores_labels_weights_2[1])
print("COEF UPDATED_", coef_updated_)
coef_ok = regression(list_scores_labels, list_scores_labels_weights_2[1])
print("COEF OK", coef_ok)
print("---------------------------------------------------------------")'''
#coef_2 = regression(list_scores_labels_weights_2)





'''file_1 = open('pickle_scores_labels_weights', 'rb')
list_scores_labels_weights = pickle.load(file_1)'''
#print(list_scores_labels_weights)
#X = list_scores_labels_weights[0]
#y = list_scores_labels_weights[1]

'''coef = regression(list_scores_labels)
print("------------------------------------------------------------")
coef = regression(list_scores_labels_weights)'''


'''list_scores_weights_1 = []
for x in list_scores_labels[0]:
    score_list  = []
    for y in x:
        new_score = y * 0.333
        score_list.append(new_score)
    list_scores_weights_1.append(score_list)
list_scores_labels_weights_1 = []
list_scores_labels_weights_1.append(list_scores_weights_1)
list_scores_labels_weights_1.append(list_scores_labels[1])
#print("list_scores_labels_weights 2", list_scores_labels_weights_1)

file_2 = open('pickle_scores_labels_weights_2', 'wb')
pickle.dump(list_scores_labels_weights_1, file_2)
file_2.close()'''


'''
#print(len(list_scores_labels_weights[0]))
#print(len(list_scores_labels[1]))'''


'''df1 = pd.read_csv("CurrencyTable.csv")
labels = states_list_string = df1['OAU State'].tolist()
es = ESLookup()
y = es.multi_search(states_list_string)
print(y)'''

'''
list = []
for key in y:
    for x in y[key]:
        list_min = []
        list_min.append(key)
        list_min.append(x[0])
        list_min.append(x[1])
        #print("list min", list_min)
        list.append(list_min)
        #print("list", list)
print(list)


df = pd.DataFrame.from_records(list)
print(df)
'''
#df.to_csv(r'C:\Users\veror\PycharmProjects\tesi_vorsanigo\dataframe1.csv', index = False)


# import currency table













'''print("--------------------------------------------------------------------------------------------------------------")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
regression_1(X_train, y_train, X_test, y_test)'''

'''list_parameters_2 = [('Capital', 'http://dbpedia.org/ontology/capital', 'edit distance', 0, '>=', coef[0][0]), ('Official Language', 'http://dbpedia.org/ontology/language', 'edit distance', 0, '>=', coef[0][1])] #, ('Name of Currency', 'http://dbpedia.org/ontology/currency', 'edit distance', 0, '>=', 0.33333)
list_scores_labels_2 = calculate_scores_labels(df, 'Candidate url state', list_parameters_2, 'Label')
coef_2 = regression(list_scores_labels_2)
print("coef0", coef_2[0][0], "coef", coef_2[0][1])'''

'''x = build_simple_filter(df, 'Official Language', 'http://dbpedia.org/ontology/language', 'edit distance', 0, '>=', 0.5)
for simple_filter in x:
    print("filter", 'property', simple_filter.get_property(), 'operator', simple_filter.get_operator(), 'value', simple_filter.get_value(), simple_filter.get_threshold(), simple_filter.get_threshold_operator(), simple_filter.get_weight())


list_parameters = [('Capital', 'http://dbpedia.org/ontology/capital', 'edit distance', 0, '>=', 0.5), ('Official Language', 'http://dbpedia.org/ontology/language', 'edit distance', 0, '>=', 0.5)]
y = zip_simple_filters(df, list_parameters)
print(y)
for x in y:
    print(x)

list_value_reconcile = df['OAU State'].tolist()
print('list_value_reconcile', list_value_reconcile)
d = build_list_json_simple_filter(list_value_reconcile, y)
print("EEEE", d)'''


'''i = 0
for y in df['url entities']:
    val = df['url entities'].values[i]
    print('val', val)
    print(type(y))
    #print(type(val[2:]))
    #print(val[2:])
    if val is not None:
        print("SSSSSS")
        y = val[2:]
    i += 1'''




'''capital_list_string = df['Capital'].tolist()
es = ESLookup()
print(es.multi_search(capital_list_string))'''

'''# it gives a list of lists, each list contains a row without the label of the row
values = df.values
print(values)
print("---------------------")

# it gives the headers of the columns
headers = df.columns
print(headers)
print("---------------------")

# it gives the indexes (names) of the rows, if they exist in the table (not here, in CurrencyTable)
indexes = df.index
print(indexes)
print("---------------------")

# select a single column as a Series
OAU_State = df['OAU State']
print(OAU_State)
print("---------------------")

# select a single column transforming the result into a list of string
OAU_State_list_string = df['OAU State'].tolist()
print(OAU_State_list_string)
capital_list_string = df['Capital'].tolist()
print(capital_list_string)

es_lookup = ESLookup()
results = es_lookup.multi_search(capital_list_string)
print("results", results)

"""{"Antwerp" : [{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/country", "operator" : "edit distance", "value" : "Belgium",
                                                                  "threshold" : 1, "threshold_operator" : "==", "weight" : 0.8}]}, 1]}"""

capital_list_string_1 = df.loc[(df['Capital'] == 'Algiers') | (df['Capital'] == 'Luanda') | (df['Capital'] == 'Porto-Novo')]
print("capital_list_string_1", capital_list_string_1)
OAU_State_list_string_1 = df.loc[(df['OAU State'] == 'Algeria') | (df['OAU State'] == 'Angola') | (df['OAU State'] == 'Benin')]
print("OAU_State_list_string_1", OAU_State_list_string_1)

i = 0
list_filters = []
for capital in capital_list_string_1:
    filter_edit = """{""" + capital + """ : [{"property filter" : [{"var" : "candidate"}, {"property" : 
    "http://dbpedia.org/ontology/country", "operator" : "edit distance", "value" :""" + OAU_State_list_string_1[i] + """,  
    "threshold" : 1, "threshold_operator" : "==", "weight" : 0.8}]}, 1]}"""
    filter_jaccard = """{""" + capital + """ : [{"property filter" : [{"var" : "candidate"}, {"property" : 
    "http://dbpedia.org/ontology/country", "operator" : "jaccard", "value" :""" + OAU_State_list_string_1[i] + """,  
    "threshold" : 1, "threshold_operator" : "==", "weight" : 0.8}]}, 1]}"""
    list_filters.append([filter_edit, filter_jaccard])
'''
print("---------------------")

'''# access a single cell of a column
val = df['OAU State'].values[0]
print(val)'''




'''prende dalle prime 10 righe della tabella i valori di OAU State e di Capital e li mette in una lista di stringhe'''
'''i = 0
OAU_State_list_string_1 = []
capital_list_string_1 = []
while i < 10:
    val = df['OAU State'].values[i]
    OAU_State_list_string_1.append(val)
    val1 = df['Capital'].values[i]
    capital_list_string_1.append(val1)
    i += 1
print("capital_list_string_1", capital_list_string_1)
print("OAU_State_list_string_1", OAU_State_list_string_1)'''

'''crea i filtri a partire dalle stringhe sopra -> valore da riconciliare = capital, valore per property = OAU state'''
'''i = 0
list_filters = []
for capital in capital_list_string_1:
    filter_edit = """{\"""" + capital + """\" : [{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/country", "operator" : "edit distance", "value" : \"""" + OAU_State_list_string_1[i] + """\",  "threshold" : 1, "threshold_operator" : "==", "weight" : 0.8}]}, 1]}"""
    #filter_edit_1 = """{\"""" + capital + """\" : [{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/country", "operator" : "edit distance", "value" : \"""" + OAU_State_list_string_1[i] + """\",  "threshold" : 1, "threshold_operator" : "==", "weight" : 0.8}]}, 1]}"""
    filter_jaccard = """{\"""" + capital + """\" : [{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/country", "operator" : "jaccard", "value" :\"""" + OAU_State_list_string_1[i] + """\",  "threshold" : 1, "threshold_operator" : "==", "weight" : 0.8}]}, 1]}"""
    list_filters.append([filter_edit, filter_jaccard])
    i += 1
print("list_filters", list_filters)'''

'''calcola score locali per ogni simple filter (edit e jaccard) per le entità prese da sopra e associa loro label 0/1'''
'''x = calculate_list_results(list_filters)
print("score filters result:", x)'''

'''applica le regressione sui risultati dati da calculate_list_results'''
'''regression(x)'''

'''print(build_json_simple_filter("Antwerp", "http://dbpedia.org/ontology/country", "edit distance", "http://dbpedia.org/resource/Belgium", "1", ">=", "0.5"))
list = [1, 2, 3, 4, 5]
import pickle
pickle.dump(list, open('list.pickle', 'w'))
pickle.load('list.pickle')'''

# select a single column as a Series
'''OAU_State = df['OAU State']
print(OAU_State)
print("---------------------")

# select a single column transforming the result into a list of string
OAU_State_list_string = df['OAU State'].tolist()
print(OAU_State_list_string)
capital_list_string = df['Capital'].tolist()
print(capital_list_string)

es_lookup = ESLookup()
results = es_lookup.multi_search(capital_list_string)
print("results", results)'''