'''
To build filters to use in jsonLogic
'''
import math

from simple_filter import *
from SPARQLWrapper import SPARQLWrapper, JSON
from json_logic import jsonLogic
from json_logic import add_operation
import json
from json_logic import jsonLogic
import distance
import editdistance
import jaccard_index
from jaccard_index.jaccard import jaccard_index
import pandas as pd

'''USEFUL FUNCTIONS'''

df=pd.read_csv("new_df_match2.csv")
def find_property(candidate, property):
    '''
    Given a candidate entity and a filter, it returns the results of a query sparql on the property and the value selected
    '''
    
    #sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    #print("candi", candidate)
    #print("prop", property)
    #query_string = "SELECT ?object WHERE { <" + candidate + "> <" + property + "> ?object. }"
    #sparql.setQuery(query_string)
    #sparql.setReturnFormat(JSON)
    #print("query", query_string)
    a=[]
    for i in df[df['product']==candidate][property]:
        a.append({ "object": { "type": "literal", "xml:lang": "en", "value": i }})
    results = { "head": { "link": [], "vars": ["object"] },     
  "results": { "distinct": False, "ordered": True, "bindings": a
     } }
    #results = df[df['product']==[candidate]][property]
    #print(results)
    #for result in results["results"]["bindings"]:
        #print("result:", result)
        #print("object:", result["object"])
        #print("type:", result["object"]["type"])
        #print("xml:lang:", result["object"]["xml:lang"])
        #print("value:", result["object"]["value"])
        #print("-----------------------------------")
    return results

def similarity_edit(s1, s2):
    '''Given 2 strings, it calculates the normalized edit distance (d) between them and later the similarity (s = 1-d)'''
    return 1 - (editdistance.eval(s1, s2) / max(len(s1), len(s2)))

'''Add normalized edit distance operation to jsonLogic'''
similarity_edit_distance = similarity_edit
add_operation("similarity_edit_distance", similarity_edit_distance)
#print(jsonLogic({"similarity_edit_distance" : ["banana", "bahama"]}))
#add_operation("edit_distance", editdistance.eval)

def similarity_jaccard(s1, s2):
    '''Given 2 strings, it calculates the jaccard similarity between them'''
    return jaccard_index(s1, s2)

'''Add jaccard similarity operation to jsonLogic'''
add_operation("similarity_jaccard", similarity_jaccard)

def similarity_equal(s1, s2):
    return s1 == s2

'''Add equal operation to jsonLogic'''
add_operation("similarity_equal", similarity_equal)


import re, math
from collections import Counter

WORD = re.compile(r'\w+')

def get_cosine(vec1, vec2):
    # print vec1, vec2
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def text_to_vector(text):
    return Counter(WORD.findall(text))

def cosine_similarity(a, b):
    a = text_to_vector(a.strip().lower())
    b = text_to_vector(b.strip().lower())

    return get_cosine(a, b)

from strsimpy.ngram import NGram

def trigram_similarity(a,b):
    trigrams=NGram(3)
    return (1-trigrams.distance(a,b))

def qgram_similarity(string1,string2):   
    score = 0
    for i in range(len(string1)-1):
        if string1[i:i+2] in string2:
             score += 1  
    for i in range(len(string2)-1):
        if string2[i:i+2] in string1:
             score += 1
    Final_Score = (score/2)/max(len(string1)-1,len(string2)-1)
    return Final_Score



#get_similarity('L & L AIR CONDITIONING', 'L & L AIR CONDITIONING Service') # returns 0.9258200997725514

'''Add equal operation to jsonLogic'''
add_operation("cosine_similarity", cosine_similarity)
add_operation("trigram_similarity", trigram_similarity)
add_operation("qgram_similarity", qgram_similarity)

