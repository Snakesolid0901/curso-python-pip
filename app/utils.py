def get_population():
    keys =['col','bol']
    values=[300,400]
    return keys, values

def population_by_poblacion (data,population):
    result = list(filter(lambda item : item["Population"] == population , data ))
    return result

def population_by_country (data, country):
    result2 = list(filter(lambda item : item["country"]==country, data))
    return result2 