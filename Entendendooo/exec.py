from conta import Conta

conta1 = Conta(345, "Victor", 50.0, 1000.0)
conta2 = Conta(555, "Carlos", 100.0, 1200.0)

conta1.transferir(20, conta2)
conta1.extrato()

