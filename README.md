# Bot de Discord - PokéBot

PokéBot es un bot de Discord desarrollado en Python utilizando `discord.py`. Permite obtener imágenes de Pokémon desde la PokéAPI y eliminar mensajes en un canal.

## 🚀 Funcionalidades

### 📌 Comandos disponibles

- `$poke <nombre_del_pokemon>`  
  Muestra la imagen del Pokémon solicitado desde la PokéAPI.  
  - Ejemplo: `$poke pikachu`

- `$limpiar`  
  Elimina todos los mensajes del canal donde se ejecuta el comando.  
  - Muestra el mensaje **"Mensajes eliminados"** y lo borra en 3 segundos.

## 🛠 Instalación

### 🔹 1. Clonar el repositorio  
```bash
git clone https://github.com/Diego-Benitez/PokeBot.git

🔹 2. Crear un entorno virtual e instalar dependencias
python -m venv venv
source venv/bin/activate   # En Linux/macOS
venv\Scripts\activate      # En Windows
pip install -r requirements.txt


🔹 3. Configurar el archivo keys.py
TOKEN = "tu_token_aqui"


🔹 4. Ejecutar el bot
python main.py


🔗 Requisitos
Este bot usa las siguientes librerías:

discord.py
requests
Las dependencias completas están en requirements.txt.

📌 Notas
Debes habilitar la intención MESSAGE CONTENT en el portal de Discord Developer.
No compartas tu token de bot públicamente.
