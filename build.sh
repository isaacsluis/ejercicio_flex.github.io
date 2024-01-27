# Activar el entorno virtual en PowerShell
../AmbientesReflex/css/Scripts/Activate

# Actualizar pip
../AmbientesReflex/css/Scripts/pip install --upgrade pip

# Instalar requisitos
../AmbientesReflex/css/Scripts/pip install -r requirements.txt

# Iniciar reflex
reflex init

# Exportar solo el frontend con reflex
reflex export --frontend-only

# Eliminar el directorio 'public'
Remove-Item -Recurse -Force public

# Descomprimir 'frontend.zip' en el directorio 'public'
Expand-Archive -Path frontend.zip -DestinationPath public -Force

# Eliminar 'frontend.zip'
Remove-Item -Path frontend.zip -Force

# Desactivar el entorno virtual
deactivate
