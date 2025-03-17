import pdf2image
import pytesseract
import re
import language_tool_python
from autocorrect import Speller
import os

os.environ['JAVA_HOME'] = '/opt/homebrew/opt/openjdk@11'

# Initialize the necessary tools
spell = Speller(lang='ru')  # Use autocorrect for spelling correction
tool = language_tool_python.LanguageTool('ru-RU')  # For grammatical checking

# Path to the original PDF file
pdf_path = r'/Users/aleksandrababkina/Documents/Python скрипты/Мама/рабочий проект том 4 ПДСУ.pdf'

# Path for saving the TXT file
txt_path = r'/Users/aleksandrababkina/Documents/Python скрипты/Мама/рабочий проект том 4 ПДСУ.txt'

# Specify the path to Poppler
poppler_path = "/opt/homebrew/opt/poppler"

# Specify the path to Tesseract and language data
pytesseract.pytesseract.tesseract_cmd = r"/opt/homebrew/bin/tesseract"
pytesseract.pytesseract.tessdata_dir_config = '--tessdata-dir "/opt/homebrew/share/tessdata"'

# List of patterns to be removed
unwanted_patterns = [
    r"047/07-ТХ", r"Инв\. Nº.*", r"подл.*", r"Подпись и дата.*", r"Взам\..*",
    r"Изм . Л и с т Nº докум\..*", r"Подпись.*", r"Дата.*", r"Ж/Д.*", r"км.*",
    r"расположен.*", r"Ё", r"Ё_;", r"\|=", r"% Ё", r"Н . й", r"П оо Ю", r"Н\\", 
    r"1&", r"Ко ", r"с\|", r"®", r"!", r";", r"Е", r"\.З 10", r"\^", r"Изм\.",
    r"Лит", r"№", r"докум\.", r"<", r"“", r"%", r"НЕ", r%"'", r"Н", r"й", r"Лист",
    r"'|", r"„", r"^[ ]{1,2}$", r"^\s*$", r"|", r"\|", r"\(", r"\)", r"\[", r"\]", r"\""
]

with open(txt_path, "w", encoding="utf-8") as txt_file:
    # Convert PDF to images, starting from page 49
    images = pdf2image.convert_from_path(pdf_path, first_page=49, poppler_path="/opt/homebrew/opt/poppler/bin")
    
    # Text recognition process for all pages
    for page_num, img in enumerate(images, start=49):
        print(f"Processing page {page_num}")  # Display the current page number
        
        # Recognize text from the image
        text = pytesseract.image_to_string(img, lang="rus", config=pytesseract.pytesseract.tessdata_dir_config)
        
        # Remove unwanted strings and characters
        for pattern in unwanted_patterns:
            text = re.sub(pattern, "", text)
        
        # Convert the text to lowercase and correct spelling
        text = text.lower()  # Convert all text to lowercase
        words = text.split()
        corrected_words = [spell(word) for word in words]  # Correct the spelling of each word
        
        corrected_text = ' '.join(corrected_words)  # Rebuild the corrected text
        
        # Correct grammatical errors using LanguageTool
        matches = tool.check(corrected_text)
        corrected_text = language_tool_python.utils.correct(corrected_text, matches)
        
        # Write the corrected text of the page to the file
        txt_file.write(corrected_text)
        
print(f"Conversion completed. File saved: {txt_path}")
