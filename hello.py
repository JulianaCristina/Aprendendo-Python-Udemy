 #--coding: utf-8 --
# r = somente leitura
# w =  escrita, cria um arquivo novo em branco, se existir apaga o existente
# a = leitura e escrita (add o novo conteudo no final do arquivo)
# r+(leitura e escrita), w+a(também apaga o conteudo anterior do arquivo), a+(abre o arquivo para atualização)

#Lendo arquivos

#read() - lê arquivo
#readline() - lê uma linha
#readlines() - lê o arquivo e o armazena em uma lista


arquivo = open("arquivo.txt")
#print(arquivo) #mostra o nome do arquivo que estou tentando abrir, o modo de leitura e o endereço na memória

#linhas = arquivo.readlines() #converte em uma lista
#print(linhas)

#for linha in linhas:
#    print(linha)

texto_completo = arquivo.read()
print(texto_completo)

w=open("arquivo2.txt", "w")
w.write("Esse é o meu arquivo")
w.close