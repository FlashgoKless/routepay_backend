from img2table.document import PDF
from img2table.ocr import TesseractOCR
import argparse
import os

def convert_pdf_tables_to_excel(pdf_path, output_excel_path):
    try:
        ocr = TesseractOCR(lang="eng+rus")
        
        pdf = PDF(src=pdf_path)
        
        pdf.to_xlsx(dest=output_excel_path,
                    ocr=ocr,
                    implicit_rows=False,
                    borderless_tables=False,
                    min_confidence=50)
        
        print(f"Успешно конвертировано! Результат сохранен в {output_excel_path}")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

def main():
    # Настройка аргументов командной строки
    parser = argparse.ArgumentParser(description='Конвертация таблиц из PDF в Excel')
    parser.add_argument('input_pdf', help='Путь к исходному PDF файлу')
    parser.add_argument('output_excel', help='Путь для сохранения Excel файла')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input_pdf):
        print(f"Ошибка: Файл {args.input_pdf} не найден!")
        return
    
    convert_pdf_tables_to_excel(args.input_pdf, args.output_excel)

if __name__ == "__main__":
    main()