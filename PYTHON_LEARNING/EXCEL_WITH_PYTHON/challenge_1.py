# Create a spreadsheet with the following data...

# Name of the spreadsheet... 'My_Computers'
# Name of the sheet... 'Computers'
# Data...
"""
Computer 1, 8gb Ram, $2,500
Computer 2, 16gb Ram, $5,500
Computer 3, 32gb Ram, $7,500
"""
import openpyxl

# Creating spreadsheet 'my_computers'
my_computers = openpyxl.Workbook()
# Adding the sheet 'computers' to my spreadsheet 'my_computers'
my_computers.create_sheet('computers')

computers = my_computers['computers']

computers.append(['Computer Name', 'Amount of RAM', 'Price'])
computers.append(['Computer 1', '8gb Ram', '$2,500'])
computers.append(['Computer 2', '16gb Ram', '$5,500'])
computers.append(['Computer 3', '32gb Ram', '$6,500'])

my_computers.save('My_Computers_Spreadsheet.xlsx')