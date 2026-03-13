import fitz

my_path = "https://www.miamidade.gov/corrections/library/MDCR_Daily_Jail_Population.pdf (2)"

doc = fitz.open(my_path)

for page in doc:
    text = page.get_text()
    print(text)