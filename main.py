from flask import Flask,render_template,request,flash,redirect,url_for
import pymongo
import json

app = Flask(__name__)
app.secret_key = "abc"  

# mongodb connection
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["fisioapp"]
c_alta = db["pacientes"]


@app.route('/altas')
def altas():
    return render_template("altas.html")

@app.route('/altas',methods=['POST'])
def altas_user():
    nombre = request.form.get('nombre_form')  
    apellidos = request.form.get('apellidos_form')
    dni = request.form.get('dni_form')
    mail = request.form.get('email_form')
    fecha = request.form.get('date_form')
    telefono = request.form.get('telefono_form')

    if c_alta.find_one({"dni": dni}) or c_alta.find_one({"email": mail}):
        return 'El usuario ' + nombre + ' ' + apellidos + ' existe en la base de datos' # será un java script
    else:
        c_alta.insert({"nombre": nombre, "apellidos": apellidos, "dni": dni, "email": mail, "fecha_nac": fecha, "telefono": telefono})
        return 'Nueva Alta ' + nombre + ' ' + apellidos         # será un java script
 

@app.route('/bajas_mod')
def bajas():
    clientes = c_alta.find()
    for i in clientes: 
        print(json.loads(i))
    return render_template("bajas_mod.html", clientes=clientes)

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