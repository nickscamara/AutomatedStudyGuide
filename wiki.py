import wikipedia
import urllib.request
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
from docx import Document
from docx.shared import Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt

def fontArial():
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Tahoma'
    font.size = Pt(11)  
    
def downloadImage(url,file_path,file_name):
    path = file_path + file_name + url[-4:]
    urllib.request.urlretrieve(url, path)
    if url[-4:] == ".svg":
        drawing = svg2rlg(path)
        renderPM.drawToFile(drawing, 'images/'+file_name+'.png', fmt="PNG")
        return ".png"
    return url[-4:]




for x in range(1):

    search = input("Enter a word that you would like to create a Study Guide: ")
    num = input("Enter the number of sub-topics that you would like to have: ")
    array = []
    nums = int(num)
    iterator = 0
    while iterator < nums:
        addthis = input("Enter a sub-topic: ")
        array.append(addthis)
        iterator = iterator + 1
    print(array)


    doc = Document()
    fontArial()
    doc.add_heading(search.capitalize(),0)
    wiki = search
    last_paragraph = doc.add_paragraph((wikipedia.summary(wiki,sentences=3)))
    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    last_paragraph.style = doc.styles['Normal']

    for y in array:
        doc.add_heading(y.capitalize(), level=1)
        last_paragraph = doc.add_paragraph((wikipedia.summary(y)))
        
        #wikipedia.random()
        
        
        br = wikipedia.page(y)
        url = br.images[0]
        print(br.images[0])
        file_name = br.title.strip()
        aa = file_name.replace(" ", "")
        print(aa)
        urls = downloadImage(url,'images/', aa)
        print(urls)
        paragraph = doc.add_paragraph()
        run = paragraph.add_run()
        picture = run.add_picture('images/'+ aa + urls, width=Inches(3))
        paragraph = doc.paragraphs[-1] 
        paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        #img = doc.add_picture('images/'+ aa + urls, width=Inches(3))
        #img.alignment  = 1
    
    doc.save('me.docx')


