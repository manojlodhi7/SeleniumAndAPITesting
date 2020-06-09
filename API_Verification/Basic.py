import requests

def test_get_locations_for_us_90210_check_status_code_equals_200():
    response = requests.get("http://api.zippopotam.us/us/90210")
    assert response.status_code == 200
    print(response.json())

def test_get_locations_for_us_90210_check_headers():
    response = requests.get("http://api.zippopotam.us/us/90210")
    headers = response.headers
    assert headers.get("Content-Type") == 'application/json'
    assert headers.get("Content-Encoding") == 'gzip'

    # print("response.json()  : ", response.json())  # {'post code': '90210', 'country': 'United States', 'country abbreviation': 'US', 'places': [{'place name': 'Beverly Hills', 'longitude': '-118.4065', 'state': 'California', 'state abbreviation': 'CA', 'latitude': '34.0901'}]}
    # print("response.content  : ", response.content)  # b'{"post code": "90210", "country": "United States", "country abbreviation": "US", "places": [{"place name": "Beverly Hills", "longitude": "-118.4065", "state": "California", "state abbreviation": "CA", "latitude": "34.0901"}]}'
    # print("response.apparent_encoding  : ", response.apparent_encoding)  # ascii
    # print("response.cookies  : ", response.cookies)  # <RequestsCookieJar[<Cookie __cfduid=dc866eeec00abc9045804ac0ea9d9aaff1591703210 for .zippopotam.us/>]>
    # print("response.headers  : ", response.headers)  # {'Date': 'Tue, 09 Jun 2020 11:46:50 GMT', 'Content-Type': 'application/json', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Set-Cookie': '__cfduid=dc866eeec00abc9045804ac0ea9d9aaff1591703210; expires=Thu, 09-Jul-20 11:46:50 GMT; path=/; domain=.zippopotam.us; HttpOnly; SameSite=Lax', 'X-Cache': 'hit', 'Charset': 'UTF-8', 'Vary': 'Accept-Encoding', 'Access-Control-Allow-Origin': '*', 'CF-Cache-Status': 'DYNAMIC', 'cf-request-id': '033a80a2a30000dcd66cb92200000001', 'Server': 'cloudflare', 'CF-RAY': '5a0a9d4a9cbedcd6-SIN', 'Content-Encoding': 'gzip'}
    # print("response.links  : ", response.links)  # Links present in response body
    # print("response.url  : ", response.url)  # http://api.zippopotam.us/us/90210
    # print("response.text  : ", response.text)  # return body as simple string == response.json()
    # print("response.raw  : ", response.raw)  # <urllib3.response.HTTPResponse object at 0x000001EF04D949D0>


def test_get_locations_for_us_90210_check_place():
    response = requests.get("http://api.zippopotam.us/us/90210")
    response_body = response.json()
    assert response_body["places"][0]["state"] == "California"

