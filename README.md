# courseware-eng

Repositorio con documentación, guías de laboratorio y presentaciones de cursos de ingeniería: programación en Python, instrumentación industrial, automatización y documentación por código.

Sitio publicado en: https://kijusa94.github.io/courseware-eng/

## Estructura

- `guides/` — Guías paso a paso (instalación y configuración de herramientas).
- `slides/` — Presentaciones de clase (RevealJS).
- `labs/` — Prácticas de laboratorio y simulación.
- `info/about.qmd` — Información del sitio.
- `templates/` — Plantillas para nuevos documentos.
- `PLAN_ARQUITECTURA.md` — Diagnóstico y plan de mejora de la arquitectura del repositorio.

## Requerimientos para renderizar localmente

- [Quarto](https://quarto.org/) ≥ 1.4
- **Python** ≥ 3.10 con `ipykernel`, `numpy`, `pandas`, `matplotlib`, `schemdraw`
  (ver `requirements.txt`)
- **R** ≥ 4.4 con los paquetes de `renv.lock` (reticulate, knitr, etc.); restaurar con `renv::restore()`

## Render y despliegue

```bash
quarto render          # genera el sitio en docs/
quarto preview         # vista previa local
```

El sitio se despliega en GitHub Pages desde la rama `gh-pages` (el directorio `docs/` no se versiona en `main`).
