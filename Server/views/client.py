import requests


getstuff=requests.get('http://127.0.0.1:5000/test')
print(getstuff.text)