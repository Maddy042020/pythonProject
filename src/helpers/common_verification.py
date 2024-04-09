def verify_https_code(response_data, expected_data):
    assert response_data.status_code == expected_data

def verify_json_key_for_not_null(key):
     assert key != 0, "Key is not empty" +key
     assert key > 0


def verify_response_key_should_not_be_none(key):
    assert key is not None