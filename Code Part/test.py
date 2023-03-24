import openpyxl
from Model import Customer

data = openpyxl.load_workbook("Taxi-information.xlsx", read_only=True)
sheet1 = data['Customer']
# print(sheet1.max_row)
# print(sheet1.max_column)

# for i in range(1, sheet1.max_row+1):
#     for cell in sheet1[i]:
#         print(cell.value)

# l1 = sheet1.iter_rows(min_row=1, max_row=2, values_only=True)
# r_set = sheet1.iter_rows(min_row=2, max_row=sheet1.max_row, values_only=True)
# l1 = [r for r in l1]
# r_set = [r for r in r_set]
# data.close()
# print(l1[0])
# print(r_set)

customer_list = []
for row in sheet1:
    new_customer = Customer.Customer()
    new_customer.set_customer(row[0].value, row[1].value, row[2].value)
    customer_list.append(new_customer)

for element in customer_list:
    print("{:8} {:<15} {:<10}".format(element.get_id(), element.get_name(), element.get_phone_num()))
