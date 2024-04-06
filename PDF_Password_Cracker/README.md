# PDF Password Cracker

This Python script attempts to crack the password of a protected PDF file by generating potential passwords from a combination of mobile number prefixes and dates. It uses multithreading to speed up the process, trying each generated password to decrypt the PDF.

## Dependencies

- `PyPDF2`: A library for PDF manipulation, including reading and decrypting PDF files.
- `concurrent.futures`: A high-level interface for asynchronously executing callables, part of Python's standard library.

## How It Works

The script generates passwords by appending a date in `ddmmyy` format to a given mobile number prefix (e.g., `00001101050`, where `00001` is the mobile number prefix and `110150` is the date 11-Jan-1950). It then attempts to decrypt the PDF using each generated password. The script is optimized to run multiple decryption attempts in parallel using Python's `ThreadPoolExecutor`, significantly speeding up the process.

## Setup

First, ensure you have Python installed on your system. Then, install the required Python package:

```sh
pip install PyPDF2
python pdf_password_cracker.py