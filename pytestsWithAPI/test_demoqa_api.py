import requests

ENDPOINT = "https://demoqa.com/"

def test_call_endpoint():
    response = requests.get(ENDPOINT + "books")
    assert response.status_code == 200

def login():
    payload = {
      "userName": "MelDem",
      "password": "Mel123,@Dem"
    }
    login_response = requests.post("https://demoqa.com/Account/v1/Login", json=payload)
    assert login_response.status_code == 200
    data = login_response.json()
    return data

def userInfo():
    data = login()
    headers = {'Authorization': f'Bearer {data["token"]}'}
    user_response = requests.get(f"https://demoqa.com/Account/v1/User/{data['userId']}", headers=headers)
    assert user_response.status_code == 200
    user_data = user_response.json()
    print(user_data)
    return [user_data, data["token"]]

def get_book(index):
    book_response = requests.get(ENDPOINT + "BookStore/v1/Books")
    assert book_response.status_code == 200
    books_data = book_response.json()
    return books_data["books"][index]

def test_add_book():
    udata, token = userInfo() #[1]
    headers = {'Authorization': f'Bearer {token}'}
    addThisBook = get_book(3)["isbn"]
    payload = {
      "userId": udata["userId"],
      "collectionOfIsbns": [
        {
          "isbn": addThisBook
        }
      ]
    }
    put_response = requests.post("https://demoqa.com/BookStore/v1/Books", json=payload, headers=headers)
    assert put_response.status_code == 201
