from abc import ABC, abstractmethod


class Filter(ABC):

    
    @abstractmethod
    def filter(self, subarray):
        """
        Apply a filter to the given subarray. Should be implemented by different filter classes.
        """
        pass