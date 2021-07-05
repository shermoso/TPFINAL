'''
TP FINAL

POO
'''

'''herencia. herencia flores hereda todos los datos de torta. polimorfismo es que tranforma el numero'''
# class Torta:
#
#     def __init__(self, sabor, relleno, tipo, tamanio):
#         self.sabor = sabor
#         self.relleno = relleno
#         self.tipo = tipo
#         self.tamanio = tamanio
#
#     def calcular_precio(self):
#         if self.tamanio == "Pequenia":
#             self.precio = 1000
#         elif self.tamanio == "Mediana":
#             self.precio = 1500
#         elif self.tamanio == "Grande":
#             self.precio = 2000
#             return print("El precio es $", self.precio)
#         else:
#            print("El tamaño ingresado es incorrecto, solo puede ser pequenia, mediana o grande")
#
#
# sabor = input(str('''Que sabor quieres?
#               Chocolate
#               Vainilla
#               Brownie'''))
# relleno = input(str('''Que relleno quieres?
#                 Dulce de leche
#                 Crema y frutillas
#                 Nutella'''))
# tipo = input(str('''Que tipo quieres?
#              Letter Cake
#              Number Cake'''))
# tamanio = input(str('''Que tamaño quieres?
#                 Pequenia
#                 Mediana
#                 Grande'''))
#
#
'''POLIMORFISMO'''
# class Flores(Torta):
#     def __init__(self, sabor, relleno, tipo, tamanio, decoracion):
#         super().__init__(sabor, relleno, tipo, tamanio)
#         self.decoracion = decoracion
#
#     def calcular_precio(self):
#         if self.tamanio == "Pequenia" :
#             self.precio = 1000 * 1.5
#         elif self.tamanio == "Mediana":
#             self.precio = 1500 * 1.5
#         elif self.tamanio == "Grande":
#             self.precio = 2000 * 1.5
#             return print("El precio de la torta con decoracion de flores es $", self.precio)
#
#         else:
#            print("El tamaño ingresado es incorrecto, solo puede ser pequenia, mediana o grande")
#
# decoracion = "Flores comestibles para decorar"
#
# instancia_torta = Torta(sabor, relleno, tipo, tamanio)
# instancia_torta.calcular_precio()
#
# instancia_flores = Flores(sabor, relleno, tipo, tamanio, decoracion)
# instancia_flores.calcular_precio()


'''ENCAPSULAMIENTO'''
#     def __calculartiempoprep(self):
#         if self.tamanio == "Pequenia":
#             self.__tiempopreparacion = 30
#         elif self.tamanio == "Mediana":
#             self.__tiempopreparacion = 60
#         elif self.tamanio == "Grande":
#             self.__tiempopreparacion = 90
#             return self.__tiempopreparacion
#
# tiempopreparacion = "hola"


'''
herencia: flores hereda los atributos, y le suma decoracion. el metodo para calcular el precio, sale 50% mas si decora con flores.
'''

#agrego class superheroe que hereda atributo, tmb defino calcular precio dif porq tiene en cta el poder del superheroe que se duplica el precio x ej=polimorfismohereda lo de la torta y le agrega cosas


'''CONSUMIENDO API DE TERCEROS'''


# import requests
#
# response = requests.get('https://api.spoonacular.com/recipes/complexSearch?query=cake&addRecipeInformation=true&apiKey=d8966faa4a5f41119eb25f9a108d8757')
#
# status_code = response.status_code
#
# if status_code == 200:
#     json = response.json()
#     receta = json['results']
#     for i in receta:
#         titulo = i['title']
#         tiempo_preparacion = i['readyInMinutes']
#         url_receta = i['sourceUrl']
#         print('Receta de', titulo)
#         print('El tiempo de preparacion estimado es de', tiempo_preparacion, 'minutos')
#         print('Se podra acceder a la receta a traves del siguiente link:', url_receta)
# else:
#     print("Error en la solicitud")

