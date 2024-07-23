
import requests
PET_URL = "https://petstore.swagger.io/v2"

def add_pet_to_pet_url(pet_data_json):

    """
    adding pet to the swagger URL
    """

    url = f"{PET_URL}/pet"
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=pet_data_json, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

new_pet_data = {
    "id": 1,
    "category": {
        "id": 0,
        "name": "string"
    },
    "name": "doggie",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 0,
            "name": "string"
        }
    ],
    "status": "available"
}

added_pet = add_pet_to_pet_url(new_pet_data)
if added_pet:
    print(f"Added new pet with ID {added_pet['id']}")
else:
    print("Failed to add new pet.")

def find_pet_by_status(status):
    """
    checking the pet avaliability :: pending :: available :: sold
    """
    get_url = f"{PET_URL}/pet/findByStatus"
    params = {'status': status}
    response = requests.get(get_url, params=params)

    if response.status_code == 200:
        print("response",response)
        return response.json()
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

statuses = ['available', 'pending', 'sold']
pets_by_status = find_pet_by_status(statuses)
for status in pets_by_status:
    if status:
        print(f"Found pets with status '{status}':")
        for pet in status:
            print(" pet ", pet)
    else:
        print(f"No pets found with status '{status}'.")
