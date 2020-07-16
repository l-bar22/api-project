# API-FRIENDS

Esta Api contiene información sobre los personajes de la mítica serie Friends y alamacena algunos de los diálogos que se han utilizado en distintos capítulos.
La Api está creada en distintos entornos virtuales y utiliza principalmente el módulo ***Flask*** para generar la estructura web para python.Además,también se utilizará el servidor ***MongoDB*** para almacenar los datos y el protocolo ***HTTP*** para crear y consultar el contenido. 

## ¿Cómo se ha creado?
### Entornos Virtuales
- **Src**
	Dentro se ubican los archivos controllers y helpers.El primero contiene la s funciones controladoras formadas por una función y un decorador que permite controlar la ruta a la que se dirige el usuario.Mediante el protocolo *HTTP* podemos o bien,trasladar insertar datos en la Api(método‘GET’) o hacer consultas(método ‘POST’).Estas funciones también permiten insertar los datos que se pasan al servidor MongoDB y crear bases de datos y colecciones.
- **App**
	Crea la estructura de la aplicación web con *Flask*.
- **Config**
	Alberga la configuración básica de nuestra app web,dónde se va a conectar en este caso a *MongoDB* y a qué base de datos lo hará.
- **Api**
	El archivo principal,permite ver todas las rutas y funciones que permiten que la app funcione.
	

## Uso
### Jupyter-notebook

- **Insertar datos**

	- Utilizando el método **POST** podemos insertar datos directamente en la base de datos que hemos creado en el entorno virtual que conecta con nuestro localhost de MongoDB.
	
	- Posteriormente con el método **GET** se realizan las consultas sobre ese database,devolviendo la información de cada personaje o de las conversaciones que han tenido.


