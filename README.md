# commit-traders

## It is important to have these 2 at the beginning of our Jupyter File, in order to have all the useful functions.
* %run commit_traders_financial.ipynb
* %run commit_traders_commodities.ipynb

## How to use this repo? 

## 1) Financial Futures
  ### Functions Available:
  * **DownloadFinancial(start_year, end_year)**
    - Gives you the excel files, creating a new directory "financial" with folders named by each year.
  * **FinancialReports(start_year, end_year, current_year)**
    - Throws a dictionary that contains start_year to end_year report of all assets, if you add current_year, shows a DF of the current year.
  * **ReportPoints(year)**
    - Shows the Report Points in the CoT report of the specified year.
  * **ReportAssets(year)**
    - Shows all the assets reported in the specified year.
  * **Asset(asset, year,  _start_date, _end_date)**
    - Throws the info of a particular Asset (str) as a DF.
  * **OpenInterest(asset, year,  _start_date, _end_date)**
    - Show the historical for Open Interest of a particular asset as a DF.
  * **DealerPosition(asset, year,  _start_date, _end_date)**
    - Shows Dealers' Positions. (Long, short, Spreading) as DF.
  * **ManagerPosition(asset, year,  _start_date, _end_date)**
    - Shows Managers' Positions. (Long, short, Spreading) as DF.
  * **LevFundsPosition(asset, year,  _start_date, _end_date)**
    - Shows Leveraged Funds' Position.s (Long, short, Spreading) as DF.
  * **OtherRepPosition(asset, year,  _start_date, _end_date)**
    - Shows Other Reported Positions. (Long, short, Spreading) as DF.

## 2) Commodities Futures
  ### Functions Available:
  * **DownloadCommodities(start_year, end_year)**
  * - Gives you the excel files, creating a new directory "commodities" with folders named by each year.
  **CommoditiesReports(start_year, end_year, current_year)**
    - Throws a dictionary that contains start_year to end_year report of all assets, if you add current_year, shows a DF of the current year.
  * **ReportPoints(year)**
    - Shows the Report Points in the CoT report.
  * **ReportAssets(year)**
    - Shows all the assets reported in the specified year.
  * **Asset(asset, year,  _start_date, _end_date)**
    - Throws the info of a particular Asset (str) as a DF.
  * **OpenInterest(asset, year,  _start_date, _end_date)**
    - Show the historical for Open Interest of a particular asset as a DF.
  * **ProducerMerchantPosition(asset, year,  _start_date, _end_date)**
    - Shows Producer & Merchant's Positions. (Long, short, Spreading) as DF.
  * **SwapDealerPosition(asset, year,  _start_date, _end_date)**
    - Shows Dealers' Positions. (Long, short, Spreading) as DF.
  * **ManagedMoneyPosition(asset, year,  _start_date, _end_date)**
    - Shows Managed Money Positions. (Long, short, Spreading) as DF.
  * **OtherRepPosition(asset, year,  _start_date, _end_date)**
    - Shows Other Reported Positions. (Long, short, Spreading) as DF.
  * **NonRepPosition(asset, year,  _start_date, _end_date)**
    - Shows Non Reported Positions. (Long, short, Spreading) as DF.

Developed by: Israel Castillo. Financial Engineer. castillo.israelh@gmail.com
