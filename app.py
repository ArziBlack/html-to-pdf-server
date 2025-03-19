from flask import Flask, request, send_file
from weasyprint import HTML
from io import BytesIO

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_html_to_pdf():
    html_content = request.form.get('html')
    if not html_content:
        return 'No HTML content provided', 400

    pdf_file = BytesIO()
    HTML(string=html_content).write_pdf(pdf_file)
    pdf_file.seek(0)

    return send_file(pdf_file, mimetype='application/pdf', as_attachment=True, download_name='output.pdf')

if __name__ == '__main__':
    app.run(debug=True)
