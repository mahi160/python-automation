import camelot

tables = camelot.read_pdf('./samples/sample.pdf', pages='1')
print(tables)
tables.export('sample.csv', f='csv', compress=True)
tables[0].to_csv('./samples/table_pdf.csv')