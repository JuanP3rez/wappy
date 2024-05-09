import argparse # Importar las bibliotecas necesarias
import colorama
from colorama import Fore as c_fore
from Wappalyzer import Wappalyzer, WebPage

# Configurar el analizador de argumentos
parser = argparse.ArgumentParser(description="analiza sitio web.")

# Agregar argumento para la URL del sitio web
parser.add_argument('-U', '--url', help="La url de la web a analizar.", required=True)

# Agregar argumento para el nombre del archivo de salida
parser.add_argument('-O', '--output', help="nombre del archivo donde se almacenara el resultado", required=False)

# Analizar los argumentos de la línea de comandos
args = parser.parse_args()

# Crear una nueva página web a partir de la URL proporcionada
webpage = WebPage.new_from_url(args.url)
# Obtener la última versión de Wappalyzer
wappalyzer = Wappalyzer.latest()
# Analizar la página web y obtener una lista de las tecnologías utilizadas
results = list(wappalyzer.analyze(webpage))
# Obtener un diccionario de las tecnologías y sus versiones
versiones = wappalyzer.analyze_with_versions_and_categories(webpage)

# Inicializar colorama
colorama.init()

# Iterar sobre las tecnologías y sus versiones
for tecnologia, detalles in versiones.items():
    # Obtener la versión de la tecnología, si está disponible
	version = detalles['versions'][0] if detalles['versions'] else ' '
    # Si se proporcionó un archivo de salida, escribir los resultados en el archivo
	if args.output is not None:
		with open(args.output, "a") as abierto:
			abierto.write(tecnologia + " " +  version + "\n")
    # Imprimir los resultados en la consola
	print(c_fore.BLUE + "Tecnologia : " + colorama.Style.RESET_ALL + c_fore.YELLOW + tecnologia + " " + colorama.Style.RESET_ALL + " Version : " + c_fore.RED + " " + version + colorama.Style.RESET_ALL)

