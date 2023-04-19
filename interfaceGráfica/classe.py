class Pessoa:

    idade = 15

    def saudacao (self):
        
        print('Olá Pessoas!')

# create a new object of Person class
matheus = Pessoa()
# Output: 15
print(matheus.idade)
# Output: <bound method Person.greet of <__main__.Person object>>
print(matheus.saudacao)
# Chamando o método saudacao()
# Output: “Olá Pessoas!”
matheus.saudacao()