import os
import re


def rename_files(directory, start_number):
    # الگوی فایل‌های مورد نظر
    pattern = re.compile(r"(\d+)\s+(Vocabulary|Story)\.mp3")

    # لیستی از فایل‌های موجود در پوشه
    files = os.listdir(directory)

    # فیلتر کردن فایل‌های مورد نظر و مرتب‌سازی آن‌ها بر اساس شماره فایل
    files = sorted([f for f in files if pattern.match(f)], key=lambda x: int(pattern.match(x).group(1)))

    # تغییر نام فایل‌ها از شماره جدید
    for file in files:
        match = pattern.match(file)
        if match:
            new_number = start_number
            start_number += 1
            new_name = f"{new_number:02d} {match.group(2)}.mp3"
            os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
            print(f"Renamed '{file}' to '{new_name}'")


# مسیر پوشه و شماره شروع
directory_path = "D:/6/"  # مسیر پوشه را اینجا قرار دهید
start_number = 301

# فراخوانی تابع با مسیر پوشه و شماره شروع
rename_files(directory_path, start_number)
