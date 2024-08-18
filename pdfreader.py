import tabula
import pandas as pd
import json


pdf_path = "JIPMERS R1.pdf"
tables = tabula.read_pdf(pdf_path, pages="all", multiple_tables=True)

tables_json = []

for table in tables:
    table.columns = table.iloc[0]
    table = table[1:]
    table_json = table.to_dict(orient="records")
    tables_json.append(table_json)

with open("output.json", "w") as json_file:
    json.dump(tables_json, json_file, indent=4)

print("Tables have been written to output.json")
