import requests


words = {'name': "ed1", "tags": ['animals', 'peope2']}

res = requests.post('http://127.0.0.1:5000/newartist', json=words)

print(res.status_code)
print(res.json())
