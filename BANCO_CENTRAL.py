import requests
import pandas as pd
import plotly.io as pio
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import talib
pio.templates.default = "plotly_dark"

token = "BEARER {TOKEN}"
#endopint al que se llama (Ver listado de endpoins)

def cotizacion_oficial():
    endpoint = "usd"
    #datos para el llamado
    url = "https://api.estadisticasbcra.com/"+endpoint
    headers = {"Authorization": token}
    #Llamado
    data_json = requests.get(url, headers=headers).json()
    #Armamos una tabla con los datos
    data = pd.DataFrame(data_json)
    #Le asignamos la fecha como indice
    data.set_index('d', inplace=True, drop=True)
    data.to_csv('csv/bcra.csv')
    count = 0
    for data in pd.read_csv('csv/bcra.csv',encoding = 'ISO-8859-1',chunksize  = 1000):
        count += 1                          # counting the number of chunks
        lastlen = len(data)                 # finding the length of last chunk
        datalength = (count*1000 + lastlen - 1000) # length of total file
        rowsdiff = datalength - 300
    df = pd.read_csv('csv/bcra.csv',encoding = 'ISO-8859-1',skiprows = range(1,rowsdiff), nrows = 299)
    #print(data.tail())
    y= df['v']
    x = df['d']
    cotizacion = df["v"].iloc[-1]
    fig = go.Figure()
    fig = make_subplots(rows=2, cols=1, row_heights=[0.7, 0.3])
    fig.add_trace(go.Scatter(x=x, y=y, name=f'${cotizacion}   '))
    fig.update_xaxes(tickangle=45)
    fig.update_layout(title= f'PESO-ARG/USD',xaxis_nticks=25)
    rsi = talib.RSI(y)
    fig.add_trace(go.Scatter(y=rsi,line=dict(color='fuchsia',width=1),name='rsi'), row=2, col=1)
    fig.write_image("dolar-peso.png",scale=25)



def base_monetaria():
    endpoint = "base"
    #datos para el llamado
    url = "https://api.estadisticasbcra.com/"+endpoint
    headers = {"Authorization": token}
    #Llamado
    data_json = requests.get(url, headers=headers).json()
    #Armamos una tabla con los datos
    data = pd.DataFrame(data_json)
    #Le asignamos la fecha como indice
    data.set_index('d', inplace=True, drop=True)
    data.to_csv('csv/bcra.csv')
    count = 0
    for data in pd.read_csv('csv/bcra.csv',encoding = 'ISO-8859-1',chunksize  = 1000):
        count += 1                          # counting the number of chunks
        lastlen = len(data)                 # finding the length of last chunk
        datalength = (count*1000 + lastlen - 1000) # length of total file
        rowsdiff = datalength - 900
    df = pd.read_csv('csv/bcra.csv',encoding = 'ISO-8859-1',skiprows = range(1,rowsdiff), nrows = 299)
    y= df['v']
    x = df['d']
    cotizacion = df["v"].iloc[-1]
    fig = go.Figure()
    fig = make_subplots(rows=2, cols=1, row_heights=[0.7, 0.3])
    fig.add_trace(go.Scatter(x=x, y=y, name=f'${cotizacion}    '))
    fig.update_xaxes(tickangle=45)
    fig.update_layout(title= f'base_monetaria',xaxis_nticks=25)
    rsi = talib.RSI(y)
    fig.add_trace(go.Scatter(y=rsi,line=dict(color='fuchsia',width=1),name='rsi'), row=2, col=1)
    fig.write_image("base_monetaria.png",scale=25)

