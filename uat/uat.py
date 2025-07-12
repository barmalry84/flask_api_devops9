import requests
import os

def test_user_acceptance():
    base_url = os.getenv('FLASK_ENDPOINT')

    # Test welcome message
    response = requests.get(f"{base_url}/")
    assert response.status_code == 200
    assert response.json()['message'] == "Hello people!!!"

    # Test sum operation
    response = requests.post(f"{base_url}/sum", json={'num1': 10, 'num2': 15})
    assert response.status_code == 200
    assert response.json()['result'] == 25

    # Test multiply operation
    response = requests.post(f"{base_url}/multiply", json={'num1': 4, 'num2': 5})
    assert response.status_code == 200
    assert response.json()['result'] == 20

    print("All UAT scenarios passed successfully.")

if __name__ == '__main__':
    test_user_acceptance()

