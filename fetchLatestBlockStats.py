import requests
import json


def main():
    url = "http://localhost:8545"
    headers = {'content-type': 'application/json'}

    # Example echo method
    payload = {
        "method": "eth_getBlockByNumber",
        "params": ['latest',False],
        "jsonrpc": "2.0",
        "id": 67,
    }
    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()
    
    blockNo = int(response["result"]["number"]
    print response
    assert response["jsonrpc"]
    assert response["id"] == 67

if __name__ == "__main__":
    main()
