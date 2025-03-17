# PDF_Text_Cleaner
## Description
This script extracts text from PDF files, processes it by removing unwanted patterns, correcting spelling errors, and improving grammar using language processing tools. It then saves the cleaned text into a new file for further use. This tool is particularly useful for cleaning and preparing text extracted from scanned documents or image-based PDFs for analysis or reporting purposes.

## Functional Description
The program performs the following steps:
1. Converts PDF pages into images.
2. Extracts text from the images using OCR (Optical Character Recognition) with Tesseract.
3. Removes unwanted patterns and symbols from the extracted text.
4. Converts the text to lowercase and corrects spelling errors using the `autocorrect` library.
5. Checks and corrects grammatical errors using the `language_tool_python` library.
6. Saves the cleaned text into a specified output file.

## How It Works
1. The program converts each page of a PDF document into an image using `pdf2image`.
2. The images are processed through Tesseract OCR to extract the text from them.
3. The script then filters out unwanted patterns and characters using regular expressions.
4. The text is converted to lowercase, and spelling mistakes are corrected using `Speller`.
5. Grammar errors in the text are identified and corrected using `language_tool_python`.
6. Finally, the cleaned-up text is saved into a `.txt` file for further use.

## Input Structure
To run the program, the following parameters need to be provided:
1. **pdf_path**: Path to the input PDF file.
2. **txt_path**: Path where the output text file will be saved.
3. **poppler_path**: Path to the Poppler utility (required for PDF-to-image conversion).
4. **tesseract_cmd**: Path to the Tesseract executable and its language data.

## Technical Requirements
To run the program, the following are required:
1. Python 3.x
2. Installed libraries: `pdf2image`, `pytesseract`, `re`, `language_tool_python`, `autocorrect`
3. Poppler (for PDF to image conversion) installed and configured
4. Tesseract OCR installed and configured with the Russian language data

## Usage
1. Modify the paths for `pdf_path`, `txt_path`, `poppler_path`, and `tesseract_cmd` according to your system.
2. Run the script to process the PDF.
3. The output will be a `.txt` file with the cleaned text, ready for further analysis or use.

## Example Output
Cleaned text saved in the specified `.txt` file, free from unwanted patterns, spelling mistakes, and grammatical errors.

## Conclusion
This tool provides an efficient way to process text from scanned or image-based PDFs, removing irrelevant data, correcting errors, and saving the final cleaned text for further processing or analysis.
