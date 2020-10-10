# commit-traders 

## Uso:
```python
from commit_traders_financial import * 
from commit_traders_commodities import *
```

## 1) Futuros Financieros
  
  ```python
  DownloadFinancial(start_year, end_year)
  ```
  Te entrega los archivos en formato Excel, creando un directorio "financial" con directorios por año.
  
  ```python
  FinancialReports(start_year, end_year, *current_year)
  ```
  Arroja un diccionario que contiene los reportes desde start_year hasta end_year. Si se añade current_year, se muestra un DataFrame del año específicado.
  
  ```python
  ReportPoints(year)
  ```
  Muestra una lista de los Puntos de Reporte que aparecen en el Commitment of Trader del año especificado.  
  
  ```python
  ReportAssets(year)
  ```
  Muestra una lista de los Activos reportados durante el año específicado. 
 
  ```python
  Asset(asset, year,  *start_date, **end_date)
  ```
  Muestra la información de un Activo (str), del año especificado.
  
  
  ```python
  OpenInterest(asset, year,  *start_date, **end_date)
  ```
  Muestra los historicos del Open Interest de un Activo, como un DataFrame.
  
  ```python
  DealerPosition(asset, year, *start_date, **end_date)
  ManagerPosition(asset, year,  *start_date, **end_date)
  LevFundsPosition(asset, year,  *start_date, **end_date)
  OtherRepPosition(asset, year,  *start_date, **end_date)
  ```
  Muestra las posiciones de los **Intermediarios**, tanto de Compra, Venta y Spreading, como un DataFrame.
  
  Muestra las posiciones de los **Gestores de Capital**, tanto de Compra, Venta y Spreading, como un DataFrame.
  
  Muestra las posiciones de los **Fondos Apalancados**, tanto de Compra, Venta y Spreading, como un DataFrame.
  
  Muestra las posiciones de Otros **Reportables**, tanto de Compra, Venta y Spreading, como un DataFrame.
  

## 2) Futuros de Materias Primas (Commodities)
  
  ```python
  DownloadCommodities(start_year, end_year)
  ```
  Te entrega los archivos en formato Excel, creando un directorio "commodities" con directorios por año. 
  
  ```python
  CommoditiesReports(start_year, end_year, *current_year)
  ```
   Arroja un diccionario que contiene los reportes desde start_year hasta end_year. Si se añade current_year, se muestra un DataFrame del año específicado. 
  
  ```python
  ReportPoints(year)
  ```  
   Muestra una lista de los Puntos de Reporte que aparecen en el Commitment of Trader del año especificado.  
  
  ```python
  ReportAssets(year)
  ```
   Muestra una lista de los Activos reportados durante el año específicado. 
  
  ```python
  Asset(asset, year,  *start_date, **end_date)
  ```
   Muestra la información de un Activo (str), del año especificado.
   
  ```python
  OpenInterest(asset, year,  *start_date, **end_date)
  ```
   Muestra los historicos del Open Interest de un Activo, como un DataFrame.

  ```python
  ProducerMerchantPosition(asset, year,  *start_date, **end_date)
  SwapDealerPosition(asset, year,  *start_date, **end_date)
  ManagedMoneyPosition(asset, year,  *start_date, **end_date)
  OtherRepPosition(asset, year,  *start_date, **end_date)
  NonRepPosition(asset, year,  *start_date, **end_date)
   ```
  
  Muestra las posiciones de los **Productores y Mercantes**, tanto de Compra, Venta y Spreading, como un DataFrame.
  
  Muestra las posiciones de los **Intermediarios de Swap**, tanto de Compra, Venta y Spreading, como un DataFrame.
  
  Muestra las posiciones de los **Gestores de Capital**, tanto de Compra, Venta y Spreading, como un DataFrame.
  
  Muestra las posiciones de **Otros Reportables**, tanto de Compra, Venta y Spreading, como un DataFrame.
  
  Muestra las posiciones de los **No Reportables**, tanto de Compra, Venta y Spreading, como un DataFrame.
 
 
```python
'''
Desarrollado por: Israel Castillo. // Ingenierio Financiero // castillo.israelh@gmail.com
En colaboración y supervisión de: IteraCapital
'''

