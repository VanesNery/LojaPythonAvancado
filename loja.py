#! usr/local/bin/python3
from datetime import datetime
from loja import Cliente, Vendedor, Compra


def main():
    cliente = Cliente('Maria Lima', 44)
    vendedor = Vendedor('Pedro', 36, 5000)
    compra1 = Compra(cliente, datetime.now(), 512)
    compra2 = Compra(cliente, datetime(2018, 6, 4), 256)
    cliente.registrar_compra(compra1)
    cliente.registrar_compra(compra2)
    print(f'Cliente: {cliente}', cliente.is_adulto())
    print(f'Vendedor: {vendedor}')
    
    valor_total = cliente.total_compras()
    qtde_compras = len(cliente.compras)
    print(f'Total: {valor_total} reais em {qtde_compras} compras')
    data_format = cliente.get_data_ultima_compra().strftime("%d/%m/%Y %H:%M")
    print(f'Última compra: {data_format}')


if __name__ == '__main__':
    main()
