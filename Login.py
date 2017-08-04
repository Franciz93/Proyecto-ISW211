from Categorias import *
from Framework import Login #ejemplo de import en carpeta

listaAdmin=[207960457,"bdrojasc@est.utn.ac.cr"]
listaCliente=[115260227,"fran@gmail.com"]

#Verificar si usuario ya existe en ambas listas, para evitar duplicacion de registros
def verificarClientes(cedula):
    for usuario in listaCliente:
        if usuario['cedulaUsuario']==cedula:
            return True
    return False

#Verificar si usuario ya existe en ambas listas, para evitar duplicacion de registros
def verificarAdmins(cedula):
    for usuario in listaAdmin:
        if usuario['cedulaUsuario']==cedula:
            return True
    return False

#agrega nuevo usuario administrador a la lista de administradores
def nuevoAdmin(cedula,nombre,apellido,telefono,correo):
    nuevoAministrador={
        'cedulaUsuario':cedula,
        'nombreUsuario': nombre,
        'apellidoUsuario':apellido,
        'telefonoUsuario':telefono,
        'correoUsuario':correo,
    }
    listaAdmin.append(nuevoAministrador)


# agrega nuevos usuarios clientes a la lista clientes
def nuevoCliente(cedula,nombre,apellido,telefono,correo):
    nuevoCostumer={
        'cedulaUsuario':cedula,
        'nombreUsuario': nombre,
        'apellidoUsuario':apellido,
        'telefonoUsuario':telefono,
        'correoUsuario':correo,
    }
    listaCliente.append(nuevoCostumer)



# ----------- sub-menus------------------------------------------
def administrador():
    print('---- TecnoSTORE ----\n')
    print()
    print('---- ADMINISTRADORES ----\n',
          '\n',
          '1. pendiente de asignar ')

def clientes():
    print('---- TecnoSTORE ----\n')
    print()
    print('1. Computadoras.\n',
          '2. Telefonos.\n',
          '3. Accesorios.\n',
          '4. Todas las categorias.\n',
          '5. Salir. <<\n')
    while True:
        try:
            opcion=int(input('Seleccione: '))
            break
        except:
            print('Ingrese solo valores numericos!')
        if opcion==1:
            verListaPc()
        elif opcion==2:
            print('LISTA TELEFONOS')
        elif opcion==3:
            print('LISTA ACCESORIOS')
        elif opcion==4:
            print('--- TODOS ---')
        elif opcion==5:
            print('Gracias por visitar nuestra tienda!\n',
                  'Esperamos vuelva pronto!!!')
        else:
            print('Opcion invalida!')


#------------ menu principal de ingreso o registro de usuarios ---------------------
def menu():
    print(' ----------- Bienvenido --------- \n',
          '\n',
          '1. REGISTARSE.\n',
          '2. INICAR SESION.')
    while True:
        try:
            opcion= int(input(' Seleccione la opcion deseada: '))
            break
        except:
            print('Ingrese solo valores numericos.!')
    if opcion==1:
        print('--- Como registara su cuenta: ---\n',
              '1.  Administrador.\n',
              '2.  Cliente.\n',
              '3. <Regresar\n')
        while True:
            try:
                opcion = int(input(' Seleccione la opcion deseada: '))
                break
            except:
                print('Ingrese solo valores numericos.!')
        if opcion==1:
            print(' ---- Llenar el siguiente formulario ----\n')
            while True:
                try:
                    cedula=int(input('Cedula: '))
                    break
                except:
                    print('Ingrese solo valores numericos.')
            while True:
                try:
                    nombre = input('Nombre: ')
                    apellido = input('Apellido: ')
                    break
                except:
                    print('Ingrese solo letras.')
            while True:
                try:
                    telefono=int(input('Telefono: '))
                    break
                except:
                    print('Ingrese solo valores numericos.')
            correo= input('Correo electronico: ')

            if verificarAdmins(cedula):
                print('Registro invalido, usuario ya existe en sistema.')
                menu()
            elif verificarClientes(cedula):
                print('Ya estas registrado con otro usuario.')
                menu()
            else:
                nuevoAdmin(cedula, nombre, apellido, telefono, correo)

                print('Registro exitoso!!!! ')

        elif opcion == 2:
            print(' ---- Llenar el siguiente formulario ----\n')
            while True:
                try:
                    cedula = int(input('Cedula: '))
                    break
                except:
                    print('Ingrese solo valores numericos.')
            while True:
                try:
                    nombre = input('Nombre: ')
                    apellido = input('Apellido: ')
                    break
                except:
                    print('Ingrese solo letras.')
            while True:
                try:
                    telefono = int(input('Telefono: '))
                    break
                except:
                    print('Ingrese solo valores numericos.')
            correo = input('Correo electronico: ')

            if verificarClientes(cedula):
                print('Registro invalido, usuario ya existe en sistema.')
            elif verificarAdmins(cedula):
                print('Ya estas registrado con otro usuario.')
            else:
                nuevoCliente(cedula, nombre, apellido, telefono, correo)
                nuevoCliente(123,'Franciz','Hernandez',86700606,'fran@gmail.com')
                print('Registro exitoso!!!! ')

        elif opcion==3:
            menu()
        else:
            print('Opcion Invalida, intente de nuevo!')
    elif opcion==2:

        while True:
            try:
                cedula = int(input('Ingrese su cedula: '))
                break
            except:
                print('Ingrese solo valores numericos.')
        correo=input('Ingrese correo: ')
        for usuario in listaAdmin:
            if usuario['cedulaUsuario']==cedula:
                if usuario['correoUsuario']==correo:
                    administrador()
                else:
                    print('Usuario y/o contraseña invalida')
            else:
                print('Usuario y/o contraseña invalida')

        for usuario in listaCliente:
            if usuario['cedulaUsuario']==cedula:
                if usuario['correoUsuario']==correo:
                    clientes()
                else:
                    print('Usuario y/o contraseña invalida')
            else:
                print('Usuario y/o contraseña invalida')

    menu()
menu()