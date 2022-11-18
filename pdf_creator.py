from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from datetime import date, datetime
from reportlab.platypus import Paragraph, SimpleDocTemplate
from reportlab.lib.styles import ParagraphStyle

fileName = 'Cover Letter Adrien Gaillard.pdf'
elements = []
# creating a pdf object
pdf = SimpleDocTemplate(fileName)

# Registering external fonts
pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))
pdfmetrics.registerFont(TTFont("Arial bold", 'Arial_bold.ttf'))


# Add title
title = "Adrien GAILLARD"
title_style = ParagraphStyle(name = "", fontSize = 14, fontName = "Arial bold", leading=14)
title_para = Paragraph(title, style=title_style)
elements.append(title_para)


# Add references
final_date = datetime.strftime(date.today(), "%B %d, %Y")
subtitle = f'''+33 631 651 529<br/>
    <a href=http://google.com>adrien.gaillard.pro@gmail.com</a><br/>
    My <a color="blue" href=https://www.linkedin.com/in/AdrienGaillard/>LinkedIn</a><br/>
    <br/>
    {final_date}<br/><br/><br/>
    '''
main_style = ParagraphStyle(name = "", fontSize = 11, fontName = "Arial")
elements.append(Paragraph(subtitle, style=main_style))


# Add paraphrased paragraphs
# TODO get paragraphs
paragraphs = ["Dear Sir or Madam",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    "    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    "    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    ]
for paragraph in paragraphs:
    elements.append(Paragraph(paragraph+"<br/><br/>", style=main_style))


# Add signature at the end
image = '''
    Adrien Gaillard<br/>
    <img valign='text-top' src=./signature_adrien.png width='80' height='60'/>
'''
std_indented = ParagraphStyle(name="std_indented", fontName="Arial", fontSize=11, leftIndent=44, )
signature = Paragraph(image, style=std_indented)
elements.append(signature)


# Build every element and save the pdf
pdf.build(elements)