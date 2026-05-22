from conta import Conta

conta = Conta(345, "Victor", 50.0, 1000.0)
conta1 = Conta(555, "Carlos", 45.5, 1200.0)

conta.extrato()
conta.sacar(5)
conta.extrato()
conta.depositar(10)
conta.extrato()
