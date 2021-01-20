var url = 'https://raw.githubusercontent.com/LuisMLV/VISUALIZACI-N_EJECUCIONES_EEUU_1976-2016/master/regions_states.json';

  
  var visualization = d3plus.viz()
    .format('es_ES')
    .container("#viz")  
    .data( url )  
    .type("tree_map")   
    .id(["Region",'Estado'])
    .title('Número de ejecutados en función de la región y el estado de los Estados Unidos de América')
    .title({'sub': 'Orden de navegación: Región> Estado'})   
    .size("Numero de ejecutados")      
    .draw()     


   