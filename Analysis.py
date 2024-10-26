import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# مسیر پوشه حاوی فایلهای CSV
directory = "D:/Results-V2/"

# دیتافریم خالی برای ذخیره نتایج نهایی
final_df = pd.DataFrame()

# خواندن هر فایل CSV در پوشه
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        file_path = os.path.join(directory, filename)

        # خواندن فایل CSV به کمک pandas
        df = pd.read_csv(file_path)

        # افزودن داده‌های هر فایل به دیتافریم نهایی
        final_df = pd.concat([final_df, df], ignore_index=True)

# انتخاب ستون‌های مربوط به نتایج الگوریتم‌ها و ستون "Algorithms"
df = final_df.iloc[:, [0, 1, 2, 3, 4, 5, 6]]

# تعیین مقادیر index به ترتیب مقادیر دوره‌های اجرا
#df.index = [30, 100, 1000, 10000, 25000] * (len(df) // 5)

# چاپ دیتافریم
print(df)

# تعیین مقادیر x و y برای نمودار
x = df["Algorithms"]
y = df.drop("Algorithms", axis=1).T.values  # ترانهاده کردن ماتریس مقادیر

# تعیین عنوان نمودار و محورها
plt.title('Results')
plt.xlabel('Algorithm')
plt.ylabel('Result')

# رسم نمودار
for row in y:
    plt.plot(x, row, marker='o', linestyle='-')

# نمایش نمودار
plt.legend(df.columns[1:])  # افزودن لیبل به هر خط
plt.show()
