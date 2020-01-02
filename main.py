from flask import Flask,render_template,request,flash,redirect,url_for,jsonify,abort
import pymongo
import json
from bson.objectid import ObjectId # Para crear ObjectId, porque _id como cadena no funciona

app = Flask(__name__)
app.secret_key = "abc"  

# mongodb connection
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["fisioapp"]
c_alta = db["pacientes"]

# Rutas aplicacion 
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
        return redirect(url_for('altas'))      # será un java script

@app.route('/bajas')
def bajas_user():
    cursor = c_alta.find()
    lst_usuarios = []
    for data in cursor:
        usuario = (data['nombre'],data['apellidos'],data['dni'],data['_id'])
        lst_usuarios.append(usuario)
    return render_template("bajas.html",clientes=lst_usuarios)

@app.route('/bajas',methods=['POST'])
def delete_user():
    idUser = request.form.getlist('delete')
    if idUser:
        for _id in idUser: 
            # aqui irá el mondo DELETE ID (revisar)
            print(_id)
            c_alta.remove({"_id":ObjectId(_id)})
        return redirect(url_for('bajas_user '))
    else:
        return abort(404)
        # busqueda el formulario bajas breakpoint
@app.route('/bajas',methods=['POST'])
def search_paciente():
   if request.method == 'POST':
      paciente=request.form.getlist['paciente']
      print(paciente)
      lst_usuarios_search = []
      return  render_template("bajas.html",clientes=lst_usuarios)
      """  if paciente:
        busqueda = c_alta.find(({"apellidos":/{0}/}).format(paciente))
        for sch in busqueda: 
            usuario = (data['nombre'],data['apellidos'],data['dni'],data['_id'])    
            lst_usuarios_search.append(usuario)
        return render_template('bajas.html', pacientes=lst_usuarios_search)
      else:
        return redirect('bajas') """


if __name__=='__main__':
    app.run(port=3000, debug=True)