'''
Examples of filters and related functions
'''

from filter_builder import *
from filter_evaluation import Evaluation
from candidate_selection.lookup import ESLookup
from regression import *

'''s1 = "French"
s2 = "Fula language"
print("ED", editdistance.eval('s1', 's2'))
print("SE", 1 - (editdistance.eval(s1, s2) / max(len(s1), len(s2))))'''
#print(jaccard_index("banana", "bahama"))
#print(jsonLogic({"similarity_jaccard" : ["banana", "bahama"]}))

#print(jsonLogic({}))
j = """{"Guinea" : [{"AND" : [[{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/capital", "operator" : "==", "value" : "Conakry", "threshold" : 0.5, "threshold_operator" : ">=", "weight" : 0.8}]},
                            {"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/language", "operator" : "==", "value" : "French", "threshold" : 0.5, "threshold_operator" : ">=", "weight" : 0.7}]},
                            {"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/currency", "operator" : "edit distance", "value" : "Guinean franc", "threshold" : 0.5, "threshold_operator" : ">=", "weight" : 0.6}]}]]}]}"""

evaluator = Evaluation()
print(evaluator.evaluate(j))

'''json_input_user = """{"Antwerp" : [{"AND" : [[{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/country", "operator" : "==", "value" : "http://dbpedia.org/resource/Belgium",
                                                           "threshold" : 1, "threshold_operator" : "==", "weight" : 0.8}]},
              {"AND" : [[{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/property/east", "operator" : "==", "value" : "http://dbpedia.org/resource/Brasschaat",
                                                                    "threshold" : 1, "threshold_operator" : "==", "weight" : 0.7}]},
                       {"property filter" : [{"var" : "candidate"}, {"property" : "http://www.w3.org/2000/01/rdf-schema#label", "operator" : "jaccard", "value" : "Anversa",
                                                                    "threshold" : 0.6, "threshold_operator" : ">=", "weight" : 0.6}]}]]
              }
             ]]}]}"""'''

'''json_input_user1 = """{"Milan" : [{"AND" : [[{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/country", "operator" : "==", "value" : "http://dbpedia.org/resource/Italy",
                                                           "threshold" : 1, "threshold_operator" : "==", "weight" : 0.8}]},
              {"OR" : [[{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/region", "operator" : "==", "value" : "Lombardy",
                                                                    "threshold" : 1, "threshold_operator" : "==", "weight" : 0.7}]},
                       {"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/region", "operator" : "edit distance", "value" : "http://dbpedia.org/resource/Lombardy",
                                                                    "threshold" : 0.6, "threshold_operator" : ">=", "weight" : 0.6}]}]]
              }
             ]]}]}"""'''

#print(evaluator.evaluate(json_input_user1))

#print(evaluator.evaluate(json_input_user))
#output = json.loads(json_input_user)
#print("OUTPUT", output)

'''json_input_user1 = """{"Milan" : [{"AND" : [[{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/country", "operator" : "edit distance", "value" : "http://dbpedia.org/resource/Italy",
                                                           "threshold" : 1, "threshold_operator" : "==", "weight" : 0.8}]},
              {"OR" : [[{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/region", "operator" : "==", "value" : "http://dbpedia.org/resource/Lombardy",
                                                                    "threshold" : 1, "threshold_operator" : "==", "weight" : 0.7}]},
                       {"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/region", "operator" : "edit distance", "value" : "http://dbpedia.org/resource/Lombardy",
                                                                    "threshold" : 0.6, "threshold_operator" : ">=", "weight" : 0.6}]}]]
              }
             ]]}, 3]}"""'''
#output1 = json.loads(json_input_user1)
#print("OUTPUT", output1)

filter = SimpleFilter("http://dbpedia.org/ontology/country", "==", "Belgium", 1, "==", 0.8)
#print(property_filter("http://dbpedia.org/resource/Antwerp", filter))

#simple_filter = SimpleFilter("http://dbpedia.org/ontology/wikiPageExternalLink", "edit distance", "http://www.visitantwerp.be/", 0.6, ">=", 0.6)
#print(property_filter("http://dbpedia.org/resource/Antwerp", simple_filter))

