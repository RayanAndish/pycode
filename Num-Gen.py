import numpy as np
import pandas as pd


def generate_exponential_numbers(start, end, num_samples, decimal_places, exp_scale, avg_window=3):
    # تولید اعداد نمایی بین 0 و 1 با مقیاس نمایی داده شده و معکوس کردن آن
    exponential_factor = np.exp(np.linspace(exp_scale, 0, num_samples)) - 1  # از e^exp_scale-1 تا 0
    exponential_factor /= np.max(exponential_factor)  # نرمال سازی به 0 تا 1

    # تولید اعداد تصادفی بین 0 و 1 و میانگین گیری برای کاهش نوسانات
    random_numbers = np.mean([np.random.rand(num_samples) for _ in range(avg_window)], axis=0)

    # مقیاس بندی به بازه مورد نظر
    final_numbers = start - (start - end) * exponential_factor * random_numbers

    # تنظیم تعداد رقم اعشار
    final_numbers = np.round(final_numbers, decimal_places)

    return final_numbers


def save_to_csv(numbers, filename):
    df = pd.DataFrame(numbers, columns=['Random Numbers'])
    df.to_csv(filename, index=False)


# مثال استفاده
start = 0.00756 # جد پایین بازه شروع اعداد
end = 30 # حد بالای شروع اعداد
num_samples = 1000 # تعداد اعداد مورد نیاز
decimal_places = 7 # تعداد اعشار مورد نیاز
exp_scale = 70  # مقیاس نمایی برای تنظیم شیب
avg_window = 35  # تعداد اعداد تصادفی برای میانگین گیری

random_numbers = generate_exponential_numbers(start, end, num_samples, decimal_places, exp_scale, avg_window)
save_to_csv(random_numbers, 'random_numbers.csv')

print("Numbers saved to random_numbers.csv")
