from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from datetime import date, datetime
from reportlab.platypus import Paragraph, SimpleDocTemplate
from reportlab.lib.styles import ParagraphStyle


def get_cover_letter(paragraphs: list, offer_title: str):
    """
    Generate the cover letter in a pdf file
        "paragraph" is a list of strings, one per paragraph
        "offer_title" is a string
    """

    print("Generating cover letter")
    fileName = 'Cover Letter Adrien Gaillard.pdf'

    # Create the template object
    pdf = SimpleDocTemplate(fileName)

    # Elements to be rendered in the pdf file
    elements = []

    # Register fonts as a family
    pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))
    pdfmetrics.registerFont(TTFont("Arial-Bold", 'Arial_bold.ttf'))
    pdfmetrics.registerFont(TTFont("Arial-Italic", 'Arial_Italic.ttf'))
    pdfmetrics.registerFont(TTFont("Arial-Bold_Italic", 'Arial_Bold_Italic.ttf'))
    pdfmetrics.registerFontFamily('Arial', normal='Arial',
                                      bold='Arial-Bold',
                                      italic='Arial-Italic',
                                      boldItalic='Arial-Bold-Italic')

    # Add title
    title_style = ParagraphStyle(name = "", fontSize = 14, fontName = "Arial", leading = 16)
    subtitle_style = ParagraphStyle(name = "", fontSize = 11, fontName = "Arial", leading = 14, alignment = 4)
    main_style = ParagraphStyle(name = "", fontSize = 11, fontName = "Arial", leading=14, firstLineIndent = 22, alignment = 4)

    title_para = Paragraph("<b>Adrien GAILLARD</b>", style=title_style)
    elements.append(title_para)

    # Add references and date
    today = date.today()
    day = today.day
    month = datetime.strftime(today, "%B")
    year = datetime.strftime(today, ", %Y")
    subtitle = f'''
        +33 631 651 529<br/>
        <a href=mailto:adrien.gaillard.pro@gmail.com>adrien.gaillard.pro@gmail.com</a><br/>
        My <a color="blue" href=https://www.linkedin.com/in/AdrienGaillard/>LinkedIn</a><br/>
        My <a color="blue" href=https://github.com/AdrienGaill/>GitHub</a><br/>
        <br/>
        {month} {day}{year}<br/><br/><br/>
        '''
    elements.append(Paragraph(subtitle, style=subtitle_style))

    elements.append(Paragraph("Dear Sir or Madam,<br/><br/>", style = main_style))

    AI_project = "First of all, I didn't write this cover letter. Indeed, it was created by an algorithm using NLP to reflect your job offer's requirements. You can learn more about <a color='blue' href=https://github.com/AdrienGaill/Cover_Letter_AI/>this project</a> on my GitHub.<br/><br/>"
    elements.append(Paragraph(AI_project, style=main_style))

    if offer_title == "":
        internship = '''Currently on a gap year after my 2nd year at Ecole Centrale de Nantes, a top French engineering school, I am seeking an internship or a fixed-term contract of at least 6 months in an IT related field, preferably AI, located in Germany, in Berlin.
            Thus, I am offering you my unsolicited application to join your team for a position related to AI.<br/><br/>
            '''

    else:
        internship = f'''Currently on a gap year after my 2nd year at Ecole Centrale de Nantes, a top French engineering school, I am seeking an internship or a fixed-term contract of at least 6 months in an IT related field, preferably AI, located in Germany, in Berlin.
            Thus I'm interested in the <b>{offer_title}</b> position you offer.<br/><br/>
            '''

    elements.append(Paragraph(internship, style=main_style))

    # Add paraphrased paragraphs
    for paragraph in paragraphs:
        elements.append(Paragraph(paragraph+"<br/><br/>", style=main_style))

    elements.append(Paragraph("Therefore I would like to propose that we meet in order to convince you of my motivation and I am already enclosing my resume to that effect. I look forward to your reply and thank you in advance for your time and attention.<br/><br/>", style=main_style))

    elements.append(Paragraph("Sincerely,<br/><br/>", style=main_style))
    
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