#simple_filter1 = SimpleFilter("http://dbpedia.org/ontology/wikiPageRevisionID", "edit distance", "744641987 ", 0.6, ">=", 0.6) #TYPED LITERAL
#print(property_filter("http://dbpedia.org/resource/Antwerp", simple_filter1))

#simple_filter2 = SimpleFilter("http://dbpedia.org/property/arms", "==", "Wapenantwerpen.jpg", 0.6, ">=", 0.6) #TYPED LITERAL
#print(property_filter("http://dbpedia.org/resource/Antwerp", simple_filter2))

es_lookup = ESLookup()
#print(es_lookup.multi_search(["http://dbpedia.org/resource/Milan"]))

json_input_user = """{"Milan" : [{"AND" : [[{"property filter" : [{"var" : "candidate"}, {"var" : "list_scores"}, {"property" : "http://dbpedia.org/ontology/country", "operator" : "==", "value" : "http://dbpedia.org/resource/Italy",
                                                           "threshold" : 1, "threshold_operator" : "==", "weight" : 0.8}]},
              {"OR" : [[{"property filter" : [{"var" : "candidate"}, {"var" : "list_scores"}, {"property" : "http://dbpedia.org/ontology/region", "operator" : "==", "value" : "http://dbpedia.org/resource/Lombardy",
                                                                    "threshold" : 1, "threshold_operator" : "==", "weight" : 0.7}]},
                       {"property filter" : [{"var" : "candidate"}, {"var" : "list_scores"}, {"property" : "http://dbpedia.org/ontology/region", "operator" : "edit distance", "value" : "http://dbpedia.org/resource/Lombardy",
                                                                    "threshold" : 0.6, "threshold_operator" : ">=", "weight" : 0.6}]}]]
              }
             ]]}, 3], "Paris" : [{"OR" : [[{"property filter" : [{"var" : "candidate"}, {"var" : "list_scores"}, {"property" : "http://dbpedia.org/ontology/location", "operator" : "==", "value" : "http://dbpedia.org/resource/Luxembourg",
                                                           "threshold" : 1, "threshold_operator" : "==", "weight" : 0.8}]}]]}, 1]}"""

json_input_user_0 = """{"Milan" : [{"AND" : [[{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/country", "operator" : "==", "value" : "http://dbpedia.org/resource/Italy",
                                                           "threshold" : 1, "threshold_operator" : "==", "weight" : 0.8}]},
              {"OR" : [[{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/region", "operator" : "==", "value" : "http://dbpedia.org/resource/Lombardy",
                                                                    "threshold" : 1, "threshold_operator" : "==", "weight" : 0.7}]},
                       {"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/region", "operator" : "jaccard", "value" : "http://dbpedia.org/resource/Lombardy",
                                                                    "threshold" : 0.6, "threshold_operator" : ">=", "weight" : 0.6}]}]]
              }
             ]]}, 3], "Paris" : [{"OR" : [[{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/location", "operator" : "==", "value" : "http://dbpedia.org/resource/Luxembourg",
                                                           "threshold" : 1, "threshold_operator" : "==", "weight" : 0.8}]}]]}, 1]}"""

json_input_user1 = """{"Antwerp" : [{"AND" : [[{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/country", "operator" : "==", "value" : "http://dbpedia.org/resource/Belgium",
                                                           "threshold" : 1, "threshold_operator" : "==", "weight" : 0.8}]},
              {"OR" : [[{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/property/east", "operator" : "==", "value" : "http://dbpedia.org/resource/Brasschaat",
                                                                    "threshold" : 1, "threshold_operator" : "==", "weight" : 0.7}]},
                       {"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/campus", "operator" : "edit distance", "value" : "http://dbpedia.org/resource/Katholieke_Universiteit_Leuven",
                                                                    "threshold" : 0.6, "threshold_operator" : ">=", "weight" : 0.6}]}]]
              }
             ]]}, 3]}"""

json_input_user2 = """{"Antwerp" : [{"OR" : [[{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/country", "operator" : "==", "value" : "http://dbpedia.org/resource/Belgium",
                                                           "threshold" : 1, "threshold_operator" : "==", "weight" : 0.8}]}]]}, 1]}"""

