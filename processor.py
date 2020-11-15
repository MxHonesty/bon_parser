from PIL import Image
import pytesseract
import cv2
import re


class Processor:
	""" Clasa care proceseaza imaginea si obtine informatiile relevante din
		aceasta. """
	def __init__(self):
		""" Initializam tesseract din constructor. """
		pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

	def get_data(self, filename):
		""" Metoda determina informatiile relevante din imaginea data.
			Date de intrare: filename (path la fisier)
			Date de iesire: dictionar cu valorile relevante. """
		# https://github.com/muratlutfigoncu
		text = pytesseract.image_to_string(Image.open(filename))

		textList = text.split('\n')

		# Regex pentru datele relevante
		date_Regex 		 = re.compile(".*(data|DATA){1}.*\d{2}(\/|\.|\-|\—)\d{2}.*(\/|\.|\-|\—).*\d{2,4}.*")
		receipt_No_Regex = re.compile(".*(cod identificare fiscala|c.i.f.|cif|cod Fiscal){1}.*:")
		amount_Regex 	 = re.compile(".*(total|TOTAL|subtotal|SUBTOTAL|total lei|TOTAL LEI|LEI|lei){1}.*\d,*\d")
		bunuri_Regex 	 = re.compile(".*\d.*(X|x){1}.*\d,*\d")

		data = {

			"Amount": [],
			"Date": [],
			"Receipt Number": [],
			"Place":[],
			"Preturi": [],
			"Bunuri": [],
		}

		counter = 0
		type = -1
		for rand, x in enumerate(textList):
			x = x.lower()
			#print(x)	# Linie pentru DEBUG
			if counter == 0:
				data["Place"].append(x)

			if date_Regex.match(x):
				data["Date"].append(x)

			if amount_Regex.match(x):
				data["Amount"].append(x)

			if receipt_No_Regex.match(x):
				data['Receipt Number'].append(x)

			if bunuri_Regex.match(x):
				data["Preturi"].append(x)
				# Type 1 inseamna ca obiectul e dupa pret
				# Type 0 inseamna ca obiectul e inainte de pret
				if type == -1:
					if textList[rand-1].isspace() or textList[rand-1] == "":
						type = 1
					elif textList[rand+1].isspace() or textList[rand+1] == "":
						type = 0
				if type == 1:
					data["Bunuri"].append(textList[rand+1])
				elif type == 0:
					data["Bunuri"].append(textList[rand-1])
		print("============================")
		for el in data:
			if len(data[el]) == 0:
				data[el].append("")
			counter += 1
		return data
