'''Examples sparql wrapper'''

from SPARQLWrapper import SPARQLWrapper, JSON
from json_logic import jsonLogic
from json_logic import add_operation
import editdistance

sparql = SPARQLWrapper("http://dbpedia.org/sparql")

add_operation("edit_distance", editdistance.eval)

'''print(jsonLogic({"edit_distance" : ['bahama', 'banana']}))
print(jsonLogic({"edit_distance" : ['bahama', 'de']}))
print(jsonLogic({"edit_distance" : ['bahama', 'rear']}))
print(jsonLogic({"some" : [["banana", "de", "rear"], { "<=" : [{"edit_distance" : [{"var" : ""}, "bahama"]}, 2]}]}))
'''

y = """
    PREFIX dbo: <http://dbpedia.org/ontology/> SELECT ?object WHERE { <http://dbpedia.org/resource/Milan> dbo:country ?object. }
"""

y = """SELECT ?object WHERE { <http://dbpedia.org/resource/Milan> <http://dbpedia.org/ontology/country> ?object. }"""
print(y)
sparql.setQuery(y)
sparql.setReturnFormat(JSON)
results1 = sparql.query().convert()
print(results1)

for result in results1["results"]["bindings"]:
    print("result:", result)
    print("object:", result["object"])
    print("type:", result["object"]["type"])
    #print("xml:lang:", result["object"]["xml:lang"])
    print("value:", result["object"]["value"])
    if(result["object"]["value"] == "italy"): #dice se l'uri è uguale alla stringa, non lo è naturalmente, ma si possono comparare
        print('true')
    else:
        print('false')
    print('---------------------------')

x = """
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> SELECT ?label WHERE { <http://dbpedia.org/resource/Asturias> rdfs:label ?label. }
"""
print(x)
sparql.setQuery(x)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
print(results)

for result in results["results"]["bindings"]:
    print("result:", result)
    print("object:", result["object"])
    print("type:", result["object"]["type"])
    print("xml:lang:", result["object"]["xml:lang"])
    print("value:", result["object"]["value"])
    print('---------------------------')