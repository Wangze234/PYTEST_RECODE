
import requests
import json
def request_value():
    url = 'http://example.com/api/endpoint'
    data = {
        "key": "value",
        "another_key": "another_value"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    return response.status_code

def test_departur_station():

    # 从响应中获取测试列表
    trainSli = request_value()
    assert trainSli == 403
