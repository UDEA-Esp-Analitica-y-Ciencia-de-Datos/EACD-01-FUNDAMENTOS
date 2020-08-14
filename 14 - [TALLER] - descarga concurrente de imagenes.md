# Descarga concurrente de imágenes

En este taller pondrás a prueba lo que aprendiste sobre concurrencia y manipulación de archivos. Tu tarea será leer un conjunto de [archivos en formato CSV que contenien una base de datos de pókemons](./local/data/pokemon/) y descargar el *sprite* de cada pókemon.

Cada archivo CSV es como el siguiente:

| Pokemon    | Number | Type1    | Type2    | Ability1      | Ability2      | Ability3      | HP  | Attack | Defense | Sp. Atk | Sp. Def | Speed | Sprite                                                     |
|------------|--------|----------|----------|---------------|---------------|---------------|-----|--------|---------|---------|---------|-------|------------------------------------------------------------|
| Bulbasaur  | 1      | GRASS    | POISON   | Overgrow      | Chlorophyll   | none          | 45  | 49     | 49      | 65      | 65      | 45    | https://play.pokemonshowdown.com/sprites/bw/bulbasaur.png  |
| Ivysaur    | 2      | GRASS    | POISON   | Overgrow      | Chlorophyll   | none          | 60  | 62     | 63      | 80      | 80      | 60    | https://play.pokemonshowdown.com/sprites/bw/ivysaur.png    |
| Venusaur   | 3      | GRASS    | POISON   | Overgrow      | Chlorophyll   | none          | 80  | 82     | 83      | 100     | 100     | 80    | https://play.pokemonshowdown.com/sprites/bw/venusaur.png   |
| Charmander | 4      | FIRE     | none     | Blaze         | Solar Power   | none          | 39  | 52     | 43      | 60      | 50      | 65    | https://play.pokemonshowdown.com/sprites/bw/charmander.png |
| Charmeleon | 5      | FIRE     | none     | Blaze         | Solar Power   | none          | 58  | 64     | 58      | 80      | 65      | 80    | https://play.pokemonshowdown.com/sprites/bw/charmeleon.png |


Al descargar cada imagen, esta debe ser guardada en un directorio con el nombre del tipo de pókemon y la imágen debe ser guardada con el nombre del pókemon, como se muestra a continuación:

```
output
│
└───grass
│   │   bulbasaur.png
│   │   ivysaur.png
│   │   ...
│   
└───fire
    │   charmander.png
    │   charmeleon.png
    |   ...
```

Para retarte un poco más, incluí algunos links que no funcionan, por lo que tu código debe estar en la capacidad de manejar esta situación. Este reto adicional es bastante similar a una situación normal en el trabajo. 

Tu tarea es resolver este reto utilizando las 3 formas de concurrencia vistas en clase y reportar el tiempo que te toma cada una. Cuando termines, envía un correo al profesor y monitor del curso, adjuntando el link al repositorio privado en GitHub con la respuesta (debes compartir el repo con el monitor y el profesor). El repositorio debe contener las instrucciones necesarias para ejecutar el código de tal manera que tanto el profesor y el monitor puedan ejecutarlo y debe contener capturas de pantalla que demuestren que funciona como debe funcionar. 