def base_monetaria_usd():
    endpoint = "base_usd"
    #datos para el llamado
    url = "https://api.estadisticasbcra.com/"+endpoint
    headers = {"Authorization": token}
    #Llamado
    data_json = requests.get(url, headers=headers).json()
    #Armamos una tabla con los datos
    data = pd.DataFrame(data_json)
    #Le asignamos la fecha como indice
    data.set_index('d', inplace=True, drop=True)
    data.to_csv('csv/bcra.csv')
    count = 0
    for data in pd.read_csv('csv/bcra.csv',encoding = 'ISO-8859-1',chunksize  = 1000):
        count += 1                          # counting the number of chunks
        lastlen = len(data)                 # finding the length of last chunk
        datalength = (count*1000 + lastlen - 1000) # length of total file
        rowsdiff = datalength - 900
    df = pd.read_csv('csv/bcra.csv',encoding = 'ISO-8859-1',skiprows = range(1,rowsdiff), nrows = 299)
    y= df['v']
    x = df['d']
    cotizacion = df["v"].iloc[-1]
    fig = go.Figure()
    fig = make_subplots(rows=2, cols=1, row_heights=[0.7, 0.3])
    fig.add_trace(go.Scatter(x=x, y=y, name=f'${cotizacion}    '))
    fig.update_xaxes(tickangle=45)
    fig.update_layout(title= f'base_monetaria_usd',xaxis_nticks=25)
    rsi = talib.RSI(y)
    fig.add_trace(go.Scatter(y=rsi,line=dict(color='fuchsia',width=1),name='rsi'), row=2, col=1)
    fig.write_image("base_monetaria_usd.png",scale=25)
def reservas():
    endpoint = "reservas"
    #datos para el llamado
    url = "https://api.estadisticasbcra.com/"+endpoint
    headers = {"Authorization": token}
    #Llamado
    data_json = requests.get(url, headers=headers).json()
    #Armamos una tabla con los datos
    data = pd.DataFrame(data_json)
    #Le asignamos la fecha como indice
    data.set_index('d', inplace=True, drop=True)
    data.to_csv('csv/bcra.csv')
    count = 0
    for data in pd.read_csv('csv/bcra.csv',encoding = 'ISO-8859-1',chunksize  = 1000):
        count += 1                          # counting the number of chunks
        lastlen = len(data)                 # finding the length of last chunk
        datalength = (count*1000 + lastlen - 1000) # length of total file
        rowsdiff = datalength - 900
    df = pd.read_csv('csv/bcra.csv',encoding = 'ISO-8859-1',skiprows = range(1,rowsdiff), nrows = 299)
    y= df['v']
    x = df['d']
    cotizacion = df["v"].iloc[-1]
    fig = go.Figure()
    fig = make_subplots(rows=2, cols=1, row_heights=[0.7, 0.3])
    fig.add_trace(go.Scatter(x=x, y=y, name=f'${cotizacion}    '))
    fig.update_xaxes(tickangle=45)
    fig.update_layout(title= f'reservas',xaxis_nticks=25)
    rsi = talib.RSI(y)
    fig.add_trace(go.Scatter(y=rsi,line=dict(color='fuchsia',width=1),name='rsi'), row=2, col=1)
    fig.write_image("reservas.png",scale=25) 
def circulacion_monetaria():
    endpoint = "circulacion_monetaria"
    #datos para el llamado
    url = "https://api.estadisticasbcra.com/"+endpoint
    headers = {"Authorization": token}
    #Llamado
    data_json = requests.get(url, headers=headers).json()
    #Armamos una tabla con los datos
    data = pd.DataFrame(data_json)
    #Le asignamos la fecha como indice
    data.set_index('d', inplace=True, drop=True)
    data.to_csv('csv/bcra.csv')
    count = 0
    for data in pd.read_csv('csv/bcra.csv',encoding = 'ISO-8859-1',chunksize  = 1000):
        count += 1                          # counting the number of chunks
        lastlen = len(data)                 # finding the length of last chunk
        datalength = (count*1000 + lastlen - 1000) # length of total file
        rowsdiff = datalength - 900
    df = pd.read_csv('csv/bcra.csv',encoding = 'ISO-8859-1',skiprows = range(1,rowsdiff), nrows = 299)
    y= df['v']
    x = df['d']
    cotizacion = df["v"].iloc[-1]
    fig = go.Figure()
    fig = make_subplots(rows=2, cols=1, row_heights=[0.7, 0.3])
    fig.add_trace(go.Scatter(x=x, y=y, name=f'${cotizacion}    '))
    fig.update_xaxes(tickangle=45)
    fig.update_layout(title= f'circulacion_monetaria',xaxis_nticks=25)
    rsi = talib.RSI(y)
    fig.add_trace(go.Scatter(y=rsi,line=dict(color='fuchsia',width=1),name='rsi'), row=2, col=1)
    fig.write_image("circulacion_monetaria.png",scale=25)   