json_input_user3 = """{"Antwerp" : [{"OR" : [[{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/property/east", "operator" : "==", "value" : "http://dbpedia.org/resource/Brasschaat",
                                                                    "threshold" : 1, "threshold_operator" : "==", "weight" : 0.7}]},
                       {"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/campus", "operator" : "edit distance", "value" : "http://dbpedia.org/resource/Katholieke_Universiteit_Leuven",
                                                                    "threshold" : 0.6, "threshold_operator" : ">=", "weight" : 0.6}]}]]
                        }, 2]}"""

json_input_user4 = """{"Antwerp" : [{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/property/east", "operator" : "==", "value" : "http://dbpedia.org/resource/Brasschaat",
                                                                    "threshold" : 1, "threshold_operator" : "==", "weight" : 0.7}]}, 1]}"""

json_input_user5 = """{"Antwerp" : [{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/campus_of", "operator" : "edit distance", "value" : "http://dbpedia.org/resource/Katholieke_Universiteit_Leuven",
                                                                    "threshold" : 0.6, "threshold_operator" : ">=", "weight" : 0.6}]}, 1]}"""

evaluator = Evaluation()
#print("CIAOOOOOOOOOOOOOOO", evaluator.evaluate(json_input_user))
#print(evaluator.evaluate(json_input_user5))
f1_e = """{"Antwerp" : [{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/country", "operator" : "edit distance", "value" : "Belgium",
                                                                  "threshold" : 1, "threshold_operator" : "==", "weight" : 0.8}]}, 1]}"""
f1_j = """{"Antwerp" : [{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/country", "operator" : "jaccard", "value" : "Belgium",
                                                                  "threshold" : 1, "threshold_operator" : "==", "weight" : 0.8}]}, 1]}"""
f2_e = """{"Antwerp" : [{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/country", "operator" : "edit distance", "value" : "http://dbpedia.org/resource/Belgium",
                                                           "threshold" : 1, "threshold_operator" : "==", "weight" : 0.8}]}, 1]}"""
f2_j = """{"Antwerp" : [{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/country", "operator" : "jaccard", "value" : "http://dbpedia.org/resource/Belgium",
                                                           "threshold" : 1, "threshold_operator" : "==", "weight" : 0.8}]}, 1]}"""
f3_e = """{"Milan" : [{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/country", "operator" : "edit distance", "value" : "http://dbpedia.org/resource/Italy",
                                                           "threshold" : 1, "threshold_operator" : "==", "weight" : 0.8}]}, 1]}"""
f3_j = """{"Milan" : [{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/country", "operator" : "jaccard", "value" : "http://dbpedia.org/resource/Italy",
                                                           "threshold" : 1, "threshold_operator" : "==", "weight" : 0.8}]}, 1]}"""

f_ant_1 = """{"Antwerp" : [{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/country", "operator" : "edit distance", "value" : "Belgium",
                                                                  "threshold" : 1, "threshold_operator" : "==", "weight" : 0.8}]}, 1]}"""
f_ant_2 = """{"Antwerp" : [{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/mayor", "operator" : "edit distance", "value" : "Bart De Wever",
                                                                  "threshold" : 1, "threshold_operator" : "==", "weight" : 0.8}]}, 1]}"""
f_mil_1 = """{"Milan" : [{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/country", "operator" : "jaccard", "value" : "http://dbpedia.org/resource/Italy",
                                                           "threshold" : 1, "threshold_operator" : "==", "weight" : 0.8}]}, 1]}"""
f_mil_2 = """{"Milan" : [{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/leaderName", "operator" : "jaccard", "value" : "http://dbpedia.org/resource/Giuseppe_Sala",
                                                           "threshold" : 1, "threshold_operator" : "==", "weight" : 0.8}]}, 1]}"""


list = [[f_ant_1 , f_ant_2], [f_mil_1, f_mil_2]]
#x = calculate_list_results(list)
#print(x)
'''regression(x)'''


y = {"property" : "http://dbpedia.org/ontology/country", "operator" : "==", "value" : "http://dbpedia.org/resource/Italy",
                                                           "threshold" : 1, "threshold_operator" : "==", "weight" : 0.8}

