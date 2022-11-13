import abc
class KVCacheServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def search(self, attribute_key, attribute_value):
        pass

    @abc.abstractmethod
    def put(self, key, map_of_attribute_pairs):
        pass

    @abc.abstractmethod
    def delete(self, key):
        pass

    @abc.abstractmethod
    def keys(self):
        pass