def billetes_y_monedas():
    endpoint = "billetes_y_monedas"
    #datos para el llamado
    url = "https://api.estadisticasbcra.com/"+endpoint
    headers = {"Authorization": token}
    #Llamado
    data_json = requests.get(url, headers=headers).json()
    #Armamos una tabla con los datos
    data = pd.DataFrame(data_json)
    #Le asignamos la fecha como indice
    data.set_index('d', inplace=True, drop=True)
    data.to_csv('csv/bcra.csv')
    count = 0
    for data in pd.read_csv('csv/bcra.csv',encoding = 'ISO-8859-1',chunksize  = 1000):
        count += 1                          # counting the number of chunks
        lastlen = len(data)                 # finding the length of last chunk
        datalength = (count*1000 + lastlen - 1000) # length of total file
        rowsdiff = datalength - 900
    df = pd.read_csv('csv/bcra.csv',encoding = 'ISO-8859-1',skiprows = range(1,rowsdiff), nrows = 299)
    y= df['v']
    x = df['d']
    cotizacion = df["v"].iloc[-1]
    fig = go.Figure()
    fig = make_subplots(rows=2, cols=1, row_heights=[0.7, 0.3])
    fig.add_trace(go.Scatter(x=x, y=y, name=f'${cotizacion}    '))
    fig.update_xaxes(tickangle=45)
    fig.update_layout(title= f'billetes_y_monedas',xaxis_nticks=25)
    rsi = talib.RSI(y)
    fig.add_trace(go.Scatter(y=rsi,line=dict(color='fuchsia',width=1),name='rsi'), row=2, col=1)
    fig.write_image("billetes_y_monedas.png",scale=25)   
def efectivo_en_ent_fin():
    endpoint = "efectivo_en_ent_fin"
    #datos para el llamado
    url = "https://api.estadisticasbcra.com/"+endpoint
    headers = {"Authorization": token}
    #Llamado
    data_json = requests.get(url, headers=headers).json()
    #Armamos una tabla con los datos
    data = pd.DataFrame(data_json)
    #Le asignamos la fecha como indice
    data.set_index('d', inplace=True, drop=True)
    data.to_csv('csv/bcra.csv')
    count = 0
    for data in pd.read_csv('csv/bcra.csv',encoding = 'ISO-8859-1',chunksize  = 1000):
        count += 1                          # counting the number of chunks
        lastlen = len(data)                 # finding the length of last chunk
        datalength = (count*1000 + lastlen - 1000) # length of total file
        rowsdiff = datalength - 900
    df = pd.read_csv('csv/bcra.csv',encoding = 'ISO-8859-1',skiprows = range(1,rowsdiff), nrows = 299)
    y= df['v']
    x = df['d']
    cotizacion = df["v"].iloc[-1]
    fig = go.Figure()
    fig = make_subplots(rows=2, cols=1, row_heights=[0.7, 0.3])
    fig.add_trace(go.Scatter(x=x, y=y, name=f'${cotizacion}    '))
    fig.update_xaxes(tickangle=45)
    fig.update_layout(title= f'efectivo_en_ent_fin',xaxis_nticks=25)
    rsi = talib.RSI(y)
    fig.add_trace(go.Scatter(y=rsi,line=dict(color='fuchsia',width=1),name='rsi'), row=2, col=1)
    fig.write_image("efectivo_en_ent_fin.png",scale=25)   
