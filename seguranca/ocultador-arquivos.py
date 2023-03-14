"""Este script oculta arquivos do OS como se fosse lá nas propriedades do arquivo e selecionasse ele como oculto."""

import ctypes

atributo_ocultar = 0x02  # atributo em hexadecimal que significa que o arquivo sera ocultado.

retorno = ctypes.windll.kernel32.SetFileAttributesW("ocultar.txt", atributo_ocultar)

if retorno:
    print("Arquivo foi ocultado")
else:
    print("Arquivo nao foi ocultado")