# Así uso Codex App para programar, automatizar y trabajar [Curso Completo]

## Source Metadata

- source_url: https://www.youtube.com/watch?v=NhHuPU0SZF8&t=150s
- canonical_url: https://www.youtube.com/watch?v=NhHuPU0SZF8
- video_id: NhHuPU0SZF8
- channel: DevExpert - IA para Desarrolladores
- language: es
- is_auto_generated: True
- retrieved_at: 2026-05-20T16:47:03Z
- source_type: youtube_video
- confidence: verified source capture; auto-caption accuracy not independently verified
- raw_artifact: ../../raw/youtube/youtube-transcript-devexpert-ia-para-desarrolladore-as-uso-codex-app-para-programar-automatizar-y-trabajar-curso-completo-NhHuPU0SZF8-es.json
- extraction_strategy: yt-dlp
- caption_track: Spanish (auto-generated)
- warnings: timedtext_empty_used_ytdlp_fallback
- raw_segments: 3880
- normalized_word_count: 13032

## Normalization Notes

- The raw JSON preserves the extractor output, including original caption segments and `plain_text`.
- This Markdown transcript collapses repeated rolling auto-caption fragments by keeping only incremental text already present in consecutive captions.
- No missing words were inferred or reconstructed beyond de-duplicating overlapping caption windows.
- The source URL included `t=150s`; the available public captions were captured for the full video.

## Transcript

### 00:02

Debo reconocerlo, estoy obsesionado con la nueva app de Codex. Codex es la puesta de Open AI para desarrollo,
pero la realidad es que la app de Codex se está convirtiendo en la aplicación que más uso todo el día en mi
máquina. Mis cálculos me dicen que rondo en torno al 70 80% del tiempo que paso en mi ordenador utilizando
esta aplicación. ¿Por qué? porque la aplicación sirve literalmente para todo. Y en este vídeo te quiero
enseñar cómo funciona, qué es lo que le hace tan especial, todas las funcionalidades que tiene para que puedas
sacarle el máximo partido tanto en tus tareas de desarrollo de software, pero mucho más en todas las tareas
que tengas que hacer en tu día a día. Mi objetivo es desbloquearte esa idea de que puedes utilizar esta
aplicación para absolutamente todo y que te puede ayudar en todas las tareas rutinarias de tu día a día. Así
que prepárate porque se viene un vídeo en profundidad, un curso completo de cómo utilizar Codex App en tu día
a día. Esta aplicación la puedes usar en cualquier plan de chat GPT, incluido el plan gratuito, pero
obviamente si quieres sacarle el máximo partido, tienes que empezar con el plan

### 01:01

de $20 o incluso pasar al de $100 si lo usas tanto como yo. Así que si te parece, vamos a empezar. Lo primero
que tienes que hacer es irte a chagpt.com/codex y de ahí descargarte la aplicación para la plataforma en la
que estés. A día de hoy está en macOS, en Windows y en Linux. Sí que es verdad que alguna de las
funcionalidades que vamos a ver hoy, especialmente la de Computer Use, de la que ya te hablaré después, solo
está a día de hoy en MacOS. Una vez descargada e instalada, entrarás en una interfaz de este estilo.
Probablemente si entras de nuevas estará vacío, pero si estás acostumbrado o acostumbrada a desarrollo de
software y a trabajar dentro de un ID, verás que esto es un poco diferente. En vez de tener en el centro de la
pantalla nuestro código, lo que tenemos son las conversaciones con el agente y podemos tener múltiples
conversaciones en paralelo con distintos agentes. Cuando entramos en una nueva conversación tenemos aquí
varios lectores. Viendo desde el principio podemos darle la opción de añadir fotos

### 02:01

y archivos. Al final pienso que esto incluso lo puedes utilizar exactamente igual que usarías CH GPT o
similares y puedes incluir fotos y archivos para darle más contexto a la conversación. Puedes activar el modo
plan, que lo veremos más adelante, que nos permite generar un plan sobre el que luego trabajar en vez de que
se dedique directamente a trabajar y luego una sección de plugins de la que luego hablaremos. En el segundo
punto, y esto es bastante importante, tenemos la selección de los permisos que le otorgamos a la gente, de tal
forma que podemos darle los permisos por defecto y codex lo que hará es ejecutar los comandos en un sandbox,
es decir, solo afectará a la carpeta en la que estás trabajando y no podrá hacer nada fuera de ella. Tenemos
el Full Access, que es todo lo contrario. Tiene acceso sobre todo a tu máquina, muy cómodo, pero también con
muchos más riesgos. Yo siempre te recomiendo empezar por aquí hasta que empieces a soltura. Y luego tenemos un
tercero que es muy nuevo que salió recientemente que es el Autor Review. Lo que hace Codex es por defecto
ejecutar todo en un sandbox y

### 03:02

cuando tiene que hacer alguna tarea que necesita permisos elevados, por ejemplo, tocar otras carpetas,
instalar herramientas o cualquier acción que pueda tener cierto riesgo, el propio modelo valora si esa acción
tiene riesgo o no en función de la conversación y la hace automáticamente o pide permiso al usuario en su
lugar. En mis pruebas he visto que prácticamente nunca te pide nada, es decir, hace la revisión y si considera
que es seguro sigue adelante, pero a cambio, obviamente, hace el trabajo más lento porque tiene que hacer esas
comprobaciones intermedias. Este autor es el que recomienda hoy en día el equipo de codex. Yo voy a utilizar
Full Access para ir más rápido y no pararnos en todos esas comprobaciones. Y luego, por otro lado, tenemos los
modelos. Hoy en día tenemos GPT5, distintos niveles de inteligencia y también podemos acceder a 54 o algunos
modelos más antiguos. Y finalmente tenemos esta opción de velocidad que solo está en 55 y 54, que hace que las
peticiones vayan

### 04:02

un 1,5 más rápidas, pero a cambio el gasto de la suscripción se dispara. Creo que es como un 2,5 el gasto en
comparación con usar el modelo de forma normal. En cuanto a los niveles de la inteligencia, ¿cuál es elegir?
Pues esto ya depende mucho de tu experiencia. En general, para el 5.5 se recomienda utilizar low o medium y
dejar el high y el extra high para tareas más complejas. Finalmente, tenemos aquí la opción de dictar por voz,
que la usaremos bastante en el día de hoy y que actualmente incluso se puede utilizar para aplicaciones que no
sean la propia Codex, es decir, lo podemos utilizar en cualquier campo de texto de nuestra máquina, ya lo
iremos viendo. Y por supuesto, el botón de enviar. Y esta parte de aquí lo que nos permite es o bien
seleccionar un proyecto sobre el que trabajar, lo que le dará cierto contexto extra y cierta organización, ya
hablaremos sobre ello, o si no, si no seleccionamos ningún proyecto, todo va a ir a caer a este proyecto
especial de chats, que lo que hará es que cada conversación sea como su propio

### 05:01

miniyecto y tendrá una carpeta propia dentro de nuestra máquina. Así que yo aquí le puedo decir, "Buenos días,
¿qué tiempo hace hoy en Madrid?" Lo enviamos y esto bueno pues nos indica que ahora hace unos 14º nublado,
aproximadamente tendremos hasta 22º sobre las 5. Cuando hacemos una conversación en la sección de chats, si le
damos al botón derecho y opening finder o el equivalente en la plataforma en la que estéis, veréis que esto
abre una carpeta codex y dentro de ella tenemos todas las conversaciones que hemos ido teniendo recientemente.
En el día de hoy tenemos la que hemos estado conversando ahora. Si tiene que crear algún fichero por la
conversación que vayamos teniendo, pues lo guardará aquí. Por ejemplo, yo le puedo decir, "Guárdame toda la
información meteorológica de hoy en un Word." Y esto nos dice que nos va a preparar un doc X. Si yo me voy a
otra conversación, por ejemplo, aquí tenía una automatización de mantenimiento del sistema, que luego veremos
qué son esto de las automatizaciones. Esto es algo que se me lanza todas las mañanas para actualizar mi
máquina y comprobar que no hay nada que requiera de intervención en mi

### 06:01

sistema, pues yo puedo seguir trabajando en otras conversaciones. Y cuando acabe, fíjate que sale aquí un
icono azul indicando que ya ha terminado de trabajar. Entonces, todas las conversaciones que yo tengo sin leer
me aparecerán con ese icono azul y yo puedo volver a ella y ya ver el resultado. Aquí me ha generado el
documento y yo puedo abrirlo y tengo una preview directamente en codex que puedo poner a tamaño completo para
observar el documento que me ha generado. Esto de las previews es supercmodo porque puede seguir trabajando
con el documento sin necesidad de cerrarlo. Veremos que en algunas ocasiones, como las previews de las webs,
es incluso mejor porque hasta podemos hacer anotaciones sobre el propio documento. Así que yo me puedo volver
aquí y decirle, por ejemplo, quiero que uses tonos rojos en lugar de tonos azules. Y puedo ir viendo la
iteración en la que está trabajando aquí desplegando este menú de aquí abajo. Cambio la paleta de azul a rojo
y regenero el documento. Vale, ya nos lo nos dice que lo ha actualizado. En este caso no se actualiza
automáticamente la preview. Hay para otros documentos que

### 07:00

