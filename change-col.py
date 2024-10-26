import os
import pandas as pd

# مسیر پوشه حاوی فایلهای CSV
directory = 'D:/Results-V2'

# خواندن هر فایل CSV در پوشه و تغییر جای سطرها و ستون‌ها
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        file_path = os.path.join(directory, filename)

        # خواندن فایل CSV به کمک pandas
        df = pd.read_csv(file_path, header=None)

        # تغییر محورهای سطرها و ستون‌ها و ذخیره فایل
        df = df.transpose()
        df.to_csv(file_path, index=False, header=False)
