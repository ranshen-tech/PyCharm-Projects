import httpx
client = httpx.Client(http2=True)

response = client.get('https://spa16.scrape.center/')
print(response.text)


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}
client = httpx.Client(http2=True)
response = client.get('https://spa16.scrape.center', headers=headers)
print(response.text)
