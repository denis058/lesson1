dict = {
    'city': 'Москва',
    'temperature': '20'
}
dict['temperature'] = '5'
print(dict.get('country', 'Россия'))
dict['date'] = '27.05.2019'
print(len(dict))