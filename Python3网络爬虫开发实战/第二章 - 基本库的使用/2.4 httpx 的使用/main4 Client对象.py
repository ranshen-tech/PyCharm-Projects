import httpx

# with httpx.Client() as client:
#     response = client.get('https://httpbin.org/get')
#     print(response)


# client = httpx.Client()
# try:
#     response = client.get('https://httpbin.org/get')
# finally:
#     client.close()


url = 'http://httpbin.org/headers'
headers = {'User-Agent': 'my-app/0.0.1'}
with httpx.Client(headers=headers) as client:
    r = client.get(url)
    print(r.text)
    print(r.json()['headers']['User-Agent'])
