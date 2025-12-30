# Selenium_Mercado_Libre
Este proyecto es un script de automatización web desarrollado en Python con Selenium que navega en MercadoLibre y extrae información de productos de manera automática. El script realiza las siguientes acciones:
1. Abre MercadoLibre desde un navegador Chrome
2. Selecciona la región México
3. Busca el producto PS5
4. Aplica filtros:
    *Productos nuevos
    *Ubicación local (CDMX)
    +Ordena los resultados por precio: de mayor a menor
5. Obtiene y muestra en consola el top 5 de productos, incluyendo:
    *Nombre del producto
    *Precio

Este proyecto es ideal como ejemplo de:
Web scraping con Selenium
Automatización de navegación y filtros
Uso de WebDriverWait y manejo de elementos dinámicos

## 🚀 Tecnologías utilizadas
- **Python 3.11+**
- **Selenium WebDriver**
- **Google Chrome / ChromeDriver**

## Librerias usadas
- pip install selenium

## 🧩 Instalación
1. Clonar este repositorio:
   - git clone https://github.com/ederhoppe/Selenium_Mercado_Libre.git
   - cd Selenium_Mercado_Libre
   - python main.py
