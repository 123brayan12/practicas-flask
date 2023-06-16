from flask import Flask

app=Flask(__name__)

#ruta
@app.route('/')
#vista
def index():
    return 'Hola,Brayn ,Bienvenido!'

@app.route('/about/<nombre>')
def about(nombre):
    return f'Hola yo soy {nombre} y estudio 8vo grado'

@app.route('/aficion/<aficion>')
def aficion(aficion):
    return f'Soy Brayan  y me gusta mucho el {aficion} '

@app.route('/objetivo/<objetivo>')
def objetivos(objetivo):
    return f'Me llamo Brayan y quiero ser {objetivo}'