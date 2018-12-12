from PIL import Image
import matplotlib.pyplot as plt
from PIL import Image
import pytesseract
from PIL import ImageGrab

def cap(x1,y1,x2,y2,param):

    try:
        img = ImageGrab.grab(bbox=(int(x1), int(y1), int(x2), int(y2)))
        img.save("out.png")
    except IOError:
        print("IO ImageGrab.grab ERROR")
    else:
        pass
    img = img.convert("RGB")
    newImg = Image.new("RGB", img.size, (255,255,255,255))

    w,h = img.size
    rmg = Image.new("RGB", img.size, (255,255,255,255))
    for i in range(w):
        for j in range(h):
            r,g,b = img.getpixel((i,j))
            t = r*255*255 + g * 255 + b
            # yellow

            if t > int(param):
                rmg.putpixel((i, j), (255, 255, 255))
            else:
                rmg.putpixel((i, j), (0, 0, 0))

    rmg.show()
    text = pytesseract.image_to_string(rmg, lang='chi_sim')
    print(text)