sí, ya lo veremos. Pero si yo vuelvo a entrar, pues ahora veré que está usando esos tonos rojos en algunas
partes del documento. Fíjate que este menú lateral puede ser de mucha utilidad porque nos va mostrando los
artefactos que ha ido generando esta conversación y también las fuentes que ha ido utilizando. Por un lado
tenemos esta skill de documents, luego hablaremos de las skills y también ha utilizado la búsqueda web. Si
esta conversación requeriría de varios pasos, además aquí nos saldría el progreso del mismo. Lo podemos abrir
y cerrar con option command B y la de la izquierda con comand B. Pero imagínate que queremos ir más allá y
queremos hacer varias tareas que se ejecuten paralelo sobre la misma conversación. Para eso, Codex nos ofrece
la funcionalidad de subagentes. Los subagentes ya están en prácticamente todos los agentes de IA que con los
que trabajemos, pero quiero enseñarte cómo se ve en la aplicación de Codex porque es muy interesante que
podemos acceder a las conversaciones individuales, volver a la conversación principal que actuará como
orquestadora de esos subagentes y podemos hacer prácticamente lo que se nos ocurra. Por ejemplo, yo ahora le
voy a decir,

### 08:01

utiliza tres subagentes para buscar el tiempo meteorológico que ha habido durante el último mes en las tres
capitales principales de Europa. Cada subagente debe generar un Excel con esta información y vamos a lanzarlo
para que se ponga a trabajar. ¿Vale? Aquí vemos el tema de las tareas. Va a lanzar tres subaagentes, cada uno
para una de las ciudades. Y aquí los vemos que están empezando a trabajar. está arrancando los suagentes. Como
curiosidad, yo no lo he hecho porque tampoco me merece mucho la pena, pero puedes definir cuáles son los
nombres de los suagentes que van a aparecer aquí y luego si nos vamos al menú lateral veremos que también
podemos ver aquí el progreso. Como te comentaba, en cualquier momento podemos entrar en cualquiera de los
subagentes y ver lo que le ha dicho Generó Uncel independiente con la meteorología diaria de LER durante el
último mes. Y aquí está empezando a trabajar buscando información en este caso en Open Meteo y en cualquier
momento podemos volver a la conversación principal. Fíjate que aquí

### 09:00

aparecen como subconversaciones, entonces yo me puedo ir moviendo por todas ellas y ver en qué punto está cada
una. Y si vuelvo a la principal, vuelvo a ver el estado general de los tres subagentes. Vamos a dejarle que
termine de trabajar y ahora vemos el resultado. Aquí nos indica que París ya está generado y verificado y que
quedan Londres y Berlín. Mientras esto termina, que sepas que aquí siempre desde settings en el rate limits
puedes comprobar cuáles son los límites que te quedan tanto de las 5 horas como el semanal. En el plan
gratuito creo que solo hay raid limit semanal y además obviamente no es muy grande, pero lo puedes tener aquí
siempre visible. Ya han terminado los tres agentes, los tres subagentes, y ahora pues va a terminar dándonos
la información de lo que ha realizado, ¿vale? Y aquí tenemos los tres. Y bien, los podemos abrir aquí en la
preview, como hacíamos antes, o incluso podríamos abrirlo en la carpeta contenedora. Si recuerdas, aquí te
había dicho que se van incluyendo en esa carpeta que genera automáticamente todos los ficheros que vaya
generando. Y aquí, bueno, pues si lo ampliamos a tamaño

### 10:01

completo, podemos ver la información de cada una de las ciudades, el periodo, eh temperatura mínima, máxima,
días más lluviosos. Esto es un resumen y luego podemos ir a la sección de datos y nos da la información de las
temperaturas mínimas máximas que ha habido cada uno de los días del último mes. Esto obviamente lo puedes
aplicar a todo lo que se te ocurra, pero plantéate que puedes utilizar Codex para extraer información de
cualquier punto y luego estructurarla de la forma que quieras. A mí me gusta especialmente el formato
Marddown, aunque quería enseñarte estas herramientas por si tú eres más de Excel o o de Word, pero si yo le
digo, "Convierte el primer Doc X que hemos generado a Marddown." El Marddown me gusta mucho porque entre otras
cosas, además de ser muy portable, aquí la preview que nos sale es muy buena, pero no solo eso, sino que
podemos trabajar en tiempo real. Puedo decirle, por ejemplo, conviérteme las horas a 12 horas con AMPM. Y
aquí, sin necesidad de cerrarlo, veremos cómo se va actualizando el documento y ya lo

### 11:00

tenemos modificado y podemos trabajar sobre él de forma muy natural. Y una vez que tenemos el Mardown tal y
como lo queremos, ahora ya sí podríamos convertirlo al formato que queramos. Yo incluso con una skill que
tengo le podría decir, générame un PDF de este marnow. Fíjate que aquí me ha dicho que le falta una librería
para hacer la transformación. Y otra cosa que te quería enseñar es esto. Cuando estás en medio de una
conversación y quieres añadirle información extra, es decir, no quieres esperar a que acabe el turno, lo que
puedes decirle que haga un steir de la conversación. Tú puedes escribir cualquier cosa y aquí te da la opción
de steir o si en vez de mandarlo con enter lo mandas con command enter lo hace automáticamente. ¿Qué significa
esto de ser? que lo va a añadir a la conversación actual en el siguiente paso y esa información se va a
incluir en lo que está haciendo en ese momento. Entonces, puede redireccionar loir es como el volante, puedes
mover la dirección de lo que se está haciendo en ese momento para que vaya en otra dirección o que utilice esa
información

### 12:00

para complementar a lo que le has dicho antes. Yo lo uso mucho, sobre todo cuando le doy prompts que son muy
vagos, información muy vaga, y veo que no está yendo por donde yo esperaba, pues uso el steir para darle
información extra y que vaya por esa dirección. Pues bueno, ya ha generado el PDF y aquí lo tenemos, un PDF,
la verdad que muy limpio. En mi caso, ya te contaré por qué, pues añade aquí el el logo de mi empresa y este
PDF ya sería perfecto para enviarlo por cualquier parte. Esto es un camino que yo sigo muy a menudo. Te
comentaba lo del logo y es porque yo, por ejemplo, genero las propuestas de formaciones para empresa
directamente en un Marddown y a partir de ese Marddown, una vez que ya lo tengo exactamente como quiero, pido
que me genere un PDF y el PDF ya es lo que le envío a las empresas. Pero esto lo puedes aplicar a cualquier
idea que tengas en tu cabeza. Por ejemplo, haces una investigación de un tema concreto y luego quieres
pasárselo a alguien, a un miembro del equipo, alguien de tu familia o lo que sea, lo conviertes a PDF. y se lo
envías. La generación de PDF es el modelo es algo

### 13:01

que por sí es capaz de hacer, es decir, encontrarás siempre la manera para hacerlo si no se lo dices. Pero
aquí entra otro concepto del que quiero hablarte, que es el de las skills. No voy a profundizar mucho en las
skills porque de skills ya tengo un vídeo concreto donde te explicaba qué son y para qué sirven, pero lo que
sí quiero enseñarte es cómo están integradas dentro de Codex y también de paso introducirte el concepto de
plugins. Entonces, las skills son funciones extra que le podemos dar al sistema. Es un contexto dinámico que
carga cuando necesita y que le puede dar superpereres extra. En particular, si nos vamos aquí a la sección de
plugins, que ahora hablaremos de ellos, hay una pestaña llamada skills donde tenemos todas las skills que
tenemos en nuestro sistema. Yo tengo muchas que me he ido generando para tareas repetitivas y es lo que te
recomiendo que hagas. Cada vez que hagas algo que a la gente le cueste descubrir cómo hacerlo, para qué sirve
y que sea una tarea que realic habitualmente en tu día a día, lo que te recomiendo es que le pidas que genere
una skill y esa skill luego será reutilizable para distintas conversaciones. Por ejemplo,

### 14:01

la de generación de PDFs. Yo tengo por aquí una que se llama, vamos a buscarla, Gen PDF y que esta le explica
cómo generar un PDF sin tener que estar repitiéndolo cada vez, cada vez descubriendo cómo hacerlo. Además,
pues bajo ciertas reglas. Yo también tengo lo que os decía, el logo que se pone en la parte inferior derecha y
que por tanto me sirve para generar mis PDFs. Pero en cualquier caso, si necesitas skills para generar PDFs,
te puedes ir, por ejemplo, a skills.sh genere PDFs e incluirla. La de Antropics, que esta también la tengo
instalada, realmente sirve para procesar con extracción de textos, fusión, partir, rellenar. Es decir, esto es
más procesamiento de PDF es más que generación y por eso yo me creé la mía propia para generar. Pero como esto
puedes tener 1000 skills. Yo tengo algunas que me ayudan, lo que os decía, para generar propuestas para la
formación de AI Expert, para añadir personas en la academia. Yo, por ejemplo, le puedo decir da de alta al

### 15:00

usuario Antonio Leiva con el email@despert. En la formación de AI Expert para la edición de diciembre en
Listmk y dale de alta también en la academia al pack Android Legacy. Lismon, que es la herramienta que yo
utilizo para newsletters y donde voy almacenando cuáles son las personas que van a entrar en la próxima
edición de la formación y luego como a las personas que entran les doy acceso a los tres a las tres
formaciones que tenía sobre Android, pues le puedo pedir que también lo haga. Y esto va a lanzar una serie de
skills, ahora lo iremos viendo aquí, que van a permitirle realizar la tarea. Fíjate, aquí va a seguir el flujo
de la skill de Academy Enrollments y de Lismon CLI y está cargando las skills para leerlas y ver cómo se hace
el proceso. Entonces, va a buscar las listas de Lismonk, aquí encuentra cuál es la de septiembre y de ahí la
va a sacar y va a darme de alta como usuario allí. Fíjate también por curiosidad que si entramos en en Dev
Expert y vamos a la formación, que ahora

