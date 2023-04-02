import openpyxl
import database_reader as dr
import Management


system = Management.Management()
test_cus = ["C100", "Jamb", "0989222333"]
system.set_new_customer(test_cus)

# 
customer_sheet = wb['Customer']
driver_sheet = wb['Driver']
vehicle_sheet = wb['Vehicle']
invoice_sheet = wb['Invoice']




#
for row in customer_sheet.iter_rows(min_row=2):
    for customer in system.get_list("customer"):
        for cell in row:
            pass