'''
-----------------------------------------------------------------------------
Developed by: Israel Castillo / Financial Engineer ---> castillo.israel@gmail.com
In collaboration and supervision of IteraCapital
----------------------------------------------------------------------------
'''

import urllib.request
import zipfile
import pandas as pd
import plotly
from plotly.offline import iplot, init_notebook_mode
init_notebook_mode(connected = True)
import plotly.graph_objs as go
import yfinance as yf
import os

## Financial Futures of CoT
def DownloadFinancial(start_year, end_year):
    yearly_report = {}
    years_to_download =  [str(x) for x in range(start_year, end_year+1, 1)]
    #years_to_download = ['2015', '2016', '2017', '2018', '2019', '2020']
    os.mkdir('../financial')
    for year in years_to_download:
        print('File download Year ' + year)
        url = 'https://www.cftc.gov/files/dea/history/fut_fin_xls_'+year+'.zip'
        path_to_zip_file = '../financial/fut_disagg_xls_'+year+'.zip'
        urllib.request.urlretrieve(url, path_to_zip_file)
        with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
            zip_ref.extractall('../financial/'+year)
        path = '../financial/'+year
        yearly_report[year] = pd.read_excel(path+'/FinFutYY.xls')

## After Downloading Give me the FinancialReports in DF
def FinancialReports(start_year, end_year, *current_year):
    yearly_report = {}
    years_to_download =  [str(x) for x in range(start_year, end_year+1, 1)]
    for year in years_to_download:
        path = '../financial/'+year
        yearly_report[year] = pd.read_excel(path+'/FinFutYY.xls')
    if current_year:
        return yearly_report[str(*current_year)]
    else:
        return yearly_report

## Show me the Data Points reported this year
def ReportPoints(year):
    overview_year = FinancialReports(year, year, year).head(-1)
    report_points = overview_year.T.reset_index()
    report_points = report_points['index'].unique()
    #print(report_points)
    print("# Data Points Reported in this Fin Fut CoT: ", len(report_points))
    return report_points

## Show me which assets are reported this year
def ReportAssets(year):
    assets_reported = FinancialReports(year, year, year)['Market_and_Exchange_Names'].unique()
    print("# Assets Reported in this Fin Fut CoT: ", len(assets_reported))
    return assets_reported

## VAMOS A LIMPIAR LOS DATOS QUE NO NOS INTERESAN
def not_interesting_pile():
    not_interesting = ['CFTC_Market_Code', 'As_of_Date_In_Form_YYMMDD', 'CFTC_Contract_Market_Code',
    'CFTC_Region_Code', 'CFTC_Commodity_Code', 'CFTC_SubGroup_Code',
    'Change_in_Open_Interest_All','Change_in_Dealer_Long_All',
    'Change_in_Dealer_Short_All', 'Traders_Dealer_Long_All',
    'Change_in_Dealer_Spread_All','Change_in_Asset_Mgr_Long_All',
    'Change_in_Asset_Mgr_Short_All','Change_in_Asset_Mgr_Spread_All',
    'Change_in_Lev_Money_Long_All','Change_in_Lev_Money_Short_All',
    'Change_in_Lev_Money_Spread_All','Change_in_Other_Rept_Long_All',
    'Change_in_Other_Rept_Short_All','Change_in_Other_Rept_Spread_All',
    'Change_in_Tot_Rept_Long_All','Change_in_Tot_Rept_Short_All',
    'Change_in_NonRept_Long_All','Change_in_NonRept_Short_All',
    'Pct_of_Open_Interest_All', 'Pct_of_OI_Dealer_Long_All',
    'Pct_of_OI_Dealer_Short_All', 'Pct_of_OI_Dealer_Spread_All',
    'Pct_of_OI_Asset_Mgr_Long_All', 'Pct_of_OI_Asset_Mgr_Short_All',
    'Pct_of_OI_Asset_Mgr_Spread_All', 'Pct_of_OI_Lev_Money_Long_All',
    'Pct_of_OI_Lev_Money_Short_All', 'Pct_of_OI_Lev_Money_Spread_All',
    'Pct_of_OI_Other_Rept_Long_All', 'Pct_of_OI_Other_Rept_Short_All',
    'Pct_of_OI_Other_Rept_Spread_All', 'Pct_of_OI_Tot_Rept_Long_All',
    'Pct_of_OI_Tot_Rept_Short_All', 'Pct_of_OI_NonRept_Long_All',
    'Pct_of_OI_NonRept_Short_All', 'Traders_Tot_All',
    'Traders_Dealer_Short_All', 'Traders_Dealer_Spread_All',
    'Traders_Asset_Mgr_Long_All', 'Traders_Asset_Mgr_Short_All',
    'Traders_Asset_Mgr_Spread_All', 'Traders_Lev_Money_Long_All',
    'Traders_Lev_Money_Short_All', 'Traders_Lev_Money_Spread_All',
    'Traders_Other_Rept_Long_All', 'Traders_Other_Rept_Short_All',
    'Traders_Other_Rept_Spread_All', 'Traders_Tot_Rept_Long_All',
    'Traders_Tot_Rept_Short_All', 'Conc_Gross_LE_4_TDR_Long_All',
    'Conc_Gross_LE_4_TDR_Short_All', 'Conc_Gross_LE_8_TDR_Long_All',
    'Conc_Gross_LE_8_TDR_Short_All', 'Conc_Net_LE_4_TDR_Long_All',
    'Conc_Net_LE_4_TDR_Short_All', 'Conc_Net_LE_8_TDR_Long_All',
    'Conc_Net_LE_8_TDR_Short_All', 'FutOnly_or_Combined',
    'Tot_Rept_Positions_Long_All', 'Tot_Rept_Positions_Short_All']
    return not_interesting

## Show me the DF of an Asset
def Asset(asset, year,  *start_date, **end_date):
    not_interesting = not_interesting_pile()
    if start_date or end_date:
        yearly_report = FinancialReports(start_date[0], start_date[1])
        df = pd.DataFrame()
        for i in range(start_date[0], start_date[1]+1):
            dict_new = yearly_report[str(i)]
            df = df.append(dict_new, ignore_index=True)
        yearly_report = df.set_index("Market_and_Exchange_Names").\
                loc[asset].reset_index().set_index('Report_Date_as_MM_DD_YYYY')
        return yearly_report.T.drop(not_interesting).T.sort_index()
    else:
        yearly_report = FinancialReports(year, year, year).set_index("Market_and_Exchange_Names").\
                        loc[asset].reset_index().set_index('Report_Date_as_MM_DD_YYYY')
        return yearly_report.T.drop(not_interesting).T.sort_index()

def OpenInterest(asset, year,  *start_date, **end_date):
    if start_date or end_date:
        open_interest = pd.DataFrame(Asset(asset, year, start_date[0], start_date[1])['Open_Interest_All'])
        return open_interest
    else:
        open_interest = pd.DataFrame(Asset(asset, year)['Open_Interest_All'])
    return open_interest

def DealerPosition(asset, year,  *start_date, **end_date):
    dealer_points = ['Dealer_Positions_Long_All', 'Dealer_Positions_Short_All','Dealer_Positions_Spread_All']
    if start_date or end_date:
        DealerPosition = Asset(asset, year, start_date[0], start_date[1])[dealer_points]
        return DealerPosition
    else:
        DealerPosition = Asset(asset, year)[dealer_points]
    return DealerPosition

def ManagerPosition(asset, year,  *start_date, **end_date):
    manager_points = ['Asset_Mgr_Positions_Long_All', 'Asset_Mgr_Positions_Short_All',
                      'Asset_Mgr_Positions_Spread_All']
    if start_date or end_date:
        ManagerPosition = Asset(asset, year, start_date[0], start_date[1])[manager_points]
        return ManagerPosition
    else:
        ManagerPosition = Asset(asset, year)[manager_points]
    return ManagerPosition

def LevFundsPosition(asset, year,  *start_date, **end_date):
    levfunds_points = ['Lev_Money_Positions_Long_All', 'Lev_Money_Positions_Short_All',
                      'Lev_Money_Positions_Spread_All']
    if start_date or end_date:
        LevFundsPosition = Asset(asset, year, start_date[0], start_date[1])[levfunds_points]
        return LevFundsPosition
    else:
        LevFundsPosition = Asset(asset, year)[levfunds_points]
    return LevFundsPosition

def OtherRepPosition(asset, year,  *start_date, **end_date):
    otherrep_pos = ['Other_Rept_Positions_Long_All', 'Other_Rept_Positions_Short_All',
                                        'Other_Rept_Positions_Spread_All']
    if start_date or end_date:
        OtherRepPosition = Asset(asset, year, start_date[0], start_date[1])[otherrep_pos]
        return OtherRepPosition
    else:
        OtherRepPosition = Asset(asset, year)[otherrep_pos]
    return OtherRepPosition
