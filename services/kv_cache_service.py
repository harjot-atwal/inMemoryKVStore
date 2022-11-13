from services.kv_cache_service_interface import KVCacheServiceInterface


class KVCacheService(KVCacheServiceInterface):
    kv_cache = {}

    def get(self, key):
        return self.__class__.kv_cache.get(key)

    def search(self, attribute_key, attribute_value):
        keys_containing_given_attribute = []
        for key, value in self.__class__.kv_cache.items():
            for object_key, object_value in value.items():
                if object_key == attribute_key and object_value == attribute_value:
                    keys_containing_given_attribute.append(key)
                    break

        return keys_containing_given_attribute

    def put(self, key, map_of_attribute_pairs):
        self.__class__.kv_cache.update({key: map_of_attribute_pairs})

    def clear(self):
        self.__class__.kv_cache.clear()

    def keys(self):
        return self.__class__.kv_cache.keys()

    def delete(self, key):
        self.__class__.kv_cache.pop(key)
