import pandas as pd

class DataLoader:
    def load_data(self):
        try:
            # 注意路径：data/sensor_data.csv
            df = pd.read_csv("data/sensor_data.csv")
            df['date'] = pd.to_datetime(df['date'])
            return df
        except FileNotFoundError:
            print("未找到数据文件，返回空数据集")
            return pd.DataFrame()
