
listaAdmin=[]
listaCliente=[]


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
    print('---- ADMINISTRADORES ----\n',
          '\n',
          '1. pendiente de asignar ')

def clientes():
    print('---- ASIGANR NOMBRE A LA TIENDA ----\n',
          '\n',
          '1. pendiente de asignar ')

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
                    nombre=input('Nombre: ')
                    apellido=input('Apellido: ')
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
            elif verificarClientes(cedula):
                print('Ya estas registrado con otro usuario.')
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
        for usuario in listaCliente:
            if usuario['cedulaUsuario']==cedula:
                if usuario['correoUsuario']==correo:
                    clientes()


    menu()
menu()