import pandas as pd
from urllib.request import Request, urlopen, urlretrieve
from bs4 import BeautifulSoup
import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


files_dict = {1995:{'diario':'', 'mensual':'-historico-mensual-1995', 'anual':'-historico-anual-1995'},
             1996:{'diario':'', 'mensual':'-historico-mensual-1996', 'anual':'-historico-anual-1996'},
             1997:{'diario':'', 'mensual':'-historico-mensual-1997', 'anual':'-historico-anual-1997'},
             1998:{'diario':'', 'mensual':'-historico-mensual-1998', 'anual':'-historico-anual-1998'},
             1999:{'diario':'', 'mensual':'-historico-mensual-1999', 'anual':'-historico-anual-1999'},
             2000:{'diario':'', 'mensual':'-historico-mensual-2000', 'anual':'-historico-anual-2000'},
             2001:{'diario':'', 'mensual':'-historico-mensual-2001', 'anual':'-historico-anual-2001'},
             2002:{'diario':'', 'mensual':'-historico-mensual-2002', 'anual':'-historico-anual-2002'},
             2003:{'diario':'', 'mensual':'-historico-mensual-2003', 'anual':'-historico-anual-2003'},
             2004:{'diario':'', 'mensual':'-historico-mensual-2004', 'anual':'-historico-anual-2004'},
             2005:{'diario':'', 'mensual':'-historico-mensual-2005', 'anual':'-historico-anual-2005'},
             2006:{'diario':'', 'mensual':'-historico-mensual-2006', 'anual':'-historico-anual-2006'},
             2007:{'diario':'', 'mensual':'-historico-mensual-2007', 'anual':'-historico-anual-2007'},
             2008:{'diario':'', 'mensual':'-historico-mensual-2008', 'anual':'-historico-anual-2008'},
             2009:{'diario':'', 'mensual':'-historico-mensual-2009', 'anual':'-historico-anual-2009'},
             2010:{'diario':'', 'mensual':'-historico-mensual-2010', 'anual':'-historico-anual-2010'},
             2011:{'diario':'', 'mensual':'-historico-mensual-2011', 'anual':'-historico-anual-2011'},
             2012:{'diario':'', 'mensual':'-historico-mensual-2012', 'anual':'-historico-anual-2012'},
             2013:{'diario':'', 'mensual':'-historico-mensual-2013', 'anual':'-historico-anual-2013'},
             2014:{'diario':'', 'mensual':'-historico-mensual-2014', 'anual':'-historico-anual-2014'},
             2015:{'diario':'', 'mensual':'-historico-mensual-2015', 'anual':'-historico-anual-2015'},
             2016:{'diario':'', 'mensual':'-historico-mensual-2016', 'anual':'-historico-anual-2016'},
             2017:{'diario':'-diario-2017', 'mensual':'-mensual-2017', 'anual':'-historico-anual-2017'},
             2018:{'diario':'-diario-2018', 'mensual':'-mensual-2018', 'anual':'-historico-anual-2018'},
             2019:{'diario':'-diario-2019', 'mensual':'-mensual-2019', 'anual':'-anual-2019'},
             2020:{'diario':'-diario-2020', 'mensual':'-mensual-2020', 'anual':'-anual-2020'},
             2021:{'diario':'-diario-2021', 'mensual':'-mensual-2021', 'anual':'-anual-2021'}}


def get_data(topic, frq='', year1='', year2=''):
    df_return = pd.DataFrame()
    url=''
    df = pd.DataFrame()
    
    # Creamos lista de topicos y periodicidad, para controlar que existan en el servidor
    lista_topicos = ['credito', 'recursos']
    list_frq = ['d', 'm','a']

    
    # Creamos un diccionario de frecuencias, para vincular lo ingresado por el usuario con el dict de urls.    
    frq_dict = {'d':'diario','m':'mensual','a':'anual'}
    
    # Verificamos que el topico ingresado exista
    if topic not in lista_topicos:
        logging.debug('Error! El tema {0} no existe en el servidor!'.format(topic))
        return()
    
    # Verificamos que la periodicidad ingresada exista
    if frq not in list_frq:
        logging.debug('Error! La periodicidad {0} no existe en el servidor!'.format(frq))
        return()
    
    # Verificamos que la periodicidad ingresada exista
    if year1<1995 or year1>2021:
        logging.debug('Error! El año {0} no existe en el servidor!'.format(year1))
        return()
    
    # Corregimos la fecha superior
    if year2 =='' or year2<year1:
        year2=year1

    
    # La lista de topicos es para una posible extensión del módulo
    list_topic = ['apertura-programatica','clasificador-economico','finalidad-funcion','fuente-financiamiento','institucion','objeto-gasto','rubro-recurso','sector-institucional','servicio','ubicacion-geografica']

    # Iteramos en el ranga seleccionado por el usuario
    for year in range(year1,year2+1):

        # Definimos variables
        read_url='https://www.presupuestoabierto.gob.ar/datasets/' + str(year) + '/'
        ext = '.zip'
        read_file_ext = ''
        
        logging.debug('Ejercicio: {}'.format(year))
        
        # Descartamos los periodos para los cuales no existe la frecuencia en credito y armamos la url
        if files_dict[year][frq_dict[frq]]!='':
            if frq in list_frq:
                url = read_url + topic + files_dict[year][frq_dict[frq]] + '.zip' 
                    


        # Descargamos el archivo
        try:
            logging.debug('  Intentando descargar desde {}'.format(url))
            df = pd.read_csv(url, compression = 'zip')
            logging.debug('  Se descargó con éxito el archivo solicitado desde {}'.format(url))
        except:
            logging.debug('  Error al intentar descargar desde {0}'.format(url))

        # 'Pegamos' el dataframe al acumulado (si el rango de periodos es >1)
        df_return = df_return.append(df)
        
    return(df_return)


# Función que devuelve el contenido del directorio en el servidor.

def get_docs(year='2021'):
    url = 'https://www.presupuestoabierto.gob.ar/datasets/' + str(year) + '/'
    print(url)
    req = Request(url)
    site = urlopen(req).read()
    sp = BeautifulSoup(site, 'html.parser')
    links = (sp.find_all('a'))
    links = links[5:] # Cortamos los primeros 5 elementos que son basura (entre ellos 'Parent Directory')
    links = [link.get('href') for link in links] # Pasamos los links a una lista
    elem = []
    for item in links:
        if '.zip' in item:
            item = item[:-4] # Borramos la extensión .zip
            if 'd-' in item:
                item = item[2:] # Borramos el "d-" al inicio de algunos nombres
            print(item)
