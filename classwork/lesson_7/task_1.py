import requests


def get_data_requests():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
    params = {'people': 10}
    result = requests.get('http://httpbin.org/get', params=params, headers=headers)
    return result.json()

# def google_it(prompt):
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
#     params = {'q': prompt}
#     result = requests.get('https://google.com/search', params=params, headers=headers)
#     if result.status_code == 200:
#         return result.text


print(get_data_requests())
# print(google_it('How much is the fish?'))
