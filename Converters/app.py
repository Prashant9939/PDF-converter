from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
from pdf2docx import Converter
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

# Get the user's Downloads folder dynamically
DOWNLOADS_FOLDER = os.path.join(os.path.expanduser("~"), "Downloads")

# Ensure folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(DOWNLOADS_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["OUTPUT_FOLDER"] = DOWNLOADS_FOLDER  # Save to Downloads

@app.route("/")
def upload_file():
    return render_template("pdf-to-word.html")

@app.route("/convert", methods=["POST"])
def convert_pdf_to_word():
    if "file" not in request.files:
        return "No file uploaded", 400
    
    file = request.files["file"]

    if file.filename == "":
        return "No selected file", 400

    filename = secure_filename(file.filename)
    pdf_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(pdf_path)

    # Debug: Check if file exists and print its size
    if not os.path.exists(pdf_path):
        return f"Error: File {pdf_path} was not saved properly.", 500
    else:
        file_size = os.path.getsize(pdf_path)
        print(f"File saved: {pdf_path} ({file_size} bytes)")

    # Convert PDF to Word
    word_filename = filename.replace(".pdf", ".docx")
    word_path = os.path.join(app.config["OUTPUT_FOLDER"], word_filename)

    try:
        cv = Converter(pdf_path)
        cv.convert(word_path, start=0, end=None)
        cv.close()
    except Exception as e:
        print(f"Conversion error: {e}")
        return f"Conversion failed: {e}", 500

    return send_file(word_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
