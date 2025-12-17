from flask import Flask, request, send_file, render_template
from werkzeug.utils import secure_filename
from docx import Document
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.path.expanduser("~"), "Downloads")  # Save in Downloads
DOWNLOADS_FOLDER = os.path.join(os.path.expanduser("~"), "Downloads")  # Default download path

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def upload_file():
    return render_template("word-to-pdf.html")

@app.route("/convert/word-to-pdf", methods=["POST"])
def convert_word_to_pdf():
    if "file" not in request.files:
        return "No file uploaded", 400
    
    file = request.files["file"]
    if file.filename == "":
        return "No selected file", 400

    filename = secure_filename(file.filename)
    word_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(word_path)

    pdf_filename = filename.replace(".docx", ".pdf")
    pdf_path = os.path.join(DOWNLOADS_FOLDER, pdf_filename)  # Save in Downloads folder

    try:
        # Convert Word to PDF
        doc = Document(word_path)
        c = canvas.Canvas(pdf_path, pagesize=letter)
        width, height = letter
        y_position = height - 50

        c.setFont("Helvetica", 12)

        for para in doc.paragraphs:
            if y_position < 50:
                c.showPage()
                c.setFont("Helvetica", 12)
                y_position = height - 50

            text = para.text.strip()
            c.drawString(50, y_position, text)
            y_position -= 20

        c.save()

    except Exception as e:
        return f"Conversion failed: {e}", 500

    return send_file(pdf_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
