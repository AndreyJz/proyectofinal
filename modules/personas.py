import corefiles as cf
from corefiles import Try


def AddPersona(dataInventario):
    id = Try('int','Ingrese el Nro de Id <-> ',dataInventario)
    nombre = Try('str','Ingrese el Nombre <-> ',dataInventario)
    email = Try('str','Ingrese el email <-> ',dataInventario)
    movil = Try('int','Ingrese el Nro del movil <-> ',dataInventario)
    casa = Try('int','Ingrese el Nro de telefono de su casa <-> ',dataInventario)
    personal = Try('int','Ingrese el Nro de telefono personal <-> ',dataInventario)
    oficina = Try('int','Ingrese el Nro de telefono de la oficina <-> ',dataInventario)
    Person = {
        'id':str(id),
        'nombre':nombre,
        'email':email,
        'telefono':{
            'movil':movil,
            'casa':casa,
            'personal':personal,
            'oficina':oficina
        }
    }
    dataInventario.get('personas').update({id:Person})


def EditPersona(dataInventario):
    if dataInventario['personas']:
        cf.borrar_pantalla()
        print('ingresa el Id de la persona que desees editar :')
        codCampus= cf.Search(dataInventario, 'personas')
        isValueTrue = True
        while isValueTrue:
            cf.borrar_pantalla()
            opciones = '1. Nombre\n2. Email\n3. telefono\n4. Guardar y salir'
            print(opciones)
            op = input('Ingrese el numero de la seccion que quiere editar <-> ')
            editar = dataInventario['personas'][codCampus]
            if (op=='1'):
                nuevoValor= Try('str','Ingrese el nuevo valor para el nombre <-> ',dataInventario)
                editar['nombre'] = nuevoValor
            elif (op=='2'):
                nuevoValor= Try('str','Ingrese el nuevo valor para el email <-> ',dataInventario)
                editar['email'] = nuevoValor
            elif (op=='3'):
                cf.borrar_pantalla()
                opciones = '1. Movil\n2. Casa\n3. Personal\n4. Oficina\n5. Guardar y salir'
                print(opciones)
                op = input('Ingrese el numero de la seccion que quiere editar <-> ')
                editar = dataInventario['personas'][codCampus]['telefono']
                if (op == '1'):
                    nuevoValor= Try('int','Ingrese el nuevo valor para el movil <-> ',dataInventario)
                    editar['movil'] = nuevoValor
                elif (op == '2'):
                    nuevoValor= Try('int','Ingrese el nuevo valor para el Nro de Casa <-> ',dataInventario)
                    editar['casa'] = nuevoValor
                elif (op == '3'):
                    nuevoValor= Try('int','Ingrese el nuevo valor para el Nro personal <-> ',dataInventario)
                    editar['personal'] = nuevoValor
                elif (op == '4'):
                    nuevoValor= Try('int','Ingrese el nuevo valor para el Nro de Oficina <-> ',dataInventario)
                    editar['oficina'] = nuevoValor
            elif (op=='4'):
                break
            else:
                print('El valor ingresado no esta asociado a una seccion...')
                cf.pausar_pantalla()
    else:
        print('No has ingresado ninguna persona...')
        cf.pausar_pantalla()
        