def similarity_filter(simple_filter, list):
    '''
    Given a filter and a list of literals, it returns a tuple (True/False, best_score), where True/False depends on if
    the filter is satisfied, best_score is the best distance or similarity
    If operator by the user in filter == "edit distance" it calculates similarities using edit distance
    '''
    op = simple_filter.get_operator()
    print("OP", op)
    list_similarity = []
    filter = {}
    if simple_filter.get_operator() == "edit distance":
        filter = {"some" : [list, {simple_filter.get_threshold_operator() : [{"similarity_edit_distance" : [{"var" : ""}, simple_filter.get_value()]}, simple_filter.get_threshold()]}]}
        list_similarity = jsonLogic({"map": [list, {"similarity_edit_distance": [{"var": ""}, simple_filter.get_value()]}]})
    elif simple_filter.get_operator() == "jaccard":
        filter = {"some": [list, {simple_filter.get_threshold_operator(): [{"similarity_jaccard": [{"var": ""}, simple_filter.get_value()]}, simple_filter.get_threshold()]}]}
        list_similarity = jsonLogic({"map": [list, {"similarity_jaccard": [{"var": ""}, simple_filter.get_value()]}]})
    elif simple_filter.get_operator() == "==":
        filter = {"some": [list, {simple_filter.get_threshold_operator(): [{"similarity_equal": [{"var": ""}, simple_filter.get_value()]}, simple_filter.get_threshold()]}]}
        list_similarity = jsonLogic({"map": [list, {"similarity_equal": [{"var": ""}, simple_filter.get_value()]}]})
    elif simple_filter.get_operator() == "cosine similarity":
        filter = {"some": [list, {simple_filter.get_threshold_operator(): [{"cosine_similarity": [{"var": ""}, simple_filter.get_value()]}, simple_filter.get_threshold()]}]}
        list_similarity = jsonLogic({"map": [list, {"cosine_similarity": [{"var": ""}, simple_filter.get_value()]}]})
    elif simple_filter.get_operator() == "trigram similarity":
        filter = {"some": [list, {simple_filter.get_threshold_operator(): [{"trigram_similarity": [{"var": ""}, simple_filter.get_value()]}, simple_filter.get_threshold()]}]}
        list_similarity = jsonLogic({"map": [list, {"trigram_similarity": [{"var": ""}, simple_filter.get_value()]}]})
    elif simple_filter.get_operator() == "qgram similarity":
        filter = {"some": [list, {simple_filter.get_threshold_operator(): [{"qgram_similarity": [{"var": ""}, simple_filter.get_value()]}, simple_filter.get_threshold()]}]}
        list_similarity = jsonLogic({"map": [list, {"qgram_similarity": [{"var": ""}, simple_filter.get_value()]}]})
    else:
        filter = False
    print("LIIIIIIIIIISSSSSS", list)
    print("LLLLLLLLUUUUUUUUUUUEEEE", simple_filter.get_value())
    print("list similarity", list_similarity)
    if len(list_similarity) != 0:
        best_score = jsonLogic({"max": list_similarity})
    else:
        best_score = 0
    print("value", filter)
    print("best score", best_score)
    # TODO: if we want: define other filters for different similarities/distances and modify
    return [filter, best_score]


#TODO
def property_filter(candidate, simple_filter):
    '''
    Given a candidate entity and a filter, executes method property_filter_uri / property_filter_literal if value in
    simple_filter is an URI / literal

    If sparql query on the property gives as result res a literal -> direct check between res and simple_filter.get_value()
    using edit distance and its similarity
    If  sparql query on the property gives as result res an URI -> direct check between res and simple_filter.get_value()
    using "==", if it is different, calculates redfs:label and foaf:name on res as property and gives res2, check
    between res2 and simple_filter.get_value() using edit distance and its similarity

    LOCAL SCORE for each filter on a candidate entity
    0 if no matches
    simple_filter.get_weight() if URI == simple_filter.get_value() for at least one in res
    max(similarity_edit_distance) * simple_filter.get_weight() if list_uri empty, but list_literal not empty -> max is
    taken comparing elements in list_literal with simple_filter.get_value()
    '''
    list_uri = []
    list_literal = []
    value = simple_filter.get_value()
    results = find_property(candidate, simple_filter.get_property())
    print("CANDIDATE", candidate)
    #print("RES", results)
    for result in results["results"]["bindings"]:
        #print("TYPE", result["object"]["type"])
        if result["object"]["type"] == 'literal':
            list_literal.append(result["object"]["value"])
        elif result["object"]["type"] == 'uri':
            #print("CIAOCIAO")
            #print("res", result["object"]["value"])
            if result["object"]["value"] == simple_filter.get_value():
                #print("rrrrrrrrr")
                list_uri.append(result["object"]["value"])
                #print("list uri", list_uri)
            else:
                #print("qqqqqqqqqqqqqqq")
                x = find_property(result["object"]["value"], "http://www.w3.org/2000/01/rdf-schema#label")
                #print("x", x)
                y = find_property(result["object"]["value"], "http://xmlns.com/foaf/0.1/name")
                #print("y", y)
                for j in x["results"]["bindings"]:
                    if j["object"]["type"] == 'literal':
                        list_literal.append(j["object"]["value"])
                for k in y["results"]["bindings"]:
                    if k["object"]["type"] == 'literal':
                        list_literal.append(k["object"]["value"])
                #print("list_literal", list_literal)
    #print("list_uri_tot", list_uri)
    #print("list_literal_tot", list_literal)
    if len(list_uri) != 0:
        #print("SSSSSSSSSSS")
        res_return  = [True, 1 * simple_filter.get_weight(), simple_filter.get_weight()]
    elif len(list_literal) != 0:
        #print("wwwwwww", list_literal)
        filter_and_score = similarity_filter(simple_filter, list_literal)
        #print("q", filter_and_score[0])
        #print("r", filter_and_score[1])
        #print("j", jsonLogic(filter_and_score[0]))
        res_return = [jsonLogic(filter_and_score[0]), filter_and_score[1] * simple_filter.get_weight(), simple_filter.get_weight()]
        #print("QQQQQQQQ", res_return)
    else:
        res_return = [False, 0.0, simple_filter.get_weight()]
    print("RES", res_return)
    #print("----------------")
    return res_return



