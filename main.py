import cv2
import pytesseract
import collections
import sys

image = sys.argv[1]

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread(image)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
prikol = []

config = r'--oem 3 --psm 6'

data = pytesseract.image_to_data(img, config=config)

for i, el in enumerate(data.splitlines()):
	if i == 0:
		continue

	el = el.split()
	try:
		# x, y, w, h = int(el[6]), int(el[7]), int(el[8]), int(el[9])
		print(el[11])
		prikol.append(el[11])
	except IndexError:
		print("hmm")

print(prikol)
print("code: " + str([item for item, count in collections.Counter(prikol).items() if count > 4]))
