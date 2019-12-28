from flask import Flask,render_template,request,flash,redirect,url_for
from pymongo import MongoClient
#from flask_mongoalchemy import MongoAlchemy


app = Flask(__name__)
app.secret_key = "abc"  

# mongodb connection
MONGO_URI = "mongodb://localhost:27017"
client = MongoClient(MONGO_URI)
db = client['fisioapp']
collection = db['pacientes']

@app.route('/altas')
def altas():
    return render_template("alta_form.html")

@app.route('/altas_user',methods=['POST'])
def altas_user():
    nombre = request.form.get('nombre_form')  
    return nombre
    """    apellidos = request.form('apellidos_form')
    dni = request.form('dni_form')
    mail = request.form('email_form')
    fecha = request.form('date_form')
    telefono = request.form('telefono_form') """
    """   if collection.find({"dni": dni}) or collection.find({"email": mail}):
        return 'El usuario ' + nombre + ' ' + apellidos + ' existe en la base de datos'     # será un java script
    else:
        collection.insert({"nombre": nombre, "apellidos": apellidos, "dni": dni, "email": mail, "fecha_nac": fecha, "telefono": telefono})
        return 'Nueva Alta ' + nombre + ' ' + apellidos         # será un java script """

""" 
@app.route('/default/create')
def default_create():
    pet = Pets(name="Puki", age=7)
    pet.save()
    return "Ha sido Creada la Mascota"

@app.route('/default/update')
def default_update():
    pet = Pets.query.filter(Pets.name == "Puki").first()
    pet.name = "Arroba"
    pet.age = 8
    pet.save()
    return "Ha sido Actualizada la Mascota"

@app.route('/default/remove')
def default_remove():
    pet = Pets.query.get("5e00bad0e4a2d93a0fb6bfaf")
    pet.remove()
    return "Ha sido Eliminada la Mascota"
 """



if __name__=='__main__':
    app.run(port=3000, debug=True)