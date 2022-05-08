""" 
Layered PDF Merge for LearnMYOG

Combines multi-page A0 pdfs into a single file with Optional Content Groups
Useful for sewing patterns with multiple size options
PDF view such as Adobe Acrobat Reader required to view layers

Requires:
python 3.7    
pymupdf - https://pymupdf.readthedocs.io/en/latest/intro.html
    mupdf "brew install mupdf"
    pip install wheel setuptools
    pip install pymupdf

Workings:
1. Save a Copy of A0 layers from Inkscape:
    Common elements and all text and pattern symbols to common.pdf
    Each size garment pattern (by color) to individual file e.g. small.pdf
2. Copy pdf layers to path variable location e.g. patterns/
3. Run script. Output file has layers across multiple pages.

"""

import os, time, pprint
import fitz

# location for src pdfs
path = "patterns/"
paths = sorted(os.listdir(path))

# create empty output pdf
doc = fitz.open()


for i, obj in enumerate(paths): 
    if obj.endswith('.pdf'):
        
        src = fitz.open(path+obj)

        # add empty pages to doc to match page count of source pages
        if len(doc) < len(src):
            for pg in range(len(src)):
                # default page size is A4 @ 72 dpi 595 x 842
                # A0 @ 72 dpi 2384 x 3370
                page = doc.new_page(-1, 3370, 2384)
                #determine rect size for placing layers later
                r0 = page.rect

        # create optional content group for pattern size
        name = os.path.splitext(obj)[0]
        xref0 = doc.add_ocg(name, on=True)

        # iterate over each page
        for pg in range(len(src)):
            doc.load_page(pg).show_pdf_page(r0, src, pg, oc = xref0)
            
        src.close()

print('------------------------')
print('Option Content Groups')
print('------------------------')
pprint.pprint(doc.get_ocgs())


timestr = str('D:' + time.strftime("%Y%m%d%H%M%S"))

doc.set_metadata({})
doc.set_metadata({
    'author': 'Tim @ LearnMYOG.com',
    'creationDate': timestr
})
print('------------------------')
print('metadata')
print('------------------------')
pprint.pprint(doc.metadata)



doc.save('new_pattern.pdf',  
    garbage=3,
    pretty=True,
    deflate=True,
    linear=True,
    clean=True,)

doc.close()

