text = "X-DSPAM-Confidence:    0.8475"
position = text.find("0")
number = text[position:]
floatnum = float(number)
print(floatnum)