# import sqlite3
#
# conexion = sqlite3.connect("RECETAS.db")
# cursor = conexion.cursor()
#
# sentenciaSQL = "CREATE TABLE recetas"
# sentenciaSQL = sentenciaSQL + "(Titulo VARCHAR(100), "
# sentenciaSQL = sentenciaSQL + "Tiempo  INTEGER,"
# sentenciaSQL = sentenciaSQL + "Link VARCHAR(100))"
#
# recetas = [
#     ('Cake Balls', 60, 'https://www.pinkwhen.com/cake-balls-recipe/'), #no es lo mejor usar tuplas
#     ('Cake De Naranja', 45, 'https://www.foodista.com/recipe/XL4YYGS5/cake-de-naranja/'),
#     ('Cake Mix Donuts', 20, 'https://www.pinkwhen.com/cake-mix-donuts/'),
#     ('Cake Batter Chocolates', 45, 'http://www.foodista.com/recipe/T287CBWD/cake-batter-chocolates/'),
#     ('Cake with wine and olive oil', 45, 'https://www.foodista.com/recipe/8S2CHHYJ/cake-with-wine-and-olive-oil'),
#     ('Cake Mix Cookie Bars Brownie', 35, 'https://www.pinkwhen.com/cake-mix-cookie-bars-brownie-recipe/'),
#     ('Cake with lemon, rosewater and pistachios', 45, 'https://www.foodista.com/recipe/F8MSDTTK/cake-with-lemon-rosewater-and-pistachios'),
#     ('Dump Cake', 45, 'https://www.foodista.com/recipe/WGSFVKKC/dump-cake'),
#     ('Plum Cake', 45, 'https://www.foodista.com/recipe/LXVZGLQ5/plum-cake'),
#     ('Oreo Cake', 45, 'http://www.foodista.com/recipe/MQXQDZWD/oreo-cake'),
# ]
#
# sentenciaSQL = "INSERT INTO recetas VALUES (?,?,?)"
# cursor.executemany(sentenciaSQL, recetas)
# conexion.commit()
# conexion.close()


# lo dejamos enuna base de datos para llamar una vez sola a la api, y que nos cobren una vez sola

'''
explicacion:
accedemos a una API para consultar recetas de tortas. si el status code es 200, es decir, esta OK, queremos que nos devuelva en formato json ciertos valores.
para cada elemento de receta, queremos que nos muestre (imprima) el titulo de la receta, el tiempo de preparacion estimado y por ultimo, un link donde podremos acceder a la receta y fotos de la misma.
Por ultimo, trasladamos estos datos a una base de datos para tener un mejor acceso a las recetas'''

#http://json.parser.online.fr/


''' DECISIONES DE NEGOCIO'''

'''ARMAMOS UN DATAFRAME EN BASE A LOS MESES Y LAS CANTIDADES DE TORTAS QUE SE VENDIERON POR MES, PARA ANALIZAR CUANDO TENDREMOS MAYOR DEMANDA'''
'''EMPEZAMOS NUESTRO EMPRENDIMEINTO EN 2017, ENTONCES PONEMOS LOS DATOS DE LAS TORTAS VENDIDAS POR MES, DURANTE LOS ULTIMOS 4 ANIOS, SIN CONTAR EL 2021.'''
'''estos datos no son reales, son estimados. es un programa que tenemos en produccion, y queremos que provengan de datos veridicos'''


# import pandas as pd
# import matplotlib.pyplot as plt
#
# tortas_vendidas = [530, 515, 342, 401, 360, 335, 391, 407, 523, 422, 621, 659]
# meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
#
# frame = pd.DataFrame({'Meses': meses, 'Total unidades vendidas': tortas_vendidas})
#
# print(frame)
#
# frame.plot.bar(x='Meses', y='Total unidades vendidas', rot=0)
# plt.savefig('grafico_unidadespormes.png')
# plt.title('Total unidades vendidas por mes durante 2017 a 2020')
# plt.show()


