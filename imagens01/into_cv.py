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