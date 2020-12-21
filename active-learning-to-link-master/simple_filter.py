class SimpleFilter:
    '''
    Class of simple ("flat") filter
    '''
    def __init__(self, property, operator, value, threshold, threshold_operator, weight):
        self.property = property
        self.operator = operator
        self.value = value
        self.threshold = threshold
        self.threshold_operator = threshold_operator
        # tipo se è una edit distance, volgiamo sia sotto un certo valore, se è una jaccard o uno score, lo vogliamo sopra
        self.weight = weight # da usare per importanza attributi riconciliazione multicolonna

    # GETTER

    def get_property(self):
        return self.property

    def get_operator(self):
        return self.operator

    def get_value(self):
        return self.value

    def get_threshold(self):
        return self.threshold

    def get_threshold_operator(self):
        return self.threshold_operator

    def get_weight(self):
        return self.weight

    # SETTER

    def set_property(self, property):
        self.property = property

    def set_operator(self, operator):
        self.operator = operator

    def set_value(self, value):
        self.value = value

    def set_threshold(self, threshold):
        self.threshold = threshold

    def set_threshold_operator(self, threshold_operator):
        self.threshold_operator = threshold_operator

    def set_weight(self, weight):
        self.weight = weight