#TODO
def property_filter_learning(candidate, simple_filter):
    '''
    Same as property_filter, but the score is not multiplied by the weight of the filter
    -> use it for the active learning -> in method calculate_scores

    Given a candidate entity and a filter, executes method property_filter_uri / property_filter_literal if value in
    simple_filter is an URI / literal

    If sparql query on the property gives as result res a literal -> direct check between res and simple_filter.get_value()
    using edit distance and its similarity
    If  sparql query on the property gives as result res an URI -> direct check between res and simple_filter.get_value()
    using "==", if it is different, calculates redfs:label and foaf:name on res as property and gives res2, check
    between res2 and simple_filter.get_value() using edit distance and its similarity

    LOCAL SCORE for each filter on a candidate entity
    0 if no matches
    simple_filter.get_weight() if URI == simple_filter.get_value() for at least one in res
    max(similarity_edit_distance) * simple_filter.get_weight() if list_uri empty, but list_literal not empty -> max is
    taken comparing elements in list_literal with simple_filter.get_value()
    '''
    list_uri = []
    list_literal = []
    # value = simple_filter.get_value()
    results = find_property(candidate, simple_filter.get_property())
    # print("CANDIDATE", candidate)
    # print("RES", results)
    for result in results["results"]["bindings"]:
        # print("TYPE", result["object"]["type"])
        # if result["object"]["type"] == 'typed-literal':
        #    list_literal.append(result["object"]["value"])
        if result["object"]["type"] == 'literal':
            list_literal.append(result["object"]["value"])
        elif result["object"]["type"] == 'uri':
            # print("CIAOCIAO")
            # print("res", result["object"]["value"])
            if result["object"]["value"] == simple_filter.get_value():
                # print("rrrrrrrrr")
                list_uri.append(result["object"]["value"])
                # print("list uri", list_uri)
            else:
                # print("qqqqqqqqqqqqqqq")
                x = find_property(result["object"]["value"], "http://www.w3.org/2000/01/rdf-schema#label")
                # print("x", x)
                y = find_property(result["object"]["value"], "http://xmlns.com/foaf/0.1/name")
                # print("y", y)
                for j in x["results"]["bindings"]:
                    if j["object"]["type"] == 'literal':
                        list_literal.append(j["object"]["value"])
                for k in y["results"]["bindings"]:
                    if k["object"]["type"] == 'literal':
                        list_literal.append(k["object"]["value"])
                # print("list_literal", list_literal)
    # print("list_uri_tot", list_uri)
    # print("list_literal_tot", list_literal)
    if len(list_uri) != 0:
        # print("SSSSSSSSSSS")
        res_return = [True, 1, simple_filter.get_weight()]
    # elif len(list_literal) != 0:
    elif len(list_literal) != 0:
        # print("wwwwwww", list_literal)
        filter_and_score = similarity_filter(simple_filter, list_literal)
        # print("q", filter_and_score[0])
        # print("r", filter_and_score[1])
        # print("j", jsonLogic(filter_and_score[0]))
        res_return = [jsonLogic(filter_and_score[0]), filter_and_score[1], simple_filter.get_weight()]
    else:
        res_return = [False, 0.0, simple_filter.get_weight()]
    return res_return

