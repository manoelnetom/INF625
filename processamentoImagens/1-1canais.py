# Importação das bibliotecas
import cv2
# Leitura da imagem com a função imread()
imagem = cv2.imread('lena.jpg')
print('Largura em pixels: ', end='')
print(imagem.shape[1]) #largura da imagem
print('Altura em pixels: ', end='')
print(imagem.shape[0]) #altura da imagem
print('Qtde de canais: ', end='')
print(imagem.shape[2])
# Mostra a imagem com a função imshow
cv2.imshow("Nome da janela", imagem)
#flip1 = cv2.flip(imagem, 1)
#cv2.imshow("flip1", flip1)
#cubic = cv2.resize(imagem, None, fx=.75, fy=.75, interpolation=cv2.INTER_CUBIC)
#cubic = cv2.resize(imagem, (300, 200), interpolation=cv2.INTER_LINEAR)
#cv2.imshow("interpolação cubica", cubic)
cv2.waitKey(0) #espera pressionar qualquer tecla
# Salvar a imagem no disco com função imwrite()
cv2.imwrite("saida.jpg", imagem)