'''x = build_filter({"property" : "http://dbpedia.org/ontology/country", "operator" : "==", "value" : "http://dbpedia.org/resource/Italy",
                                                           "threshold" : 1, "threshold_operator" : "==", "weight" : 0.8})
print(x.get_property())
print(x.get_operator())
print(x.get_value())
print(x.get_threshold())
print(x.get_threshold_operator())
print(x.get_weight())'''

'''print("EEEEEEE:", property_filter_json("http://dbpedia.org/resource/Milan", {"property" : "http://dbpedia.org/ontology/country", "operator" : "==", "value" : "http://dbpedia.org/resource/Italy",
                                                           "threshold" : 1, "threshold_operator" : "==", "weight" : 0.8}))'''

'''and_operation([(True, 0.8), (False, 0.2)])
#print("AND:", and_operation([True, True, False]))
print("OR:", jsonLogic({"OR" : [[(True, 8), (True, 6), (False, 2)]]}))
print("AND", jsonLogic({"AND" : [[(True, 8), (True, 6), (True, 2)]]}))
print("res:", jsonLogic({"AND" : [[{"OR" : [[(True, 8), (True, 6)]]}, (False, 2)]]}))'''


# examples using single/multi search, property_filter_literal/uri
# NB atm change "return" of method property_filter if you use literal/uri






aggregate_filter_1 = {"AND" : [[{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/country", "operator" : "==", "value" : "http://dbpedia.org/resource/Italy",
                                                           "threshold" : 1, "threshold_operator" : "==", "weight" : 0.8}]},
              {"OR" : [[{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/region", "operator" : "==", "value" : "http://dbpedia.org/resource/Lombardy",
                                                                    "threshold" : 1, "threshold_operator" : "==", "weight" : 0.7}]},
                       {"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/region", "operator" : "edit distance", "value" : "http://dbpedia.org/resource/Lombardy",
                                                                    "threshold" : 0.6, "threshold_operator" : ">=", "weight" : 0.6}]}]]
              }
             ]]}

aggregate_filter_2 = {"OR" : [[{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/location", "operator" : "==", "value" : "http://dbpedia.org/resource/Luxembourg",
                                                           "threshold" : 1, "threshold_operator" : "==", "weight" : 0.8}]}]]}

#dict_input_user = {"Milan" : [aggregate_filter_1, 3]}
json_input2 = """{"AND" : [[{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/country", "operator" : "==", "value" : "http://dbpedia.org/resource/Italy",
                                                           "threshold" : 1, "threshold_operator" : "==", "weight" : 0.8}]},
              {"OR" : [[{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/region", "operator" : "==", "value" : "http://dbpedia.org/resource/Lombardy",
                                                                    "threshold" : 1, "threshold_operator" : "==", "weight" : 0.7}]},
                       {"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/region", "operator" : "edit distance", "value" : "http://dbpedia.org/resource/Lombardy",
                                                                    "threshold" : 0.6, "threshold_operator" : ">=", "weight" : 0.6}]}]]
              }
             ]]}"""

#json_input1 = '{"Milan" : [1]}'
#dict_input_user1 = {"Milan" : [aggregate_filter_1, 3], "Paris" : [aggregate_filter_2, 1]}


'''xp = es_lookup.multi_search(['Milan', 'Paris'])
print(xp)
dict_candidate_tot = build_dict_candidate_tot(xp)
print(dict_candidate_tot)
print(evaluate_filter_loop(dict_candidate_tot, dict_input_user))'''
#print("ECCOLO", evaluate(json_input_user))







#xp = es_lookup.search("Milan")
'''xp = es_lookup.multi_search(['Milan', 'Paris'])
print(xp)
xd = build_dict_candidate_tot(xp)
print(xd)
xs = build_dict_candidate(xp, 'Milan')
print("XS", xs)
print("---------------------")
'''
# filter literal
#filter5 = SimpleFilter("http://dbpedia.org/ontology/country", "edit distance", "Italy", 0.3, "<=", 0.8)
filter5 = SimpleFilter("http://dbpedia.org/ontology/country", "edit distance", "Italy", 0.6, ">=", 0.8)
#dict_filter_tot = {'Milan': [filter5]}

