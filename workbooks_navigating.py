import openpyxl as xl

# open an existing workbook
wb = xl.load_workbook(filename="maven_ski_shop_data.xlsx")

# assign a variable to a worksheet
ws_inventory_levels = wb["Inventory_Levels"]

# get a value from a cell
header_a = ws_inventory_levels["A1"].value
header_b = ws_inventory_levels["B1"].value
print(header_a)  # Product_ID
print(header_b)  # Quantity_in_stock

print(ws_inventory_levels["B2"].value)  # 100
