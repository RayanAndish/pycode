import os
import pandas as pd

def calculate_statistics(df):
    result_df = pd.DataFrame()

    # محاسبه مقادیر مورد نیاز برای ستون Best_Fitness
    best_fitness_mean = df['Best_Fitness'].mean()
    best_fitness_min = df['Best_Fitness'].min()
    best_fitness_max = df['Best_Fitness'].max()
    best_fitness_variance = df['Best_Fitness'].var()
    best_fitness_std = df['Best_Fitness'].std()

    # اضافه کردن مقادیر محاسبه شده به DataFrame نتیجه
    result_df['Best_Fitness_Mean'] = [best_fitness_mean]
    result_df['Best_Fitness_Minimum'] = [best_fitness_min]
    result_df['Best_Fitness_Maximum'] = [best_fitness_max]
    result_df['Best_Fitness_Variance'] = [best_fitness_variance]
    result_df['Best_Fitness_Standard_Deviation'] = [best_fitness_std]

    return result_df

def process_csv(input_file_path):
    # خواندن فایل ورودی
    df = pd.read_csv(input_file_path)

    # محاسبه آماره‌های مورد نیاز
    result_df = calculate_statistics(df)

    # ساخت مسیر و نام فایل خروجی
    output_file_name = os.path.basename(input_file_path).replace('.csv', '-v.csv')
    output_file_path = os.path.join(os.path.dirname(input_file_path), output_file_name)

    # ذخیره نتایج در یک فایل CSV
    result_df.to_csv(output_file_path, index=False)

    print(f"پردازش فایل {output_file_name} به اتمام رسید.")

if __name__ == '__main__':
    # مسیر پوشه حاوی فایل‌های CSV
    directory_path = 'D:/vvv/'

    # خواندن تمام فایل‌های درون پوشه
    for file_name in os.listdir(directory_path):
        if file_name.endswith('.csv'):
            # مسیر فایل ورودی
            input_file_path = os.path.join(directory_path, file_name)
            # پردازش فایل ورودی
            process_csv(input_file_path)

    print("پردازش تمامی فایل‌ها به اتمام رسید.")