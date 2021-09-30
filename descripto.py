# Dicionario para descriptografar
letra_criptografada =  {'&':'a','*':'b','+':'c','@':'d','!':'e',
'-':'f','#':'g','C':'h','[':'i','¨':'j','..':'k','°':'l',
'°°':'m','^':'n','ª':'o','º':'p','$':'q','´':'r','`':'s',
'()':'t','(}':'u','<,':'v','??':'w',';':'x',':;':'y','::':'z',
}
msg_criptografada = str(input('Mensagem: '))
mensagem_descriptografada = ''

#Descriptografa a mensagem
for letra in msg_criptografada:
    
    if letra in letra_criptografada:
        mensagem_descriptografada += letra_criptografada[letra]

print(mensagem_descriptografada)



    