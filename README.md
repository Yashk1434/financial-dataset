# 📊 Financial Document Classification Dataset

A curated dataset for training and evaluating document classification models in financial and accounting workflows. This dataset is designed to help automate the categorization of various financial documents like invoices, receipts, payroll slips, investment reports, and financial statements.

---

## 📁 Dataset Structure

Each folder contains:
- 📄 **PDFs** / 📸 **JPG images** of documents belonging to that category.
- You can add scanned images, converted HTML snapshots, or digital financial documents.

---

## 📚 Categories

| Code | Label              |
|:------|:-------------------|
| 0    | Purchase Receipt     |
| 1    | Sales                |
| 2    | Income               |
| 3    | Expense              |
| 4    | Credit Note          |
| 5    | Debit Note           |
| 6    | Payroll              |
| 7    | Bank Transfer        |
| 8    | Asset Purchase       |
| 9    | Others               |
| 10   | Financial Report (optional)|

---

## 📦 Usage

You can use this dataset for:
- 📄 Text-based classification (after OCR)
- 🖼️ Image-based document classification (CNN/transformers)
- 🔍 Financial NLP projects
- 🧾 OCR accuracy testing on financial documents

---

## 🛠️ Scripts Included

- 📂 Folder generation
- 📄 PDF/HTML to image conversion
- 📝 OCR extraction and dataset creation in CSV/JSONL format

---

## 📌 Notes

- Ensure you have [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed for text extraction.
- Use `pdfplumber` or `pdf2image` for working with PDFs.
- Validate OCR results for scanned or poor-quality images.

---

## 📃 Example CSV Format

| text                                      | label        |
|:------------------------------------------|:-------------|
| "Paid ₹5000 to vendor X for software"     | Expense      |
| "Salary processed for May 2024"           | Payroll      |
| "250,000 equity shares in Experis Tech"   | Financial Report |

---
