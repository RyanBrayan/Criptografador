from time import sleep
# Dicionario que muda as letras

letra_criptografada = {'a' : '&','b' : '*','c' : '+','d' : '@','e' : '!',
'f' : '-','g' : '#','h' : 'C','i' : '[','j' : '¨','k' : '..','l' : '°',
'm' : '°°','n' : '^','o' : 'ª','p' : 'º','q' : '$','r' : '´','s' : '`',
't' : '()','u' : '(}','v' : '<,','w' : '??','x' : ';','y' : ':;','z' : '::',
}

mensagem = str(input('Mensagem a ser criptografada: ')).lower()
#Cada letra vai ser substituida pela caractere proposta no dicionario
palavra = ''
for letra in mensagem:
    if letra in letra_criptografada:
        palavra += letra_criptografada[letra]


print('Criptografando a mensagem...')
print()
sleep(0.5)
print(f'Mensagem Criptografada\n\n{palavra}')