def depositos_cuenta_ent_fin():
    endpoint = "depositos_cuenta_ent_fin"
    #datos para el llamado
    url = "https://api.estadisticasbcra.com/"+endpoint
    headers = {"Authorization": token}
    #Llamado
    data_json = requests.get(url, headers=headers).json()
    #Armamos una tabla con los datos
    data = pd.DataFrame(data_json)
    #Le asignamos la fecha como indice
    data.set_index('d', inplace=True, drop=True)
    data.to_csv('csv/bcra.csv')
    count = 0
    for data in pd.read_csv('csv/bcra.csv',encoding = 'ISO-8859-1',chunksize  = 1000):
        count += 1                          # counting the number of chunks
        lastlen = len(data)                 # finding the length of last chunk
        datalength = (count*1000 + lastlen - 1000) # length of total file
        rowsdiff = datalength - 900
    df = pd.read_csv('csv/bcra.csv',encoding = 'ISO-8859-1',skiprows = range(1,rowsdiff), nrows = 299)
    y= df['v']
    x = df['d']
    cotizacion = df["v"].iloc[-1]
    fig = go.Figure()
    fig = make_subplots(rows=2, cols=1, row_heights=[0.7, 0.3])
    fig.add_trace(go.Scatter(x=x, y=y, name=f'${cotizacion}    '))
    fig.update_xaxes(tickangle=45)
    fig.update_layout(title= f'depositos_cuenta_ent_fin',xaxis_nticks=25)
    rsi = talib.RSI(y)
    fig.add_trace(go.Scatter(y=rsi,line=dict(color='fuchsia',width=1),name='rsi'), row=2, col=1)
    fig.write_image("depositos_cuenta_ent_fin.png",scale=25)   
def depositos():
    endpoint = "depositos"
    #datos para el llamado
    url = "https://api.estadisticasbcra.com/"+endpoint
    headers = {"Authorization": token}
    #Llamado
    data_json = requests.get(url, headers=headers).json()
    #Armamos una tabla con los datos
    data = pd.DataFrame(data_json)
    #Le asignamos la fecha como indice
    data.set_index('d', inplace=True, drop=True)
    data.to_csv('csv/bcra.csv')
    count = 0
    for data in pd.read_csv('csv/bcra.csv',encoding = 'ISO-8859-1',chunksize  = 1000):
        count += 1                          # counting the number of chunks
        lastlen = len(data)                 # finding the length of last chunk
        datalength = (count*1000 + lastlen - 1000) # length of total file
        rowsdiff = datalength - 900
    df = pd.read_csv('csv/bcra.csv',encoding = 'ISO-8859-1',skiprows = range(1,rowsdiff), nrows = 299)
    y= df['v']
    x = df['d']
    cotizacion = df["v"].iloc[-1]
    fig = go.Figure()
    fig = make_subplots(rows=2, cols=1, row_heights=[0.7, 0.3])
    fig.add_trace(go.Scatter(x=x, y=y, name=f'${cotizacion}    '))
    fig.update_xaxes(tickangle=45)
    fig.update_layout(title= f'depositos',xaxis_nticks=25)
    rsi = talib.RSI(y)
    fig.add_trace(go.Scatter(y=rsi,line=dict(color='fuchsia',width=1),name='rsi'), row=2, col=1)
    fig.write_image("depositos.png",scale=25)   
