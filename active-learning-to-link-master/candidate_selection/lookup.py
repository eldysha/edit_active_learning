from elasticsearch import Elasticsearch, TransportError
from elasticsearch_dsl import Search, Q

from candidate_selection import CandidateSelector


class SimpleLookup(CandidateSelector):
    """
    A lookup that uses only a single label
    """
    def _get_candidates(self, labels):
        """
        Actual lookup method. Must be implemented by all the subclasses
        :param labels:
        :return:
        """
        raise NotImplementedError

    def _multi_search(self, labels):
        """
        Helper method that lookups for several sub-labels of a label, and aggregates the results
        :param labels:
        :return:
        """
        to_compute = self._get_short_labels_set(labels)
        results_dict = dict(list(self._get_candidates(to_compute)))
        '''result_list = list(self._get_candidates(to_compute)) #   qui
        print("RES LIST", result_list) #   qui'''
        results = []
        for label in labels:  # aggregate results for short labels
            label_candidates = []
            for short_label in self._get_short_labels(label):
                if results_dict[short_label] not in label_candidates: # remove duplicates
                    label_candidates = label_candidates + results_dict[short_label]
            results.append((label, label_candidates))

        return results

    def multi_search(self, labels):
        """
        Return a set of candidate for each given label
        :param labels:
        :return:
        """
        return dict(self._multi_search(labels))

    def search(self, label):
        """
        Return a set of candidate for the given label
        :param label:
        :return:
        """
        return self.multi_search([label])


class ESLookup(SimpleLookup):
    """
    A lookup class based on ES
    """
    def __init__(self, config='ES'):
        super().__init__(config)
        if 'size' not in self._config.keys():
            self._config['size'] = '10'  # it is the default value set by ES

        assert Elasticsearch(self._config['host']).ping()  # check if the server is up and running

    def _get_es_docs(self, labels):
        """
        Runs the lookup query against ES and returns all the Hits
        :param labels:
        :return:
        """
        # CRITICAL: DO NOT set the ES client instance as a class member: it is not picklable! -> no parallel execution
       
        elastic = Elasticsearch(self._config['host'])
        config_keys = self._config.keys()
        for label in labels:
            s = Search(using=elastic, index=self._config['index'])
            #manufacturer
            
            s.query = Q('match', name=label)
            s = s[0:int(self._config['size'])]
            #print(int(self._config['size']))

            try:
                yield label, [hit for hit in s.execute()]
            except TransportError:
                yield label, []

    def _get_candidates(self, labels):
        """
        Return a list of tuples (label, (uri, [list_of_surface_forms]), one tuple for each given label
        :param labels:
        :return:
        """
        return [(short_label, [(hit['id'], hit['manufacturer'], hit['name']) for hit in candidates])
                for short_label, candidates in self._get_es_docs(labels)]
                
    '''print("EEEEEEEEEEEEEE")
    for x in self._get_es_docs(labels):
        print(x)
    print("WWWWWWWWWWWWWW")
    print([[hit['uri'] for hit in candidates]
           for short_label, candidates in self._get_es_docs(labels)])'''