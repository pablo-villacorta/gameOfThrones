IMPORTANTE:
1) Hemos instalado algunos paquetes adicionales (djangorestframework y django-hreflang).
No estamos seguros de si hace falta alguno más para que funcione, por lo que adjuntamos
una captura del comando pip list en un dispositivo en el que funciona.

2) El proyecto se ha desarrollado usando Django 2.2.6, es posible que al ejecutarlo con Django 3 
no funcione (un error similar al siguiente: Cannot import name 'lru_cache' from Django.util)
En tal caso, es necesario instalar una versión anterior de django mediante pip install Django=2.2.6

-----------------------------------
La estructura del proyecto es la misma que en la entrega anterior: Lore, Foro y Quiz:

-Lore: una especie de "Wiki" con información sobre personajes, casas y episodios/temporadas.
-Foro: conjunto de hilos que agrupan posts que escriben usuarios. Para leer el contenido del foro
	no es necesario haber iniciado sesión, pero para crear un hilo nuevo así como para escribir
	un post, sí.
-Quiz: formulario que indica la casa más afín al usuario en base a sus respuestas.

Para esta entrega, hemos decidido usar una plantilla ya creada por temas de estética.

Hemos implementado una API utilizando el módulo Django Rest Framework.
Se hace uso de la API en múltiples casos, como en la barra de búsqueda superior (con vue y assiox) o
en las ventanas flotantes que aparecen al poner el ratón sobre ciertos elementos (con jquery/ajax).

También usamos vue para realizar una previsualización cuando el usuario está redactando un post nuevo
para el foro.

La página está disponible tanto en castellano como en inglés, se puede cambiar de idioma desde la
cabecera del sitio (EN/ES). Esto se ha implementado usando i18n. Las traducciones son estáticas, es decir,
el contenido almacenado en la BD no se traduce (por ejemplo, los posts del foro). No se ha traducido el quiz
porque implica traducir bastantes frases.

Existe un fichero "bd.json" que ha sido generado mediante el comando "python manage.py dumpdata > db.json", que
contiene valores de prueba para la base de datos. Para cargar dichos datos, usar el comando
"python manage.py loaddata --app app db.json".

Hemos incluido algunas capacidades micro-semánticas (microdata) y de la web de datos (JSON-LD), en el archivo
app/templates/lore/character.html

También hemos añadido dos botones a pie de página, uno para compartir en Facebook y otro para escribir un tweet (capacidades sociales).

Aunque es bastante visible, hemos añadido ajax y efectos con jQuery: las animaciones de la sección "acerca de", las ventanas
flotantes sobre nombres de personajes y casas con ajax/jQuery, etc.

En cuanto al rendimiento, para permitir el sistema de ventanas flotantes (que muestran una imagen), en vez de descargar
todas las imágenes al cargar la página, hacemos que se vayan descargando dinámicamente, a medida que se van pidiendo.

En lo que respecta a la seguridad, hemos hecho que las contraseñas almacenadas en la base de datos estén hasheadas.

En el foro, para hacer referencia a un personaje, los usuarios pueden utilizar su atributo "slug" (@jon_snow, por ejemplo), que
es interpretado de manera especial, y que al poner el cursor sobre él se muestra la imagen del personaje correspondiente.


