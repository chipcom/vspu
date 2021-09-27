import requests

class Singleton:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance

def get_location_info():
    # получить информацию о размещении IP-адреса
    return requests.get("http://ip-api.com/json/").json()

if __name__ == "__main__":
    # print(get_location_info())
    a = Singleton()
    b = Singleton()

    print(a is b)