import utils

data = [
        {
            "country":"Colombia",
            "Population": 320
        },
        {
            "country":"brazil",
            "Population": 820
        },
        {
            "country":"salvador",
            "Population": 120
        }
    ]

def run ():
    x,y = utils.get_population()
    
    new_dict = dict(zip(x,y))
    print(new_dict)
        
   
    cualquieresp = int(input("selecciona el tamaño de la poblacion quieres ver"))
    cualquieres = input("selecciona tu pais")
    
    poblacion300 = utils.population_by_poblacion(data, cualquieresp) 
    print(poblacion300)
    
    country = utils.population_by_country(data,cualquieres) 
    print(country)
if __name__ == '__main__':
    run()
    

    