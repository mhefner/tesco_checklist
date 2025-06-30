# Tesco Order Checklist

A simple Flask web application that converts your Tesco order confirmation emails into an easy-to-use shopping checklist. No more squinting at printed order sheets or highlighting items with a marker - just upload your PDF and get a clean, interactive checklist!

## 🛒 What it does

- Upload a PDF of your Tesco order confirmation email
- Automatically extracts all items from your order
- Generates a clean, interactive checklist
- Tick off items as you collect them during shopping
- Makes grocery collection quick and stress-free

## 🚀 Features

- **PDF Upload**: Simply drag and drop or select your Tesco order PDF
- **Automatic Parsing**: Extracts product names and quantities from the confirmation email
- **Interactive Checklist**: Clean, mobile-friendly interface for ticking off items
- **Lightweight**: Fast and responsive Flask application
- **No Registration**: Just upload and go

## 📋 How to Use

1. **Export your Tesco order confirmation email to PDF**
   - Open your order confirmation email from Tesco
   - Print/Save as PDF (Ctrl+P → Save as PDF)

2. **Upload to the app**
   - Visit the web app
   - Upload your PDF file
   - Wait for processing

3. **Use your checklist**
   - View your generated checklist
   - Tick off items as you collect them
   - Enjoy stress-free shopping!

## 🛠️ Installation

### Prerequisites
- Python 3.7+
- pip

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/tesco-order-checklist.git
   cd tesco-order-checklist
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:5000`

## 📦 Dependencies

- Flask - Web framework
- PyPDF2 or pdfplumber - PDF text extraction
- Werkzeug - File upload handling
- Additional dependencies listed in `requirements.txt`

## 🏗️ Project Structure

```
tesco-order-checklist/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/
│   ├── index.html        # Upload page
│   └── checklist.html    # Generated checklist view
├── static/
│   ├── css/
│   │   └── style.css     # Styling
│   └── js/
│       └── script.js     # Interactive functionality
├── uploads/              # Temporary PDF storage
└── README.md
```

## ⚡ Quick Start with Docker

```bash
# Build the image
docker build -t tesco-checklist .

# Run the container
docker run -p 5000:5000 tesco-checklist
```

## 🔒 Privacy & Security

- PDFs are processed locally and automatically deleted after use
- No data is stored permanently
- No personal information is retained
- Files are temporarily stored only during processing

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🐛 Known Issues

- Currently optimized for Tesco UK order confirmation emails
- PDF format variations may affect parsing accuracy
- Some special characters in product names may not display correctly

## 🔮 Future Enhancements

- [ ] Support for other supermarket order confirmations
- [ ] Save/share checklist functionality
- [ ] Dark mode support
- [ ] Mobile app version
- [ ] Barcode scanning integration

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built to solve the everyday frustration of grocery collection
- Inspired by the need for a digital solution to paper-based shopping lists
- Thanks to the Flask and Python PDF processing communities

## 📞 Support

If you encounter any issues or have suggestions:
- Open an issue on GitHub
- Check existing issues for solutions
- Contribute improvements via pull requests

---

**Made with ❤️ for easier grocery shopping**