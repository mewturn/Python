from docx import Document

doc = Document("C:/Users/user/Desktop/NVN013.docx")
for i in doc.paragraphs:
    text = ""
    for j in i.runs:
        if str(j.font.color.rgb) == "FF0000":
            text += j.text
    text = text.replace("\n", "").strip()
    print(text)
