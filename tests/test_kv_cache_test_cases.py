from unittest import TestCase
from controllers.kv_cache_controller import KVCacheController


class KVCacheTestCases(TestCase):
    def setUp(self):
        self.kv_cache_controller = KVCacheController()

    def test_search_kvcache_response(self):
        value_dict = {"attribute_key1": "attribute_value1",
                      "attribute_key2": "attribute_value2",
                      "attribute_key3": "attribute_value3",
                      "attribute_key4": "attribute_value4"}
        self.kv_cache_controller.put("key", value_dict)
        self.kv_cache_controller.put("key1", {**value_dict, "attribute_key2": "attribute_value2",
                      "attribute_key3": "attribute_value3"})
        self.assertEqual(["key", "key1"], self.kv_cache_controller.search("attribute_key1", "attribute_value1"))
        self.kv_cache_controller.put("key1", {**value_dict, "attribute_key1": "attribute_value2"})
        self.assertEqual(["key"], self.kv_cache_controller.search("attribute_key1", "attribute_value1"))

    def test_delete_kvcache_validity(self):
        value_dict = {"attribute_key1": "attribute_value1",
                      "attribute_key2": "attribute_value2",
                      "attribute_key3": "attribute_value3"}
        self.kv_cache_controller.put("key", value_dict)
        self.assertIsNotNone(self.kv_cache_controller.get("key"))
        self.kv_cache_controller.delete("key")
        self.assertIsNone(self.kv_cache_controller.get("key"))
