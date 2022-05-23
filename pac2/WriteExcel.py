from openpyxl import Workbook

wb=Workbook()

wb["Sheet"].title = "sanity report"     #Sheet1 should be bt we took Sheet , need to ask
sh1=wb.active


sh1["A1"].value="name"
sh1["B1"].value="fname"

sh1["A2"].value="naman"
sh1["B2"].value="rastogi"

sh1["A3"].value="pooja"
sh1["B3"].value="jain"

#wb.save("Sanityreport1.xlsx")
wb.save("\\Users\\pragtgupta\\Desktop\\extracted data.xlsx")

# \\Users\\pragtgupta\\Desktop\\extracted data.xlsx


