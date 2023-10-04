import openpyxl

# Passing an already existent spreadsheet to my variable called 'book'
book = openpyxl.load_workbook('Buying_List.xlsx')
# Getting the specific page that I want to work with
fruits_page = book['Fruits']
# Printing the elements
for rows in fruits_page.iter_rows(min_row = 2, max_row = 4):
    for cell in rows:
        print(cell.value, end=" ")
    print()