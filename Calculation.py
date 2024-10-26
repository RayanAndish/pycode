import os
import pandas as pd
from ast import literal_eval
from concurrent.futures import ProcessPoolExecutor

# مسیر فایل CSV
file_path = 'D:/vvv/AFHA-Ackley-D30-25000.csv'

# تابع پردازش یک فایل CSV
def process_csv(file_path):
    df = pd.read_csv(file_path, converters={'Best_Solutions': literal_eval})
    result_df = pd.DataFrame()

    for column in df.columns:
        if column != 'Iteration':
            if df[column].apply(type).eq(list).any():
                column_values = [val for sublist in df[column] for val in sublist]
                result_df[column + '_Mean'] = [sum(column_values) / len(column_values)]
                result_df[column + '_Minimum'] = [min(column_values)]
                result_df[column + '_Maximum'] = [max(column_values)]
                result_df[column + '_Variance'] = [sum((x - (sum(column_values) / len(column_values))) ** 2 for x in column_values) / len(column_values)]
                result_df[column + '_Standard_Deviation'] = [(sum((x - (sum(column_values) / len(column_values))) ** 2 for x in column_values) / len(column_values)) ** 0.5]

    result_df['Best_Fitness_Mean'] = df['Best_Fitness'].mean()
    result_df['Best_Fitness_Minimum'] = df['Best_Fitness'].min()
    result_df['Best_Fitness_Maximum'] = df['Best_Fitness'].max()
    result_df['Best_Fitness_Variance'] = df['Best_Fitness'].var()
    result_df['Best_Fitness_Standard_Deviation'] = df['Best_Fitness'].std()

    result_df['Execution_Time_Mean'] = df['Execution_Time'].mean()
    result_df['Execution_Time_Minimum'] = df['Execution_Time'].min()
    result_df['Execution_Time_Maximum'] = df['Execution_Time'].max()
    result_df['Execution_Time_Variance'] = df['Execution_Time'].var()
    result_df['Execution_Time_Standard_Deviation'] = df['Execution_Time'].std()

    # ذخیره نتایج به یک فایل csv
    output_file_name = os.path.basename(file_path).replace('.csv', '-v.csv')
    output_file_path = os.path.join(os.path.dirname(file_path), output_file_name)
    result_df.to_csv(output_file_path, index=False)

    print(f"پردازش فایل {output_file_name} به اتمام رسید.")

# استفاده از شرط محافظت
if __name__ == '__main__':
    # ایجاد یک ProcessPoolExecutor برای اجرای موازی با حداکثر تعداد هسته‌های فیزیکی
    with ProcessPoolExecutor(max_workers=os.cpu_count()) as executor:  # تعداد هسته های سیستم
        # فراخوانی تابع process_csv با مسیر فایل به عنوان ورودی
        executor.submit(process_csv, file_path)

    print("پردازش به اتمام رسید.")