### 16:01

mismo quedan 28 plazas disponibles. Me ha entendido diciembre, así que le voy a decir me refería a la lista de
septiembre. No sé si me ha entendido mal o es que yo se lo dicho mal, que también puede ser. Aquí ya se ha
incluido en la conversación y dice, "Entendido corrijo a la lista de septiembre." Yo ya os digo, el stirt este
lo uso muchísimo porque me sirve para guiar la conversación cuando veo que se está yendo por donde no debe. Lo
he añadido en la lista de septiembre. Me había creado una lista para diciembre, pero la ha eliminado porque me
había confundido yo al decírselo. Y si ahora yo me vengo aquí, veremos que quedan 27 plazas en vez de 28. Así
que lo ha añadido correctamente a la newsletter y también ha seguido el proceso de darle de alta. Eso no lo
vamos a ver porque tampoco aporta mucho en las tres formaciones. Y todo esto lo consigo simplemente creando
skills que ya saben lo que tienen que hacer por detrás para hacer esas cosas y ya me puedo comunicar en
lenguaje natural con la herramienta para que haga todas esas tareas administrativas por mí. Le voy a decir
borr lo de la lista y borra también el usuario de Lismonk para

### 17:00

volver a dejarlo como estaba. Si te interesa el desarrollo con IAIA, te recomiendo que le eches un vistazo a
AI Expert. Tenemos la próxima edición en la que tenemos plazas es en septiembre. La de mayo ya está ocupada y
empieza la semana que viene, especialmente si estás interesado en desarrollo impulsado por inteligencia
artificial. Aquí ya lo hemos devuelto el contador al estado previo. Perfecto. Y podemos seguir con nuestras
tareas. Si volvemos a plugins, ya te he enseñado algunos de los que tengo en skills, tengo muchas más para
ayudarme en el día a día, pero una parte muy interesante y que viene muy bien integrada es la de plugins. Los
plugins lo que nos permiten es añadir contexto extra empaquetado por Codex para ayudarnos con una tarea
concreta. Hay algunos, no muchos, que ya nos vienen instalados por defecto y otros que podemos instalar
nosotros. Incluso se pueden crear plugins externos de terceros e instalarlos manualmente, pero aquí nos vienen
un montón de plugins, de hecho creo que hay ya más de 100, que se integran con las herramientas habituales.
Vamos a entrar, por ejemplo, en el Deslck para que veas cómo

### 18:00

funciona. Lo que nos ofrece es una serie de recursos que nos permiten sacarle el máximo partido a esa
herramienta. Por ejemplo, en el de Slack tenemos esto, el Slack App, que realmente es un MCP que permite
comunicarse con Slack. La primera vez que lo integramos nos pedirá hacer login en la herramienta oficial y a
partir de ahí ya tiene acceso a lo que nosotros le demos. Y luego tenemos una serie de skills en este caso que
le permiten hacer tareas extra. Tenemos una general, pero otra que le permite hacer resúmenes de canales, otra
que permite hacer un resumen diario, un triaje de notificaciones, mensajes de salida, borradores de
respuestas, etcétera. Y como estas, pues tenemos otras. Tenemos conexión con GitHub, que yo no lo hago porque
utilizo el CLI, que me consume menos recursos. Tenemos también Notion, Gmail, Google Calendar, Google Drive.
Bueno, un montón. Yo muchas de estas las utilizo con con CLI, que al final todo esto son MCPs y por tanto van
a ir ocupando contexto en nuestra ventana de contexto,

### 19:01

pero para usuarios que sean menos avanzados, esto es supercmodo. Conectas y lo tienes ya listo para empezar a
trabajar con él. Y luego todas las skills que se aportan, pues también le dan funcionalidad extra. Pues puede
hacer un triaje de lo que hay en la bandeja de entrada para saber cuáles son los más importantes y muchas
funcionalidades muy interesantes. De hecho, la de Gmail, si yo solo tuviera emails en Gmail, la utilizaría,
pero como también tengo en otras plataformas, me he montado una skill aparte. Y bueno, pues como veis hay de
todo. Google Drive, Teams, Outlook, Pagin Face, Netli, Fy. Hay muchas de código, obviamente. De hecho, voy a
instalar la de Build Web Apps porque la utilizaremos luego. Le da información de cómo construir el frontend,
las mejores prácticas de React, cómo utilizar la librería de SATCN, que es una librería de componentes web muy
popular, mejores prácticas con Stripe, con Supabase. Así que le vamos a dar a tocx y esto nos lo instala. Pero
no hay solo para web. El equipo de codex está muy encima de temas

### 20:02

de macOS y de iOS. Así que fijaos, aquí tenéis, si os dedicáis a estas tecnologías, sus propios plugins. Me da
un poco de pena no ver uno de Android aquí, pero ojalá que en el futuro lo tengamos. Y bueno, pues hay de
muchas otras herramientas de expo para crear aplicaciones híbridas, temas de diseño, remoion muy interesante
para crear vídeos a partir de JavaScript, temas de latex, estilo de vida, productividad, por ejemplo, la de
generación de documentos que hemos visto antes, esta viene preinstalada y por eso puede generar documentos de
Word, los Excel, que también hay otro por ahí. Y bueno, pues como ves, hay muchas más, no vamos a verlas
todas. Tema de investigación. Bueno, muchísimos plugins que le pueden añadir funcionalidades extra.
Simplemente recordarte que hay que tener cuidado porque especialmente si tienen MCPS ocupan ventana de
contexto que se envía en todas las conversaciones. Y luego si le damos aquí a gestionar los podemos manejar,
los plugins que tenemos instalados, las aplicaciones, los MCPs y

### 21:00

las skills. Yo podría utilizar, por ejemplo, la de Slack para decirme si tengo mensajes. De hecho, esto lo uso
todas las mañanas para saber si alguien me ha escrito por el slack de la formación. le podría decir, "Revisa
si hay mensajes sin responder en el canal de AI Expert que va a revisar Slack." Y mira, aquí ha hecho una
búsqueda de canales, ha localizado el canal y ahora está leyendo los mensajes, está leyendo las respuestas a
los mensajes, a los hilos que hay en Slack para ver si hay algo sin contestar y ya me dice, pues los hilos
recientes están contestados o son una conversación ya cerrada y por tanto, pues en principio no hay nada que
contestar. La verdad que esto me es muy cómodo porque a mí no me gusta tener slack abierto todo el día y por
tanto un par de veces al día hago una pasada por los emails y por Slack. En realidad la hace el propio codex y
de ahí extraigo si hay algo que necesite revisión por mi parte. Y esto lo puedes extrapolar a lo que necesites
porque al final puedes integrar herramientas. Por ejemplo, puedes decir que eh un email que te

### 22:01

interesa de Gmail te lo guarda en Notion porque lo quieres tener guardado para revisarlo más adelante o que a
partir de eso te genere tareas en tu herramienta de tareas de forma muy natural y a través de conversaciones
puedes integrar herramientas entre sí y que trabajen juntas y además de forma totalmente dinámica ajustada a
las necesidades que tengas en ese día. Pero te comentaba que una de las partes que más me gusta de codex son
las automatizaciones. Estas automatizaciones te permiten lanzar tareas sin necesidad de interacción humana. Y
existen dos tipos de automatizaciones, las clásicas, que podríamos llamar automations, y otras un poco más
especiales que se llaman hardbeats. Vamos a ver con ejemplos cuáles son las diferencias entre unas y otras. La
automatización que vimos aquí previamente, esta que vimos de mantenimiento del sistema, es una automatización
clásica. ¿Qué quiero decir con esto? que cada vez que se ejecuta la automatización me genera un nuevo hilo,
una nueva conversación. Si yo me voy aquí a la sección de automatizaciones, veremos las que tengo listas para
ser ejecutadas y también me

### 23:00

puedo crear automatizaciones nuevas. Además, me da una serie de plantillas por si quieres inspirarte sobre el
tipo de cosas que puedes hacer, desde escanear los cómics recientes, crear release noes semanales de los PRs
que se han ido mergeando, hacer un resumen de la actividad de ayer. Bueno, un montón de ellas. Puedes pedirle,
por ejemplo, que todas las mañanas te genere un pequeño proyecto nuevo con una idea loca basada en tus
conversaciones. Bueno, puedes hacer prácticamente lo que se te ocurra. Por ejemplo, yo tengo esta de
mantenimiento del sistema, que lo que hace es hacer una pasada donde ejecutar el BRW update y BRW grade para
ver si tengo que actualizar herramientas y luego utiliza Mold, que es una herramienta de limpieza del sistema
donde revisa si hay algo que requiera de mi atención y esto se lanza todas las mañanas a primera hora. me
genera aquí un nuevo informe que yo cuando he terminado con él puedo archivar y desaparece de mi vista. Otra
que tengo, pues por ejemplo, es una que todos los martes se descarga la clase que hemos tenido el lunes de la
formación y lo que

### 24:00

hace es transcribirla, crearse un notebook LM, extraer los capítulos, actualizar mi plataforma de formación de
forma automatizada para que los alumnos tengan toda esa información para seguir trabajando sobre la sesión. Y
todo esto nuevamente está integrado con múltiples herramientas a través de skills y de la propia información
de la automatización. Luego tengo otra que a partir de las conversaciones que he tenido con Codex me saca
ideas que luego puedo contar en las redes sociales, revisión de facturas, bueno, varias automatizaciones que
se van ejecutando y luego tengo algunas que como no tengo un momento del día concreto en el que quiero que se
lancen, pues las tengo aquí para poder lanzarlas manualmente. Esto es un pequeño parche en vez de crearme una
skill porque hay veces que las lanzo a mano y hay veces que pues prefiero no tener que pensar en el prompt y
le doy aquí y lo ejecuto. Pero vamos, lo principal es esto. Para crear una nueva automatización o bien la
podemos crear desde aquí y decirle, por ejemplo, revisa si hay algún mensaje pendiente en

