import requests

class VakSmsApi:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://vak-sms.com/api/"

    def get_balance(self):
        url = f"{self.base_url}getBalance/?apiKey={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()["balance"]
        else:
            raise Exception(response.status_code)

    def get_count_number(self, service, country, operator):
        url = f"{self.base_url}getCountNumber/?apiKey={self.api_key}&service={service}&country={country}&operator={operator}&price"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(response.status_code)

    def get_number(self, service, country, operator):
        url=f"{self.base_url}getNumber/?apiKey={self.api_key}&service={service}&country={country}&operator={operator}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(response.status_code)

    def prolongNumber(self, service, tel):
        url=f"{self.base_url}prolongNumber/?apiKey={self.api_key}&service={service}&tel={tel}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(response.status_code)

    def get_sms(self, idNum):
        url=f"{self.base_url}getSmsCode/?apiKey={self.api_key}&idNum={idNum}&all"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Ошибка при получение SMS: {response.status_code}")

    def change_status(self, idNum, status):
        url=f"{self.base_url}setStatus/?apiKey={self.api_key}&status={status}&idNum={idNum}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(response.status_code)