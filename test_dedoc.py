import requests
filename= "/home/iv.kem/Downloads/Доклад по БЖД.docx"
data = {
    "document_type": "other",
    "language": "rus",
    "need_pdf_table_analysis": "true",
    "need_header_footer_analysis": "false",
    "is_one_column_document": "false",
    "return_format": 'plain_text',
    "structure_type": "tree"
}
with open(filename, 'rb') as file:
    files = {'file': (filename, file)}
    r = requests.post("http://localhost:1231/upload", files=files, data=data)
    result = r.content.decode('utf-8')
    print(result)



