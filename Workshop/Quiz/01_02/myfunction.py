# import necessary library here
import requests

# function 
def converter(value:int, fr:str, to:str)->int:
  # write your code here
  response = requests.get(f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{fr.lower()}/{to.lower()}.json', timeout=5)
  data = response.json()

  return value *  int(data[to.lower()]) # return name and result value of the test


if __name__ == '__main__':
  print(converter(1000,'USD','IDR'))