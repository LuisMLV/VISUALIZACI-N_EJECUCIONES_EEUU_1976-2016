
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 13:10:27 2021

@author: luism
"""



'''

Este es el código de python que ha generado la mayoría de las diferentes visualizaciones del proyecto de
visualización "Ejecuciones en Estados Unidos: análisis del periodo 1976-2016".

'''


#LIBRERÍAS UTILIZADAS

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

execution_df = pd.read_csv('executions.csv') #Carga del dataset en forma de dataframe.

execution_df = execution_df.dropna() # Elimino los posibles valores nulos.


# VISUALIZACIÓN 1. PRISIONEROS EJECUTADOS EN FUNCIÓN DEL GÉNERO.

ex_bygenre = execution_df['Sex'].value_counts() #Creo el subconjunto a usar.
ex_bygenre = ex_bygenre.rename({'Male': 'Masculino', 'Female': 'Femenino'}) # Traduzco las categorías al español, puesto que es lenguaje del proyecto.


colors =('indianred', 'cyan') #Colores de las categorías en el gráfico.

font = {'family' : 'monospace', #Establezco las características que tendrá a priori el texto en el gráfico.
        'weight' : 'normal',
        'size'   : 16}

#Dibujo la visualización:

plt.rc('font', **font) #Aplico estas características del texto al gráfico.
plt.figure(figsize=(14,10)) # Establezco las dimensiones del gráfico.
plt.pie(ex_bygenre.values, colors=colors, autopct= '%1.1f%%', startangle=90, pctdistance=1.06)
plt.title ('PRESOS EJECUTADOS SEGÚN GÉNERO \n', fontsize= 18)
plt.axis('equal')
plt.legend(ex_bygenre.index, bbox_to_anchor=(1.1,0.1), fontsize=16)
plt.show()
plt.savefig('ex_bygenre.png') #Guardo el gráfico o visualización en formato png.


#VISUALIZACIÓN 2. PRISIONEROS EJECUTADOS EN FUNCIÓN DEL GRUPO RACIAL.

ex_byrace = execution_df['Race'].value_counts() #Subconjunto a usar.
#Renombro las categorías al español debido a que el proyecto está en español:
ex_byrace = ex_byrace.rename({'White':'Blanca', 'Black':'Negra', 'Latino': 'Latina', 'Native American': 'Nat. Amer.', 'Asian':'Asiática', 'Other': 'Otras'})
ex_byrace = ex_byrace.sort_values(ascending=False) #Ordeno los valores de mayor a menor para un entendimiento más intuitivo de la visualización.
colors=['cyan', 'blue', 'red', 'gray', 'tan', 'navy', 'darkred'] #Determino los diferentes colores de las diferentes categorías.

#Dibujo la visualización:

plt.figure(figsize=(12,8))
plt.barh(ex_byrace.index, ex_byrace.values, color=colors, edgecolor='black')
plt.xlabel('Nº ejecutados', fontsize=16)
plt.ylabel('Raza', fontsize=16)
plt.xticks(fontsize= 13) #Tamaño de fuente en la que apareceran los valores del eje de las x.
plt.yticks(fontsize=13) #Tamaño de la fuente en la que aparecen los valores del eje de las y.
plt.title('REOS EJECUTADOS EN FUNCIÓN DE SU GRUPO RACIAL', fontsize=18)
plt.show()
plt.savefig('ex_byrace.png')


# VISUALIZACIÓN 3. PRISIONEROS EJECUTADOS POR INTERVALO DE EDAD.

'''
En el dataset, los registros referentes a la edad no aparecen por intervalos, sino por valores discretos.
Para una mejor visualización de estos datos, es conveniente representarlos por intervalos:

'''



age_interval = [] # Creo una lista donde almacenaré cada registro de edad transformado en determinado rango de edad.

for i in execution_df['Age']: # Con este bucle llevo a cabo la transformación de valor de edad discreto a intervalo de edad, y voy guardando los datos en la lista antes mencionada.
    
    if i>=15 and i<=24:
        age_interval.append('15-24')
    elif i>=25 and i<= 34:
        age_interval.append('25-34')
    elif i>=35 and i<= 44:
        age_interval.append('35-44')
    elif i>=45 and i<=54:
        age_interval.append('45-54')
    elif i>=55 and i<=64:
        age_interval.append('55-64')
    elif i>= 65 and i<=74:
        age_interval.append('65-74')
    else:
        age_interval.append('+75')


execution_df['age_interval'] = age_interval #Finalmente introduzco en el dataframe un nuevo campo donde inserto todos los datos de la lista.


ex_byage = execution_df['age_interval'].value_counts() #Creo el subconjunto a usar en la visualización.

ex_byage = ex_byage.sort_values(ascending=False) #Lo ordeno de mayor a menor.

#Dibujo la visualización:

plt.figure(figsize=(12,8))
plt.bar(ex_byage.index, ex_byage.values, color='cyan',  edgecolor='black', width=0.8)
plt.xlabel('Intervalo de edad', fontsize=16)
plt.ylabel('Nº de ejecutados', fontsize=16)
plt.title('REOS EJECUTADOS POR INTERVALO DE EDAD', fontsize=18)
plt.xticks(fontsize= 13)
plt.yticks(fontsize=13)
plt.savefig('ex_byage.png')


#VISUALIZACIÓN 4.PRESOS EJEUTADOS POR MÉTODO DE EJECUCIÓN

ex_bymethod = execution_df['Method'].value_counts() #Subconjunto de la visualización.
ex_bymethod = ex_bymethod.sort_values(ascending=False) #Orden descendente.
#Transformo las categorías de inglés a español. Abreviadas para no tener problemas de espacio en el gráfico:
ex_bymethod = ex_bymethod.rename({'Firing Squad': 'Pelot. fus.', 'Electrocution':'Electroc.', 'Gas Chamber': 'Cám. gas', 'Lethal Injection': 'In. letal', 'Hanging': 'Ahorca.'})


#Dibujo la gráfica:

plt.figure(figsize=(12,8))
plt.bar(ex_bymethod.index, ex_bymethod.values, color='orange', edgecolor='black', width=0.8)
plt.xlabel('Método de ejecución', fontsize=16)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
plt.ylabel('Nº de ejecutados', fontsize=16)
plt.title('REOS EJECUTADOS POR MÉTODO DE EJECUCIÓN', fontsize=18)
plt.savefig('ex_bymethod.png')


#VISUALIZACIÓN 5. VÍCTIMAS: ASESINATO ÚNICO O MÚLTIPLE.

'''

Para esta visualización vuelvo a hacer un tratamiento con los datos del dataset. Hay un campo, "Victim Count", que cuenta el número de
víctimas de cada ejecutado por la pena de muerte. Para un mejor manejo en la creación del gráfico voy a crear un campo en el dataset variable
categórica con dos categorías: Víctima única y Víctima múltiple. Ello para identificar y resumir mejor la información que quiero representar:
proporción de ejecutados con víctima única frente a proporción de ejecutados con víctima múltiple.
 
'''

victim_count = [] # Lista que va a recoger si el asesinato por el que se juzgo al condenado fue múltiple o no.



for i in execution_df['Victim Count']: # Obtendré si el asesinato fue múltiple o no a partir del campo "Victim Count".
    
    if i != 1: #Si el número indicado en Victim Count es distinto de 1
        victim_count.append('Víctima múltiple') #Se añade un registro de Víctima múltiple a la lista.
    
    else: # Si no
        victim_count.append('Víctima única') #Se añade un registro de Víctima única.
        
        
execution_df['multiple_unique'] = victim_count # Se crea el campo en el dataset y se añade la información que reside en la lista antes creada y rellenada.

ex_bynumber = execution_df['multiple_unique'].value_counts() #  Subconjunto de datos para la visualización.

colors=('grey', 'black') # Establezco las características de la fuente.
font = {'family' : 'monospace',
        'weight' : 'normal',
        'size'   : 16}


#Dibujo la visualización:

plt.rc('font', **font)
plt.figure(figsize=(12,8))
plt.pie(ex_bynumber.values, colors = colors, autopct='%1.1f%%' , startangle=90, textprops=dict(color="w") )
plt.title('EJECUTADOS EN BASE A SI COMETIERON ASESINATO MÚLTIPLE O NO', fontsize=18)
plt.legend(ex_bynumber.index, bbox_to_anchor=(1.2,0.1), fontsize=16)
plt.show()
plt.savefig('ex_bynumber.png')


#VISUALIZACIÓN 6. VÍCTIMAS: PROPORCIÓN DE VÍCTIMAS ASESINADAS POR LOS EJECUTADOS EN FUNCIÓN DEL GÉNERO.


'''

Como ya se ha indicado antes, los ejecutados en el dataset tuvieron o víctima única o víctima múltiple.

Las característica de cómo se ofrecen los datos en este dataset hace necesario un tratamiento algo  particular
para acceder a la información deseada en el caso del género de las víctimas. El campo donde se indica el género o 
género de la/s víctima/s es  "Victim Sex". Cuando el número de víctimas es más de uno pero han sido de un sólo sexo, 
en "Victim Sex" se muestra sólo la categoría Male o Female según corresponda. Cuando las víctimas han sido de varios 
géneros se suele mostrar el campo "Victim Sex" con el número de víctimas de cada género (ej: 1 Male, 2 Female). Teniendo 
en cuenta esto, he procedido a llevar a cabo el proceso que a continuación muestro para realizar la presente visualización:

'''
victim_male = [] #Creo una lista que alojará el número de víctimas de género masculino.

victim_female = [] #Creo una list que alojará el número de víctimas de género femenino.

for i,j in zip(execution_df['Victim Sex'], execution_df['Victim Count']): #por cada registro de los campos "Victim Sex" y "Victim Count"
    
    if i == 'Male': # Miro si el registro de "Victim Sex" es igual a Male
        if j == 1: # Si en Victim Count sólo aparece una víctima
            victim_male.append(1) #Añado uno a victim_male.
            
        else: #Si no
            victim_male.append(j) # Añado el número de víctimas que aparece en "Victim Count".
            
        victim_female.append(0) #Añado 0 a victim_female.
            
    elif i ==  'Female': # Lo mismo en el caso de las mujeres
        if j == 1:
            victim_female.append(1)
            
        else:
            victim_female.append(j)
            
        victim_male.append(0)
        
    else: # Si resulta que i no es igual ni a "Male" ni a "Female", será porque el registro tiene la estructura antes mencionada "x Male, y Female".
        
        victim_male.append(int(i[0])) #Por consiguiente añado a victim_male el caracter en la posición 0, que es el número de víctimas masculinas.
        victim_female.append(int(i[8])) #y también añado a victim_female el caracter en la posición 8, que es el número de víctimas femeninas.
               

execution_df['victim_male'] = victim_male #Creo los campos correspondientes y les introduzco los datos de las listas.
execution_df['victim_female'] = victim_female


vic_bygenre = execution_df[['victim_male', 'victim_female']].sum() # Subconjunto de datos para la visualización.
vic_bygenre =vic_bygenre.rename({'victim_male':'Víctima varón', 'victim_female': 'Víctima mujer'}) # Traduzco las categorías al español.
colors = ('indianred', 'cyan') # Determino los colores.
font = {'family' : 'monospace', # Establezco las características del texto.
        'weight' : 'normal',
        'size'   : 16}

#Dibujo la visualización:

plt.rc('font', **font)
plt.figure(figsize=(12,8))
plt.pie(vic_bygenre.values, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('VÍCTIMAS DE REOS EJECUTADOS EN FUNCIÓN DEL GÉNERO',fontsize=18)
plt.legend(vic_bygenre.index, bbox_to_anchor=(1.2,0.1), fontsize=16)
plt.show()
plt.savefig('vic_bygenre.png')


#VISUALIZACIÓN 7. VÍCTIMAS: VÍCTIMAS ASESINADAS POR LOS EJECUTADOS EN FUNCIÓN DE LA RAZA:

'''

El campo correspondiente a las características raciales de las víctimas, "Victim Race", es parecido al campo 
"Victim Sex" en su presentación. Cuando hay más de una víctima pero todas son de la misma raza, simplemente aparece
una categoría con la raza a la que pertenecen los asesinados, sin ninguna información numérica. No obstante, cuando
las razas de las víctimas son distintas aparecen las distintas razas del asesinato múltiple con el número de víctimas de
cada raza (ej: x White, y Black). Pero debido al mayor número y variabilidad de categorías del campo
la estructura en la que se expresa la diversidad de razas de las víctimas no es tan fija como en el caso del campo "Victim Sex" 
(ej: un registro puede ser "x White, y Black", pero otro registro será "x Black, y Asian", y otro "x White, y Latino, z Asian".
Teniendo todo esto en cuenta se llevó a cabo el siguiente proceso para llevar a cabo la siguiente visualización:


'''

white_race = [] #Creo las listas que contendrán el número de víctimas de cada raza por registro.
black_race = []
asian_race = []
latin = []
nat_american = []

# Para abordar el problema, divido el dataset entre los datos de ejecutados que tuvieron víctima única y los datos de ejecutados que tuvieron víctima múltiple.


unique_df = execution_df[execution_df['multiple_unique']=='Víctima única'] # Empiezo por los de víctima única.


 


for i in unique_df['Victim Race']: # por cada registro en el dataset con los registros de asesinos que tuvieron víctima única
    
    
# Compruebo de qué raza es la víctima, y en función de esto añado datos a la lista correspondiente:
        
        if i == 'White':
            white_race.append(1)
            black_race.append(0)
            asian_race.append(0)
            latin.append(0)
            nat_american.append(0)
      
      
        elif i == 'Black':
            white_race.append(0)
            black_race.append(1)
            asian_race.append(0)
            latin.append(0)
            nat_american.append(0)
        
        elif i == 'Asian':
            white_race.append(0)
            black_race.append(0)
            asian_race.append(1)
            latin.append(0)
            nat_american.append(0)
    
        elif i == 'Latino':
            white_race.append(0)
            black_race.append(0)
            asian_race.append(0)
            latin.append(1)
            nat_american.append(0)
    
        elif i == 'Native American':
            white_race.append(0)
            black_race.append(0)
            asian_race.append(0)
            latin.append(0)
            nat_american.append(1)
            
          
        
multiple_df = execution_df[execution_df['multiple_unique']=='Víctima múltiple'] # Dataset con los registros de los ejecutados que tuvieron víctima múltiple.



for j,k in zip(multiple_df['Victim Race'], multiple_df['Victim Count']): # Por cada registro en el dataset de víctima múltiple:   

    
# Compruebo si el registro es una de las categorías presentes en el campo para víctimas múltiples.

        if j == '2 White, 1 Black': #Si es así añadimos las correspondientes cantidades de víctimas de cada raza a las listas correspondientes.
            white_race.append(2)
            black_race.append(1)
            asian_race.append(0)
            latin.append(0)
            nat_american.append(0)
        
        if j == '4 White, 1 Black':
            white_race.append(4)
            black_race.append(1)
            asian_race.append(0)
            latin.append(0)
            nat_american.append(0)
            
            
        if j == '4 White, 1 Black, 1 Latino':
            white_race.append(4)
            black_race.append(1)
            asian_race.append(0)
            latin.append(1)
            nat_american.append(0)
            
        if j == '1 White, 3 Latino':
            white_race.append(1)
            black_race.append(0)
            asian_race.append(0)
            latin.append(3)
            nat_american.append(0)
            
        if j == '1 White, 2 Black':
            white_race.append(1)
            black_race.append(2)
            asian_race.append(0)
            latin.append(1)
            nat_american.append(0)
        
        if j == '1 White, 1 Latino':
            
            white_race.append(1)
            black_race.append(0)
            asian_race.append(0)
            latin.append(1)
            nat_american.append(0)
            
        if j == '2 White, 1 Latino':
          
            white_race.append(2)
            black_race.append(0)
            asian_race.append(0)
            latin.append(1)
            nat_american.append(0)
    
        if j == '1 White, 1 Black':
          
            white_race.append(1)
            black_race.append(1)
            asian_race.append(0)
            latin.append(0)
            nat_american.append(0)
     
        if j == '2 White, 2 Asian':
         
            white_race.append(2)
            black_race.append(0)
            asian_race.append(2)
            latin.append(0)
            nat_american.append(0)
        
        if  j == '2 White, 1 Asian':
            
            white_race.append(2)
            black_race.append(0)
            asian_race.append(1)
            latin.append(0)
            nat_american.append(0)
            
        if j == '3 White, 1 Black':
            
            white_race.append(3)
            black_race.append(1)
            asian_race.append(0)
            latin.append(0)
            nat_american.append(0)
        
        if j == '1 White, 2 Latino':
            
            white_race.append(1)
            black_race.append(0)
            asian_race.append(0)
            latin.append(2)
            nat_american.append(0)
            
        if j == '1 White, 3 Asian':
            
            white_race.append(1)
            black_race.append(0)
            asian_race.append(3)
            latin.append(0)
            nat_american.append(0)
            
        if j == '4 White, 1 Latino':
            
            white_race.append(4)
            black_race.append(0)
            asian_race.append(0)
            latin.append(1)
            nat_american.append(0)
        
        if j == '2 White, 3 Black':
            
            white_race.append(2)
            black_race.append(3)
            asian_race.append(0)
            latin.append(0)
            nat_american.append(0)
        
        if j == '1 White, 8 Latino':
            
            white_race.append(1)
            black_race.append(0)
            asian_race.append(0)
            latin.append(8)
            nat_american.append(0)
        
        if j == '2 White, 6 Black':
            
            white_race.append(2)
            black_race.append(6)
            asian_race.append(0)
            latin.append(0)
            nat_american.append(0)
        
        if j == 'White':
            
            white_race.append(k)
            black_race.append(0)
            asian_race.append(0)
            latin.append(0)
            nat_american.append(0)
            
        if j == 'Black':
            
            white_race.append(0)
            black_race.append(k)
            asian_race.append(0)
            latin.append(0)
            nat_american.append(0)
        
        if j == 'Latino':
            
            white_race.append(0)
            black_race.append(0)
            asian_race.append(0)
            latin.append(k)
            nat_american.append(0)
        
        if j == 'Asian':
            
            white_race.append(0)
            black_race.append(0)
            asian_race.append(k)
            latin.append(0)
            nat_american.append(0)
        
        
        if j == 'Native American':
            
            white_race.append(0)
            black_race.append(0)
            asian_race.append(0)
            latin.append(0)
            nat_american.append(k)
        
        

execution_df['Víctima raza blanca'] = white_race # Creo campos para las víctimas de cada raza y los lleno con los datos de las correspondientes listas.
execution_df['Víctima raza negra'] = black_race
execution_df['Víctima asiática'] = asian_race
execution_df['Víctima latina'] = latin
execution_df['Víctima nat. americano'] = nat_american
        
        
vic_byrace = execution_df[['Víctima raza blanca', 'Víctima raza negra', 'Víctima asiática', 'Víctima latina', 'Víctima nat. americano']].sum() # Subconjunto de datos para realizar la visualización.
vic_byrace = vic_byrace.sort_values(ascending=False) # Ordeno los datos de mayor a menor.
vic_byrace = vic_byrace.rename({'Víctima raza blanca':'Blanca', 'Víctima raza negra':'Negra', 'Víctima latina': 'Latina', 'Víctima nat. americano': 'Nat. Amer.', 'Víctima asiática':'Asiática'}) #Traduzco las categorías al español y las abrevio para que no ocupen un espacio excesivo en el gráfico.
colors=['cyan', 'blue', 'red', 'gray', 'tan', 'navy'] #Determino los colores a usar.


#Dibujo la visualización:

plt.figure(figsize=(12,8))
plt.barh(vic_byrace.index, vic_byrace.values, color=colors, edgecolor='black')
plt.title ('NÚMERO DE VÍCTIMAS EN FUNCIÓN DE LA RAZA', fontsize=18)
plt.xlabel('Nº de víctimas', fontsize=16)
plt.ylabel('Raza', fontsize=16)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
plt.show()
plt.savefig('vic_byrace.png')


#VISUALIZACIÓN 8.EVOLUCIÓN DEL NÚMERO DE EJECUCIONES A LO LARGO DEL TIEMPO

execution_df['Date'] = pd.to_datetime(execution_df['Date']) # Transformo el campo "Date" de formato string al formato date, más correcto.
execution_df['year'] = execution_df['Date'].dt.year # Uso el campo "Date" para extraer el año en el que fueron ejecutados los ejecutados y meto esos datos en un campo que creo para ello, "year".

ex_time = execution_df['year'].value_counts() #Subconjunto a usar en la visualización.
ex_time = ex_time.sort_index(ascending=True) #Ordeno de menor a mayor, ya que quiero representar los datos en orden cronológico.


#Dibujo la gráfica:

plt.figure(figsize=(12,7))
sns.lineplot(data=ex_time)
plt.title('EVOLUCION DEL Nº DE EJECUCIONES POR AÑO EN ESTADOS UNIDOS ENTRE 1976 Y 2016 \n', fontsize=18)
plt.ylabel('Nº de ejecuciones \n', fontsize=16)
plt.xlabel('Año \n', fontsize=16)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
#sns.set(color='black')
sns.set_context("paper", rc={"lines.linewidth": 2.15})
plt.savefig('ex_time.png')


#EVOLUCIÓN DEL NÚMERO DE EJECUCIONES A LO LARGO DEL TIEMPO SEGÚN MÉTODO DE EJECUCIÓN

electrocution = execution_df[execution_df['Method'] == 'Electrocution'] #Divido el dataset en distintos subconjuntos según el método de ejecución.
gas_cham = execution_df[execution_df['Method'] == 'Gas Chamber']
letal_inj = execution_df[execution_df['Method'] == 'Lethal Injection']

#Selecciono los subconjuntos a usar en la visualización y los ordeno de menor a mayor, ya que quiero representar los datos en orden cronológico.

elect_time = electrocution['year'].value_counts().sort_index(ascending=True) 
gascham_time = gas_cham['year'].value_counts().sort_index(ascending=True)
letalinj_time = letal_inj['year'].value_counts().sort_index(ascending=True)


#Dibujo la visualización:

plt.figure(figsize=(12,8))
sns.lineplot(data=elect_time, color='navy') # Dibujo tres líneas en la gráfica
sns.lineplot(data=gascham_time, color='orange') #cada una correspondiente 
sns.lineplot(data=letalinj_time, color='red') #a uno de los principales métodos de ejecución en el dataset.
plt.title('EVOLUCIÓN DEL NÚMERO DE EJECUCIONES SEGÚN MÉTODO DE EJECUCIÓN ENTRE 1976 Y 2016 \n', fontsize=18)
sns.set_context('paper', rc={'lines.linewidth':2.15})
plt.ylabel('Nº de ejecuciones \n', fontsize=16)
plt.xlabel('Año \n', fontsize=16)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
plt.legend(('Silla eléctrica', 'Cámara de gas', 'Inyección letal'), fontsize=14)
plt.savefig('ex_time_methods.png')