def cuentas_corrientes():
    endpoint = "cuentas_corrientes"
    #datos para el llamado
    url = "https://api.estadisticasbcra.com/"+endpoint
    headers = {"Authorization": token}
    #Llamado
    data_json = requests.get(url, headers=headers).json()
    #Armamos una tabla con los datos
    data = pd.DataFrame(data_json)
    #Le asignamos la fecha como indice
    data.set_index('d', inplace=True, drop=True)
    data.to_csv('csv/bcra.csv')
    count = 0
    for data in pd.read_csv('csv/bcra.csv',encoding = 'ISO-8859-1',chunksize  = 1000):
        count += 1                          # counting the number of chunks
        lastlen = len(data)                 # finding the length of last chunk
        datalength = (count*1000 + lastlen - 1000) # length of total file
        rowsdiff = datalength - 900
    df = pd.read_csv('csv/bcra.csv',encoding = 'ISO-8859-1',skiprows = range(1,rowsdiff), nrows = 299)
    y= df['v']
    x = df['d']
    cotizacion = df["v"].iloc[-1]
    fig = go.Figure()
    fig = make_subplots(rows=2, cols=1, row_heights=[0.7, 0.3])
    fig.add_trace(go.Scatter(x=x, y=y, name=f'${cotizacion}    '))
    fig.update_xaxes(tickangle=45)
    fig.update_layout(title= f'cuentas_corrientes',xaxis_nticks=25)
    rsi = talib.RSI(y)
    fig.add_trace(go.Scatter(y=rsi,line=dict(color='fuchsia',width=1),name='rsi'), row=2, col=1)
    fig.write_image("cuentas_corrientes.png",scale=25)   
def cajas_ahorro():
    endpoint = "cajas_ahorro"
    #datos para el llamado
    url = "https://api.estadisticasbcra.com/"+endpoint
    headers = {"Authorization": token}
    #Llamado
    data_json = requests.get(url, headers=headers).json()
    #Armamos una tabla con los datos
    data = pd.DataFrame(data_json)
    #Le asignamos la fecha como indice
    data.set_index('d', inplace=True, drop=True)
    data.to_csv('csv/bcra.csv')
    count = 0
    for data in pd.read_csv('csv/bcra.csv',encoding = 'ISO-8859-1',chunksize  = 1000):
        count += 1                          # counting the number of chunks
        lastlen = len(data)                 # finding the length of last chunk
        datalength = (count*1000 + lastlen - 1000) # length of total file
        rowsdiff = datalength - 900
    df = pd.read_csv('csv/bcra.csv',encoding = 'ISO-8859-1',skiprows = range(1,rowsdiff), nrows = 299)
    y= df['v']
    x = df['d']
    cotizacion = df["v"].iloc[-1]
    fig = go.Figure()
    fig = make_subplots(rows=2, cols=1, row_heights=[0.7, 0.3])
    fig.add_trace(go.Scatter(x=x, y=y, name=f'${cotizacion}    '))
    fig.update_xaxes(tickangle=45)
    fig.update_layout(title= f'cajas_ahorro',xaxis_nticks=25)
    rsi = talib.RSI(y)
    fig.add_trace(go.Scatter(y=rsi,line=dict(color='fuchsia',width=1),name='rsi'), row=2, col=1)
    fig.write_image("cajas_ahorro.png",scale=25)   