def build_filter(json_simple_filter):
    '''
    Given a json simple filter, it returns the object simple filer of the class SimpleFilter
    '''
    return SimpleFilter(json_simple_filter["property"], json_simple_filter["operator"], json_simple_filter["value"],
                        json_simple_filter["threshold"], json_simple_filter["threshold_operator"], json_simple_filter["weight"])

def property_filter_json(candidate, json_filter):
    '''
    Given a candidate entity and a json simple filter, it returns the result of the property filter on it
    '''
    simple_filter = build_filter(json_filter)
    return property_filter(candidate, simple_filter)

# NB: PER OR E AND è NECESSARIO METTERE DOPPIA PARENTESI QUADRA PER COSTRUIRE IL FILTRO
#def or_operation(list_result):   # list_result = [(True, 0.8), (False, 0.6)...]
    '''
    Given a list of results of property filters, it returns the "OR" operation on them, which is always true and sums
    all the scores
    '''
    '''score = 0
    #print("LIST RES OR", list_result)
    for x in list_result:
        score += x[1]
    return [True, score]'''

#TODO
def or_operation(list_result):   # list_result = [(True, 0.8), (False, 0.6)...]
    '''
    Given a list of results of property filters, it returns the "OR" operation on them, which is always true, sums
    all the scores and sums all the weights
    '''
    score = 0
    sum_weights = 0
    #print("LIST RES OR", list_result)
    for x in list_result:
        score += x[1]
        sum_weights += x[2]
    return [True, score, sum_weights]

# NB: PER OR E AND è NECESSARIO METTERE DOPPIA PARENTESI QUADRA PER COSTRUIRE IL FILTRO
#def and_operation(list_result):   # list_result = [(True, 0.8), (False, 0.6)...]
    '''
    Given a list of results of property filters, it returns the "AND" operation on them, if they are all true
    it is true and the score is sum all the scores, otherwise it is false and the score is 0
    '''
    '''score = 0
    value = True
    #print("LIST RES AND", list_result)
    for x in list_result:
        if x[0] == False:
            value = False
            score = 0.0
            break  # immediately exit the loop
        else:
            score += x[1]
    return [value, score]'''

#TODO
def and_operation(list_result):   # list_result = [(True, 0.8), (False, 0.6)...]
    '''
    Given a list of results of property filters, it returns the "AND" operation on them, if they are all true
    it is true and the score is sum all the scores, otherwise it is false and the score is 0, it also sums all the
    weights
    '''
    score = 0
    sum_weights = 0
    value = True
    #print("LIST RES AND", list_result)
    for x in list_result:
        if x[0] == False:
            value = False
            score = 0.0
            sum_weights += x[2]
            #break  # immediately exit the loop
        else:
            score += x[1]
            sum_weights += x[2]
    return [value, score, sum_weights]

add_operation("property filter", property_filter_json)
add_operation("OR", or_operation)
add_operation("AND", and_operation)

'''FUNCTIONS FOR ACTIVE LEARNING'''

def build_simple_filter(df, column_value, property, operator, threshold, threshold_operator, weight):
    '''Given a Data Frame and the fields of a Simple Filter, it returns a list containing a single type of filter, that
    is created for each value to reconcile (es: State) in the table (es: CurrencyTable-entities.csv -> for each row)'''
    i = 0
    list_filters = []
    for x in df[column_value]:
        value = df.iloc[i][column_value]
        #print("===============value", value, "type", type(value))
        if pd.isnull(df.at[i, column_value]):
           #print("SSSSSSSSSSSSSSSSSSSS")
           simple_filter = SimpleFilter(property, operator, 'NO_FILTER', threshold, threshold_operator, weight)
        else:
            simple_filter = SimpleFilter(property, operator, value, threshold, threshold_operator, weight)
        list_filters.append(simple_filter)
        i += 1
    return list_filters

