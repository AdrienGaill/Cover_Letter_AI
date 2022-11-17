from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors, pagesizes
from datetime import date, datetime
from reportlab.platypus import Paragraph, SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
styles=getSampleStyleSheet()

fileName = 'Cover Letter Adrien Gaillard.pdf'
elements = []
# creating a pdf object
pdf = SimpleDocTemplate(fileName)
width, height = pagesizes.A4
margin = 85
line_break = 11
current_y = height-margin
fontsize = 11

def linebreak():
    global current_y
    current_y -= fontsize
    # print(round(current_y))

# registering a external font in python
pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))
pdfmetrics.registerFont(TTFont("Arial bold", 'Arial_bold.ttf'))

# creating the title by setting it's font 
# and putting it on the canvas
# title = "<para style={fontName=Arial, fontSize:14}>Adrien GAILLARD</para>"
title = "Adrien GAILLARD"
title_style = ParagraphStyle(name = "", fontsize = 14, fontName = "Arial bold")
title_para = Paragraph(title, style=title_style)
elements.append(title_para)
# pdf.build([title_para,])

current_y -= 14

documentTitle = fileName
final_date = datetime.strftime(date.today(), "%B %d, %Y")
    # TODO configure the date of document
subtitle = f'''+33 631 651 529<br/>
    <a href=http://google.com>adrien.gaillard.pro@gmail.com</a><br/>
    <a href=https://www.linkedin.com/in/AdrienGaillard/>My LinkedIn</a><br/>
    <br/>
    {final_date}<br/>
    '''
info_para = Paragraph(subtitle)
elements.append(info_para)
# pdf.build([info_para,])

paragraphs = ["Le 1er.",
    "Le 2e dfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff",
    "Le 3e."
    ]
image = 'signature_adrien.png'
# (0, 0) at the bottom left of the page in point, 1 pt = 1/72 inch, max is (595 x 842)



# creating the subtitle by setting it's font, 
# colour and putting it on the canvas
# pdf.setFont("Arial", 11)
# TODO check how to line break
# text = pdf.beginText(margin, current_y)
# for line in para_infos:
#     text.textLine(line)
#     linebreak()
# pdf.drawText(text)
# pdf.drawText(para_infos)
# pdf.drawText([para_infos])
linebreak()


# drawing a line
# pdf.line(margin, current_y, width-margin, current_y) 
linebreak()
linebreak()

# creating a multiline text using
# textline and for loop
# text = pdf.beginText(margin, current_y)
# text.setFont("Arial", 11)
for paragraph in paragraphs:
    # text.textLine(paragraph)
    linebreak()
    # text.textLine()
    linebreak()    
# pdf.drawText(text)


# drawing a image at the 
# specified (x.y) position
# pdf.drawInlineImage(image, 130, 100)

# saving the pdf
pdf.build(elements)