def plazo_fijo():
    endpoint = "plazo_fijo"
    #datos para el llamado
    url = "https://api.estadisticasbcra.com/"+endpoint
    headers = {"Authorization": token}
    #Llamado
    data_json = requests.get(url, headers=headers).json()
    #Armamos una tabla con los datos
    data = pd.DataFrame(data_json)
    #Le asignamos la fecha como indice
    data.set_index('d', inplace=True, drop=True)
    data.to_csv('csv/bcra.csv')
    count = 0
    for data in pd.read_csv('csv/bcra.csv',encoding = 'ISO-8859-1',chunksize  = 1000):
        count += 1                          # counting the number of chunks
        lastlen = len(data)                 # finding the length of last chunk
        datalength = (count*1000 + lastlen - 1000) # length of total file
        rowsdiff = datalength - 900
    df = pd.read_csv('csv/bcra.csv',encoding = 'ISO-8859-1',skiprows = range(1,rowsdiff), nrows = 299)
    y= df['v']
    x = df['d']
    cotizacion = df["v"].iloc[-1]
    fig = go.Figure()
    fig = make_subplots(rows=2, cols=1, row_heights=[0.7, 0.3])
    fig.add_trace(go.Scatter(x=x, y=y, name=f'${cotizacion}    '))
    fig.update_xaxes(tickangle=45)
    fig.update_layout(title= f'plazo_fijo',xaxis_nticks=25)
    rsi = talib.RSI(y)
    fig.add_trace(go.Scatter(y=rsi,line=dict(color='fuchsia',width=1),name='rsi'), row=2, col=1)
    fig.write_image("plazo_fijo.png",scale=25)   
def prestamos():
    endpoint = "prestamos"
    #datos para el llamado
    url = "https://api.estadisticasbcra.com/"+endpoint
    headers = {"Authorization": token}
    #Llamado
    data_json = requests.get(url, headers=headers).json()
    #Armamos una tabla con los datos
    data = pd.DataFrame(data_json)
    #Le asignamos la fecha como indice
    data.set_index('d', inplace=True, drop=True)
    data.to_csv('csv/bcra.csv')
    count = 0
    for data in pd.read_csv('csv/bcra.csv',encoding = 'ISO-8859-1',chunksize  = 1000):
        count += 1                          # counting the number of chunks
        lastlen = len(data)                 # finding the length of last chunk
        datalength = (count*1000 + lastlen - 1000) # length of total file
        rowsdiff = datalength - 900
    df = pd.read_csv('csv/bcra.csv',encoding = 'ISO-8859-1',skiprows = range(1,rowsdiff), nrows = 299)
    y= df['v']
    x = df['d']
    cotizacion = df["v"].iloc[-1]
    fig = go.Figure()
    fig = make_subplots(rows=2, cols=1, row_heights=[0.7, 0.3])
    fig.add_trace(go.Scatter(x=x, y=y, name=f'${cotizacion}    '))
    fig.update_xaxes(tickangle=45)
    fig.update_layout(title= f'prestamos',xaxis_nticks=25)
    rsi = talib.RSI(y)
    fig.add_trace(go.Scatter(y=rsi,line=dict(color='fuchsia',width=1),name='rsi'), row=2, col=1)
    fig.write_image("prestamos.png",scale=25)   
def LEBACs():
    endpoint = "LEBACs"
    #datos para el llamado
    url = "https://api.estadisticasbcra.com/"+endpoint
    headers = {"Authorization": token}
    #Llamado
    data_json = requests.get(url, headers=headers).json()
    #Armamos una tabla con los datos
    data = pd.DataFrame(data_json)
    #Le asignamos la fecha como indice
    data.set_index('d', inplace=True, drop=True)
    data.to_csv('csv/bcra.csv')
    count = 0
    for data in pd.read_csv('csv/bcra.csv',encoding = 'ISO-8859-1',chunksize  = 1000):
        count += 1                          # counting the number of chunks
        lastlen = len(data)                 # finding the length of last chunk
        datalength = (count*1000 + lastlen - 1000) # length of total file
        rowsdiff = datalength - 900
    df = pd.read_csv('csv/bcra.csv',encoding = 'ISO-8859-1',skiprows = range(1,rowsdiff), nrows = 299)
    y= df['v']
    x = df['d']
    cotizacion = df["v"].iloc[-1]
    fig = go.Figure()
    fig = make_subplots(rows=2, cols=1, row_heights=[0.7, 0.3])
    fig.add_trace(go.Scatter(x=x, y=y, name=f'${cotizacion}    '))
    fig.update_xaxes(tickangle=45)
    fig.update_layout(title= f'LEBACs',xaxis_nticks=25)
    rsi = talib.RSI(y)
    fig.add_trace(go.Scatter(y=rsi,line=dict(color='fuchsia',width=1),name='rsi'), row=2, col=1)
    fig.write_image("LEBACs.png",scale=25)   
