from captcha.image import ImageCaptcha
#Specify image size
image = ImageCaptcha(width = 300, height = 100)
#Specify the Text for captcha
captcha_text = input("Enter captcha text : ")
#Generate the image of the given text
data = image.generate(captcha_text)
#write the image on the given file and save it
image.write(captcha_text, 'E:\CAPTCHA1.png')
from PIL import image
Image.open('E:\CAPTCHA1.png')


#imagecaptcha