def zip_simple_filters(df, list_parameters):
    '''Given a Data Frame and a list of parameters to build different types of Simple Filter, it returns a list of
    tuples, each one referred to a single entity (row) to reconcile and containing all the different filters (es:
    single tuple = (filter_country, filter_language, filter_currency) for entity State to reconcile'''
    list_total_filters = []
    for x in list_parameters:
        y = build_simple_filter(df, x[0], x[1], x[2], x[3], x[4], x[5])
        list_total_filters.append(y)
    zip_lists = list(zip(*list_total_filters))
    return zip_lists

def calculate_scores(list_candidates, zip_list_simple_filters):
    '''Given a list of candidate entities (url) and a zip list of simple filters from zip_simple_filters, it returns a
    list of lists containing the scores of each filter for each candidate entity'''
    i = 0
    list_scores_total = []
    for candidate in list_candidates:
        list_filters = zip_list_simple_filters[i]
        list_scores = []
        #print("CANDIDATE", candidate)
        for simple_filter in list_filters:
            #print(simple_filter.get_property(), simple_filter.get_operator(), simple_filter.get_value(), simple_filter.get_threshold(), simple_filter.get_threshold_operator(), simple_filter.get_weight())
            if simple_filter.get_value() == 'NO_FILTER':
                score = 0
            else:
                score = property_filter_learning(candidate, simple_filter)[1]
                print("SCORE", score)
            list_scores.append(score)
        list_scores_total.append(list_scores)
        i += 1
    return list_scores_total

def calculate_scores_labels(df, column_candidates, list_parameters, column_labels):
    '''Given a dataframe, the name of the column of the candidate entities in df, the list of simple filters to apply on
    each candidate and the column of df containing the labels (0/1) for each candidate to say if it is
    incorrect/correct (lookup first entity first), it returns a list of lists of scores (as in calculate_scores) and a list of
    labels as in the corresponding column'''
    zip_list_simple_filters = zip_simple_filters(df, list_parameters)
    list_candidates = df[column_candidates].to_list()
    list_scores = calculate_scores(list_candidates, zip_list_simple_filters)
    list_labels = df[column_labels].to_list()
    return [list_scores, list_labels]




# SI PUO' LASCIARE SIMPLE FILTER E APPLICARE DIRETTAMENTE PROERTY_FILTER SU DI ESSI E NON USARE I DUE METODI SEGUENTI,
# INFATTI NON SONO USATI
def build_json_simple_filter(value_reconcile, simple_filter):
    '''Given a single value to reconcile and a Simple Filter, it returns the corresponding json simple filter (so the
    correspondent of build_simple_filter, but in json)'''
    json_simple_filter = """{\"""" + value_reconcile + """\" : [{"property filter" : [{"var" : "candidate"}, {"property" : \"""" + simple_filter.get_property() + """\", "operator" : \"""" + simple_filter.get_operator() + """\", "value" : \"""" + simple_filter.get_value() + """\", "threshold" : \"""" + str(simple_filter.get_threshold()) + """\", "threshold_operator" : \"""" + simple_filter.get_threshold_operator() + """\", "weight" : \"""" + str(simple_filter.get_weight()) + """\"}]}, 1]}"""
    return json_simple_filter

def build_list_json_simple_filter(list_value_reconcile, zip_list_simple_filters):
    '''Given a list of values to reconcile and a zip list of Simple Filter, it returns the corresponding zip list of
    json simple filters -> [(filter_country_1, filter_language_1, filter_currency_1), (filter_country_2,
    filter_language_2, filter_currency_2), ...] each tuple is for a different row -> [(json_filter_country_1,
    json_filter_language_1, json_filter_currency_1), (json_filter_country_2, json_filter_language_2,
    json_filter_currency_2), ...]'''
    i = 0
    list_total_filters = []
    for value_reconcile in list_value_reconcile:
        tuple_simple_filter = zip_list_simple_filters[i]
        list_json = []
        for simple_filter in tuple_simple_filter:
            json_simple_filter = build_json_simple_filter(value_reconcile, simple_filter)
            list_json.append(json_simple_filter)
        list_total_filters.append(list_json)
        i += 1
    return list_total_filters



#TODO loop su url e su list_total_filters per determinare score dei filtri e creare lista labels giuste
# (quella della tabella) per usare lista degli score dei filtri e lista delle labels per fare la regressione
# fare file pickle
# fare regression una classe
# test regressione ?
























