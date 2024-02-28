import corefiles as cf

def AddPersona(dataInventario):
    id = input('Ingrese el Nro de Id <-> ')
    nombre = input('Ingrese el Nombre <-> ')
    email = input('Ingrese el email <-> ')
    movil = input('Ingrese el Nro del movil <-> ')
    casa = input('Ingrese el Nro de telefono de su casa <-> ')
    personal = input('Ingrese el Nro de telefono personal <-> ')
    oficina = input('Ingrese el Nro de telefono de la oficina <-> ')
    Person = {
        'id':id,
        'nombre':nombre,
        'email':email,
        'telefono':{
            'movil':movil,
            'casa':casa,
            'personal':personal,
            'oficina':oficina
        }
    }
    dataInventario.get('personal').update({id:Person})


def EditPersona(dataInventario):
    if dataInventario['personal']:
        print('ingresa el Id de la persona que desees editar :')
        codCampus= cf.Search(dataInventario, 'activos')
        isValueTrue = True
        while isValueTrue:
            cf.borrar_pantalla()
            opciones = '1. ID\n2. Nombre\n3. Email\n4. telefono\n5. Salir'
            print(opciones)
            op = input('Ingrese el numero de la seccion que quiere editar <-> ')
            editar = dataInventario['personal'][codCampus]
            if (op=='1'):
                nuevoValor= int(input('Ingrese el nuevo valor para el Id <-> '))
                editar['id'] = nuevoValor
            elif (op=='2'):
                nuevoValor= str(input('Ingrese el nuevo valor para el nombre <-> '))
                editar['nombre'] = nuevoValor
            elif (op=='3'):
                nuevoValor= str(input('Ingrese el nuevo valor para el email <-> '))
                editar['email'] = nuevoValor
            elif (op=='4'):
                opciones = '1. Movil\n2. Casa\n3. Personal\n4. Oficina\n5. Salir'
                print(opciones)
                op = input('Ingrese el numero de la seccion que quiere editar <-> ')
                editar = dataInventario['personal'][codCampus]['telefono']
                if (op == '1'):
                    nuevoValor= str(input('Ingrese el nuevo valor para el movil <-> '))
                    editar['movil'] = nuevoValor
                elif (op == '2'):
                    nuevoValor= str(input('Ingrese el nuevo valor para el Nro de Casa <-> '))
                    editar['casa'] = nuevoValor
                elif (op == '3'):
                    nuevoValor= str(input('Ingrese el nuevo valor para el Nro personal <-> '))
                    editar['personal'] = nuevoValor
                elif (op == '4'):
                    nuevoValor= str(input('Ingrese el nuevo valor para el Nro de Oficina <-> '))
                    editar['oficina'] = nuevoValor
            elif (op=='5'):
                break
    else:
        print('No has ingresado ninguna persona...')
        cf.pausar_pantalla()


def AddAsig(dataInventario):
    NroAsig = input('Ingrese el Nro de la Zona <-> ')
    fechaAsig = input('Ingrese el Nombre de la Zona <-> ')
    tipoAsig = input('Ingrese el capacidad total de la Zona <-> ')
    AsignadoA = input('Ingrese el Nro de la Zona <-> ')
    Activos = []
    while True: #Ciclo para listar los Activos que no se encuentran asignados
        for key,value in dataInventario['Activos'].items():
            print(f'{key} -- {value["nombre"]}')
        Activo = input('Estos son los Activos que no se encuentran asigados seleccione <-> ')
        Activos.append(Activo)
        if not bool(input('Desea seguir asignando Activos? S(si) o Enter(no) -> ')):
            break
    Asig={
        'NroAsig':NroAsig,
        'fechaAsig':fechaAsig,
        'tipoAsig':tipoAsig,
        'AsignadoA':AsignadoA,
        'activos':Activos
    }
    dataInventario.get('asignacion').update({NroAsig:Asig})