### 25:01

Slack y le podemos decir en qué proyecto queremos trabajar, por ejemplo, que directamente nos lo pase a chats
o en algún proyecto concreto que nosotros tengamos le podemos decir la frecuencia, por ejemplo, le podemos
decir que se lance cada hora. Elegimos aquí el modelo. Para cosas tan sencillas como estas, yo os recomiendo
usar el 54 mini, que gasta mucho menos y razonamiento medio está bien. Entonces, yo lo me falta el título, le
voy a decir revisar slack y le damos a crear. Y entonces aquí cada hora se lanzará esta automatización que de
hecho puedo entrar y revisar cuál va a ser la próxima ejecución. En este caso será hoy a las 11:02. Y aquí
puedo modificar todo lo que necesite sobre la automatización. Pero tenemos otra opción. Puedo borrar esto.
Imagínate que estás trabajando y quieres que algo que has hecho recientemente se ejecute como una
automatización. Le puedes decir, "Créame una automatización para que se lance en el proyecto Automations cada
hora y revise esto en Slack." Entonces, está

### 26:01

comprobando qué automatizaciones hay recientemente para ver si alguna cumple con lo que le habíamos pedido.
Como no es el caso, ha creado una nueva. Dice que revisará ese canal, abrirá ahí los recientes y solo
reportará mensajes realmente pendientes. Y si le damos aquí, podemos ver cómo ha configurado la
automatización. Aquí vemos la preview de la automatización, pero le podemos dar y acceder al mismo lugar donde
estábamos antes y nos lo ha creado en el proyecto correspondiente. Así que piensa que aunque tengas interfaz
que puede ser cómoda para plantearte la automatización paso a paso, la realidad es que puedes pedirle a Codes
que lo haga y no tener que hacerlo manualmente. Pero como te comentaba, hay otro tipo especial de
automatizaciones llamadas Harbits que son muy interesantes porque te permiten que esa automatización en vez de
generar un nuevo hilo cada vez se ejecute sobre el mismo hilo y por tanto mantenga el contexto de esa
conversación. Imagínate, yo podría entrar aquí y decirle, "Crea un hardbit que se ejecute cada media

### 27:01

hora y que compruebe si tengo pull request nuevas abiertas en mi GitHub." Cuando mencionas alguna palabra para
la que tiene un plugin, te recomienda instalar el plugin. Yo no lo voy a hacer porque uso GH, pero podríais
instalar el plugin de GitHub en ese momento en el que te lo recomienda. ¿Qué ventaja tiene esto? Que ahora
cada 30 minutos se lanzará en este mismo hilo esa automatización y solo me responderá en el caso de que
realmente haya nuevos pull request. Si son pull request que de los que ya me ha informado antes, pues no me
volverá a molestar y no me aparecerá aquí el simbolito de no leído. Esto tiene doble ventaja, la primera que
mantiene el contexto y la segunda que no me molesta a no ser que haya algo relevante. Una parte interesante es
que cuando un hilo tiene una automatización nos sale el símbolo del reloj ahí. Es independiente de si esa
conversación tiene un hardbit o ha sido un hilo que se ha lanzado a partir de una automatización. Yo espero
que esto lo cambien porque es un poco confuso y normalmente los hilos que son Harbits te interesa mantenerlos
siempre a la vista,

### 28:02

mientras que lo que son automatizaciones para las que ya has terminado, pues una vez que acaban lo interesante
es archivarla. Yo, por ejemplo, esta que ya no la necesito para nada, la voy a archivar también. Mi
recomendación operativa es que te vayas quitando de medio todas esas conversaciones que ya no necesitas e
incluso proyectos con los que ahora mismo no estás trabajando para quitarte ruido de esa sección de proyectos,
que por otro lado siempre es muy fácil volver a añadir un proyecto, que por otro lado tener proyectos es muy
interesante, incluso aunque no sean proyectos de código, porque te permiten tener conversaciones comunes que
trabajan sobre un mismo espacio de trabajo. Y ahora mismo si quisiera que todo este trabajo que hemos hecho
sobre el hilo de chats lo pudiera utilizar desde otra conversación, me va a ser mucho más difícil porque no
están compartiendo carpeta las distintas conversaciones del chat. Sin embargo, en un proyecto sí que comparten
carpeta. Entonces, si yo me voy a este, por ejemplo, es un poco con el que he estado planificando lo que iba a
hablar en este vídeo. Si yo ahora creo una nueva conversación, le puedo decir, crea un Excel con los ejemplos
que quiero

### 29:01

mostrar durante la grabación del vídeo. Y entonces esto lo primero que va a hacer es leerse la carpeta del
proyecto para saber qué documentos tiene. Ya ha encontrado la propuesta y con una lista de sesiones reales y
por tanto lo que va a hacer es generar el Excel a partir de esa propuesta. Aquí ha ya extraído los ejemplos.
Va a construir el Wordbook con pestañas de planificación y finalmente verificar el resultado. Y yo no he
tenido que pasarle ningún contexto. El contexto es el de la propia carpeta. Por eso te quería explicar que
esto obviamente tiene sentido cuando estamos desarrollando, porque el tener el código con el que estamos
trabajando en la misma carpeta es útil, pero puede ser útil para muchas situaciones distintas. Por ejemplo, si
tienes una carpeta donde guardas toda la información de los gastos que tienes a nivel, pues si tienes una
empresa o incluso a nivel personal. puede trabajar directamente sobre ellos o en mi caso tener una carpeta con
información de lo que voy haciendo en redes sociales para que se inspire a partir de ello. Puedes tener
proyectos compartimentados por distintas facetas que tengas en tu día a día y que

### 30:02

cuando empieces una nueva conversación tenga ya todo eso como contexto para empezar a trabajar. Ahora veremos
lo que ha generado, pero debo de reconocerte que yo soy muy malo siguiendo guiones, así que muchos de los
ejemplos que estoy poniendo seguramente no estaban en el guion. Bueno, ya ha finalizado y vamos a abrirlo. Y
aquí tenemos el resumen, los ejemplos que se habían planteado para hacer durante la grabación. Además, yo le
pedí que revisara mis conversaciones para que buscara ejemplos de cómo lo utilizo yo para luego mostrarlos. Ya
te digo, esto al final es simplemente como inspiración base, pero no lo estoy siguiendo ni mucho menos al pie
de la letra. Y bueno, luego esta es otra parte que contaré después a que todavía no hemos llegado. Y aquí
debajo incluso tiene un checklist de lo que hacen antes de grabar durante la demo, el cierre. Bueno, pues para
organizarte puede estar muy bien, pero de nuevo yo no le he tenido que decir nada. Lo teníamos todo ya
disponible gracias a que estamos en el mismo proyecto y por tanto en la misma carpeta contenedora. Así que ya
has visto que Codex puede hacer prácticamente cualquier cosa por nosotros. La puede hacer de forma

### 31:01

asistida, la puede hacer de forma automatizada, puede llamar a todas las herramientas de terminal que tengamos
instaladas en nuestra aplicación, utilizar skills, que al final son pequeños ficheros Smartdowns con
documentos extra o scripts que les permiten hacer tareas más potentes. puede utilizar MCPs que ya pueden ser
todo lo complejos que necesitemos y pueden estar instalados o bien en nuestra máquina o en los servidores de
la herramienta que estemos utilizando como el que hemos hecho de Slack, pero le falta una pequeña cosa que es
ser nuestras manos. ¿A qué me refiero con esto? A que pueda controlar el ordenador por nosotros y abrir todas
las herramientas que necesitemos e interactuar con ellas. Para ello tiene una funcionalidad llamada computer
use, que lamentablemente a día de hoy no está disponible en Europa, pero que si quieres saber cómo utilizarlo,
suscríbete a la newsletter, que te dejaré el enlace en la descripción porque en los próximos días enviaré un
email explicando cómo activarlo y que le permite tener control automatizado de todas las herramientas, de
todas las aplicaciones que tengamos instaladas en nuestra máquina. En realidad va a actuar

### 32:01

por nosotros. Esta es una funcionalidad que actualmente solo está en MacOS, así que si la tienes en Windows o
en Linux, lamentablemente todavía no está disponible, pero quiero que le echemos un vistazo a cómo funciona.
Así que aquí podríamos decirle la configuración de esto está en settings y en computer use. Ya te digo que si
estás en Europa no estará activado. Y yo me puedo ir aquí y decirle, usa Brave Browser para acceder a X y
escribir una publicación indicando que estoy grabando un vídeo sobre codex, explicando toda la funcionalidad
completa de la aplicación. Pon algunos ejemplos y añade como imagen asociada un pantallazo de esta aplicación
y se la voy a identificar por si acaso para que Computer Use sepa qué herramientas necesita utilizar.
Entonces, le damos a enter. Y lo bueno de esto es que ni siquiera necesitamos que esas aplicaciones estén en
primer plano. Puede trabajar en segundo plano sobre esas aplicaciones mientras nosotros estamos trabajando en
otras. Yo lo que estoy haciendo para que utilice el navegador es darle un navegador propio. En este caso, eh,
ya le estoy dejando

### 33:01

