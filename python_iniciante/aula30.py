"""
CONSTANTE = "Variáveis" que não pode mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

velocidade = 86 # velocidade atual do carro
local_carro = 100 # local em que o carro está na estrada

# isso é constante
RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # a distância onde o radar pega

velocidade_carro_passou_radar_1 = velocidade > RADAR_1
carro_multado_radar_range_99 = local_carro >= (LOCAL_1 - RADAR_RANGE)
carro_multado_radar_range_101 = local_carro <= (LOCAL_1 + RADAR_RANGE)

if velocidade_carro_passou_radar_1:
    print("O carro excedeu o limite de velocidade, e foi")
else:
    print("O carro está dentro do limite de velocidade")

if carro_multado_radar_range_99 and \
    carro_multado_radar_range_101 and \
        velocidade_carro_passou_radar_1:
    print("multado pelo radar 1")