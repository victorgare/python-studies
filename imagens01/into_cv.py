import cv2

# Visualizando uma imagem com matplotlib

import matplotlib.pyplot as plt

img = cv2.imread('imagem.jpg')

# o open CV usa como padrao para cada cor o BGR (RGB invertido), sendo assim
# precisamos que o array de bytes seja lido de trás para frente
plt.imshow(img[:, :, ::-1])
plt.xticks([]), plt.yticks([])
plt.show()


# converte a imagem para tons de cinza
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cmap é o color map que gostariamos de usar
# preto = frio, cinza = quente
plt.imshow(imgray, cmap='gray')
plt.show()

# mostra o histograma da imagem
plt.figure() # cria uma nova janela grafica
plt.hist(imgray.ravel(), bins=256)

# aumenta o brilho da imagem
imgray2 = imgray + 50
plt.figure()
plt.imshow(imgray2, cmap='gray')

# usa uma funcao do cv2 para somar 50 ao valor da cor
# esta funcao nao deixa o pixel estourar, passando de 255 ou ficando abaixo de 0
imgray2 = cv2.add(imgray, 50)
plt.figure()
plt.imshow(imgray2, cmap='gray')


# mostra o histograma da imagem do imgray2
plt.figure() # cria uma nova janela grafica
plt.hist(imgray2.ravel(), bins=256)

# aumenta o contraste
mult = 2
adic = -200
imgray3 = cv2.convertScaleAbs(imgray, alpha=mult, beta=adic)
plt.figure()
plt.imshow(imgray3, cmap='gray')

plt.figure() # cria uma nova janela grafica
plt.hist(imgray3.ravel(), bins=256)


# diminui o contraste
mult = 0.5
adic = 100
imgray4 = cv2.convertScaleAbs(imgray, alpha=mult, beta=adic)
plt.figure()
# importa o normalizer que servira para ajustar a escala do grafico
from matplotlib.colors import Normalize
plt.imshow(imgray4, cmap='gray', norm=Normalize(vmin=0, vmax=255))

plt.figure() # cria uma nova janela grafica
plt.hist(imgray4.ravel(), bins=256)
plt.xlim([0, 255])

# equaliza o histograma
imgray5 = cv2.equalizeHist(imgray4)
plt.figure()
plt.imshow(imgray5, cmap='gray', norm=Normalize(vmin=0, vmax=255))
plt.figure()
plt.hist(imgray5.ravel(), bins=256)
plt.xlim([0, 255])