brave para que use el ese navegador. De tal forma que si yo necesito utilizar otro navegador para otra cosa,
no me interrumpe en mi trabajo. Aquí dice que Codex en concreto no le deja manejarla, no se deja manejar a sí
mismo, pero ha hecho una captura local del sistema. Y aquí tenemos el pantallazo de nuestra aplicación. No sé
muy bien cómo lo ha hecho, pero sí que ha sido capaz de abrir una nueva conversación y generar un pantallazo.
Le preocupaba que saliera esto en el menú lateral, así que ha decidido recortarlo y quedarse solo con la parte
principal. Bueno, me vale. Y ahora está haciendo cosas sobre el navegador. Aquí le podemos ver cómo está
rellenando la URL, ha accedido a la composición del post. Fíjate como hay un puntero aparte que lo tenemos por
aquí que es el que usa computer use para identificarnos lo que está haciendo. Se está yendo ahora al a la
parte de escribir. Ha pegado el texto. Estoy grabando un vídeo sobre codex intentando enseñar la app completa.
Cada vez me cuesta más explicarle un tir. Voy a meter ejemplos reales. Repos, plugins,

### 34:00

automatizaciones, navegadores, lag, notion, capturas. Es bastante más que un chat para programar. Me parece
bastante bueno el texto. Vamos a ver si consigue adjuntar la imagen, que eso ya es otro tema. Incluso mientras
esto está trabajando, yo le podría decir crea una nota en las notas de Mac indicando un paso a paso muy
escueto de las partes del vídeo. Y como hablábamos, podemos tener dos hilos perfectamente trabajando en
paralelo, dos y muchos más. Ahora nos indica que ha abierto la aplicación de notas, se crea una nueva nota.
Vemos aquí el cursor cómo se va moviendo a las distintas tareas. está añadiendo ahora las distintas partes del
vídeo y bueno, ya habría terminado de incluir la nota. Mientras tanto, aquí está buscando el PNG que ha creado
para esta publicación para incluirlo en la publicación de X de abrir y ya la tiene insertada. La verdad es que
aquí no sé qué ha hecho, que se ha quedado sin los saltos de línea, los acentos, etcétera. Ahora ya ha
conseguido incluir todo lo que le faltaba. Me pedirá confirmación. le

### 35:00

expliqué yo que le faltaban los eñes, acentos, etcétera. Y eso sí, siempre nos pide confirmación para hacer
las cosas. Así que le voy a decir, "Adelante, publícalo." Y así que ahora vemos como el puntero se ha ido
hasta el botón de postear y nos lo ha publicado. Ha añadido ahí un pequeño texto inicial, así que bueno, voy a
borrar esta publicación porque además se solapa con una que acabo de publicar, pero cuando tengas alguna
aplicación que no tenga una API clara para utilizarlo, puedes utilizar el computer use para que trabaje por
ti. Especialmente en aplicaciones nativas funciona muy bien porque se basa en todo el sistema de accesibilidad
de MacOS para trabajar sobre esa aplicación. Pero para temas de navegador hay una parte que me gusta incluso
más que es el brow use. Le voy a decir aquí, por ejemplo, búscame enlaces sobre temas de codex que puedan ser
interesantes para incluir en este vídeo. Y listame los enlaces en la conversación. Y aquí tenemos una serie de
enlaces que si hacemos clic sobre ellos se nos abrirán en nuestro navegador por defecto, pero si hacemos
command click o control click se abrirán

### 36:00

dentro de un navegador interno sobre el que luego podemos seguir trabajando. Le podemos decir, por ejemplo, en
el navegador abierto por brows use, haz clic en la tarjeta de learn about pronting y de manera equivalente a
como ocurre cuando estamos trabajando con el computer use, puede utilizar este navegador directamente. Esto es
muy interesante usarlo para controlar el navegador, pero también veremos que es superútil cuando estamos
trabajando con nuestras propias aplicaciones web, que además nos da algunas funcionalidades extra, luego lo
veremos. De esto también hay una configuración especial en settings. Si nos vamos a browser use, podremos
elegir pues qué dominios no queremos que acceda nunca, a qué dominios están permitidos siempre por defecto.
Tiene cookies que nos pueden mantener sesiones abiertas, las podemos borrar en cualquier momento, elegir si
queremos que nos pregunte antes de abrir sitios o si queremos que lo permita por defecto. Y este navegador
podemos esperar que lo vayan mejorando mucho con el tiempo. De hecho, hasta hace nada solo se puede usar para
local hostilado para poder navegar en cualquier web. Y

### 37:01

por supuesto, también lo podemos tener en modo pantalla completa y pedirle guarda un resumen sobre esta página
en un mardown y aquí lo tendríamos y lo podríamos abrir también en el menú lateral. Mirad, aquí todo lo que
vayas abriendo, el summary, el navegador, el nuevo Marddown que hemos generado, se van abriendo como pestañas
que luego podemos ir cerrando cuando queramos e incluso abrir archivos que formen parte de esta carpeta,
porque además Codex lo podemos utilizar como un explorador de archivos del proyecto en el que estamos
actualmente. Le podemos dar aquí esto nos abre el listado de ficheros. Voy a cerrar la barra lateral para que
no nos ocupe mucho. Y aquí podemos ver todas las carpetas que se han creado, incluido un ritmi que hay por
aquí, que lo podemos abrir y echarle un vistazo. Las notas, es decir, que de un vistazo podemos ver cuál es la
estructura de nuestro proyecto y acceder a los ficheros que necesitemos. Luego veremos que cuando configuremos
Git nos da algunas funcionalidades extra, pero de momento nos sirve para inspeccionar los

### 38:00

archivos de nuestro proyecto. Mientras tanto, nuestro hardbit se ha ejecutado, el de las PRs abiertas y ha
encontrado un par de PRs que están abiertos en dos de mis proyectos y en unos minutos se volverá a ejecutar la
siguiente pasada. Otra parte muy interesante que tiene Codex es que podemos pinear las conversaciones que nos
interesen. Yo normalmente aquí tengo las conversaciones en las que estoy trabajando actualmente. Imaginemos
que, por ejemplo, quiero tener esta de los pull request aquí siempre disponible, pues la puedo tener aquí
arriba, la puedo renombrar y decirle, por ejemplo, trs activos y de esa forma tenerla siempre visible para
cuando quiera utilizarla. Yo lo que te digo, aquí suelo tener pineadas las conversaciones en las que estoy
trabajando activamente y por ejemplo esta que lo que hace es revisarme los emails y el Slack, lo que te
comentaba antes, para revisarlo a lo largo del día. Y la última parte relevante que te quería contar de Codex
antes de empezar con el proyecto que quiero implementar es el tema de la memoria. Codex automáticamente si se
lo activamos es capaz de ir actualizando la memoria tanto de las automatizaciones

### 39:01

como de conversaciones que vamos teniendo para luego poder utilizarla en futuras conversaciones y que no parta
desde cero. De hecho, si vamos aquí, por ejemplo, a la automatización de mantenimiento del sistema, veremos
que cada vez que acaba actualiza la memoria. Podemos ver aquí incluso lo que ha actualizado y se va quedando
con información que le puede servir para siguientes iteraciones, pero esto va más allá porque de forma
automática también va apuntando memorias y curándolas para luego poder utilizarlas. Tanto memorias por
proyecto para que de esa forma el mismo proyecto pueda tener información. Por ejemplo, yo en este de Postflow,
que es mi proyecto que utilizo para publicar en redes sociales, fíjate que ahora se ha lanzado la
automatización que generamos antes, la de revisar el slack. Mientras tanto, yo le puedo decir qué tareas hemos
estado haciendo recientemente en el proyecto. Revisa tu memoria. Y ahora fíjate que ha buscado en memory.md
para buscar información sobre lo que tiene almacenado de lo que hemos estado haciendo recientemente, temas
sobre las URLs públicas de Instagram, de LinkedIn,

### 40:02

integración continua, temas de Culify, etcétera. Y aquí si nos vamos vemos que está citando cinco elementos de
la memoria. Esto lo hemos hecho activamente y a veces puede ser interesante, pero otras veces de manera
automática veremos qué está buscando en la memoria cuando lo cree relevante. Para activar esta funcionalidad
nos tenemos que ir a settings y en personalización activar esta parte de memorias que como vemos es
experimental. Las podemos activar aquí, las podemos resetear si queremos que las limpie y la verdad que es muy
útil para tener una memoria sencilla que además se guarda en Mard y por tanto podríamos utilizar desde
cualquier agente, no solo desde el propio Codex. Pero además, Codex ha lanzado de forma experimental y de
momento no está para todos los usuarios, de hecho creo que solo está en Estados Unidos y no sé dónde más. Una
funcionalidad llamada Chronical, que es una memoria mucho más avanzada, se ejecuta en background y utiliza
agentes de IA para construir memorias desde capturas de pantalla. Es decir, que no solo memoriza lo que
estamos haciendo en

### 41:00

codex, sino lo que estamos haciendo en toda nuestra máquina. A mí personalmente me da un poco de mal rollo
esta funcionalidad, eso de que te esté haciendo pantallazos y almacenando información sobre lo que vas
haciendo, pero imagino que usado en el día a día puede ser muy cómodo, pero por supuesto esto puede tener
montones de temas de protección de datos y por tanto en la Unión Europea todavía no está activo y además ya
avisan de que consume muchísimos tokens, así que esto hay que tenerlo en cuenta. Pero bueno, es el camino
hacia el que va. En cualquier caso, estas memorias consumen muchísimos menos tokens y nos sirven como una base
sencilla para trabajar sobre lo que hemos ido haciendo en ese proyecto o incluso en otros proyectos. Y ahora
ya sí, vamos a empezar a trabajar sobre una aplicación. Y quiero hacer prácticamente todo el proceso sin salir
desde codex, es decir, quiero desarrollar el proyecto, pero también integrarlo en GitHub, habilitar la
integración continua en GitHub, desplegarlo para que el proyecto se quede público, incluso hacer el diseño
desde el propio codex. Para ello vamos a iterar sobre una idea,

