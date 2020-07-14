#Este es el archivo principal de nuestra API donde se importa la configuración que se le ha dado y el servidor que se crea con Flask.
from src.app import *
from src.config import PORT
import src.controllers.queries


#Ejecuta un servidor que escucha las requests.PORT,puerto al que se conecta la app.
#Se le pasa la IP"0.0.0.0" para que se pueda  usar cualuiera.
app.run("0.0.0.0",PORT,debug=True)