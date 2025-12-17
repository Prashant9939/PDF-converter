# PDF Converter & Image Compressor System

## 📌 Project Description
The PDF Converter & Image Compressor System is a web-based utility application that allows users to convert documents between PDF and Word formats and compress images efficiently. The system is designed to simplify document handling and image optimization through an easy-to-use interface and backend processing.

This project demonstrates practical skills in **file handling, backend development using Flask, PDF processing, and client-side image compression**, making it suitable for real-world productivity and utility applications.

---

## 🚀 Features
### PDF Converter
- Convert **Word (.docx) to PDF**
- Convert **PDF to Word (.docx)**
- Automatic download of converted files
- Files saved directly to the user's Downloads folder

### Image Compressor
- Upload and preview images
- Crop images using interactive crop tool
- Compress images to reduce file size
- Download compressed images instantly

---

## 🛠️ Technologies Used
- Python
- Flask
- HTML, CSS, JavaScript
- ReportLab (Word to PDF)
- python-docx
- pdf2docx
- Cropper.js (Image cropping)
- Canvas API (Image compression)

---

## 📁 Project Structure



pdf-converter-image-compressor/
│
├── app.py # Flask backend (PDF conversion)
├── word-to-pdf.py # Word to PDF logic
├── templates/
│ ├── word-to-pdf.html
│ ├── pdf-to-word.html
│
├── static/
│ └── img-compressor.html # Image compressor frontend
│
├── uploads/ # Temporary uploaded files
├── requirements.txt # Dependencies
└── README.md # Project documentation


---

## ⚙️ How to Run the Project

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd pdf-converter-image-compressor

Step 2: Install Dependencies
pip install -r requirements.txt

Step 3: Run the Flask Application
python app.py

Step 4: Use the Application

Open browser and go to:

http://127.0.0.1:5000/


Upload a PDF or Word file to convert

Access the Image Compressor page to upload, crop, and compress images

Download the converted or compressed files

🔄 How It Works
PDF Conversion

User uploads a Word or PDF file.

Flask backend processes the file.

Conversion is performed using PDF/Docx libraries.

Converted file is automatically downloaded.

Image Compression

User uploads an image.

Image is previewed and optionally cropped.

Image is compressed using canvas-based processing.

Compressed image is downloaded.

📈 Use Cases

Document format conversion

Academic assignments and submissions

Office document handling

Image size optimization

Learning backend file processing and utilities

🔮 Future Enhancements

Add more document formats (Excel, PPT)

Batch file conversion

Adjustable compression levels

Cloud deployment

Improved UI/UX

👤 Author

Prashant Kumar Mishra
Aspiring Data Science & Analytics Intern


---

### ✅ Why this README is strong
- Clear explanation for **both PDF conversion & image compression**
- Matches your **actual code and files**
- Professional and recruiter-friendly
- Ready for **GitHub, college submission, or internship review**

If you want, I can also:
- Shorten this README for **quick recruiter view**
- Write a **2-line resume description**
- Add **screenshots section template**

Just tell me 👍