### 42:02

vamos a generar diseños con la capacidad de imágenes. Codex también puede generar imágenes gracias a GPT Image
2. Y luego implementaremos ese diseño y pondremos a varios agentes en paralelo a trabajar sobre distintas
partes de nuestra aplicación. La idea que tengo en mente es la de desarrollar una página web que de momento
dejaré pública y en función de el uso que le deis puede que se quede ahí o puede que en un tiempo la dé de
baja, que va a consistir en un lugar donde los desarrolladores puedan ir a un único sitio a informarse sobre
las noticias que han ocurrido sobre inteligencia artificial aplicada al desarrollo de software. Para ello
vamos a crear una aplicación. Me voy a crear un hardbit que me permita extraer las noticias más relevantes
desde X y poder curarlas para luego de forma activa decidir cuáles van a la página web. Es decir, no van a ser
automáticas, sino que van a ser curadas por un humano y ese humano voy a ser yo y que cada día se me lance ese
listado de noticias y yo decida cuáles se publican en la página web. Para ello, vamos a venirnos aquí y vamos
a crear un nuevo proyecto. Todavía

### 43:02

no te he enseñado cómo crear nuevos proyectos, pero es tan sencillo como irse aquí, le podemos dar a start
from scratch y entonces el proyecto se creará en la carpeta de codex que mencionamos previamente con el nombre
que le indiquemos o si le decimos que use una carpeta existente, nos abrirá el selector de carpetas y
elegiremos la que nosotros queramos. Yo voy a ir por aquí porque prefiero tener organizados donde a mí me
interesen esas carpetas. Y en project me voy a ir a Antonio LG, voy a crear una nueva carpeta aquí y la vamos
a llamar, por ejemplo, AI News. Y ahora ya estamos trabajando sobre esta carpeta y yo le voy a decir este
proyecto va a consistir en una aplicación que permita a los desarrolladores estar al día sobre las noticias de
desarrollo con inteligencia artificial. Va a ser una web muy sencilla, minimalista, donde mediante una línea
de tiempo se especifique cuáles son las noticias relevantes que ha habido durante el día. Estas noticias se
extraerán de un fichero que puede ser un JSON, por ejemplo, y que ese Jason será

### 44:01

actualizado manualmente en el repositorio mediante un hardbit que también crearemos posteriormente, que me
traerá las noticias más relevantes desde X. La web solo mostrará una línea de tiempo y cuando hagamos clic
sobre una de las noticias nos llevará directamente a la noticia. Inicialmente vamos a empezar con X, pero en
el futuro es posible que añadamos nuevas fuentes como blogs de las empresas más activas sobre temas de
inteligencia artificial o cualquier otro sitio que nos permita o bien utilizar un RSS o hacer un scraping de
la web. De momento, lo único que quiero es que me crees un Ritmi con la información. en inglés y que
inicialices el repositorio Git ignore clásico para una web. Lo que quiero es crearme una base para luego en
paralelo poder ir trabajando sobre la integración continua, sobre el despliegue y este tipo de cosas. ¿Vale?
Pues ya nos ha creado el RMImi, el Git ignore, ha inicializado el Git. Esto lo podemos ver

### 45:00

porque ya aquí nos aparecen cosas, nos permite la opción de hacer commit desde aquí, crear una rama, hacer un
push si lo tenemos integrado con un repositorio en remoto y luego pues podemos abrir con el ID o la
herramienta que queramos para ver la carpeta en la que estamos trabajando. Luego por aquí también tenemos la
opción de ver los cambios y si pulsamos sobre cualquiera de ellos veremos cuáles son los cambios que ha habido
en cada uno de los ficheros y si queremos como previamente podemos darle a todos los archivos y ver todos los
archivos que tenemos en la carpeta. Y lo dicho, si quisiéramos trabajar en un ID, ya lo podemos abrir desde
aquí y estaríamos directamente en el proyecto sobre el que estamos trabajando. Vamos a utilizar la
funcionalidad de Comit desde aquí. Aquí me permite decidir qué es lo que voy a añadir y si lo dejo en blanco
se genera automáticamente el mensaje de commit. Yo normalmente se lo pido directamente en el chat, pero para
que veas que Git está bastante integrado dentro de la herramienta. Y luego le puedo decir usando GH crea un
repositorio remoto público en Antonio

### 46:02

LG. Usando GH realmente no necesito decírselo porque yo lo tengo en el AG MD principal, pero bueno, lo va a
crear desde aquí. Y si ahora hacemos clic en el enlace que nos ha generado, pues podremos acceder al
repositorio, que de momento está vacío, pero yo podría hacer aquí ahora push o incluso lo podemos hacer desde
aquí, pero yo ahora que ya he definido el origen, podemos ver aquí que tenemos el push, le podemos dar incluso
si estuviéramos en una rama que no fuera la principal, podríamos crear un pull request. En este caso va a ser
simplemente un push. nos está diciendo que el remoto no está bien configurado, así que le voy a decir que haga
push directamente aquí y ya se buscará las maneras para conseguirlo. Y si ahora refrescamos esto, pues ya
veremos que está subido en nuestro repositorio. Perfecto. Genial. Pues ahora con esto podemos ir haciendo
varios pasos. El primero que le voy a decir aquí es, basado en lo que hemos hablado, recomiéndame un stack
tecnológico. Ten en cuenta que queremos mantener una buena arquitectura, división de capas para que sea
fácilmente testeable, mantenible y escalable y que nos permita

### 47:02

crear una interfaz visualmente atractiva. Lo que quiero es tener ya una primera estructura de la aplicación,
un scaffold que todavía no tenga nada implementado, pero que me permita ir integrando toda la integración
continua y el despliegue en mi servidor, que en particular yo utilizo Coolify, pero que podría ser un Netlify
o incluso pues GitHub Pags, lo que se te ocurra. Me está recomendando que utilicemos Astro con Typ Script,
tailwin, Bites y Playwght. Astro solo presenta la lógica vive fuera. Así podremos cambiar news Jason por RSS.
scraping una base de datos sin reescribir la UI. Nesj sería más potente si ya supiéramos que vamos a necesitar
autenticación, pero efectivamente como no necesitamos autenticación le vamos a a dar como válido esto. Le voy
a decir, "Vale, crea un scaffold del proyecto, pero actualmente no implementes nada, simplemente que sea un al
mundo para que yo lo pueda subir a GitHub y pueda empezar con temas de integración continua y despliegue en
paralelo mientras tú trabajas sobre el código. Mientras esto está creando el scaffold,

### 48:01

voy a crear un nuevo chat y le voy a decir, revisa este proyecto y quiero que me generes cinco diseños
diferentes que puedan representar la interfaz de usuario de esta aplicación. Utiliza gen. Esta es una skill
que le explica cómo utilizar la generación de imágenes de codex. En principio no hace falta decírselo, pero
como yo tengo también otra skill de nanobanana, a veces se lía, así que le voy a decir específicamente que
haga esto. Entonces va a revisar lo que tenemos del proyecto, que ahora mismo es el RMI, y a partir de ahí nos
va a ofrecer cinco diseños diferentes para la aplicación web. Tardará un rato porque en general las imágenes
tarda un poquillo y además le hemos pedido cinco. De hecho, aquí ya ha creado una que la llama cambio de
estado, donde nos muestra pues eso, el timeline que le habíamos mencionado con las noticias de cada día, una a
cada lado. Aquí tenemos un buscador, identificación de cuándo fue actualizado por última vez. Bastante limpio,
en realidad es un poco lo que buscamos. Mientras tanto, esto ya ha terminado. Ha generado un escafol mínimo
con Astro. Lo

### 49:01

tenemos corriendo en local host y de hecho pues podemos ir trabajando con esta preview e ir mejorando cosas.
Yo le podría poner mejor que la interfaz de usuario esté en español. Cambia los textos por textos en español.
Y ahora pues ya ha [resoplido] cambiado los textos al español. También está actualizando algunos tests que
tenía en TUEN. Mira que ya los ha ejecutado. Esto nos va a venir muy bien para luego definir la integración
continua que haga todos estos chequeos. cada vez que se suba algo a main. Y ahora pues le vamos a decir
perfecto, haz commit y push. Mientras tanto aquí ha ido generando otros diseños. Este del pulso que parece
como un el pulso del corazón. La verdad que es muy curioso, pero no sé si a nivel de implementación va a ser
un poco complejo de conseguirlo. Y luego este otro que tiene esta barra a la izquierda y a la derecha el
listado en plan bitácora con un cuaderno de de viaje aquí con el formato del cuaderno, etcétera. La verdad que
es muy curioso

### 50:01