# filters uri
filter6 = SimpleFilter("http://dbpedia.org/ontology/country", "==", "http://dbpedia.org/resource/Italy", 1, "==", 0.8)
filter7 = SimpleFilter("http://dbpedia.org/ontology/region", "==", "http://dbpedia.org/resource/Lombardy", 1, "==", 0.7)
filter8 = SimpleFilter("http://dbpedia.org/ontology/country", "==", "http://dbpedia.org/resource/France", 1, "==", 0.8)
dict_filter_tot = {'Milan': [filter6, filter7], 'Paris': [filter8]}

#loop_property_filter_tot(xd, dict_filter_tot)










'''print("----------------------------------------------------------------------------")
print("OR:", jsonLogic({"OR" : [[(True, 8), (True, 6), (False, 2)]]}))
print("AND", jsonLogic({"AND" : [[(True, 8), (False, 6), (True, 2)]]}))
print("CIAO")
print("----------------------------------------------------------------------------")'''







'''data = {"candidate" : "http://dbpedia.org/resource/Milan"}
x = jsonLogic({"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/country", "operator" : "==", "value" : "http://dbpedia.org/resource/Italy",
                                                           "threshold" : 1, "threshold_operator" : "==", "weight" : 0.8}]}, data)
q = jsonLogic({"AND" : [[{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/country", "operator" : "==", "value" : "http://dbpedia.org/resource/Ita",
                                                           "threshold" : 1, "threshold_operator" : "==", "weight" : 0.8}]},
              {"OR" : [[{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/region", "operator" : "==", "value" : "http://dbpedia.org/resource/Lombardy",
                                                                    "threshold" : 1, "threshold_operator" : "==", "weight" : 0.7}]},
                       {"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/region", "operator" : "edit distance", "value" : "http://dbpedia.org/resource/Lombardy",
                                                                    "threshold" : 0.6, "threshold_operator" : ">=", "weight" : 0.6}]}]]
              }
             ]]
   }, data)

print("Q", q)'''

#print("X", x)

print("-----------------------------------------------------------------------------------------------------------")






'''print(evaluate_filter(xs, {"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/country", "operator" : "==", "value" : "http://dbpedia.org/resource/Italy",
                                                           "threshold" : 1, "threshold_operator" : "==", "weight" : 0.8}]}))
'''

'''print(evaluate_filter(xs, {"AND" : [[{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/country", "operator" : "==", "value" : "http://dbpedia.org/resource/Italy",
                                                           "threshold" : 1, "threshold_operator" : "==", "weight" : 0.8}]},
              {"OR" : [[{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/region", "operator" : "==", "value" : "http://dbpedia.org/resource/Lombardy",
                                                                    "threshold" : 1, "threshold_operator" : "==", "weight" : 0.7}]},
                       {"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/region", "operator" : "edit distance", "value" : "http://dbpedia.org/resource/Lombardy",
                                                                    "threshold" : 0.6, "threshold_operator" : ">=", "weight" : 0.6}]}]]
              }
             ]]}
    , 3))'''

print("----------------------------------------------------------------------------------")








'''# examples using simple and aggregate filters
simple_filter1 = SimpleFilter("Milan", "==", "Milan", None, None, None)
simple_filter2 = SimpleFilter("Paris", "==", "Paris", None, None, None)

dict_filter1 = dict_filter(simple_filter1)
dict_filter2 = dict_filter(simple_filter2)
print("dict_filter1:", dict_filter1)
print("dict_filter2:", dict_filter2)
print('----------------')

list_dict_filter = [dict_filter1, dict_filter2]
print("list_dict_filter:", list_dict_filter)
print('----------------')

x = aggregate_filters("and", list_dict_filter)
print(x)
print("evaluate_filter(x):", evaluate_filter(x))
print('----------------')

simple_filter3  = SimpleFilter("Luanda", "==", "uanda", None, None, None)
dict_filter3 = dict_filter(simple_filter3)
print("dict_filter3:", dict_filter3)
list_dict_filter = [x, dict_filter3]
y = aggregate_filters("and", list_dict_filter)
print("y:", y)
print("evaluate_filter(y):", evaluate_filter(y))
print('----------------')

z = aggregate_filters("or", [x, y, {"==" : [1, 1]}])
print(z)
print("evaluate_filter(z):", evaluate_filter(z))
print('----------------')

# example label_filter
candidate = ["uri", ["milan", "Milan"]]
filter = SimpleFilter("prop", "==", "milan", None, None, None)
filter1 = label_filter(candidate, filter)
data1 = None # forse non è necessario in questo caso (?)
print("filter1:", filter1)
print("jsonLogic:", jsonLogic(filter1, data1))
print('----------------')

# example threshold_filter
filter2 = threshold_filter(10, 7, ">")
print("filter2:", filter2)
print("jsonLogic:", jsonLogic(filter2))
print('----------------')

# examples similarities strings
print("edit distance: Milan, Milan_Italy:", editdistance.eval("Milan", "Milan_Italy"))
print("jaccard similarity: Milan, Milan_Italy:", distance.jaccard("Milan", "Milan_Italy"))
print('----------------')'''

'''# example similarity filter jaccard
filter3 = SimpleFilter("Milan", 'jaccard', "Milano", 0.8, ">=", None)
filter_similarity3 = similarity_filter(filter3)
print(filter_similarity3)
print("jsonLogic:", jsonLogic(filter_similarity3))
print('----------------')'''

'''# example similarity filter edit distance
filter4 = SimpleFilter("Milan", 'edit distance', "Milano", 3, "<=", None)
filter_similarity4 = similarity_filter(filter4)
print(filter_similarity4)
print("jsonLogic:", jsonLogic(filter_similarity4))
print('----------------')'''

'''
# examples find_property
# NB: per rdfs schema: NO / prima di label, solo #
q = find_property("http://dbpedia.org/resource/Milan", "http://www.w3.org/2000/01/rdf-schema#label")
print("________________________________________________________________________________________________________")
r = find_property("http://dbpedia.org/resource/Milan", "http://dbpedia.org/ontology/country")
print("________________________________________________________________________________________________________")
find_property("http://dbpedia.org/resource/Milan", "http://dbpedia.org/ontology/areaTotal")
print("________________________________________________________________________________________________________")
find_property("http://dbpedia.org/resource/Milan", "http://dbpedia.org/property/en")
print("________________________________________________________________________________________________________")
print('----------------')
'''
'''
# example property_filter_literal
filter5 = SimpleFilter("http://dbpedia.org/ontology/country", "edit distance", "Italy", 0.3, "<=", 0.8)
print(property_filter_literal("http://dbpedia.org/resource/Milan", filter5))
print('----------------')
'''
'''
# example property_filter_uri
filter6 = SimpleFilter("http://dbpedia.org/ontology/country", "==", "http://dbpedia.org/resource/Italy", 3, "<=", 0.8)
x = property_filter_uri("http://dbpedia.org/resource/Milan", filter6)
print(x)
print(x[0])
print(x[1])
'''

# Random examples
'''
print("RRRRRRRR", jsonLogic({"or": [True, False, True]}))'''

'''print(jsonLogic({"map" : [["banana", "bahama", "badada"], {"edit_distance": [{"var": ""}, "banana"]}]}))

list_editdistance = jsonLogic({"map": [list, {"edit_distance": [{"var": ""}, "italy"]}]})
print("list_editdistance:", list_editdistance)

list = ['Italy', 'إيطاليا', 'Italien', 'Italia', 'Italie', 'Italia', 'イタリア', 'Italië', 'Włochy', 'Itália', 'Италия', '意大利', 'Italy']
filterq = SimpleFilter("<http://dbpedia.org/ontology/country>", "edit distance", "Italy", 3, "<=", 0.8)
qqqqqq = similarity_filter(filterq, list)
print("qqqqqqqqq", qqqqqq)

# example 
s1 = "banana"
s2 = "bahama"
print("similarity edit distance normalized:", jsonLogic({"similarity_edit_distance" : ["banana", "bahama"]}))
print("normalized edit distance:", (editdistance.eval(s1, s2) / max(len(s1), len(s2))))

# not used
normalized_levenshtein = NormalizedLevenshtein()
add_operation("edit distance", normalized_levenshtein.distance)
print("nor dis", normalized_levenshtein.distance("banana", "bahama"))'''