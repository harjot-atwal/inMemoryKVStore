from services.kv_cache_service import KVCacheService


class KVCacheController:
    def __init__(self):
        self.kv_cache_service = KVCacheService()

    # Should return the value (object with attributes and their values). Return null if key not present
    def get(self, key):
        return self.kv_cache_service.get(key)

    # Returns a list of keys that have the given attribute key, value pair.
    def search(self, attribute_key, attribute_value):
        return self.kv_cache_service.search(attribute_key, attribute_value)

    # Adds the key and the attributes to the key-value store. If the key already exists then the value is replaced.
    def put(self, key, map_of_attribute_pairs):
        self.kv_cache_service.put(key, map_of_attribute_pairs)

    # Deletes the key, value pair from the store.
    def delete(self, key):
        self.kv_cache_service.delete(key)

    # Return a list of all the keys
    def keys(self):
        return self.kv_cache_service.keys()
