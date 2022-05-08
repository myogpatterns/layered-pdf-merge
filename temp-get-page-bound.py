# test file for determing pdf size instead of hard coding A0 expectation

import fitz

fpath = "patterns/common.pdf"
doc = fitz.open(fpath)
page = doc[0]

r0 = page.bound()
print(r0) #Rect(0.0, 0.0, 3370.393798828125, 2383.93701171875)

newpage = doc.new_page(-1, round(r0[2]), round(r0[3]))
print(newpage.bound()) #Rect(0.0, 0.0, 3370.0, 2384.0)

doc.close()