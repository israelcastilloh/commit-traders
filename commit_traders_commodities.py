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

## Commodities Futures of CoT
def DownloadCommodities(start_year, end_year):
    yearly_report = {}
    years_to_download =  [str(x) for x in range(start_year, end_year+1, 1)]
    #years_to_download = ['2015', '2016', '2017', '2018', '2019', '2020']
    os.mkdir('../commodities')
    for year in years_to_download:
        print('File download Year ' + year)
        url = 'https://www.cftc.gov/files/dea/history/fut_disagg_xls_'+year+'.zip'
        path_to_zip_file = '../commodities/fut_disagg_xls_'+year+'.zip'
        urllib.request.urlretrieve(url, path_to_zip_file)
        with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
            zip_ref.extractall('../commodities/'+year)
        path = '../commodities/'+year
        yearly_report[year] = pd.read_excel(path+'/f_year.xls')
    return yearly_report

## After Downloading Give me the Reports in DF
def CommoditiesReports(start_year, end_year, *current_year):
    yearly_report = {}
    years_to_download =  [str(x) for x in range(start_year, end_year+1, 1)]
    for year in years_to_download:
        path = '../commodities/'+year
        yearly_report[year] = pd.read_excel(path+'/f_year.xls')
    if current_year:
        return yearly_report[str(*current_year)]
    else:
        return yearly_report

## Show me the Data Points reported this year
def ReportPoints(year):
    overview_year = CommoditiesReports(year, year, year).head(-1)
    report_points = overview_year.T.reset_index()
    report_points = report_points['index'].unique()
    #print(report_points)
    print("# Data Points Reported in this Commodities Fut CoT: ", len(report_points))
    return report_points

## Show me which assets are reported this year
def ReportAssets(year):
    assets_reported = CommoditiesReports(year, year, year)['Market_and_Exchange_Names'].unique()
    print("# Assets Reported in this Commodities Fut CoT: ", len(assets_reported))
    return assets_reported

## VAMOS A LIMPIAR LOS DATOS QUE NO NOS INTERESAN
def not_interesting_pile():
    not_interesting = [
        "CFTC_Region_Code", "CFTC_Commodity_Code",
    'CFTC_Market_Code', 'As_of_Date_In_Form_YYMMDD', 'CFTC_Contract_Market_Code',
    'Tot_Rept_Positions_Long_All',
       'Tot_Rept_Positions_Short_All', 'Open_Interest_Old',
       'Prod_Merc_Positions_Long_Old', 'Prod_Merc_Positions_Short_Old',
       'Swap_Positions_Long_Old', 'Swap_Positions_Short_Old',
       'Swap_Positions_Spread_Old', 'M_Money_Positions_Long_Old',
       'M_Money_Positions_Short_Old', 'M_Money_Positions_Spread_Old',
       'Other_Rept_Positions_Long_Old', 'Other_Rept_Positions_Short_Old',
       'Other_Rept_Positions_Spread_Old', 'Tot_Rept_Positions_Long_Old',
       'Tot_Rept_Positions_Short_Old', 'NonRept_Positions_Long_Old',
       'NonRept_Positions_Short_Old', 'Open_Interest_Other',
       'Prod_Merc_Positions_Long_Other',
       'Prod_Merc_Positions_Short_Other', 'Swap_Positions_Long_Other',
       'Swap_Positions_Short_Other', 'Swap_Positions_Spread_Other',
       'M_Money_Positions_Long_Other', 'M_Money_Positions_Short_Other',
       'M_Money_Positions_Spread_Other',
       'Other_Rept_Positions_Long_Other',
       'Other_Rept_Positions_Short_Other',
       'Other_Rept_Positions_Spread_Othr',
       'Tot_Rept_Positions_Long_Other', 'Tot_Rept_Positions_Short_Other',
       'NonRept_Positions_Long_Other', 'NonRept_Positions_Short_Other',
       'Change_in_Open_Interest_All', 'Change_in_Prod_Merc_Long_All',
       'Change_in_Prod_Merc_Short_All', 'Change_in_Swap_Long_All',
       'Change_in_Swap_Short_All', 'Change_in_Swap_Spread_All',
       'Change_in_M_Money_Long_All', 'Change_in_M_Money_Short_All',
       'Change_in_M_Money_Spread_All', 'Change_in_Other_Rept_Long_All',
       'Change_in_Other_Rept_Short_All',
       'Change_in_Other_Rept_Spread_All', 'Change_in_Tot_Rept_Long_All',
       'Change_in_Tot_Rept_Short_All', 'Change_in_NonRept_Long_All',
       'Change_in_NonRept_Short_All', 'Pct_of_Open_Interest_All',
       'Pct_of_OI_Prod_Merc_Long_All', 'Pct_of_OI_Prod_Merc_Short_All',
       'Pct_of_OI_Swap_Long_All', 'Pct_of_OI_Swap_Short_All',
       'Pct_of_OI_Swap_Spread_All', 'Pct_of_OI_M_Money_Long_All',
       'Pct_of_OI_M_Money_Short_All', 'Pct_of_OI_M_Money_Spread_All',
       'Pct_of_OI_Other_Rept_Long_All', 'Pct_of_OI_Other_Rept_Short_All',
       'Pct_of_OI_Other_Rept_Spread_All', 'Pct_of_OI_Tot_Rept_Long_All',
       'Pct_of_OI_Tot_Rept_Short_All', 'Pct_of_OI_NonRept_Long_All',
       'Pct_of_OI_NonRept_Short_All', 'Pct_of_Open_Interest_Old',
       'Pct_of_OI_Prod_Merc_Long_Old', 'Pct_of_OI_Prod_Merc_Short_Old',
       'Pct_of_OI_Swap_Long_Old', 'Pct_of_OI_Swap_Short_Old',
       'Pct_of_OI_Swap_Spread_Old', 'Pct_of_OI_M_Money_Long_Old',
       'Pct_of_OI_M_Money_Short_Old', 'Pct_of_OI_M_Money_Spread_Old',
       'Pct_of_OI_Other_Rept_Long_Old', 'Pct_of_OI_Other_Rept_Short_Old',
       'Pct_of_OI_Other_Rept_Spread_Old', 'Pct_of_OI_Tot_Rept_Long_Old',
       'Pct_of_OI_Tot_Rept_Short_Old', 'Pct_of_OI_NonRept_Long_Old',
       'Pct_of_OI_NonRept_Short_Old', 'Pct_of_Open_Interest_Other',
       'Pct_of_OI_Prod_Merc_Long_Other',
       'Pct_of_OI_Prod_Merc_Short_Other', 'Pct_of_OI_Swap_Long_Other',
       'Pct_of_OI_Swap_Short_Other', 'Pct_of_OI_Swap_Spread_Other',
       'Pct_of_OI_M_Money_Long_Other', 'Pct_of_OI_M_Money_Short_Other',
       'Pct_of_OI_M_Money_Spread_Other',
       'Pct_of_OI_Other_Rept_Long_Other',
       'Pct_of_OI_Other_Rept_Short_Other',
       'Pct_of_OI_Other_Rept_Spread_Othr',
       'Pct_of_OI_Tot_Rept_Long_Other', 'Pct_of_OI_Tot_Rept_Short_Other',
       'Pct_of_OI_NonRept_Long_Other', 'Pct_of_OI_NonRept_Short_Other',
       'Traders_Tot_All', 'Traders_Prod_Merc_Long_All',
       'Traders_Prod_Merc_Short_All', 'Traders_Swap_Long_All',
       'Traders_Swap_Short_All', 'Traders_Swap_Spread_All',
       'Traders_M_Money_Long_All', 'Traders_M_Money_Short_All',
       'Traders_M_Money_Spread_All', 'Traders_Other_Rept_Long_All',
       'Traders_Other_Rept_Short_All', 'Traders_Other_Rept_Spread_All',
       'Traders_Tot_Rept_Long_All', 'Traders_Tot_Rept_Short_All',
       'Traders_Tot_Old', 'Traders_Prod_Merc_Long_Old',
       'Traders_Prod_Merc_Short_Old', 'Traders_Swap_Long_Old',
       'Traders_Swap_Short_Old', 'Traders_Swap_Spread_Old',
       'Traders_M_Money_Long_Old', 'Traders_M_Money_Short_Old',
       'Traders_M_Money_Spread_Old', 'Traders_Other_Rept_Long_Old',
       'Traders_Other_Rept_Short_Old', 'Traders_Other_Rept_Spread_Old',
       'Traders_Tot_Rept_Long_Old', 'Traders_Tot_Rept_Short_Old',
       'Traders_Tot_Other', 'Traders_Prod_Merc_Long_Other',
       'Traders_Prod_Merc_Short_Other', 'Traders_Swap_Long_Other',
       'Traders_Swap_Short_Other', 'Traders_Swap_Spread_Other',
       'Traders_M_Money_Long_Other', 'Traders_M_Money_Short_Other',
       'Traders_M_Money_Spread_Other', 'Traders_Other_Rept_Long_Other',
       'Traders_Other_Rept_Short_Other',
       'Traders_Other_Rept_Spread_Other', 'Traders_Tot_Rept_Long_Other',
       'Traders_Tot_Rept_Short_Other', 'Conc_Gross_LE_4_TDR_Long_All',
       'Conc_Gross_LE_4_TDR_Short_All', 'Conc_Gross_LE_8_TDR_Long_All',
       'Conc_Gross_LE_8_TDR_Short_All', 'Conc_Net_LE_4_TDR_Long_All',
       'Conc_Net_LE_4_TDR_Short_All', 'Conc_Net_LE_8_TDR_Long_All',
       'Conc_Net_LE_8_TDR_Short_All', 'Conc_Gross_LE_4_TDR_Long_Old',
       'Conc_Gross_LE_4_TDR_Short_Old', 'Conc_Gross_LE_8_TDR_Long_Old',
       'Conc_Gross_LE_8_TDR_Short_Old', 'Conc_Net_LE_4_TDR_Long_Old',
       'Conc_Net_LE_4_TDR_Short_Old', 'Conc_Net_LE_8_TDR_Long_Old',
       'Conc_Net_LE_8_TDR_Short_Old', 'Conc_Gross_LE_4_TDR_Long_Other',
       'Conc_Gross_LE_4_TDR_Short_Other',
       'Conc_Gross_LE_8_TDR_Long_Other',
       'Conc_Gross_LE_8_TDR_Short_Other', 'Conc_Net_LE_4_TDR_Long_Other',
       'Conc_Net_LE_4_TDR_Short_Other', 'Conc_Net_LE_8_TDR_Long_Other',
       'Conc_Net_LE_8_TDR_Short_Other', 'Conc_Net_LE_8_TDR_Short_Other',
       'CFTC_SubGroup_Code', 'FutOnly_or_Combined']
    return not_interesting

## Show me the DF of an Asset
def Asset(asset, year,  *start_date, **end_date):
    not_interesting = not_interesting_pile()
    if start_date or end_date:
        yearly_report = CommoditiesReports(start_date[0], start_date[1])
        df = pd.DataFrame()
        for i in range(start_date[0], start_date[1]+1):
            dict_new = yearly_report[str(i)]
            df = df.append(dict_new, ignore_index=True)
        yearly_report = df.set_index("Market_and_Exchange_Names").\
                loc[asset].reset_index().set_index('Report_Date_as_MM_DD_YYYY')
        return yearly_report.T.drop(not_interesting).T.sort_index()
    else:
        yearly_report = CommoditiesReports(year, year, year).set_index("Market_and_Exchange_Names").\
                        loc[asset].reset_index().set_index('Report_Date_as_MM_DD_YYYY')
        return yearly_report.T.drop(not_interesting).T.sort_index()

def OpenInterest(asset, year,  *start_date, **end_date):
    if start_date or end_date:
        open_interest = pd.DataFrame(Asset(asset, year, start_date[0], start_date[1])['Open_Interest_All'])
        return open_interest
    else:
        open_interest = pd.DataFrame(Asset(asset, year)['Open_Interest_All'])
    return open_interest


def ProducerMerchantPosition(asset, year,  *start_date, **end_date):
    dealer_points = ['Prod_Merc_Positions_Long_ALL', 'Prod_Merc_Positions_Short_ALL']
    if start_date or end_date:
        ProducerMerchantPosition = Asset(asset, year, start_date[0], start_date[1])[dealer_points]
        return ProducerMerchantPosition
    else:
        ProducerMerchantPosition = Asset(asset, year)[dealer_points]
    return ProducerMerchantPosition


def SwapDealerPosition(asset, year,  *start_date, **end_date):
    dealer_points = ['Swap_Positions_Long_All', 'Swap__Positions_Short_All', 'Swap__Positions_Spread_All']
    if start_date or end_date:
        SwapDealerPosition = Asset(asset, year, start_date[0], start_date[1])[dealer_points]
        return SwapDealerPosition
    else:
        SwapDealerPosition = Asset(asset, year)[dealer_points]
    return SwapDealerPosition

def ManagedMoneyPosition(asset, year,  *start_date, **end_date):
    dealer_points = ['M_Money_Positions_Long_ALL', 'M_Money_Positions_Short_ALL', 'M_Money_Positions_Spread_ALL']
    if start_date or end_date:
        ManagedMoneyPosition = Asset(asset, year, start_date[0], start_date[1])[dealer_points]
        return ManagedMoneyPosition
    else:
        ManagedMoneyPosition = Asset(asset, year)[dealer_points]
    return ManagedMoneyPosition

def OtherRepPosition(asset, year,  *start_date, **end_date):
    dealer_points = ['Other_Rept_Positions_Long_ALL', 'Other_Rept_Positions_Short_ALL',
                     'Other_Rept_Positions_Spread_ALL']
    if start_date or end_date:
        OtherRepPosition = Asset(asset, year, start_date[0], start_date[1])[dealer_points]
        return OtherRepPosition
    else:
        OtherRepPosition = Asset(asset, year)[dealer_points]
    return OtherRepPosition

def NonRepPosition(asset, year,  *start_date, **end_date):
    dealer_points = ['NonRept_Positions_Long_All', 'NonRept_Positions_Short_All']
    if start_date or end_date:
        NonRepPosition = Asset(asset, year, start_date[0], start_date[1])[dealer_points]
        return NonRepPosition
    else:
        NonRepPosition = Asset(asset, year)[dealer_points]
    return NonRepPosition
