import unittest
from filter_evaluation import *

'''
test_more_entities : labels to be search ("Milan", "Paris"), 3 simple filters for "Milan", 1 simple filter for "Paris",
                     AND and OR

test_single_entity1 : Only one label to be search ("Antwerp"), 3 simple filters, all AND, all properties satisfied with
                      similarity 1 only by 'http://dbpedia.org/resource/Antwerp'

test_single_entity2 : Only one label to be search ("Antwerp"), 1 simple filters, property satisfied with similarity 1
                     only by 'http://dbpedia.org/resource/Antwerp', sparql gives an uri for the property and it is the
                     case where we explore rdfs:label and foaf:name
                     value from user = Belgium
                     http://dbpedia.org/ontology/country = dbr:Belgium -> rdfs:label = Belgium
                     
test_no_matches : no matches because no entities with property dbo:region
'''

#TODO perché dà errore se run tutti insieme ?
class TestFilterBuilder(unittest.TestCase):

    def test_more_entities(self):
        evaluator = Evaluation()
        es_lookup = ESLookup()
        self.maxDiff = None
        json_input_user = """{"Milan" : [{"AND" : [[{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/country", "operator" : "==", "value" : "http://dbpedia.org/resource/Italy",
                                                           "threshold" : 1, "threshold_operator" : "==", "weight" : 0.8}]},
              {"OR" : [[{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/region", "operator" : "==", "value" : "http://dbpedia.org/resource/Lombardy",
                                                                    "threshold" : 1, "threshold_operator" : "==", "weight" : 0.7}]},
                       {"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/region", "operator" : "edit distance", "value" : "http://dbpedia.org/resource/Lombardy",
                                                                    "threshold" : 0.6, "threshold_operator" : ">=", "weight" : 0.6}]}]]
              }
             ]]}, 3], "Paris" : [{"OR" : [[{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/location", "operator" : "==", "value" : "http://dbpedia.org/resource/Luxembourg",
                                                           "threshold" : 1, "threshold_operator" : "==", "weight" : 0.8}]}]]}]}"""
        dict_input_user = json.loads(json_input_user)
        list_labels = evaluator.create_list_labels(dict_input_user)
        result_candidates = es_lookup.multi_search(list_labels)
        #self.assertEqual(list_labels, ["Milan", "Paris"])
        dict_candidate_tot = evaluator.build_dict_candidate_tot(result_candidates)
        #self.assertEqual(dict_candidate_tot, {"Milan": {'http://dbpedia.org/resource/Milan': [], 'http://dbpedia.org/resource/A.C._Milan': [],'http://dbpedia.org/resource/MILAN': [], 'http://dbpedia.org/resource/Milan,_Washington': [],'http://dbpedia.org/resource/Milan,_Wisconsin': [],'http://dbpedia.org/resource/Milan,_Indiana': [],'http://dbpedia.org/resource/Milan,_Illinois': [],'http://dbpedia.org/resource/Milan,_Tennessee': [],'http://dbpedia.org/resource/Milan,_Quebec': [],'http://dbpedia.org/resource/Milan,_Minnesota': []},"Paris": {'http://dbpedia.org/resource/Paris_(Paris_album)': [],'http://dbpedia.org/resource/Paris–Brest–Paris': [],'http://dbpedia.org/resource/Paris–Bordeaux–Paris': [],'http://dbpedia.org/resource/Paris_(Paris_Hilton_album)': [],'http://dbpedia.org/resource/Olympia_(Paris)': [],'http://dbpedia.org/resource/Salon_(Paris)': [], 'http://dbpedia.org/resource/Paris-Plages': [],'http://dbpedia.org/resource/Europe/Paris': [],'http://dbpedia.org/resource/Christuskirche_(Paris)': [],'http://dbpedia.org/resource/Paris–Luxembourg': []}})
        sorted_candidates = evaluator.evaluate_filter_loop(dict_candidate_tot, dict_input_user)
        print(sorted_candidates)
        self.assertEqual(sorted_candidates, {'Milan': [('http://dbpedia.org/resource/Milan', 1.0), ('http://dbpedia.org/resource/Milan,_Illinois', 0.05555555555555555), ('http://dbpedia.org/resource/A.C._Milan', 0.0), ('http://dbpedia.org/resource/MILAN', 0.0), ('http://dbpedia.org/resource/Milan,_Washington', 0.0), ('http://dbpedia.org/resource/Milan,_Wisconsin', 0.0), ('http://dbpedia.org/resource/Milan,_Indiana', 0.0), ('http://dbpedia.org/resource/Milan,_Tennessee', 0.0), ('http://dbpedia.org/resource/Milan,_Quebec', 0.0), ('http://dbpedia.org/resource/Milan,_Minnesota', 0.0)], 'Paris': [('http://dbpedia.org/resource/Paris–Luxembourg', 1.0), ('http://dbpedia.org/resource/Paris_(Paris_album)', 0.0), ('http://dbpedia.org/resource/Paris–Brest–Paris', 0.0), ('http://dbpedia.org/resource/Paris–Bordeaux–Paris', 0.0), ('http://dbpedia.org/resource/Paris_(Paris_Hilton_album)', 0.0), ('http://dbpedia.org/resource/Olympia_(Paris)', 0.0), ('http://dbpedia.org/resource/Salon_(Paris)', 0.0), ('http://dbpedia.org/resource/Paris-Plages', 0.0), ('http://dbpedia.org/resource/Europe/Paris', 0.0), ('http://dbpedia.org/resource/Christuskirche_(Paris)', 0.0)]})

    def test_single_entity1(self):
        evaluator = Evaluation()
        es_lookup = ESLookup()
        self.maxDiff = None
        json_input_user = """{"Antwerp" : [{"AND" : [[{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/country", "operator" : "==", "value" : "http://dbpedia.org/resource/Belgium",
                                                           "threshold" : 1, "threshold_operator" : "==", "weight" : 0.8}]},
              {"AND" : [[{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/property/east", "operator" : "==", "value" : "http://dbpedia.org/resource/Brasschaat",
                                                                    "threshold" : 1, "threshold_operator" : "==", "weight" : 0.7}]},
                       {"property filter" : [{"var" : "candidate"}, {"property" : "http://www.w3.org/2000/01/rdf-schema#label", "operator" : "edit distance", "value" : "Anversa",
                                                                    "threshold" : 0.6, "threshold_operator" : ">=", "weight" : 0.6}]}]]
              }
             ]]}]}"""
        dict_input_user = json.loads(json_input_user)
        list_labels = evaluator.create_list_labels(dict_input_user)
        result_candidates = es_lookup.multi_search(list_labels)
        self.assertEqual(list_labels, ["Antwerp"])
        dict_candidate_tot = evaluator.build_dict_candidate_tot(result_candidates)
        self.assertEqual(dict_candidate_tot, {'Antwerp': {'http://dbpedia.org/resource/Antwerp,_Ohio': [], 'http://dbpedia.org/resource/Antwerp': [], 'http://dbpedia.org/resource/Antwerp,_New_York': [], 'http://dbpedia.org/resource/Aquatopia_(Antwerp)': [], 'http://dbpedia.org/resource/Antwerp,_Victoria': [], 'http://dbpedia.org/resource/Antwerp_(district)': [], 'http://dbpedia.org/resource/Grote_Markt_(Antwerp)': [], 'http://dbpedia.org/resource/Meir,_Antwerp': [], 'http://dbpedia.org/resource/Antwerp_(province)': [], 'http://dbpedia.org/resource/Weert,_Antwerp': []}})
        sorted_candidates = evaluator.evaluate_filter_loop(dict_candidate_tot, dict_input_user)
        print(sorted_candidates)
        self.assertEqual(sorted_candidates, {'Antwerp': [('http://dbpedia.org/resource/Antwerp', 1.0), ('http://dbpedia.org/resource/Antwerp,_Ohio', 0.0), ('http://dbpedia.org/resource/Antwerp,_New_York', 0.0), ('http://dbpedia.org/resource/Aquatopia_(Antwerp)', 0.0), ('http://dbpedia.org/resource/Antwerp,_Victoria', 0.0), ('http://dbpedia.org/resource/Antwerp_(district)', 0.0), ('http://dbpedia.org/resource/Grote_Markt_(Antwerp)', 0.0), ('http://dbpedia.org/resource/Meir,_Antwerp', 0.0), ('http://dbpedia.org/resource/Antwerp_(province)', 0.0), ('http://dbpedia.org/resource/Weert,_Antwerp', 0.0)]})

    def test_single_entity2(self):
        evaluator = Evaluation()
        es_lookup = ESLookup()
        self.maxDiff = None
        json_input_user = """{"Antwerp" : [{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/country", "operator" : "==", "value" : "Belgium",
                                                           "threshold" : 1, "threshold_operator" : "==", "weight" : 0.8}]}]}"""
        dict_input_user = json.loads(json_input_user)
        list_labels = evaluator.create_list_labels(dict_input_user)
        result_candidates = es_lookup.multi_search(list_labels)
        #self.assertEqual(list_labels, ["Antwerp"])
        dict_candidate_tot = evaluator.build_dict_candidate_tot(result_candidates)
        #print("DICT CAND TOTAL", dict_candidate_tot)
        #self.assertEqual(dict_candidate_tot, {'Antwerp': {'http://dbpedia.org/resource/Antwerp,_Ohio': [], 'http://dbpedia.org/resource/Antwerp': [], 'http://dbpedia.org/resource/Antwerp,_New_York': [], 'http://dbpedia.org/resource/Aquatopia_(Antwerp)': [], 'http://dbpedia.org/resource/Antwerp,_Victoria': [], 'http://dbpedia.org/resource/Antwerp_(district)': [], 'http://dbpedia.org/resource/Grote_Markt_(Antwerp)': [], 'http://dbpedia.org/resource/Meir,_Antwerp': [], 'http://dbpedia.org/resource/Antwerp_(province)': [], 'http://dbpedia.org/resource/Weert,_Antwerp': []}})
        sorted_candidates = evaluator.evaluate_filter_loop(dict_candidate_tot, dict_input_user)
        #print("XXXXX", sorted_candidates)
        print(sorted_candidates)
        self.assertEqual(sorted_candidates, {'Antwerp': [('http://dbpedia.org/resource/Antwerp', 1.0), ('http://dbpedia.org/resource/Antwerp_(district)', 1.0), ('http://dbpedia.org/resource/Antwerp_(province)', 1.0), ('http://dbpedia.org/resource/Antwerp,_Ohio', 0.0), ('http://dbpedia.org/resource/Antwerp,_New_York', 0.0), ('http://dbpedia.org/resource/Aquatopia_(Antwerp)', 0.0), ('http://dbpedia.org/resource/Antwerp,_Victoria', 0.0), ('http://dbpedia.org/resource/Grote_Markt_(Antwerp)', 0.0), ('http://dbpedia.org/resource/Meir,_Antwerp', 0.0), ('http://dbpedia.org/resource/Weert,_Antwerp', 0.0)]})

    def test_single_entity3(self):
        evaluator = Evaluation()
        es_lookup = ESLookup()
        self.maxDiff = None
        json_input_user = """{"Algeria" : [{"OR" : [[{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/capital", "operator" : "edit distance", "value" : "Algiers", "threshold" : 0.5, "threshold_operator" : ">=", "weight" : 0.8}]},
                            {"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/language", "operator" : "edit distance", "value" : "Arabic", "threshold" : 0.5, "threshold_operator" : ">=", "weight" : 0.7}]},
                            {"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/currency", "operator" : "edit distance", "value" : "Dinar", "threshold" : 0.5, "threshold_operator" : ">=", "weight" : 0.6}]}]]}]}"""
        dict_input_user = json.loads(json_input_user)
        list_labels = evaluator.create_list_labels(dict_input_user)
        result_candidates = es_lookup.multi_search(list_labels)
        dict_candidate_tot = evaluator.build_dict_candidate_tot(result_candidates)
        # print("DICT CAND TOTAL", dict_candidate_tot)
        sorted_candidates = evaluator.evaluate_filter_loop(dict_candidate_tot, dict_input_user)
        # print("XXXXX", sorted_candidates)
        print(sorted_candidates)
        self.assertEqual(sorted_candidates, {'Algeria': [('http://dbpedia.org/resource/Algeria', 0.8163265306122448), ('http://dbpedia.org/resource/Hamri_(Algeria)', 0.0), ('http://dbpedia.org/resource/Liberté_(Algeria)', 0.0), ('http://dbpedia.org/resource/Algeria–Serbia_relations', 0.0), ('http://dbpedia.org/resource/Algeria–Kenya_relations', 0.0), ('http://dbpedia.org/resource/Algeria–Ukraine_relations', 0.0), ('http://dbpedia.org/resource/Algeria–Malaysia_relations', 0.0), ('http://dbpedia.org/resource/Algeria–Japan_relations', 0.0), ('http://dbpedia.org/resource/Algeria–Mexico_relations', 0.0), ('http://dbpedia.org/resource/Algeria–Cyprus_relations', 0.0)]})

    def test_no_matches(self):
        evaluator = Evaluation()
        es_lookup = ESLookup()
        self.maxDiff = None
        json_input_user = """{"Antwerp" : [{"property filter" : [{"var" : "candidate"}, {"property" : "http://dbpedia.org/ontology/region", "operator" : "==", "value" : "Belgium",
                                                                  "threshold" : 1, "threshold_operator" : "==", "weight" : 0.8}]}]}"""
        dict_input_user = json.loads(json_input_user)
        list_labels = evaluator.create_list_labels(dict_input_user)
        result_candidates = es_lookup.multi_search(list_labels)
        # self.assertEqual(list_labels, ["Antwerp"])
        dict_candidate_tot = evaluator.build_dict_candidate_tot(result_candidates)
        # print("DICT CAND TOTAL", dict_candidate_tot)
        # self.assertEqual(dict_candidate_tot, {'Antwerp': {'http://dbpedia.org/resource/Antwerp,_Ohio': [], 'http://dbpedia.org/resource/Antwerp': [], 'http://dbpedia.org/resource/Antwerp,_New_York': [], 'http://dbpedia.org/resource/Aquatopia_(Antwerp)': [], 'http://dbpedia.org/resource/Antwerp,_Victoria': [], 'http://dbpedia.org/resource/Antwerp_(district)': [], 'http://dbpedia.org/resource/Grote_Markt_(Antwerp)': [], 'http://dbpedia.org/resource/Meir,_Antwerp': [], 'http://dbpedia.org/resource/Antwerp_(province)': [], 'http://dbpedia.org/resource/Weert,_Antwerp': []}})
        sorted_candidates = evaluator.evaluate_filter_loop(dict_candidate_tot, dict_input_user)
        #print("QQQQ", sorted_candidates)
        print(sorted_candidates)
        self.assertEqual(sorted_candidates, {'Antwerp': [('http://dbpedia.org/resource/Antwerp,_Ohio', 0.0), ('http://dbpedia.org/resource/Antwerp', 0.0), ('http://dbpedia.org/resource/Antwerp,_New_York', 0.0), ('http://dbpedia.org/resource/Aquatopia_(Antwerp)', 0.0), ('http://dbpedia.org/resource/Antwerp,_Victoria', 0.0), ('http://dbpedia.org/resource/Antwerp_(district)', 0.0), ('http://dbpedia.org/resource/Grote_Markt_(Antwerp)', 0.0), ('http://dbpedia.org/resource/Meir,_Antwerp', 0.0), ('http://dbpedia.org/resource/Antwerp_(province)', 0.0), ('http://dbpedia.org/resource/Weert,_Antwerp', 0.0)]})

if __name__ == '__main__':
    unittest.main()