'''NOT USEFUL FUNCTIONS'''

'''normalized_levenshtein = NormalizedLevenshtein()
add_operation("edit distance", normalized_levenshtein.distance)
print("nor dis", normalized_levenshtein.distance("banana", "bahama"))'''

# FORSE NON DA USARE
def loop_property_filter(dict_candidate, list_filter):
    '''
    Given the the dictionary of candidate entities for a single short-label and a list of filters for that short-label,
    it applies each filter chosen on each candidate entity and returns the dictionary updated with the results
    '''
    for filter in list_filter:
        for key in dict_candidate:
            x = dict_candidate[key]
            filter_and_score = property_filter(key, filter)
            x[0].append(filter_and_score)
            x[1].append(filter_and_score[0])
            x[2].append(filter_and_score[1])
    return dict_candidate

# FORSE NON DA USARE
def loop_property_filter_tot(dict_candidate_tot, dict_filter_tot):
    '''
    Given a dictionary with all the short-labels and their respective candidate entities (a dictionary of dictionaries)
    and a dictionary of all the filters for each short-label, it applies all the filters and updates the dictionary of
    candidate entities with the results
    '''
    for key in dict_filter_tot:
        #print(key)
        #print(dict_candidate_tot[key])
        #print(dict_filter_tot[key])
        loop_property_filter(dict_candidate_tot[key], dict_filter_tot[key])
    print("dict_candidate_tot:", dict_candidate_tot)
    return dict_candidate_tot

# questo non considera threshold
def dict_filter(simple_filter):
    '''
    Given a simple filter (SimpleFilter), it creates the related dictionary
    Probably it has to be changed, due to different types of filters (eg: label_filter)
    '''
    dict_filter = {}
    dict_filter[simple_filter.get_operator()] = [simple_filter.get_property_value(), simple_filter.get_value()]
    return dict_filter

def aggregate_filters(aggr_operator, list_filters):
    '''
    Given a list of simple/aggregate filters and an aggregate operator, it creates the related dictionary
    '''
    aggr_filter = {aggr_operator : list_filters}
    return aggr_filter

'''def evaluate_filter(filter):
   
   Given a filter written for jasonLogic, it returns the evaluation of it using jsonLogic (maybe useless)
   
   return jsonLogic(filter)'''

def filter_candidates(candidate_list, total_filter):
    '''
    Given the list of candidate entities for a single value and the filter that aggregates all the filters, it returns
    only the candidate entities which satisfy total_filter
    '''
    new_candidate_list = []
    for x in candidate_list:
        if jsonLogic(total_filter):
            new_candidate_list.append(x)
    return new_candidate_list

def label_filter(candidate, simple_filter):
    '''
    Given a candidate entity, tuple ("uri", list_labels), and a filter, it builds the jsonLogic filter that checks if
    at least one of the labels in list_labels is equal to the requested value (maybe it needs equalIgnoreCase..
    maybe it has to be changed)
    '''
    return {"some" : [candidate[1], {"==" : [{"var" : ""}, simple_filter.get_value()]}]}
    #candidate[1] could be substituted by simple_filter.get_property_value()

def threshold_filter(value, threshold, operator):
    '''
    Given a value, a threshold and an operator, it builds the related filter
    '''
    return {operator : [value, threshold]}

def calculate_similarity(e1, e2, s):
    '''
    Given 2 elements, it calculates the similarity between them, the computation depends on the type of similarity
    '''
    if s == 'edit distance':
        return editdistance.eval(e1, e2)
    elif s == 'jaccard':
        return distance.jaccard(e1, e2)
    # TODO: implement function, add stuff

'''def similarity_filter(simple_filter):
    Given a filter, it calculates the similarity required and bulits the filter jsonLogic to check the threshold
    sim = calculate_similarity(simple_filter.get_property_value(), simple_filter.get_value(), simple_filter.get_operator())
    return threshold_filter(sim, simple_filter.get_threshold(), simple_filter.get_threshold_operator())'''



'''Metodi sostituiti con property_filter sopra'''