'''Podemos observar en que los ultimos meses del anio son los que mayor demanda hay, por lo que podemos anticiparnos a esto comprando mas materia prima'''
''' Queremos aclarar estos datos son estimados, no son reales. sabemos que en diciembre las ventas aumentan por las fiestas, en septiembre porque es cuando mas cumple la gente...es un programa que tenemos en produccion, y queremos que provengan de datos veridicos'''


'''CONSTRUYENDO UNA API'''


# from flask import Flask, jsonify, request
#
# app = Flask(__name__)
#
# tortas = [
#     {'Nro pedido': 5200, 'Tipo torta':'Letter cake', 'Sabor':'Chocolate', 'Relleno':'Dulce de leche', 'Tamanio':'Grande', 'Cantidad':1},
#     {'Nro pedido': 5201, 'Tipo torta':'Letter cake', 'Sabor': 'Vainilla', 'Relleno': 'Dulce de leche', 'Tamanio': 'Mediana', 'Cantidad': 1},
#     {'Nro pedido': 5202, 'Tipo torta':'Number cake', 'Sabor': 'Brownie', 'Relleno': 'Nutella', 'Tamanio': 'Grande','Cantidad': 2},
#     {'Nro pedido': 5203, 'Tipo torta': 'Number cake', 'Sabor': 'Chocolate', 'Relleno': 'Dulce de leche', 'Tamanio': 'Pequenia', 'Cantidad': 1},
#     {'Nro pedido': 5204, 'Tipo torta': 'Letter cake', 'Sabor': 'Brownie', 'Relleno': 'Crema y frutillas', 'Tamanio': 'Pequenia', 'Cantidad': 3},
#     {'Nro pedido': 5205, 'Tipo torta': 'Number cake', 'Sabor': 'Vainilla', 'Relleno': 'Nutella', 'Tamanio': 'Mediana',  'Cantidad': 1}]
#
# @app.route('/tortas', methods=['GET'])
# def tortasGet():
#     return jsonify({'tortas': tortas, 'status': 'ok'})
#
# @app.route('/tortas', methods=['POST']) #llamo a la API. por la ruta POST, manda datos en formato JSON, ejecuto la funcion tortasPost.
# def nuevopedido(): #el programa debe dar de alta el nuevo pedido, con datos del body
#     body = request.json #objeto request json que esta en el body. obtenemos un dicc que contiene el body. para acceder al valor del campo nombre del json, lo accedemos a traves del body yla clave de busqueda
#     nro_pedido = body['Nro pedido'] #body: lugar donde mando info en formato JSON.
#     tipo_torta = body['Tipo torta']
#     sabor = body['Sabor']
#     relleno = body['Relleno']
#     tamanio = body['Tamanio']
#     cantidad = body['Cantidad']
#     nuevo_pedido = {'Nro pedido': nro_pedido, 'Tipo torta': tipo_torta, 'Sabor': sabor, 'Relleno': relleno, 'Tamanio': tamanio,  'Cantidad': cantidad}
#     return jsonify({'tortas': nuevo_pedido, 'status': 'ok'})
# # en una base de datos seria un insert. devuelvo un json que digo que este es el nuevo pedido. podemos dar de alta un producto que ya existe, si existe deberia dar un status de ya existe y se entere que exista
#
# if __name__ == '__main__':
#     app.run(debug=True, port=4000)
#



'''USO DE BASE DE DATOS'''

#import sqlite3
# import pandas as pd
# import datetime


#conexion = sqlite3.connect("Clientes.db")
#cursor = conexion.cursor()


