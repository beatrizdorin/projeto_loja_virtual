class Main:
    pass

print ("Testando o Projeto")

from Cliente import Cliente

from Conta import Conta

c1= Cliente('João', '114444-2222')
conta=Conta(c1.nome,6565,0)
#pra puxar o nome novamente, precisa ser "c1.get_nome()"

print (conta.titular," Numero: ",conta.numero,"Seu Saldo: ", conta.saldo)


