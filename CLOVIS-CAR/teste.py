from loja import Cliente, CarroVendido, CarroNovo

cliente1 = Cliente("Vinicius", "123.456.789-00", "10/05/2005", 60000, 0)

print("===EXTRATO INICIAL===")
cliente1.extrato()

carro_usado = CarroVendido(2015, "Gol", 120000, 25000)

print("\n===VENDA DO CARRO USADO===")
carro_usado.gerar_credito(cliente1)

print("\n===EXTRATO APÓS GERAR CRÉDITO===")
cliente1.extrato()

carro_novo = CarroNovo(2024, "Honda Civic", 0, 70000)
print(f"\nLoja: {CarroNovo.nome_loja()}")

print("\n===COMPRA DO CARRO NOVO===")
carro_novo.vender(cliente1)

print("\n===EXTRATO FINAL===")
cliente1.extrato()