#sentenciaSQL = "CREATE TABLE Clientes"
#sentenciaSQL = sentenciaSQL + "(nro INTEGER NOT NULL,"
#sentenciaSQL = sentenciaSQL + "nombre VARCHAR(100) NOT NULL,"
#sentenciaSQL = sentenciaSQL + "apellido VARCHAR(100) NOT NULL,"
#sentenciaSQL = sentenciaSQL + "telefono INTEGER NOT NULL,"
#sentenciaSQL = sentenciaSQL + "fecha TIMESTAMP NOT NULL,"
#sentenciaSQL = sentenciaSQL + "fecha_entrega INTERGER NOT NULL,"
#sentenciaSQL = sentenciaSQL + "orden TEXT NOT NULL,"
#sentenciaSQL = sentenciaSQL + "total INTEGER NOT NULL)"
#
# sentenciaSQL2 = "CREATE TABLE Materia_Prima"
# sentenciaSQL2 = sentenciaSQL2 + "(nombre VARCHAR(100) NOT NULL,"
# sentenciaSQL2 = sentenciaSQL2 + "stock INTEGER NOT NULL)"


# nro = int(input('ingrese el nro:'))
# nombre = str(input('ingrese el nombre:'))
# apellido = str(input('ingrese el apellido:'))
# telefono = int(input('ingrese el nro de telefono:'))
# fecha = datetime.datetime.now()
#fecha_entrega = datetime.datetime.strptime(input('ingrese fecha y hora de entrega: '))

# def comprobar_fecha(text):
#     try:
#         datetime.datetime.strptime(text, '%Y/%m/%d')
#     except:
#         return "El formato debe ser  YYYY/MM/DD"
#     return datetime.datetime.strptime(text, '%Y/%m/%d')
#
# fecha_entrega = input("ingrese la fecha de entrega: ")
#
# comprobar_fecha(fecha_entrega)
#
# sabor = str(input('¿vainilla, chocolate o brownie? '))
# relleno = str(input('¿ddl, crema y frutillas o nutella? '))
# tipo = str(input('¿letter o number cake? '))
# tamanio = str(input('¿pequenia, mediana o grande? '))
# decoracion = str(input('¿flores comestibles, cobertura de chocolate o nada? '))
# orden = '{}; {}; {}; {}; {}'.format(sabor,relleno,tipo,tamanio, decoracion)
# precio = int(input('ingrese el precio: $'))
#
#
# clientes = [
#             (nro, nombre, apellido, telefono, fecha, fecha_entrega, orden, precio)
#         ]
# sentenciaSQL = "INSERT INTO clientes VALUES (?, ?, ?, ?, ?, ?, ?, ?)"


# Materia_Prima = [
#     ('Harina', 2000),
#     ('Chocolate', 5000),
#     ('Dulce de Leche', 5500),
#     ('Huevos', 3000),
#     ('Frutillas', 6600),
#     ('Crema', 2000),
#     ('Nutella', 5500),
#     ('Esencia de Vainilla', 1500)
# ]
# sentenciaSQL2 = "INSERT INTO Materia_Prima VALUES (?, ?)"
#
#
#cursor.execute(sentenciaSQL)
# cursor.execute(sentenciaSQL2)
# cursor.executemany(sentenciaSQL, clientes)
# cursor.executemany(sentenciaSQL2, Materia_Prima)
#conexion.commit()
# conexion.close()

''' FUNCION str2: si algun caracter es un nro lanzo except '''

# Pandas me permite trabajar con estructuras amigables (csv, pkl, db)
#
# Conexion --> hago la conexion con la db. Acá se me crea el db de covid y se me agrega a carpeta en la compu.
#
# El cursor me permite ejecutar: llamar a una db, crear tablas, etc.
#
# CREATE TABLE --> creo las tablas y les agrego los campos que quiero que tenga
#                 INTEGER: para números enteros
#                 TEXT: sólo texto
#                 TIMESTAMP: devuelve una indicación de fecha y hora a partir de un valor o par de valores.
#                 NOT NULL:   obliga a que un campo siempre contenga un valor, lo que significa que no puede insertar un
#                             nuevo registro o actualizar un registro sin agregar un valor a este campo.
#                 VARCHAR (100): almacena series de caracteres, los datos pueden consistir en letras, números y símbolos.
#
# Input -->   para poder ingresar datos desde la terminal.
#             int: los input son siempre datos de tipo stream, es por eso que a los datos numéricos le pongo int delante
#                 para transformarlos.
#
# {} . format(variables) -->  para poder ingresar varios datos de varias variables a la terminal a partir de un solo campo
#                             en el db.
#
# INSERT INTO ... VALUES (?) -->  una vez creada la tabla, quiero ingresarle datos. Por eso primero creo una variable
#                                 definiendo lo que quiero agregar, luego le ingreso la cantidad de ? necesarios
#                                 dependiendo la cantidad de campos que tiene mi tabla.
#
# Executemany --> le indico la funcion de ejecutar varias entradas de valores dentro de una misma tabla.
#
# Commit -->  define el final de una transacción ejecutada con éxito. Este comando asegura que todas las modificaciones
#             efectuadas durante la transacción se vuelvan parte permanente de la base.
#

