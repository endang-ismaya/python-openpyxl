import openpyxl as xl

# open an existing workbook
wb = xl.load_workbook(filename="maven_ski_shop_data.xlsx")

# set a ws
ws_orders_info = wb["Orders_Info"]

# updating E11, F11
subtotal = ws_orders_info["D10"].value
tax = float(round(subtotal * 0.08, 2))
total = subtotal + tax

print(f"Salex Tax: ${tax}")
print(f"Total: ${total}")
