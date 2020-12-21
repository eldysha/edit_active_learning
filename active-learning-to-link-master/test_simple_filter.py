import unittest
from simple_filter import SimpleFilter

class TestSimpleFilter(unittest.TestCase):

    def test_constructor(self):
        property = "http://dbpedia.org/ontology/country"
        operator = "=="
        value = "http://dbpedia.org/resource/Italy"
        threshold = 1
        threshold_operator = ">="
        weight = 0.8
        simple_filter = SimpleFilter(property, operator, value, threshold, threshold_operator, weight)
        self.assertEqual(simple_filter.get_property(), property)
        self.assertEqual(simple_filter.get_operator(), operator)
        self.assertEqual(simple_filter.get_value(), value)
        self.assertEqual(simple_filter.get_threshold(), threshold)
        self.assertEqual(simple_filter.get_threshold_operator(), threshold_operator)
        self.assertEqual(simple_filter.get_weight(), weight)

if __name__ == '__main__':
    unittest.main()
