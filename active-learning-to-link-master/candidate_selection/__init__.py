import os
from abc import ABC
from configparser import ConfigParser


class CandidateSelector(ABC):
    """
    Abstract class that represents a generic Candidate Selection method
    """
    def __init__(self, config):
        cfg = ConfigParser()
        cfg.read(os.path.join(os.path.dirname(__file__), 'config.ini'))
        self._config = cfg[config]

    def search(self, label):
        """
        Return a list of candidates for the given label.
        Must be implemented by all the subclasses.
        :param label:
        :return:
        """
        raise NotImplementedError

    @staticmethod
    def _get_short_labels(label, max_tokens=5):
        """
        Utility function to shorten long labels (that are useless for lookups)
        :param label: the label to shorten
        :param max_tokens: max length for the longest short label
        :return:
        """
        tokens = label.split()
        return [" ".join(tokens[:i+1]) for i in reversed(range(min(max_tokens, len(tokens))))]

    def _get_short_labels_set(self, labels, max_tokens=5):
        """
        Utility function to get the set of all the short labels computed for
        all the labels given as input.
        :param labels: a list of labels to shorten
        :param max_tokens: max length (words) for the longest short label
        :return:
        """
        ext_labels = []
        for label in labels:
            ext_labels = ext_labels + self._get_short_labels(label, max_tokens)

        return list(dict.fromkeys(ext_labels))