también. Perfecto. Ha hecho todo esto, mientras los diseños acaban, yo voy a crearme otra tarea que le voy a
decir, configura la integración continua en el repositorio para que se lancen todos los chequeos habituales en
una aplicación de este estilo, como pueden ser la compilación, el linter, la ejecución de test, chequeo de
tipos, etcétera. Y lo voy a dejar trabajando también mientras me voy a configurar en mi quify. Esto, esta
primera parte sí que la tengo que hacer desde la UI. Me creo un nuevo proyecto que de momento, bueno, pues lo
vamos a llamar AI News y aquí voy a añadir un recurso que va a ser un repositorio de GitHub y en este caso
vamos a seleccionar el de AI News. Le vamos a dar a continuar. Es un sitio estático, así que lo vamos a
seleccionar aquí y le vamos a dar a deploy. Vale, esto lo vamos a dejar ahí. Ya terminado, mientras tanto con
los cinco diseños. Vamos a verlos. Habíamos visto estos tres, nos faltaba este de que se llama señales
recientes, también está bastante bien. Y este último, pues que es quizá el más sencillo de todos, pero a la
par,

### 51:01

a lo mejor también el que es más fácil de leer y utilizar. La verdad es que yo soy muy malo para elegir
diseños. Todos me gustan, aunque ninguno me destaca especialmente. Le voy a decir, "¿Cuál elegirías tú?" me
dice que elegiría el de cambio de estado. A mí también es verdad que me parece como el más limpio, ¿no? Y más
tecnológico. Le voy a decir, "Vale, pues vamos a ir con el de cambio de estado, así que guarda la imagen en
una carpeta llamada design." Mientras tanto, voy a crearme aquí otro otra conversación que va a ser la que va
a sacar las noticias. Tengo ya aquí yo una automatización que se llama Daily Content Curation, que hace la
curación de contenidos buscando en redes sociales y eh le voy a decir basándote en la automatización que
tenemos pausada de Daily Content Curation, crea un hardbit aquí que cada día ejecute esa tarea y nos devuelva
cuáles son las noticias más relevantes del día. Como vas a tener el contexto de días anteriores, tráeme solo
las noticias nuevas y no las que sean repetidas. Hazme una propuesta de cuáles

### 52:02

crees que deberían publicarse en esta web y cuando yo te dé el OK, actualizarías la web con esas nuevas
noticias haciendo un commit y un push una vez que hayas terminado. Así que nada, vamos a dejarle creando aquí
el hardbit. Mientras tanto, el f del repositorio ya ha finalizado, así que le voy a decir aquí crea un hardbit
que se lance cada 10 minutos. y que revise tanto la integración continua como el estado de el culify. Para
ello tienes un CLI de Culify que puedes utilizar y revisar cómo han ido las últimas deploys. Echa un vistazo
ahora mismo de ambos antes de generar el hardbeit. Mientras esto se va lanzando y ya que tenemos los diseños y
que en principio tenemos aquí una carpeta con el diseño, pues nos vamos a volver a nuestro proyecto principal
que lo podemos renombrar. Esto lo podemos llamar main, esto lo podemos llamar design y esto lo podemos llamar
e noticias diarias y este

### 53:02

pues Ci. Una ventaja muy grande que tiene Codex sobre otras herramientas es que su compactación es mucho mejor
que otras herramientas que yo he utilizado, pues por ejemplo como cloud code o similares. Y se puede trabajar
en hilos muy largos que aunque se produzca la compactación rara vez pierde contexto. Por tanto, podemos tener
hilos individuales sobre distintas tareas en nuestro propio proyecto y sobre el que podemos ir trabajando e
iterando de tal forma que así no pierda el contexto previo. Vale, tenemos aquí el C, parece que el último
deploy ha funcionado, ya nos ha creado el hardbit, que cada 10 minutos se va a ir lanzando y comprobando si
alguna de los cambios que hemos hecho ha roto o bien la integración continua o bien el coolify. Aquí le voy a
cambiar la URL para que use ai.dbesperth.io. Lo guardamos. y lo tenemos que redesplegar para que utilice el
nuevo dominio. Mientras tanto, en el main le voy a decir, mira en la carpeta de diseño el diseño que hemos
creado e

### 54:01

implementa la aplicación. Para ello vamos a utilizar el modo plan para que prepares el plan para realizar toda
la implementación. Pero primero, antes de hacer nada, échale un vistazo al diseño para que tengas claro lo que
tenemos que hacer en ese plan. Parece que ya ha generado aquí el hardbit, lo tenemos aquí disponible. nos
indica lo que va a hacer en cada uno de los pasos. Vamos a darlo por válido. Y aunque bueno, esto se lanza
cada día a las 9 de la mañana, luego cuando ya tengamos la aplicación montada lo vamos a lanzar de forma
manual para comprobarlo. ¿Vale? Entonces, ha revisado el design, ha visto que el repo tiene cambio sin
comitear, así que antes de empezar le vamos a decir haz commit push de los cambios. Vale, aquí ya he hecho esa
parte, así que le voy a decir ya que empiece con lo que hemos hablado. Diseña el plan para empezar a trabajar.
El plan o bien lo podemos activar desde aquí, o bien escribiendo barraplan o incluso cuando escribimos la
palabra plan nos da aquí la opción de activarlo o con shift t hay 1000 opciones de activar el plan, como ves,
y cuando le damos empezar a

### 55:00

generar un plan de trabajo. Yo esto lo recomiendo sobre todo para tareas largas para que le dé una fase de
razonamiento previa antes de empezar a trabajar sobre eh la tarea concreta. Mientras tanto, esto ya ha
desplegado. Si yo me voy a e ai.desper. no está cargando, debe haber algún problema de certificados o algo por
el estilo, así que le voy a decir en el DCI. Ahora mismo la página no está cargando, la tengo desplegada en y
le doy la URL. Revisa los despliegues por Cullify a ver si hubiera alguna información extra y si no puedes
conectarte por SSH al servidor de Vespert-Vs. Así que voy a tratar de que Codex lo solucione por mí. Mientras
me vengo aquí, me ha generado el plan de implementación. Lo ideal sería revisarlo y darle una buena pasada. En
mi caso, le voy a decir ya que lo implemente y se va a poner a trabajar. Para la tarea de planificación y de
implementación de la base, yo os recomendaría que utilizarais un modelo más grande. Yo, por ir más

### 56:01

rápido en este ejemplo, lo he dejado con el low. Es posible que luego me toque iterar un poco más para
conseguir los resultados. Me está pidiendo acceso al VPS. entiendo que va a mirar qué es lo que puede estar
fallando en la integración continua. Vale, parece que lo que está incorrecto es el directorio de publicación.
lo va a intentar modificar por el VPS, pero a lo mejor no tiene los permisos suficientes y lo tengo que hacer
a mano. Mientras tanto, aquí sigue implementando y podemos ver en el menú lateral un poco cómo está
estructurando el proyecto. Tenemos una sección de páginas, estilos, infraestructura, que de momento carga las
noticias desde el Jason, pero el objetivo de esto es que en el futuro se pudiera cambiar si hiciera falta una
base de datos o algo por el estilo. El dominio nos ha generado la estructura de los elementos, el esquema de
los elementos que van a ir como noticias y el Jason donde podemos cargar los contenidos. Ahora se los ha
inventado, pero luego lo modificaremos y utilizaremos noticias reales. ¿Vale? Me dice que por un lado
necesitamos definir

### 57:00

que carguen dis y por otro que habría que cambiar información del DNS. Yo creo que esto no debería ser
necesario. Ha intentado hacerlo por el CLI, pero yo voluntariamente lo tengo como permisor de escritura en el
quulify para que no me toque nada y me lo pueda romper. Le puedo decir, "Lo tienes abierto en Helium, que es
el navegador que utilizo actualmente. Actualiza lo que necesites. Ya la ha cambiado a dis y ahora lo que va a
hacer es guardarlo. Y en este caso tendrá que hacer un redeploy, que no sé si lo va a hacer manualmente. Sí,
se va a redeploy y lo ejecuta. Así que ya está. lanzando el redeploy en la carpeta correcta en la que se
almacenan los ficheros de distribución de Astro. ¿Vale? Mientras se sigue solventando el tema del dominio, que
efectivamente sí que lo tenía que añadir en donde tengo configurados los DNSs. Esto ya ha terminado. Le voy a
decir ábrelo con browser use. Vale, ahora como he cambiado los dominios, le puedo pedir crea un hardbit para
que de cada 10 minutos revise si los dominios ya están resolviendo en el adecuado. Y una vez

### 58:03

que lo tengas confirmado, puedes eliminar el hardbit. Esto no me va a dejar porque ya tengo un hardbit creado
en esta conversación, así que me voy a crear una nueva conversación. Voy a poner simplemente hola para que me
conteste y me genere un hilo. Y voy a copiar el session ID y le digo aquí, como este hilo ya tiene un hardbit,
créalo en este otro que te voy a pasar, ¿vale? Y aquí ya vemos que me lo ha incluido. La siguiente ejecución
es dentro de 10 minutos. Y mientras vamos a ver qué nos ha hecho por aquí, tenemos aquí ya la web preview y el
resultado. Tiene una manía muy extraña este modelo de crear recuadros por debajo cuando yo no se lo he pedido.
Vamos a ampliarlo. La verdad es que por lo demás el diseño es muy muy parecido a lo que le habíamos dicho.
Sio, igual voy a abrir el diseño para recordarlo. Y efectivamente, pues visualmente salvo por esa cuadrícula
que me ha puesto por debajo, ya lo tenemos. Pero lo que quiero enseñarte es que una vez que estoy aquí en el
diseño, puedo activar el modo anotar. También se pueden tomar pantallazos y estos

### 59:00

