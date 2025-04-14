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


if __name__ == '__main__':
    get_all_a_share_codes()
