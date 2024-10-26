import csv
from docx import Document

def extract_tables_with_dimension(docx_file, keyword):
    doc = Document(docx_file)
    relevant_tables = []
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                if keyword in cell.text.strip():
                    table_data = []
                    for row in table.rows:
                        row_data = [cell.text.strip() for cell in row.cells]
                        table_data.append(row_data)
                    relevant_tables.append(table_data)
                    break  # فقط اولین ردیف مربوط به این کلمه را در نظر می‌گیریم
                    # اگر تمام جدول مربوط به یک ردیف باشد، این خط را حذف کنید
                    break
    return relevant_tables

def write_to_csv(tables, csv_files_prefix):
    for i, table in enumerate(tables):
        csv_file = f"{csv_files_prefix}_{i+1}.csv"
        with open(csv_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for row in table:
                writer.writerow(row)

# فایل ورد و پیشوند فایل‌های CSV
docx_file = 'D:/Algurithms/Paper-Algorithms.docx'
csv_files_prefix = 'output_table'

# استخراج جداول مربوطه از فایل ورد
relevant_tables = extract_tables_with_dimension(docx_file, "Dimention:")

# ذخیره جداول مربوطه در فایل‌های CSV
write_to_csv(relevant_tables, csv_files_prefix)
