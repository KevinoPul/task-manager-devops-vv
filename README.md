# task-manager-devops-vv

## Fallos documentados

Durante el desarrollo del proyecto se identificaron algunos fallos comunes:

- Dependencias no instaladas: se solucionó ejecutando `./scripts/install.sh`.
- Permisos en scripts: se corrigió con `chmod +x scripts/install.sh scripts/run.sh`.
- Error de sintaxis: se validó con `python -m py_compile app.py`.
- Campos vacíos: se agregó una validación para evitar crear tareas sin nombre.
- Pruebas no detectadas: se corrigió configurando correctamente la carpeta `tests`.
- Pipeline CI: se ajustó el archivo `ci.yml` para ejecutar las pruebas correctamente.

Estos fallos fueron documentados para facilitar la revisión, mantenimiento y reproducción del proyecto.
