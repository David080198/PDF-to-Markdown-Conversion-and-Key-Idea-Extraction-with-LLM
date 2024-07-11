#!/usr/bin/env python
# coding: utf-8

# In[11]:


import json

# Ruta del archivo JSON
ruta_archivo = "F:/nuevo_conocimiento/Alex Project/New_part_project/diccionario_textos.json"

# Abrir el archivo y cargar su contenido como un diccionario
with open(ruta_archivo, 'r', encoding='utf-8') as f:
    contenido_json = json.load(f)

# Ahora, puedes trabajar con el contenido del archivo JSON, que está almacenado en la variable `contenido_json`
# Por ejemplo, puedes imprimirlo
print(contenido_json.keys())
archivos = list(contenido_json.keys())
print(archivos)


# In[12]:


def separar_secciones(inicio,fin,archivo):
    #print(llaves_lista)
    #print(contenido_json[archivo])
    # Títulos de inicio y fin que deseas seleccionar
    titulo_inicio = inicio
    titulo_fin = fin
    contenido = ""
    # Seleccionar el texto entre los títulos de inicio y fin
    texto_seleccionado = {}
    seleccionando = False
    for titulo, contenido in contenido_json[archivo].items():
        if titulo == titulo_inicio:
            seleccionando = True
        elif titulo == titulo_fin:
            seleccionando = False
            break
        if seleccionando:
            #nuevo_contenido = nuevo_contenido + "" contenido
            texto_seleccionado[titulo] = contenido
    
    # Imprimir el texto seleccionado
    #for titulo, contenido in texto_seleccionado.items():
    #    print(f"Título: {titulo}")
    #    print(f"Contenido: {contenido}") 
    #print("************************************************")
    #print(texto_seleccionado)
    return texto_seleccionado


# In[13]:


print(contenido_json['Texto2.pdf'].keys())

contenido_json['Texto2.pdf']['Models']


# In[14]:


llaves_lista = list(contenido_json['Texto0.pdf'].keys())
#print(llaves_lista)
texto0_seleccionado = separar_secciones("3 Our Method","4 Experimental Evaluation",archivos[0])

#print(contenido_json['Texto1.pdf'].keys())
llaves_lista = list(contenido_json['Texto1.pdf'].keys())
#print(print(llaves_lista))
texto1_seleccionado = separar_secciones("3. Methodology","4. Results",archivos[1])
#print(type(texto1_seleccionado))
#print(texto1_seleccionado)

llaves_lista = list(contenido_json['Texto2.pdf'].keys())
#print(print(llaves_lista))
texto2_seleccionado = separar_secciones("3 Methodology","4 Results and Discussion",archivos[2])
#print(archivos[2])
print(type(texto2_seleccionado))
print(texto2_seleccionado)

llaves_lista = list(contenido_json['Texto3.pdf'].keys())
#print(print(llaves_lista))
texto3_seleccionado = separar_secciones("3 Substitution-based in-context example optimization (SICO)","4 Experiments",archivos[3])

#print(type(texto0_seleccionado))
llaves_lista = list(contenido_json['Texto4.pdf'].keys())
#print(print(llaves_lista))
texto4_seleccionado = separar_secciones("3 RADAR: Methodology and Algorithms","4 Experiments",archivos[4])

textos_finales = [texto0_seleccionado,texto1_seleccionado,texto2_seleccionado,texto3_seleccionado,texto4_seleccionado]


# In[15]:


import ollama
from tqdm import tqdm
from IPython.display import clear_output

def modelo(model,text):
    query = "Give the principal ideas about this text, if there are not principal ideas only give that 'no principal ideas detect': " + "'" + text + "'" 
    response = ollama.chat(model=model, messages=[
      {
        'role': 'user',
        'content': query,
        'temperature': 0.75,
        'stream': False
      },
    ])
    print(response['message']['content'])
    respuesta = response['message']['content']
    return respuesta

respuesta_llama_3 = []

def texto_proceso(texto_final):
    respuesta = {}
    for textos in tqdm(texto_final,desc="Secciones procesadas"):
        print(textos)
        contenido = texto_final[textos]
        #print(f"Contenido: {contenido}")
        respuesta[textos] = modelo('mixtral',contenido)
    return respuesta

respuesta = []
j = 0
for text_fuera in tqdm(textos_finales,desc="Progreso_de_textos: "):
    
    print(f"Procesando texto No. {j}")
    respuesta.append(texto_proceso(text_fuera))
    j = j + 1


# In[16]:


print(len(respuesta[0]))


# In[17]:


print((respuesta[0].keys()))


# In[18]:


nombre = "Texto"
k = 0
diccionario = {}
for i in respuesta:
    print(type(i))
    nombre_completo = nombre + "_" + str(k)
    diccionario[nombre_completo] = i
    k= k + 1


# In[19]:


print(diccionario.keys())


# In[20]:


ruta_archivo_json = "F:/nuevo_conocimiento/Alex Project/New_part_project/diccionario_metodologia_mixtral.json"
with open(ruta_archivo_json, 'w', encoding='utf-8') as archivo_json:
    json.dump(diccionario, archivo_json, ensure_ascii=False, indent=4)


# In[ ]:




