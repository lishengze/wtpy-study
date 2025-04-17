import akshare as ak
import pandas as pd

def get_all_a_share_codes():
    stock_info_df = ak.stock_info_a_code_name()
    # stock_codes = stock_info_df['代码'].tolist()
    df = pd.DataFrame(stock_info_df)
    df.to_csv('A_market_codes.csv')    
    # return stock_codes

def get_a_share_hist_data():
    stock_code = "600519"  # 以贵州茅台为例，你可以替换为其他股票代码
    start_date = "20100101"
    end_date = "20250413"
    stock_hist = ak.stock_zh_a_hist(symbol = stock_code, start_date = start_date, end_date = end_date, adjust = "qfq")
    df = pd.DataFrame(stock_hist)
    df.to_csv('a_share_hist_data.csv', index = False)
    print("数据已保存为a_share_hist_data.csv")

def get_stock_market_value():
    # 获取贵州茅台（600519）的实时行情数据
    stock_info = ak.stock_zh_a_spot_em(symbol="600519")
    # 获取总市值，单位为万元
    total_market_value = stock_info['总市值'].values[0]
    # 获取流通市值，单位为万元
    circulating_market_value = stock_info['流通市值'].values[0]

    print(f"贵州茅台总市值: {total_market_value} 万元")
    print(f"贵州茅台流通市值: {circulating_market_value} 万元")
    
if __name__ == '__main__':
    # get_all_a_share_codes()
    get_stock_market_value()
