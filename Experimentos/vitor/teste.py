import cv2

numbers_levels = 1

levels = []

for level in range(numbers_levels):
  imagem_labirinto = cv2.imread(f'labirinto{level}.png', 1)

  matriz = []
  for j in range(15):
    linha = []
    for i in range(15):
      fatia = imagem_labirinto[(j*16)+1:((j+1)*16+1), (i*16)+1:((i+1)*16)+1]
      
      string = ""

      if 0 in fatia[8, 0]: string += "<"
      if 0 in fatia[0, 8]: string += "^"
      if 0 in fatia[8, 15]: string += ">"
      if 0 in fatia[15, 8]: string += "v"

        
      cv2.imwrite(f"teste/{j,i}-foto.png", fatia)    
      cv2.imwrite(f"teste/{j,i}.png", fatia[8, 0])    
      linha.append(string)
      # cv2.waitKey(0)
    
    matriz.append(linha)
  for i in matriz:
    print(i)
  levels.append(matriz)