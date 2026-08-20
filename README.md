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

### Render local

```bash
quarto render          # genera el sitio en docs/
quarto preview         # vista previa local
```

### Despliegue manual a GitHub Pages (gh-pages)

El sitio se publica desde la rama `gh-pages` (el directorio `docs/` no se versiona en `main`). El despliegue es **manual y deliberado**, sin automatizaciones:

```bash
# 1. Renderizar el sitio (con Python y R disponibles)
quarto render

# 2. Preparar la rama gh-pages con la salida
git worktree add gh-pages-build gh-pages
rm -rf gh-pages-build/*          # limpiar la salida anterior
cp -r docs/* gh-pages-build/

# 3. Confirmar los cambios y publicar
cd gh-pages-build
git add -A
git commit -m "docs: publicar sitio"
git push origin gh-pages
cd ..
git worktree remove gh-pages-build

# 4. (Opcional) volver a main
git checkout main
```

> **Alternativa más simple** (equivalente): clonar la rama `gh-pages` en una carpeta aparte (`git clone -b gh-pages <url> sitio-publicado`), copiar el contenido de `docs/` allí y hacer commit+push desde esa carpeta.

> **Recordatorio:** antes de publicar, verifique el render local sin errores y revise que los enlaces de los índices apunten a archivos existentes (ver `CONTRIBUTING.md`).

## Contribuir

Lea [`CONTRIBUTING.md`](CONTRIBUTING.md) antes de agregar o modificar recursos.
