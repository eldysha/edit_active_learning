'''
Class to evaluate filters given by the user (json) that have to be built as the ones in test_filter_evaluation
NB: what to remember to build the big json filter from the user (so that JSON logic works):
1) AND / OR -> 2 square brackets instead on only one as usual (maybe we can modify it)
2) property_filter needs 2 arguments in the square brackets: {"var" : "candidate"} and the simple property filter
{"property" : "--", "operator" : "--", "value" : "--", "threshold" : --, "threshold_operator" : "--", "weight" : --}
3) we need the total number of property filters passed by the user to combine them using AND, OR
'''

from candidate_selection.lookup import ESLookup
from filter_builder import *
import json

class Evaluation:

    def build_dict_candidate(self, results, key):
        ''''
        Given the results from lookup.multi_search and a label (key in the results), it returns a dictionary for a
        single label with keys the URIs of the candidate entities
        '''
        dict_candidate = {}
        for candidate in results[key]:
            #print("aaaaaaaaa", candidate)
            dict_candidate[candidate[0]] = [] #candidate[0] = 'http://dbpedia.org/resource/Milan'
        #print("sssssssssss", dict_candidate)
        #("WWWWWWWWWWWWWWW", dict_candidate)
        return dict_candidate
    # {'Milan': [('http://dbpedia.org/resource/Milan', ['milan', 'Milan']), ('http://dbpedia.org/resource/A.C._Milan', ['A.C._Milan', 'a.c._milan', 'a.c. milan', 'a. c. milan', 'A. C. Milan', 'A.C. Milan']), ('http://dbpedia.org/resource/MILAN', ['MILAN', 'milan']), ('http://dbpedia.org/resource/Milan,_Washington', ['Milan, Washington', 'Milan,_Washington', 'milan,_washington', 'milan, washington']), ('http://dbpedia.org/resource/Milan,_Wisconsin', ['milan,_wisconsin', 'Milan, Wisconsin', 'Milan,_Wisconsin', 'milan, wisconsin']), ('http://dbpedia.org/resource/Milan,_Indiana', ['Milan,_Indiana', 'milan, indiana', 'milan,_indiana', 'Milan, Indiana']), ('http://dbpedia.org/resource/Milan,_Illinois', ['Milan,_Illinois', 'Milan, Illinois', 'milan, illinois', 'milan,_illinois']), ('http://dbpedia.org/resource/Milan,_Tennessee', ['milan,_tennessee', 'Milan,_Tennessee', 'milan, tennessee', 'Milan, Tennessee']), ('http://dbpedia.org/resource/Milan,_Quebec', ['Milan, Quebec', 'milan,_quebec', 'milan, quebec', 'Milan,_Quebec']), ('http://dbpedia.org/resource/Milan,_Minnesota', ['milan, minnesota', 'Milan,_Minnesota', 'milan,_minnesota', 'Milan, Minnesota'])], 'Paris': [('http://dbpedia.org/resource/Paris_(Paris_album)', ['paris_(paris_album)', 'Paris (Paris album)', 'paris ( paris album)', 'Paris ( Paris album)', 'paris (paris album)', 'Paris_(Paris_album)']), ('http://dbpedia.org/resource/Paris–Brest–Paris', ['paris–brest–paris', 'paris– brest– paris', 'Paris–Brest–Paris', 'Paris– Brest– Paris']), ('http://dbpedia.org/resource/Paris–Bordeaux–Paris', ['paris–bordeaux–paris', 'Paris–Bordeaux–Paris', 'Paris– Bordeaux– Paris', 'paris– bordeaux– paris']), ('http://dbpedia.org/resource/Paris_(Paris_Hilton_album)', ['Paris (Paris Hilton album)', 'paris_(paris_hilton_album)', 'Paris_(Paris_Hilton_album)', 'Paris ( Paris Hilton album)', 'paris (paris hilton album)', 'paris ( paris hilton album)']), ('http://dbpedia.org/resource/Olympia_(Paris)', ['Olympia ( Paris)', 'Olympia (Paris)', 'olympia (paris)', 'Olympia_(Paris)', 'olympia_(paris)', 'olympia ( paris)']), ('http://dbpedia.org/resource/Salon_(Paris)', ['Salon (Paris)', 'salon (paris)', 'salon_(paris)', 'Salon_(Paris)', 'salon ( paris)', 'Salon ( Paris)']), ('http://dbpedia.org/resource/Paris-Plages', ['paris-plages', 'paris- plages', 'Paris- Plages', 'Paris-Plages']), ('http://dbpedia.org/resource/Europe/Paris', ['europe/paris', 'europe/ paris', 'Europe/Paris', 'Europe/ Paris']), ('http://dbpedia.org/resource/Christuskirche_(Paris)', ['Christuskirche ( Paris)', 'christuskirche ( paris)', 'christuskirche_(paris)', 'Christuskirche (Paris)', 'christuskirche (paris)', 'Christuskirche_(Paris)']), ('http://dbpedia.org/resource/Paris–Luxembourg', ['Paris–Luxembourg', 'paris–luxembourg', 'Paris– Luxembourg', 'paris– luxembourg'])]}
    # key = 'Milan' oppure 'Paris'

    def build_dict_candidate_tot(self, results):
        '''
        Given the results from lookup.multi_search, it returns a dictionary for all the labels with keys the labels and
        values the dictionaries from build_dict_candidate (so a dictionary of dictionaries)
        '''
        dict_candidate_tot = {}
        for key in results:
            #print("ww", key)
            dict_candidate_tot[key] = self.build_dict_candidate(results, key)
        #print("qqqqqqq", dict_candidate_tot)
        return dict_candidate_tot

    #def evaluate_filter(self, dict_candidate, aggregate_filter, number_simple_filters):
        '''
        Given a dictionary with keys the candidate entities for a single short label, an aggregate filter and the number
        of simple filters, it evaluates it and returns the candidate entities ordered by descending global score in a
        list
        '''
        #print("ZZZZZZZZZZz", dict_candidate)
        '''for key in dict_candidate:
            data = {"candidate" : key}
            #print("KEY", key)
            #print("DATA", data)
            x = jsonLogic(aggregate_filter, data)
            #print("X", x)
            # QUI MAGARI CAMBIARE TUTTE LE TUPLE IN LISTE PRIMA ANZICHE' FARE IL CAST
            #lst = list(x)
            #lst[1] = lst[1] / number_simple_filters
            #print("lis1", lst[1])
            #dict_candidate[key] = lst[1]
            x[1] = x[1] / number_simple_filters
            #print("AAAAAA", x[1])
            #print("KEYYYYYYYYY", key)
            dict_candidate[key] = x[1]
            #print("DICT_KeY", dict_candidate[key])
        #print("DICT", dict_candidate)
        #print(dict_candidate.items())
        sorted_candidates = sorted(dict_candidate.items(), key=lambda kv: kv[1], reverse = True)
        #print("SORTED", sorted_candidates)
        return sorted_candidates
'''
#TODO
    def evaluate_filter(self, dict_candidate, aggregate_filter):
        '''
        Given a dictionary with keys the candidate entities for a single short label, an aggregate filter and the number
        of simple filters, it evaluates it and returns the candidate entities ordered by descending global score in a
        list
        '''
        #print("ZZZZZZZZZZz", dict_candidate)
        for key in dict_candidate:
            data = {"candidate" : key}
            #print("KEY", key)
            #print("DATA", data)
            x = jsonLogic(aggregate_filter, data)
            print("X", x)
            # QUI MAGARI CAMBIARE TUTTE LE TUPLE IN LISTE PRIMA ANZICHE' FARE IL CAST
            #lst = list(x)
            #lst[1] = lst[1] / number_simple_filters
            #print("lis1", lst[1])
            #dict_candidate[key] = lst[1]
            #print("x0", x[0])
            #print("x1", x[1])
            #print("x2", x[2])
            x[1] = x[1] / x[2]
            #print("x1 agg", x[1])
            #print("AAAAAA", x[1])
            #print("KEYYYYYYYYY", key)
            dict_candidate[key] = x[1]
            #print("----------------")
            #print("DICT_KeY", dict_candidate[key])
        #print("DICT", dict_candidate)
        #print(dict_candidate.items())
        sorted_candidates = sorted(dict_candidate.items(), key=lambda kv: kv[1], reverse = True)
        #print("SORTED", sorted_candidates)
        print("------------")
        return sorted_candidates

    # DA FARE CON LISTA DI FILTRI (UNO PER OGNI SHORT LABEL)
    #def evaluate_filter_loop(self, dict_candidate_tot, dict_input_user):
        '''
        Given a dictionary with keys the short labels and values the dictionary of candidate entities for short labels,
        and the dictionary passed by the user with the entities to reconcile and the filters, it returns a dictionary
        with all the short labels as keys and values the candidate entities sorted by global score
        '''
        '''for key in dict_candidate_tot:
            #print("XXXXKEY", key)
            #print("EEEEEEEE", dict_candidate_tot[key])
            #print("QQQQQQ", dict_input_user[key][0])
            #print("RRRRRR", dict_input_user[key][1])
            print(key)
            print("SSSSSSSSSSSS", dict_input_user[key])
            print("SSSSSSSSSSSS", dict_input_user[key][0])
            dict_candidate_tot[key] = self.evaluate_filter(dict_candidate_tot[key], dict_input_user[key][0],
                                                           dict_input_user[key][1])
        return dict_candidate_tot'''

