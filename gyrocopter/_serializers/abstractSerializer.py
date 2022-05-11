from abc import ABC, abstractmethod


class AbstractSerializer(ABC):
    @abstractmethod
    def dump(self, _object, file_path):
        pass

    @abstractmethod
    def dumps(self, _object):
        pass

    @abstractmethod
    def load(self, file_path):
        pass

    @abstractmethod
    def loads(self, string):
        pass