# value: URI
def property_filter_uri(candidate, simple_filter):
    '''
    Given a single candidate entity ("uri", list_labels) and a filter where the value is an URI, it gives a tuple
    (true/false, score) where true/false depends on if the filter is respected and score is the weight of the filter
    '''
    list_filter = []
    value = simple_filter.get_value()
    results = find_property(candidate, simple_filter.get_property())
    for result in results["results"]["bindings"]:
        if result["object"]["type"] == 'uri':
            list_filter.append(result["object"]["value"])
    #print("list_filter:", list_filter)
    if(len(list_filter) != 0):
        filter = {"some": [list_filter, {"==": [{"var": ""}, value]}]}  # va bene mettere "==" per l'uri e non edit distance?
        #print(jsonLogic(filter))
        return (jsonLogic(filter), simple_filter.get_weight())
    else:
        return ("No matches", None)
#TODO decide about score: how ? Now score = filter_weight
#TODO decide about True/False/"No matches" and score

# value: literal
# print(editdistance.eval("milan", "Milan")) = 1 -> maiuscole e minuscole fanno diff nella edit distance
def property_filter_literal(candidate, simple_filter):
    '''
    Given a single candidate entity ("uri", list_labels) and a filter where the value is a literal, it gives a tuple
    (true/false, score) where true/false depends on if the filter is respected and score is the product between
    similarity (or distance) and weight of the filter
    '''
    #value = simple_filter.get_value()
    #threshold = simple_filter.get_threshold()
    results = find_property(candidate, simple_filter.get_property())
    list_literal = []
    list_uri = []
    results_uri = []
    list_literal_2 = []
    for result in results["results"]["bindings"]:
        if result["object"]["type"] == 'literal':
            list_literal.append(result["object"]["value"])
        elif result["object"]["type"] == 'uri':
            #list_uri.append(result["object"]["value"])
            x = find_property(result["object"]["value"], "http://www.w3.org/2000/01/rdf-schema#label")
            y = find_property(result["object"]["value"], "http://xmlns.com/foaf/0.1/name")
            for j in x["results"]["bindings"]:
                list_literal_2.append(j["object"]["value"])
            for k in y["results"]["bindings"]:
                list_literal_2.append(k["object"]["value"])
            '''results_uri.append(x)  # rdfs:label
            results_uri.append(y)  # foaf:name'''
    #print("list literal:", list_literal)
    #print("list uri:", list_uri)
    #filter_literal =  {"some" : [list_literal, {"<=" : [{"edit_distance" : [{"var" : ""}, value]}, threshold]}]}
    #print("filter literal:", jsonLogic(filter_literal))
    '''for y in results_uri:
        for j in y["results"]["bindings"]:
            list_literal_2.append(j["object"]["value"])'''
    #print("list literal 2:", list_literal_2)
    list_total = list_literal + list_literal_2
    #print("list total:", list_total)
    '''#filter_uri =  {"some" : [list_literal_2, {"<=" : [{"edit_distance" : [{"var" : ""}, value]}, threshold]}]}
    filter = {"some" : [list_total, {"<=": [{"edit_distance": [{"var": ""}, value]}, threshold]}]}
    list_editdistance = jsonLogic({"map" : [list_total, {"edit_distance": [{"var": ""}, value]}]})
    print("list editdistace:", list_editdistance)
    min_editdistance = jsonLogic({"min" : list_editdistance})
    print("editdistance min:", jsonLogic(min_editdistance))
    #print("filter uri:", jsonLogic(filter_uri))
    print("filter total:", jsonLogic(filter))
    print("score:", min_editdistance * simple_filter.get_weight())'''
    if(len(list_total) != 0):
        filter_and_score = similarity_filter(simple_filter, list_total)
        #print("filter and score[0]", filter_and_score[0])
        #print("jsonlogic", jsonLogic(filter_and_score[0]))
        #print("result", (jsonLogic(filter_and_score[0]), filter_and_score[1] * simple_filter.get_weight()))
        return (jsonLogic(filter_and_score[0]), filter_and_score[1] * simple_filter.get_weight())
    else:
        return ("No matches", None)
     # questo dipende da chi si sceglie come similarity/distance -> da valutare cosa fare

# OTHER OPTION !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# value: literal
# print(editdistance.eval("milan", "Milan")) = 1 -> maiuscole e minuscole fanno diff nella edit distance


'''Fine metodi sostituiti con property_filter sopra'''