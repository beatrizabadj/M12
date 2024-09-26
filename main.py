from flask import Flask, jsonify, request
#flask va a ser el servidor de nuestro api

app= Flask(__name__) #creacion de app, que es igual a una instancia de flask


@app.route("/")
def root():
    return "root"

'''
GET: obtencion de info
POST: creacion info
PUT: actualizar info
DELETE: borrar

'''

@app.route("/users/<user_id>") #ruta con el nombre users y le pasamos un parametro por la url
def get_user(user_id):
    user = {'id':user_id,'name':'test','telefono':'111-111-111'} #definicion de diccionario que retorna la api
#pasamos algo a través del query:
#para llamar al end point, hacemos una peticion a /users/2444=query=query_test.
#le enviamos un argumento query con el valor query_test
    query = request.args.get('query')
    if query:
        user['query']=query
    return jsonify(user),200
if __name__ == '__main__':
    app.run(debug=True) #como arranca la app de flask, debe ir al final