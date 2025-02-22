import requests
import hashlib
import datetime

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(id):
    url = f"{base_url}/pokemon/{id}"
    response = requests.get(url)

    if response.status_code == 200: # Başarılıysa 200 kodunu döndürür.
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Pokemon bilgisi çekilemedi. Hata kodu: {response.status_code}")
def generate_fixed_number(min_val=1, max_val=1025):
    today = datetime.date.today().strftime("%Y-%m-%d")  # Bugünün tarihini alır.
    hash_value = hashlib.md5(today.encode()).hexdigest()  # Tarihi hash'ler ve unique hale getirir.
    number = int(hash_value[:8], 16)  # İlk 8 karakteri alır ve integer'a çevirir.
    return min_val + (number % (max_val - min_val + 1))  # Belirlenen aralığa sıkıştırır.