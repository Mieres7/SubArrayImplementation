from abc import ABC, abstractmethod
from subarray import Array

class Filter(ABC, Array):

    @abstractmethod
    def filter(self):
        """
        Apply a filter to the given subarray. Should be implemented by different filter classes.
        """
        pass