import fitz  # PyMuPDF
import re
import os
from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<html>
<head><title>Grocery Checklist</title></head>
<body>
<h2>Grocery Checklist</h2>
<ul>
{% for qty, item in items %}
<li><input type="checkbox"> {{ qty }}x {{ item }}</li>
{% endfor %}
</ul>
</body>
</html>
"""

REGEX_PATTERN = r"(?m)^\s*([1-9]\d{0,1})[^\w\n]*\s+[†‡§*•–-]*\s*([A-Za-z][A-Za-z0-9 &'\"’\-]+(?:\s(?:[0-9]+(?:\.\d+)?\s?(?:G|Kg|ml|L|Litre|Pack|pk|pcs|Minimum\s\d+G))?)?)"

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file uploaded", 400
        file = request.files['file']
        if file.filename == '':
            return "Empty filename", 400
        
        pdf_bytes = file.read()
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")

        text = "".join([page.get_text() for page in doc])
        matches = re.findall(REGEX_PATTERN, text)

        items = [(qty.strip(), item.strip()) for qty, item in matches]
        return render_template_string(HTML_TEMPLATE, items=items)

    return '''
    <!doctype html>
    <title>Upload Tesco PDF</title>
    <h1>Upload your Tesco order PDF</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file accept=application/pdf>
      <input type=submit value=Upload>
    </form>
    '''

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
