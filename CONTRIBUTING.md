# Contribuyendo a courseware-eng

Gracias por contribuir a este repositorio de documentación. Estas convenciones mantienen el sitio coherente, reproducible y libre de errores de renderizado.

## Estructura del repositorio

| Carpeta | Contenido | Cuándo crear un archivo aquí |
|---|---|---|
| `guides/<curso>/` | Guías paso a paso (instalación y configuración) | Tutorial o how-to de una herramienta |
| `labs/<curso>/` | Prácticas de laboratorio y simulación | Actividad práctica con objetivos, procedimiento y tablas |
| `slides/<curso>/slides/` | Presentaciones RevealJS de clase | Material de explicación |
| `templates/` | Plantillas para nuevos documentos | Copiar y completar, nunca editar directamente |
| `assets/images/<recurso>/` | Capturas e imágenes de cada recurso | Junto al curso que las usa, numeradas `NN.png` |

## Convenciones obligatorias

1. **Frontmatter YAML** en todo archivo nuevo: `title` y `description` obligatorios.
2. **Un solo H1 por archivo**: el título va en el frontmatter; no repetirlo como `#` en el cuerpo.
3. **Jerarquía sin saltos**: H2 → H3 → H4 en orden; nunca pasar de H2 a H4.
4. **Rutas relativas canónicas**: imágenes en `assets/images/<recurso>/NN.png` referenciadas como `assets/images/...` (sin `../` redundantes).
5. **Alt descriptivo** en todas las imágenes: `![Pasos 1-3 del asistente](...)`, nunca el nombre del archivo.
6. **Sintaxis prohibida** (de otros ecosistemas, se renderiza como texto literal):
   - `[TOC]` (extensión de VSCode) — Quarto genera el TOC automáticamente (`toc: true`).
   - `!!! Nota` (admonición de MkDocs) — usar `::: {.callout-note}`.
7. **Idioma**: español por defecto (el curso es en español); inglés solo en citas o nombres técnicos.
8. **Código en bloques con lenguaje**: ` ```python `, ` ```bash `, ` ```c `, ` ```mermaid ` — nunca bloques sin etiqueta cuando el contenido es código.

## Cómo añadir un recurso nuevo

1. Copie la plantilla correspondiente de `templates/` (`_docs.qmd`, `_lab.qmd` o `_slides.qmd`).
2. Complete el contenido siguiendo las convenciones.
3. Guarde las imágenes en `assets/images/<nombre_recurso>/`.
4. **Registre el recurso en el índice** de su curso (`<curso>/index.qmd`) con una tarjeta en la cuadrícula.
5. Si es una guía de instalación, verifique que sea **la única** para ese software; las demás guías la referencian con un enlace.

## Cómo agregar una guía de instalación

Cada software tiene **una sola** guía de instalación (p. ej. `vscode_install.qmd`). Las guías de configuración no repiten pasos de instalación: enlazan la guía correspondiente, idealmente dentro de un callout de requisitos:

```markdown
::: {.callout-important}
**Requisitos:** tener instalado [Software X](ruta_a_instalacion.qmd).
:::
```

## Validación antes de publicar

1. Renderice el sitio localmente: `quarto render` (requiere Python y R, ver `README.md`).
2. Verifique que no haya errores ni advertencias de render.
3. Revise que los enlaces del índice apunten a archivos existentes.
4. Despliegue siguiendo el procedimiento de **Despliegue manual** del `README.md`.

## Buenas prácticas de contenido

- Las guías **solo-imagen** deben incluir texto descriptivo por paso (accesibilidad y mantenibilidad).
- Marque contenido planificado pero no redactado como **🚧 Próximamente** en el índice, o no lo enlace.
- No versionar artefactos de build: `_freeze/site_libs/`, `*_files/` y `docs/` están en `.gitignore`.
- Antes de un PR grande, ejecute `git diff --stat` y revise que no haya archivos binarios innecesarios.