def LELIQs():
    endpoint = "LELIQs"
    #datos para el llamado
    url = "https://api.estadisticasbcra.com/"+endpoint
    headers = {"Authorization": token}
    #Llamado
    data_json = requests.get(url, headers=headers).json()
    #Armamos una tabla con los datos
    data = pd.DataFrame(data_json)
    #Le asignamos la fecha como indice
    data.set_index('d', inplace=True, drop=True)
    data.to_csv('csv/bcra.csv')
    count = 0
    for data in pd.read_csv('csv/bcra.csv',encoding = 'ISO-8859-1',chunksize  = 1000):
        count += 1                          # counting the number of chunks
        lastlen = len(data)                 # finding the length of last chunk
        datalength = (count*1000 + lastlen - 1000) # length of total file
        rowsdiff = datalength - 900
    df = pd.read_csv('csv/bcra.csv',encoding = 'ISO-8859-1',skiprows = range(1,rowsdiff), nrows = 299)
    y= df['v']
    x = df['d']
    cotizacion = df["v"].iloc[-1]
    fig = go.Figure()
    fig = make_subplots(rows=2, cols=1, row_heights=[0.7, 0.3])
    fig.add_trace(go.Scatter(x=x, y=y, name=f'${cotizacion}    '))
    fig.update_xaxes(tickangle=45)
    fig.update_layout(title= f'LELIQs',xaxis_nticks=25)
    rsi = talib.RSI(y)
    fig.add_trace(go.Scatter(y=rsi,line=dict(color='fuchsia',width=1),name='rsi'), row=2, col=1)
    fig.write_image("LELIQs.png",scale=25)   
def CER():
    endpoint = "CER"
    #datos para el llamado
    url = "https://api.estadisticasbcra.com/"+endpoint
    headers = {"Authorization": token}
    #Llamado
    data_json = requests.get(url, headers=headers).json()
    #Armamos una tabla con los datos
    data = pd.DataFrame(data_json)
    #Le asignamos la fecha como indice
    data.set_index('d', inplace=True, drop=True)
    data.to_csv('csv/bcra.csv')
    count = 0
    for data in pd.read_csv('csv/bcra.csv',encoding = 'ISO-8859-1',chunksize  = 1000):
        count += 1                          # counting the number of chunks
        lastlen = len(data)                 # finding the length of last chunk
        datalength = (count*1000 + lastlen - 1000) # length of total file
        rowsdiff = datalength - 900
    df = pd.read_csv('csv/bcra.csv',encoding = 'ISO-8859-1',skiprows = range(1,rowsdiff), nrows = 299)
    y= df['v']
    x = df['d']
    cotizacion = df["v"].iloc[-1]
    fig = go.Figure()
    fig = make_subplots(rows=2, cols=1, row_heights=[0.7, 0.3])
    fig.add_trace(go.Scatter(x=x, y=y, name=f'${cotizacion}    '))
    fig.update_xaxes(tickangle=45)
    fig.update_layout(title= f'CER',xaxis_nticks=25)
    rsi = talib.RSI(y)
    fig.add_trace(go.Scatter(y=rsi,line=dict(color='fuchsia',width=1),name='rsi'), row=2, col=1)
    fig.write_image("CER.png",scale=25)   

cotizacion_oficial()
base_monetaria()
base_monetaria_usd()
reservas()
circulacion_monetaria()
billetes_y_monedas()
efectivo_en_ent_fin()
depositos_cuenta_ent_fin()
depositos()
cuentas_corrientes()
cajas_ahorro()
plazo_fijo()
prestamos()
LEBACs()
LELIQs()
CER()
