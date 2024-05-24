#Crear un programa que calcule y obtenga el total a pagar por un producto determinado. Se debera de solicitar el nombre y descripcion
#del producto, codigo, cantidad del producto, precio unitario del producto.
#El total a pagar incluye el iva %16 y el descuento. Si se compran de 1 a 5 productos se otorga el %10 de descuento
#Si se compran de 6 a 10 el %15 de descuento y si se compran mas de 10 el %20 de descuento

nombre = input('Ingresa el nombre del producto: ')
descripcion = input('Ingresa la descripcion del producto: ')
codigo = input('Ingresa el codigo del producto: ')
cantidad = int(input('Ingresa la cantidad a comprar del producto: '))
precio = int(input('Ingresa el precio del producto: '))

iva = float(0.16)

if cantidad<=5:
    descuento=float(0.10)
    descuentop='%10'
elif cantidad>=6 and cantidad<=10:
    descuento=float(0.15)
    descuentop='%15'
elif cantidad>10:
    descuento=float(0.20)
    descuentop='%20'
    
total = ((precio*iva)+precio)-(precio*descuento)
print(f'========COMPRA========\nProducto: {nombre}\nDescripcion: {descripcion}\nCodigo: {codigo}\nCantidad: {cantidad}\nPrecio: {precio}\nIVA: %16\nDescuento por total de productos: {descuentop}\nTotal: {total}\n=====================')