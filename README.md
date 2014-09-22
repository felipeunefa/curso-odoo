curso-odoo
==========

Entrenamiento técnico 

launchpad.net/sisb-group
eginet
oca
menecio aristobulo web_ 
odoo/rumbot


herramienta

gitgt


rml para novatos



librerias para instalar openerp
apt-get install
python-dateutil
python-gdata python-lxml
python-mako python-openid
python-psycopg2 python-pybabel
python-pychart python-reportlab
python-simplejson python-tz
python-vatnumber python-werkzeug
python-yaml python-zsi
python-unittest2
python-mock
python-docutils

Para crear una clave ssh
ssh-keygen -t rsa

te hace un conjunto de preguntas en lo que termine colocs el siguiente comando
cat /root/.ssh/id_rsa.pub.

Comando para copiar una carpeta dentro de la red de una maquina

rsync -av aristobulo@192.168.1.102:~/github/odoo .

tube que instalar la lybreria rsync

el nombre de la mquina con el nombre de la ip pos los do puntos la ruta
'~' representa la ruta del home/usuario, post este simbolo la ruta de la carpeta que se va a copiar
'.' el punto representa copiarla en la ruta que estas ubicado en ese instante  

usuario postgret
root@canaima-popular:/home/felipe# su - postgres
postgres@canaima-popular:~$ createuser -P -S -d odoo
Ingrese la contraseña para el nuevo rol: 
Ingrésela nuevamente: 
¿Debe permitírsele al rol la creación de otros roles? (s/n) n
postgres@canaima-popular:~$ \dg
-su: dg: no se encontró la orden
postgres@canaima-popular:~$ psql
psql (9.1.13)
Digite «help» para obtener ayuda.

postgres=# \dg
                               Lista de roles
 Nombre de rol |                   Atributos                    | Miembro de 
---------------+------------------------------------------------+------------
 odoo          | Crear BD                                       | {}
 openerp       | Superusuario, Crear rol, Crear BD, Replicación | {}
 postgres      | Superusuario, Crear rol, Crear BD, Replicación | {}

postgres=# 

arrancar odoo y cambiar el puerto

./openerp-server -r odoo --addons-path=addons/ --netrpc-port=9071 --xmlrpc-port=9069

GIT
para hacer un clone:

*no hacerlo con root
*Ubicarse en la ruta donde vas a tra bajar 
git clone https://github.com/felipeunefa/curso-odoo.git

para ver el estatus de la rama don estas ubicado

git status

para crear una nueva rama y cambiarse a la misma ('-b' es para crear la rama y checkout es para cambiarse)

git checkout -b develop

para cambiarse de rama

git checkout  'nombre de la rama'

Para listar las rama es 

git branch --list

En el resultado de la consola el que tiene el '*' es donde estas ubicado

develop
* dia1
  master

Para ver los commit 
git log

resultado

commit 72bec16b04a66954a258221f2128ee80a47bcabe
Author: felipeunefa@gmail.com <felipe@canaima-popular>
Date:   Tue Sep 16 11:52:58 2014 -0430

    Ahora si adicione el archivo supcriptor

commit 01655683c292726382783ac66864734661b9f18d
Author: felipeunefa@gmail.com <felipe@canaima-popular>
Date:   Tue Sep 16 11:51:35 2014 -0430

    Declarado el objeto suscriptor

commit 529a258ee34c97c5ce07c76150d250aaeabcb955
Author: felipeunefa@gmail.com <felipe@canaima-popular>
Date:   Tue Sep 16 11:07:08 2014 -0430

    agregando archivo para declar  al modulo

commit 5c66a5548838ed3092cbb95c71fafc28a3481b43
Author: felipeunefa <felipeunefa@gmail.com>
Date:   Mon Sep 15 14:00:51 2014 -0430

    Initial commit
para subir al servido se hace un puch, -u original 'nombre de la rama' con esto subimos a github y creamos la rama, ya que en github na habiamos creado la rama dia1 

felipe@canaima-popular:~/local_addmons/curso-odoo$ git push -u origin dia1
Username for 'https://github.com': felipeunefa
Password for 'https://felipeunefa@github.com': 
Counting objects: 14, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (9/9), done.
Writing objects: 100% (13/13), 1.36 KiB, done.
Total 13 (delta 2), reused 0 (delta 0)
To https://github.com/felipeunefa/curso-odoo.git
 * [new branch]      dia1 -> dia1
Branch dia1 set up to track remote branch dia1 from origin.



  


Para adicionar todos los archivos de tu nuevas modificacione, el punto '.' indica que es todo
git add .

subir a la rama de gitbuker (se actualiza la rama dia1 de gitbuker)

git push origin dia1

 el parametro -u como la rama no existia la actualizo y la creo
git push -u origin develop

despues que te ubicas en la rama que se quedo atras, se hace un actualizacion y se coloca --no-ff para que no borre el log 
git merge dia1 --no-ff


Comandos de linux
para crear una carpeta  mkdir 'nombre de la carpeta'

Para crer un archivo 
touch 'nombre del archivo'

ver proceso proceso
 ps ax|grep openerp
 matar proceso
kill -9 2291 9088

-d actualiza la base de datos -u actualiza el modulo especifico
./openerp-server -r odoo --addons-path=addons/,../local_addmons/ --netrpc-port=9071 --xmlrpc-port=9069 -d curso -u curso-odoo 


XML
menor que &lt
mayor que &gt


pasos de git al fina del dia 

1) adicionamos todos con git add .
2) hacemos commit a todo los archivos. git commit -a
3) subimos y creamos la esa rama al la rama de gitbuker. git push -u origin dia2
4) nos cambiamos a la rama que se quedo atras (develop) . git checkout develop
5) actualizamos la rama (develop) con la rama (del dia)  . git merge rama (dian)
6) subimos la actualizacion de la rama (develop) a gitbucke. git push oririnal rama (develop) 

para clonar cuando te atrases...
git clon la url nombre de la carpeta

luego te mueves a la carpeta creada

git fetch && git checkout develop

se crea la rama nueva local

para enviar de un formulario a otro pais estado
en el view y dentro del field
context= defould_ algo esi..... medio esplicado

ojo que hace en la consola y como funciona
rgrep

para arracar el openerp modo programador reiniciar la base de datos y el modulo
./openerp-server -r odoo --addons-path=addons/,../local_addmons/ --netrpc-port=9071 --xmlrpc-port=9069 -d curso -u curso_odoo
solo para arrancar openerp
./openerp-server -r odoo --addons-path=addons/,../local_addmons/ --netrpc-port=9071 --xmlrpc-port=9069

