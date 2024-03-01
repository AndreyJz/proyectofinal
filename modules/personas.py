import corefiles as cf
from corefiles import Try


def AddPersona(dataInventario):
    id = Try('int','Ingrese el Nro de Id <-> ',dataInventario,'agregar')
    nombre = Try('str','Ingrese el Nombre <-> ',dataInventario,'agregar')
    email = Try('str','Ingrese el email <-> ',dataInventario,'agregar')
    movil = Try('int','Ingrese el Nro del movil <-> ',dataInventario,'agregar')
    casa = Try('int','Ingrese el Nro de telefono de su casa <-> ',dataInventario,'agregar')
    personal = Try('int','Ingrese el Nro de telefono personal <-> ',dataInventario,'agregar')
    oficina = Try('int','Ingrese el Nro de telefono de la oficina <-> ',dataInventario,'agregar')
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
    dataInventario.get('personas').update({id:Person})


def EditPersona(dataInventario):
    if dataInventario['personas']:
        print('ingresa el Id de la persona que desees editar :')
        codCampus= cf.Search(dataInventario, 'personas')
        isValueTrue = True
        while isValueTrue:
            cf.borrar_pantalla()
            opciones = '1. ID\n2. Nombre\n3. Email\n4. telefono\n5. Salir'
            print(opciones)
            op = input('Ingrese el numero de la seccion que quiere editar <-> ')
            editar = dataInventario['personas'][codCampus]
            if (op=='1'):
                nuevoValor= Try('int','Ingrese el nuevo valor para el Id <-> ',dataInventario,'')
                editar['id'] = nuevoValor
            elif (op=='2'):
                nuevoValor= Try('str','Ingrese el nuevo valor para el nombre <-> ',dataInventario,'')
                editar['nombre'] = nuevoValor
            elif (op=='3'):
                nuevoValor= Try('str','Ingrese el nuevo valor para el email <-> ',dataInventario,'')
                editar['email'] = nuevoValor
            elif (op=='4'):
                opciones = '1. Movil\n2. Casa\n3. Personal\n4. Oficina\n5. Salir'
                print(opciones)
                op = input('Ingrese el numero de la seccion que quiere editar <-> ')
                editar = dataInventario['personas'][codCampus]['telefono']
                if (op == '1'):
                    nuevoValor= Try('int','Ingrese el nuevo valor para el movil <-> ',dataInventario,'')
                    editar['movil'] = nuevoValor
                elif (op == '2'):
                    nuevoValor= Try('int','Ingrese el nuevo valor para el Nro de Casa <-> ',dataInventario,'')
                    editar['casa'] = nuevoValor
                elif (op == '3'):
                    nuevoValor= Try('int','Ingrese el nuevo valor para el Nro personal <-> ',dataInventario,'')
                    editar['personal'] = nuevoValor
                elif (op == '4'):
                    nuevoValor= Try('int','Ingrese el nuevo valor para el Nro de Oficina <-> ',dataInventario,'')
                    editar['oficina'] = nuevoValor
            elif (op=='5'):
                break
            else:
                print('El valor ingresado no esta asociado a una seccion...')
                cf.pausar_pantalla()
    else:
        print('No has ingresado ninguna persona...')
        cf.pausar_pantalla()
        