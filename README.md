# Simulación basada en Eventos Discretos
## Andy A. Castañeda Guerra C412

<div style="text-align: right"> <a href="mailto:andy.castaneda@estudiantes.matcom.uh.cu"> andy.castaneda@estudiantes.matcom.uh.cu </a>  </div>

<div style="text-align: right"> <a href="https://github.com/Yumenio/simulation-discrete-event"> Github Link </a> </div>



### 5. Aeropuerto de Barajas

En el Aeropuerto de Barajas, se desea conocer cuánto tiempo se encuentran vacı́as las pistas de aterrizaje. Se conoce que el aeropuerto cuenta con un máximo de 5 pistas de aterrizaje dedicadas a aviones de carga y que se considera que una pista está ocupada cuando hay un avión aterrizando, despegando o cuando se encuentra cargando o descargando mercancı́a o el abordaje o aterrizaje de cada pasajero. Se conoce que el tiempo cada avión que arriba al aeropuerto distribuye, mediante una función de distribución exponencial con λ = 20 minutos. Si un avión arriba al aeropuerto y no existen pistas vacı́as, se mantiene esperando hasta que se vacı́e una de ellas (en caso de que existan varios aviones en esta situación, pues se establece una suerte de cola para su aterrizaje. Se conoce además que el tiempo de carga y descarga de un avión distribuye mediante una función de distribución exponencial con λ = 30 minutos. Se considera además que el tiempo de aterrizaje y despegue de un avión distribuye normal (N(10,5)) y la probabilidad de que un avión cargue y/o descargue en cada viaje corresponde a una distribución uniforme. Además de esto se conoce que los aviones tiene una probabilidad de tener una rotura de 0.1. Ası́, cuando un avión posee alguna rotura debe ser reparado en un tiempo que distribuye exponencial con λ = 15 minutos. Las roturas se identifican justo antes del despegue de cada avión. Igualmente cada avión, durante el tiempo que está en la pista debe recargar combustible y se conoce que el tiempo de recarga de combustible distribuye expoencial λ = 30 minutos y se comienza justamente cuando el avión aterriza. Se asume además que los aviones pueden aterrizar en cada pista sin ninguna preferencia o requerimiento. Simule el comportamiento del aeropuerto por una semana para estimar el tiempo total en que se encuentran vacı́a cada una de las pistas del aeropuerto.





### Principales Ideas

Primeramente, el objetivo de la simulación es determinar cuanto tiempo pasa una pista del aeropuerto desocupada.

Consideraremos que una pista está ocupada desde que un avión aterriza por ella, y hasta que despega. El tiempo intermedio entre el aterrizaje y el despegue, en el cual el avión se encuentra realizando otros procesos, se considerará que la pista se encuentra ocupada igualmente.

Siguiendo esta idea, se puede determinar el tiempo que una pista pasa ocupada restándole al tiempo total que estuvo en funcionamiento, la suma de los tiempos en los que hubo un avión en ella. Para ello, tenemos un objeto *Plane*, el cual guarda el número de la pista que lo atendió, así como su tiempo exacto de comienzo de aterrizaje y final del despegue. Sean estos datos $P_t, P_A,P_D$ respecticamente, entonces el tiempo que una pista pasa desocupada sería igual a: $T - \sum P_D-P_A ~~~~~~\forall ~\text{Plane tal que $P_T$ sea igual a la pista analizada.  T = Tiempo Total que el aeropuerto estuvo funcionando.}$. 

Para generar las variables aleatorias requeridas, se utilizó el método de la transformada inversa para el caso de la exponencial, y el método de rechazos para la normal. Además se usó el método uniform(0,1) del módulo random como punto de partida. Los códigos se encuentran en el archivo **va.py**.

La llegada de cada avión al aeropuerto se asumió que era independiente del resto. Cuando un avión llega, se le asigna una pista de aterrizaje aleatoria, en caso de que hubiera alguna desocupada, en caso contrario se pone al final de la cola de aviones en espera. Para aleatorizar la pista que atenderá al próximo avión se utilizó una variable aleatoria uniforme, para elegir una de las que estuvieran libres en ese momento.



Dado que todos los arribos al aeropuerto son independientes y siguen una distribución exponencial con los mismos parámetros, tenemos un proceso Poisson homogéneo. De modo que seguiremos la idea iterativa de $t_{a+1}=t_a+X$ donde, el tiempo de aterrizaje de un avión $t_{a+1}$ es igual al tiempo de aterrizaje del anterior $t_a$, más una variable aleatoria X, que para nuestro problema sería una exponencial(1/20).



Cuando un avión aterriza, anotamos la pista por la cual lo hizo, luego calculamos el tiempo que pasará ocupando la pista, ya sea cargando, descargando, recargando combustible o bajo reparaciones(los cuales se consideran de manera independiente dos a dos,i.e. si el avión está recargando combustible, no estará simultáneamente bajo reparaciones), y se anotan también sus tiempos de aterrizaje y despegue.



Se consideró que la probabilidad de que un avión cargue y/o descargue en el aeropuerto es una Bernoulli(1/2).





### Modelo de simulación de Eventos Discretos para el problema

* Variable de tiempo:
  * **current_time**: tiempo actual en la simulación
  * **next_arrival_time**: tiempo de la próxima llegada simulada de un avión
  * **total_time**: tiempo total que se ejecutará la simulación
* Variable de estado:
  * **queue**: cola de aviones en espera porque todas las pistas están llenas
  * **tracks**: lista para mantener los tiempos de despegue de los aviones que las ocupan
  * **plane_history**: lista en la que se guardan todos los aviones atendidos para luego analizar los datos

Los eventos principales son *on_arrival* y *on_depart*, para cuando un avión llega y se va del aeropuerto respectivamente; así como *handle_plane* para simular el tratamiento que se le da al avión en el aeropuerto. *on_arrival* se encarga del proceso de llegada de un avión al aeropuerto, le asigna una pista de aterrizaje de ser posible, o lo añade al final de la cola de espera. Luego cuando un avión es designado para ser atendido en una pista, *handle_plane* simula todo su proceso de aterrizaje, carga/descarga, recarga de combustible y posibles reparaciones, para al final simular su despegue. Los datos de aterrizaje, pista de aterrizaje y despegue son anotados como propiedades de la clase *Plane* que representa cada avión en nuestro programa. Finalmente cuando el avión despega, se añade a la lista *plane_history* de aviones que han sido procesados durante la simulación, para, al llegar al tiempo límite, analizar los resultados obtenidos.





### Consideraciones

Luego de ejecutar la simulación unas 10 veces, se obtuvieron resultados bastante similares para cada una. Dado que no existe ninguna preferencia ni requerimiento a la hora de asignarle una pista a un avión aterrizando, los valores de tiempo desocupado oscilaban entre 2500 y 3000 minutos. Obteniendo como mínimo 1800 minutos en una ocasión, y cerca de 4000 para el máximo.