''' LECTURA DE TEXTO PLANO: BLOCK DE NOTAS'''

# from io import open
# archivo = open('C:/Users/Josefina/OneDrive/Escritorio/Facultad Josefina/Primer Cuatrimestre 2021/Fundamentos de Informatica/Naposbakery.txt', 'r+')
# lista = archivo.readlines()
# lista[2] = '- Chocolate\n- Vainilla\n- Brownie'
# lista[7] = '- Dulce de leche\n- Crema y frutillas\n- Nutella'
# lista[12] = '- Letter Cake\n- Number Cake'
# lista[16] = '- Pequenio\n- Mediano\n- Grande'
# lista[21] = '- Flores Comestibles\n- Cobertura de Chocolate'
# archivo.seek(0)
# archivo.writelines(lista)
#
# archivo.close()
# del (archivo)
# with open('C:/Users/Josefina/OneDrive/Escritorio/Facultad Josefina/Primer Cuatrimestre 2021/Fundamentos de Informatica/Naposbakery.txt', 'r+') as archivo:
#     print(archivo.read())


# r+ -->  Cuando queremos abrir un archivo en modo lectura,pero a su vez querramos tener la posibilidad de sobreescribir
#         parte del mismo.
#
# archivo.seek(0) --> Cuando indicamos a partir de qué parte quiero que inicie el puntero y desde ahí contar el índice
#                     para modificar las notas.
#
# del (archivo) -->   Es optativa, aunque nos asegura liberar de la memoria los recursos que utilizó Python para operar
#                     sobre el archivo.
#                     En programas cortos esta línea no es absolutamente necesaria, sin embargo, en sistemas de gran
#                     envergadura es una buena práctica ir liberando la memoria que ya no vamos a utilizar.




''' AUTOMATIZACION EJECUTAR DESDE LA TERMINAL '''

# import sys
# argv = sys.argv
# nombre = argv[1]
# print('Hola mundo! Bienvenido', nombre)

 # import sys
 # argv = sys.argv
 # nro1 = int(argv[1])
 # nro2 = int(argv[2])
 # suma = nro1 + nro2
 # print('La suma de los nros es:', suma)
 #
 # import sys
 # argv = sys.argv
 # print(argv)
 # if len(argv) == 3:
 #     nro1 = int(argv[1])
 #     nro2 = int(argv[2])
 #     suma = nro1 + nro2
 #     print('La suma es:', suma)
 # elif len(argv) > 3:
 #     print('No se pueden sumar más de 2 nros!')
 # else:
 #     print('Faltan parámetros de entrada')
'''Automatizacion inflacion'''
# import sys
# argv = sys.argv
# inflacion = argv[1] #voy a la terminal y pongo python TPFINAL.py 10
# print('la inflacion es:', inflacion)
# # inflacion = 1.1
# import sqlite3
# conexion = sqlite3.connect("CLIENTES.db")
# cursor = conexion.cursor()
#
# cursor.execute("UPDATE clientes SET Total = Total * ? WHERE Total = 2000", (inflacion,))
# conexion.commit()
# conexion.close()