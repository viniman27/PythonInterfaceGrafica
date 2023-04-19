from defTelevisor import *

tv = Televisor('sony', input('informe o modelo:'))

controle = ControleRemoto(tv)

controle.sintonizaCanal('sbt')
controle.trocaCanal('sbt')

print(tv.modelo)
print(tv.canal_atual)