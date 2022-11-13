test_dict = {"key": {"child_key": "child_value",
                     "child_key_1": "child_value_1"}}

test_dict["key"].update({"child_key_2": "child_value_1"})

print(test_dict)
