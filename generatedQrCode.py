import qrcode
img = qrcode.make(f' Name: Jacqueline C. Bermundo \n Age: 18 yrs. old \n Vaccination Status: Fully Vaccinated \n Vaccine Name: Sinovac')
type(img)  # qrcode.image.pil.PilImage
img.save("QrCode.png")
