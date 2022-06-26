# Layered PDF Merge
## Merge and layer PDF files using Optional Content Groups (OCG)
Conventionally, when creating a garment sewing pattern, the designer overlays all available garment sizes onto a large sheet of paper to be printed. The dressmaker or sewist locates the desired garment size and either cuts or traces that particular set of pattern panels from the set of available sizes. For home sewists, 'projector sewing' reduces paper waste and PDF Layers allow hiding unwanted sizes or pattern elements. 

This script combines A0 paper-size PDF files into single multi-page PDF, with each exported "layer" added to its own PDF Layer. Using PDF Optional Content Group and a compatible PDF viewing application e.g. Adobe Acrobat Reader, the user may show or hide different content layers. 

The PDF layers are named using the filename of the individual exports. Common page numbers are combined onto the same page in the output file. 

### Example Use Case
* small.pdf is a 2 page file exported with the small garment patterns
* medium.pdf is a 2 page file exported with the medium garment patterns
* common.pdf is a 2 page file exported with elements common to all garments patterns such as titles and pattern symbols

The resulting file is a 2 page PDF displaying all elements: common, small, and medium. Available in the PDF application's "layers" toolbar, the user may hide or show either small or medium content. The sewist who only wants to sew the small garment may hide all of the unnecessary information for a medium garment size. 


## Installation and Use

### Requires
* Python 3.7+
* [PyMuPDF] (https://github.com/pymupdf/PyMuPDF)
* PDF viewer capable of displaying optional content groups aka layers e.g. Adobe Acrobat Reader

### Installation
1. mupdf "brew install mupdf"
1. pip install wheel setuptools
1. pip install pymupdf

### Usage
1. From your design application, such as Inkscape, export individual layers into separate A0-sized PDF files
1. Save all files into patterns/ folder within this script file folder location
1. Run the script and locate the output file within the script file folder location
1. Open the output PDF in Adobe Acrobat Reader or other viewer capable of displaying Optional Content Groups (OCG)

Note: As of writing Chrome, Safari, and Preview's PDF viewers do NOT currently support OCGs


## Known Limitations or Desired Changes
* The script currently expects A0 sized input files. temp-get-page-bound.py will work to get the page size rather than defaulting to A0 but has not yet been incorporated
* All input pdfs are selectable layers. In above example, common layer may be shown or hidden. May make sense in future to have a layer such as common to be in the base PDF rather than a layer
* Only import pdfs of equal page counts and page sizes (e.g. A0) have been tested