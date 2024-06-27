import boto3


dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  # Cambia la región según tu configuración

tabla = dynamodb.Table('tabla-juan-quintero')

print("si")

clave_primaria = {'Id': '2'} 

respuesta = tabla.get_item(Key=clave_primaria)

print(respuesta['Item'])


#leer toda la tabla
respuesta = tabla.scan()
print(respuesta['Items'])

#Crear nuevo
tabla.put_item(
    
    Item={
        "Id" : "4",
        "name" : "Juan quintero",
        "city" : "NY",
        "edad" : 34
    }    
    
)

#actualizar
response = tabla.update_item(
    Key = {
        
        "Id":"3"
    } ,
    UpdateExpression = "SET edad = val1",
    ExpressionAttributeValues = {
        'val1' : 32
    }
)


#crear tabla
respuesta = dynamodb.create_table(
        TableName='MiNuevaTabla',
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'  # Clave de partición
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S'  # Tipo de atributo (S = String, N = Number, B = Binary)
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

#eliminar tabla  respuesta = dynamodb.delete_table(TableName='MiNuevaTabla')  