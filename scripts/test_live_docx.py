import urllib.request
import io
import zipfile
import json

docx_buffer = io.BytesIO()
with zipfile.ZipFile(docx_buffer, 'w') as z:
    doc_xml = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body><w:p><w:r><w:t>BEFORE THE HONBLE APPELLATE AUTHORITY UNDER GST</w:t></w:r></w:p><w:p><w:r><w:t>STATEMENT OF FACTS AND WRITTEN SUBMISSIONS</w:t></w:r></w:p><w:p><w:r><w:t>The Appellant is an innocent bona fide purchaser who paid full tax via RTGS.</w:t></w:r></w:p></w:body></w:document>'
    z.writestr('word/document.xml', doc_xml)
    z.writestr('[Content_Types].xml', '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="xml" ContentType="application/xml"/><Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/></Types>')

docx_bytes = docx_buffer.getvalue()

boundary = '----WebKitFormBoundary7MA4YWxkTrZu0gW'
body = bytearray()
body.extend(f'--{boundary}\r\n'.encode('utf-8'))
body.extend(b'Content-Disposition: form-data; name="file"; filename="Appeal_Draft.docx"\r\n')
body.extend(b'Content-Type: application/vnd.openxmlformats-officedocument.wordprocessingml.document\r\n\r\n')
body.extend(docx_bytes)
body.extend(f'\r\n--{boundary}--\r\n'.encode('utf-8'))

req = urllib.request.Request(
    'https://ngtp-litigation-engine.onrender.com/api/extract-text',
    data=bytes(body),
    headers={'Content-Type': f'multipart/form-data; boundary={boundary}'}
)

try:
    with urllib.request.urlopen(req) as res:
        data = json.loads(res.read().decode('utf-8'))
        print('HTTP Status:', res.status)
        print('Success:', data.get('success'))
        print('Character Count:', data.get('characterCount'))
        print('Clean Extracted Text:\n' + data.get('text'))
except urllib.error.HTTPError as e:
    print('HTTP Error:', e.code, e.read().decode('utf-8'))