#Se crea este archivo para darle  configuración a nuestra app.
#Se utilizan variables de entorno para privatizar la config.
import os
import dotenv
dotenv.load_dotenv()

#Se define una variable con el nombre del puerto al que se va a conectar,en este caso será el servidor mongodb.
#Se define otra variable para saber a qué base de datos se debe conectar.
PORT = os.getenv("PORT")
DBURL = os.getenv("DBURL")
