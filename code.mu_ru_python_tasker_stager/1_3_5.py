"""
Дан словарь с датой:

{
	'year' : '2025',
	'month': '12',
	'day'  : '31',
}
Из элементов этого словаря соберите дату в следующем формате:

'2025-12-31'
"""
date_dict = {
    'year': '2025',
    'month': '0',
    'day': '10',
}

result = f"{date_dict['year']}-{date_dict['month']}-{date_dict['day']}"
print(result)