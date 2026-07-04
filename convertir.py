import json
import yaml

# Leer el archivo JSON
with open("datos.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

# Agregar un nuevo puerto
datos["puertos"].append(4)

# Guardar el JSON modificado
with open("datos_modificado.json", "w", encoding="utf-8") as archivo:
    json.dump(datos, archivo, indent=4)

# Convertir a YAML
with open("datos.yaml", "w", encoding="utf-8") as archivo:
    yaml.dump(datos, archivo, sort_keys=False, allow_unicode=True)

print("Archivos generados correctamente.")