#TODO
    def evaluate_filter_loop(self, dict_candidate_tot, dict_input_user):
        '''
        Given a dictionary with keys the short labels and values the dictionary of candidate entities for short labels,
        and the dictionary passed by the user with the entities to reconcile and the filters, it returns a dictionary
        with all the short labels as keys and values the candidate entities sorted by global score
        '''
        for key in dict_candidate_tot:
            #print("XXXXKEY", key)
            #print("EEEEEEEE", dict_candidate_tot[key])
            #print("QQQQQQ", dict_input_user[key][0])
            #print("RRRRRR", dict_input_user[key][1])
            '''print(key)
            print("SSSSSSSSSSSS", dict_input_user[key])
            print("SSSSSSSSSSSS", dict_input_user[key][0])'''
            dict_candidate_tot[key] = self.evaluate_filter(dict_candidate_tot[key], dict_input_user[key][0])
        return dict_candidate_tot

    def create_list_labels(self, dict_input_user):
        """
        Given the dictionary from the user input, it returns the list of labels to search
        """
        list_labels = []
        for key in dict_input_user:
            list_labels.append(key)
        return list_labels

    def evaluate(self, json_input_user):
        """
        Given the json input from the user, it returns the candidates entities sorted by global score applying the
        property filters from the user
        """
        es_lookup = ESLookup()
        dict_input_user = json.loads(json_input_user)
        #print('dict_input_user', dict_input_user)
        list_labels = self.create_list_labels(dict_input_user)
        #print('list_labels', list_labels)
        result_candidates = es_lookup.multi_search(list_labels)
        #print('result_candidates', result_candidates)
        dict_candidate_tot = self.build_dict_candidate_tot(result_candidates)
        #print('dict_candidate_tot', dict_candidate_tot)
        sorted_candidates = self.evaluate_filter_loop(dict_candidate_tot, dict_input_user)
        #print('sorted_candidates', sorted_candidates)
        return sorted_candidates