pantallazos se los pasa a la conversación. Y en el modo anotar lo que puedo hacer es seleccionar distintas
partes y hacerle preguntas o pedirle detalles. Le puedo decir, por ejemplo, esto realmente se está
actualizando en tiempo real o siempre pone actualizado. Ahora está jarcodeado. Y luego me puedo ir, por
ejemplo, al fondo y decirle, "Ha incluido de fondo una cuadrícula que no estaba en el diseño, por favor
quítala." O aquí decirle, por ejemplo, se está viendo por debajo cómo pasa la raya. Lo ideal sería que el
fondo no fuera transparente para que la raya no se vea cuando pasa por encima del hoy, ayer, etcétera. Y me da
la sensación de que falta una cosa más. A ver que lo confirme. Era el diseño. Sí, efectivamente, faltan las
líneas que conectan con los recuadros, así que se lo voy a pedir también. Falta la línea que conecta el la
caja con el círculo que está en el timeline. Y con esto pues yo ya le puedo pasar las revisiones para que las
vaya modificando. Aquí si queremos podemos desplegar y podemos ir viendo lo que está haciendo. Esos cuatro
comentarios son buenos. Voy a

### 01:00:00

corregirlos de forma directa. Aquí se me siguen ejecutando las automatizaciones que configuramos previamente.
Voy a parar esta automatización porque si no me va a rellenar cada media hora y no me interesa realmente. Así
que siempre que queramos modificar las automatizaciones nos volvemos aquí y esta que es la que quiero eliminar
pues le voy a dar a delete. La podemos pausar para que se quede aquí abajo como pausada o borrarla
directamente. Nos dice que ahora sí va a calcular el estado actualizado desde los datos. Ahora ya nos indica
actualizado hace una hora. nos ha quitado la cuadrícula, ha creado las líneas, aunque no llegan hasta el Pero
se lo podemos volver a decir. Las líneas no llegan a conectar de todo la caja con el timeline. Le voy a poner
un nivel más alto para que se lo piense un poquito mejor. Ahora sí, ya conectan. Perfecto. Y ahora mismo no
parece que esté filtrando. Sí que hay algún cambio visual cuando empiezo a escribir, pero si yo escribo, por
ejemplo, si escribo algo que no está en ninguna, sí que desaparecen todas. Pero si escribo algo que esté en
una de ellas, parece que no filtra ninguna. Se lo voy a comentar

### 01:01:00

también. La caja de búsqueda parece que está funcionando de manera errática. Si escribo algo que no aparece en
ninguna de las cajas, sí que filtra todo y pone que no hay ninguna, pero parece que en cuanto que escribo una
palabra que existe en alguna de ellas, no desaparecen las que no lo contienen. Puedes revisarlo. Está haciendo
las comprobaciones manualmente con el browser use, escribiendo algo y viendo si cambia la configuración. Aquí
la integración continua se lanzó bien, pero nos dice que el point público del Harvin no es válido porque se
había quedado con el que genera originalmente, pero lo hemos cambiado. El tema de los DNS se sigue propagando.
Y aquí en principio ya está funcionando correctamente. Dice que se estaba usando hidden para ocultarlos, pero
que había que utilizar display non. Así que bueno, ya lo tenemos solucionado, así que le vamos a decir que haz
commit y push para tenerlo disponible para cuando esté lista la página. Y ahora vamos a aprovechar para
actualizar las noticias con noticias reales. Le voy a decir vacía el JSON actual que tiene noticias
inventadas. Y

### 01:02:02

ahora que lo va vaciado, lo que vamos a hacer es lanzar la automatización. Como no se va a lanzar hasta mañana
hasta a las 9, yo lo voy a lanzar manualmente entrando en la automatización y diciéndole run now. Y después de
pasar por aquí ha sacado cuatro noticias. La de GitHub Copilot que pasa facturación por uso, Stripe que lanza
infraestructura económica, Antropic lleva cloud a herramientas creativas y Cursor abre en beta pública su SDK.
Le voy a decir que añada las cuatro. Okay, añade las cuatro noticias. Y mientras termina de actualizar las
noticias diarias, te quería enseñar otra cosa que es muy útil cuando estamos trabajando con proyectos como
estos, que es que si tenemos tareas que se pueden ejecutar habitualmente, pues como por ejemplo todas estas,
las podemos añadir como acciones de ejecución. Para ello, pues podríamos hacer, por ejemplo, aquí el PNPM RAM,
que es el que ejecuta la aplicación. En este caso, pues pnpm RAM de lo vamos a editar. Nos vamos aquí a change
environment y a environment settings. Y si nos vamos a este entorno, tenemos aquí las acciones. Vamos a

### 01:03:01

editarlas. Esto sería pnpm RAM deh. Y si yo ahora me vengo aquí otra vez, puedo darle a ejecutar y nuestro
proyecto se ejecutará directamente. Y ya lo tenemos aquí en local host 2 1. O incluso si quiero lanzar los
tests, pues podría crearme otra acción. Podemos elegir el tipo debag y la podemos llamar test y poner pnpm
test. Entonces, cuando quiera yo puedo lanzar los test desde aquí y nos dice pues los test que han pasado,
cuánto han tardado, etcétera. Y eso lo puedo hacer con todas las tareas que quiera ejecutar habitualmente de
forma sencilla. Esto nos ha enseñado también que si yo le pulso aquí, tengo un terminal con el que puedo
trabajar directamente. No necesito trabajar todo el rato a través de la interfaz, sino que si quiero lanzar
tareas de terminal, lo puedo hacer desde aquí. Puedo tener varios terminales y, si no recuerdo mal, incluso el
agente es capaz de acceder a la información que está en el terminal. Por tanto, esto lo tenemos aquí muy a
mano por si queremos lanzar tareas, tenerlas en ejecución constante e ir validando pues los logs que salen,
etcétera. Y otra cosa que podemos estar

### 01:04:01

que podemos hacer cuando estamos trabajando con el div es que en cualquiera de las líneas que nos genera,
vamos a hacer este div más grande, podemos añadir comentarios. Aquí no tengo que tocar nada, pero por ejemplo
podríamos decir esto debería ser hidden en vez de non comentarlo. Esto se nos añade como un comentario aquí y
luego lanzarlo. Igual que hemos hecho los comentarios sobre la interfaz, los podemos hacer perfectamente sobre
los DIF para que modifique las partes que nos interese y comentar cosas directamente sobre la línea concreta
en vez de hablar sobre todo el código en general. Así que sepas que también esto es muy cómodo y que te
permite revisar antes de hacer la publicación. Entonces, vamos a hacer un commit con los cambios que tenemos
hasta ahora, que haga el commit y push. Por aquí ya ha acabado la parte de las noticias diarias, ha hecho los
cambios. También había subido la actualización de las noticias curadas, que es lo que le habíamos dicho, que
cuando las aceptemos haga el comitipus automáticamente. Esto sigue diciendo que desde esta máquina todavía
AIDBO no resuelve, así que necesita seguir

### 01:05:02

comprobándolo. Seguramente sea un tema de cachés porque fíjate que ya sí que carga y además ya tenemos las
noticias que nos ha subido de ayer que podemos ir a la fuente para verlas. el tema del SDK de cursor, lo que
ha lanzado Stripe. Además, lo bueno es que consigue sacar los enlaces de la fuente en vez de lanzarnos a X
directamente. Algunos sí que cargarán en X, supongo, pero aquí nos está llevando a la noticia original y lo
mismo de GitHub Copilot, así que bueno, ya tenemos nuestra aplicación de noticias funcionando. Además, filtra
correctamente. Podemos ver que aquí si filtramos solo la de Antropic, pues solo sale esta. La de Stripe
funciona bastante bien y cumple exactamente con lo que le estábamos pidiendo. Así que ya has visto que la
aplicación de Codex puede servir literalmente para todo. Podemos hacer desde tareas rutinarias de nuestro día
a día, automatizaciones que queramos sobre fuentes que le demos, herramientas, hemos visto Slacks, Gmail, pero
también hemos visto que en una propia conversación podemos lanzarle un

### 01:06:01

hardbit para que nos vaya recordando cosas o vaya comprobando cosas hasta que estén finalizadas y
posteriormente ese hardbit desaparezca. Podemos tener automatizaciones que se ejecuten a ciertos momentos del
día, por supuesto, podemos desarrollar cualquier aplicación que necesitemos. Y Codex sigue el formato AD,
agent development Environment, lo que quiere decir que el centro de la información es el agente y no el
código, aunque hemos visto que podemos revisar el código con Pool Request, podemos abrir el ID que queramos,
en este caso lo hemos probado con Visual Studio Code, pero con cualquiera que tengamos instalado en nuestra
máquina para revisar el código más en profundidad. Y en general, mi recomendación es que cada tarea que hagas
en tu día a día, intentes hacerla desde codex, intentes automatizarla de alguna forma, ya sea con skills,
automations, con plugins y que de esa forma poco a poco se vaya convirtiendo en tu asistente diario para todas
las tareas del día a día. Con esto hemos probado prácticamente todas las funcionalidades que tiene a día de
hoy Codex, aunque está en desarrollo muy activo, así que probablemente seguiré

### 01:07:00

subiendo vídeos posteriores cuando vayan saliendo nuevas funcionalidades, pero para mí es una de esas razones
por la que pago la suscripción de Codex y no otras. También es verdad que los modelos me gustan mucho, pero en
particular la aplicación es lo que me hace volver día a día a utilizarlo. También me gustaría que si tú
utilizas Codex me dejes en los comentarios para qué lo utilizas día a día, porque me encantaría seguir
aprendiendo de vuestras propias experiencias. Y si te ha gustado este vídeo y quieres más vídeos en
profundidad como este, déjamelo en los comentarios y ya sabes que si te suscribes, le das a la campanita, le
das like y lo compartes, me ayudas muchísimo a que este canal siga creciendo. Nos vemos en un próximo vídeo.
Hasta pronto.
