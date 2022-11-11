import httpx

# response = httpx.get('https://httpbin.org/get')
# print(response.status_code)
# print(response.headers)
# print(response.text)


# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
# }
# response = httpx.get('https://httpbin.org/get', headers=headers)
# print(response.text)


# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
# }
# response = httpx.get('https://spa16.scrape.center', headers=headers)
# print(response.text)

client = httpx.Client(http2=True)
response = client.get('https://spa16.scrape.center/')
print(response.text)
