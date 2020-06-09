import pytest
import requests
import csv

# ************************************** Reading data from List and passing to pytest function
test_data_zip_codes = [
    ("us", "90210", "Beverly Hills"),
    ("ca", "B2A", "North Sydney South Central"),
    ("it", "50123", "Firenze"),
    ("it", "50123", "FailedTest")
]


@pytest.mark.parametrize("country_code, zip_code, expected_place_name", test_data_zip_codes)
def test_using_test_data_object_get_location_data_check_place_name(country_code, zip_code, expected_place_name):
    response = requests.get(f"http://api.zippopotam.us/{country_code}/{zip_code}")
    res_body = response.json()
    assert res_body["places"][0].get("place name") == expected_place_name


# ************************************** Reading data from csv and passing to pytest function

def read_data_from_test_data_zip_codes():
    data_list = []
    with open(
            "C:/Users/mlodhi/OneDrive - Nice Systems Ltd/Desktop/Python Pract/SeleniumWithAPITesting/API_Verification/Test-Data/test_data_zip_codes.csv",  encoding='utf-8-sig') as file:
        data = csv.reader(file, delimiter=',')
        for row in data:
            data_list.append(tuple(row))
    return data_list


@pytest.mark.parametrize("country_code, zip_code, expected_place_name", read_data_from_test_data_zip_codes())
def test_using_csv_data_get_location_data_check_place_name(country_code, zip_code, expected_place_name):
    response = requests.get(f"http://api.zippopotam.us/{country_code}/{zip_code}")
    res_body = response.json()
    assert res_body["places"][0].get("place name") == expected_place_name

print(read_data_from_test_data_zip_codes())