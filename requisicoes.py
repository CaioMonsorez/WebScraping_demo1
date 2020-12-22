import requests

response = requests.get('https://www.walissonsilva.com/')

print('Status code:', response.status_code)
print('-----Header----- formato dicionario do python----')
print(response.headers)


# o comando acima imprime::::::::



#Status code: 200
#-----Header----- formato dicionario do python----
#{'Date': 'Tue, 22 Dec 2020 02:39:01 GMT', 
# 'Server': 'Apache', 
# 'X-Powered-By': 'Express', 
# 'Content-Type': 'text/html; 
# charset=utf-8', 
# 'Content-Length': '34067',
#  'ETag': 'W/"8513-7LyJWOydZiVg6n8iE64vhuzeQ7I"',
#'Set-Cookie': 'connect.sid=s%3AHyShVW-MmRi9-J3J_d4YmRJCOXkPuGk0.Ka7HoF8GH%2BFOj9GA7XikwVryXcLS0mdOQchmux3Lb7k; Path=/;
#  Expires=Tue, 22 Dec 2020 03:09:01 GMT;
#  HttpOnly', 'Via': '1.1 www.walissonsilva.com', 
# 'Keep-Alive': 'timeout=5, max=500', 'Connection': 'Keep-Alive'}


print("\n --- content ----")
print(response.content)