# Plan de Mejora de Arquitectura — courseware-eng

> Documento de diagnóstico y plan de corrección para el repositorio de documentación de cursos de ingeniería (programación, instrumentación, automatización industrial y documentación por código), construido en Markdown/Quarto con ejecución de código Python y R, y desplegado con GitHub Pages.

**Fecha:** 2026-08-20 · **Alcance:** arquitectura, reproducibilidad y mantenibilidad del repositorio.

---

## 1. Estado actual (diagnóstico con evidencia)

### 1.1 Lo que funciona bien (conservar)

| Práctica | Evidencia | Por qué es buena |
|---|---|---|
| `_freeze` versionado + `freeze: auto` | 91 archivos de `_freeze/` en git | Los resultados de ejecución de chunks se cachean: builds reproducibles y rápidos sin re-ejecutar código |
| `renv.lock` presente | 35 paquetes R, R 4.5.2 | Intención de reproducibilidad del lado R |
| `requirements.txt` presente | 109 paquetes | Intención de reproducibilidad del lado Python |
| Taxonomía de carpetas clara | `guides/` `slides/` `labs/` + `assets/` por curso | Navegación intuitiva por tipo de recurso |
| Nomenclatura consistente | `instrumentation_01_*`, `programming_0X_*`, `vscode_*_install` | Orden natural y prefijos por curso/tema |
| `_metadata.yml` compartido por curso de slides | `slides/*/slides/_metadata.yml` | Formato RevealJS centralizado (TOC, footer, navegación) |
| `embed-resources: true` | `_quarto.yml` | HTML autocontenido para GitHub Pages |
| Plantillas conceptuales | `templates/_*.qmd` | Intención de reutilizar estructura |
| Licencia y README | `LICENSE`, `README.md` | Base mínima de proyecto público |

### 1.2 Problemas encontrados (corregir)

**A. Enlaces e índices (ya corregido en esta sesión):**
1. La tarjeta "Configuración de un controlador PID" del índice de Automatización apuntaba a `codesys_install.qmd` en lugar de `codesys_factoryio_pid.qmd`.
2. Índice de Documentation sin enlaces a `vscode_slidev_install.qmd` ni `vscode_python_install.qmd` (este último estaba huérfano y además enlazado desde el índice de Programming con ruta inexistente → 404).
3. `git_ros_wsl2.qmd`, `ros2_basics_level_1/2/3.qmd`, `tgs_procedure_v02.qmd`, `slides/instrumentation_08_industrial_diagrams.qmd` sin enlace en sus índices.
4. `guides/index.qmd` no enlazaba a `tgs/`; `info/about.qmd` era huérfano (no en navbar).
5. `slides/index.qmd` tenía un div `.grid` mal anidado (`:::` en lugar de `::::`).

**B. Sintaxis de otros ecosistemas filtrada a Quarto (ya corregido):**
6. `[TOC]` (extensión Markdown All in One de VSCode) en 8 guías → se renderizaba como texto literal.
7. `!!! Nota` (admonición de MkDocs) en `vscode_workspace_extensions.qmd` → se renderizaba como texto literal.

**C. Contenido (parcialmente corregido):**
8. `instrumentation_05_rlc_circuit.qmd` titulada "Practica de Circuitos DC" (copia de la práctica 02) siendo una práctica RLC.
9. Caracteres Unicode invisibles (zero-width) en `instrumentation_06_ac_circuits.qmd` que rompían fórmulas LaTeX; error matemático $ω = 2f$ (debe ser $2πf$); fórmulas de frecuencia de corte mutiladas (`fc=12RC`).
10. Encabezados vacíos (`### `) en `instrumentation_02_dc_circuits.qmd` → entradas TOC vacías.
11. `git_ros_wsl2.qmd` era un volcado de respuesta de chatbot en inglés (sin título, sin estructura, terminaba con una pregunta al usuario).
12. Callouts "Placeholder:" (diagramas pendientes) en `instrumentation_07_sensors_analogWrite.qmd`; inconsistencia de pines del HC-SR04 entre texto (Trigger 12/Echo 11) y código (pin 13).
13. Duplicación: sección "Instalación de Visual Studio Code" duplicada en `vscode_latex_setup.qmd` y `vscode_python_install.qmd`.

**D. Arquitectura y reproducción (pendiente de corrección — fases P1-P3):**
14. **`renv.lock` sin scaffolding**: no existen `renv/` ni `.Rprofile`, por lo que `renv::restore()` no puede reproducir el entorno R. El lockfile es un snapshot decorativo.
15. **`requirements.txt` es un volcado de `pip freeze`** (109 paquetes) que incluye todo JupyterLab/Notebook: no distingue dependencias de ejecución vs. herramientas de desarrollo, y no declara la versión de Python.
16. **Sin CI/CD**: no hay GitHub Actions; el deploy a `gh-pages` es manual. No hay validación automática de enlaces ni del render.
17. **`output-dir: docs` pero `/docs` está en `.gitignore`**: la salida del render nunca se versiona en `main`; el flujo de deploy depende de la rama `gh-pages` mantenida a mano.
18. **`_freeze/site_libs/` versionado** (85 archivos de revealjs/bootstrap): artefactos de build mezclados con el caché de ejecución.
19. **Rutas de activos incoherentes**: `vscode_python_install.qmd` (en `guides/documentation/`) referenciaba imágenes en `guides/programming/assets/`; varias guías usan rutas redundantes tipo `../automation/assets/...`.
20. **Imágenes duplicadas**: 2 pares con contenido idéntico (`codesys_factoryio_opcua/01.png == codesys_install/15.png`, etc.).
21. **Archivos vacíos/esqueletos**: `templates/_*.qmd` (3 archivos de 0 bytes), `ros2_basics_level_1/2/3.qmd` (0 bytes), `ros2_basics_install.qmd` (solo título), `labs/instrumentation_08_actuators_diagrams.qmd` (solo encabezados), slides de instrumentación 06/07 (solo títulos) y 08 (solo YAML).
22. **`utils/` con código muerto**: `export_diagrams.py` y `export_all_diagrams.py` con rutas Windows hardcodeadas (`C:\Program Files\draw.io\...`) hacia archivos que no existen en el repo; `pre-render`/`post-render` comentados en `_quarto.yml`.
23. **Metadatos genéricos**: título "Mi Documentación", sin `lang`, sin página "Acerca de" navegable (corregido en esta sesión: título, `lang: es`, navbar con "Acerca de").
24. **`.gitignore` inflado**: plantilla genérica de Python con entradas irrelevantes; sin `.DS_Store`, sin `renv/`, sin `*.Rproj.user`.
25. **Textos alternativos de imagen = nombre de archivo** y guías compuestas solo de imágenes sin texto descriptivo (codesys_install, factoryio_install, codesys_modbus, vscode_git_install) — accesibilidad y mantenibilidad limitadas.

---

## 2. Metodología propuesta y justificación

El repositorio es **material didáctico publicado como sitio web técnico**. Para su arquitectura se propone la combinación de tres marcos complementarios:

### 2.1 Diátaxis (organización del contenido)
[Diátaxis](https://diataxis.fr/) clasifica la documentación por la *intención del lector*:

| Cuadrante | Intención | Recurso del repositorio |
|---|---|---|
| **Tutoriales** (aprender) | Estudiante que sigue pasos guiados | Guías de instalación y configuración (`guides/*_install`, `*_setup`) |
| **Guías de cómo hacer** (tareas) | Estudiante que resuelve una tarea concreta | Guías de configuración (OPC-UA, Modbus, PID, GitHub en WSL2) |
| **Prácticas** (hacer) | Estudiante que ejecuta un laboratorio | `labs/instrumentation/*` |
| **Explicación** (entender) | Estudiante que busca contexto | `slides/*` (material de clase) y fundamentos teóricos de las prácticas |

**Justificación:** la estructura actual (`guides`/`slides`/`labs`) ya se aproxima a Diátaxis; formalizarlo da criterio para decidir *dónde* vive cada documento nuevo y qué nivel de detalle debe tener, evitando que las guías se conviertan en volcados de chat (caso `git_ros_wsl2`).

### 2.2 Docs-as-Code (gobernanza del repositorio)
El propio curso enseña "documentación por código": el repositorio debe practicar lo que predica.

- **Convenciones**: frontmatter YAML obligatorio (`title`, `description`), un H1 por archivo, jerarquía sin saltos, rutas relativas canónicas (`assets/...`).
- **Validación automática**: lint de enlaces y estructura en CI (ver P2).
- **Revisión**: los cambios de contenido pasan por PR (branch + merge), no commits directos a `main`.
- **Versionado de dependencias**: `renv.lock` (R) y `requirements.txt` curado (Python) son *código* y se mantienen con intención.

### 2.3 Reproducibilidad pragmática (ejecución de código)
Las páginas ejecutan Python (matplotlib/schemdraw) y R (reticulate/tikz). Principios:

- **Kernels explícitos y documentados**: se declara qué se necesita (Python 3.11 + paquetes del `requirements.txt` curado; R 4.5 + renv).
- **Freeze como contrato**: `_freeze` versionado es correcto; solo se re-ejecuta cuando el código cambia (`freeze: auto`). La regla es *no forzar re-ejecución masiva*.
- **Entorno reproducible sin fricción**: `renv::restore()` (R) y `pip install -r requirements.txt` (Python) deben funcionar en una máquina limpia; hoy no ocurre (problema 14).

### 2.4 Criterio de diseño transversal
- **Una fuente de verdad**: cada software tiene UNA guía de instalación; las demás la referencian (ya aplicado con `vscode_install.qmd`).
- **Nada de código muerto**: archivos vacíos o esqueletos se completan, se marcan explícitamente "Próximamente" en los índices, o se eliminan.
- **Assets junto al curso que los usa**, con nombres semánticos (`assets/images/<recurso>/NN.png`).
- **CI como red de seguridad**: el sitio debe poder construirse y validarse sin intervención manual.

---

## 3. Arquitectura objetivo

```
courseware-eng/
├── _quarto.yml                  # config central (lang es, navbar, sidebar, freeze)
├── index.qmd                    # portada
├── README.md                    # propósito + cadena de herramientas + cómo renderizar
├── guides/                      # TUTORIALES + GUÍAS (Diátaxis)
│   ├── index.qmd
│   ├── automation/              #   codesys_install, factoryio_install (instalación)
│   │   └── ...                  #   opcua, modbus, pid (configuración → referencian instalación)
│   ├── documentation/           #   vscode_install, vscode_git_install, vscode_quarto_install,
│   │   └── ...                  #   vscode_slidev_install, vscode_latex_setup, vscode_md_setup, ...
│   ├── programming/             #   vscode_python_install, git_ros_wsl2, transfer, shortcuts, utils
│   ├── robotics/                #   ros2_basics_install + niveles 1-3 (completar)
│   └── tgs/                     #   procedimientos académicos
├── slides/                      # EXPLICACIÓN (material de clase, RevealJS)
│   ├── programming/slides/      #   _metadata.yml compartido
│   └── instrumentation/slides/
├── labs/                        # PRÁCTICAS (laboratorio y simulación)
│   └── instrumentation/
├── info/about.qmd               # linked en navbar
├── templates/                   # plantillas RELLENAS o eliminadas (hoy: 0 bytes)
├── utils/                       # scripts funcionales o eliminados (hoy: código muerto)
├── requirements.txt             # curado: solo dependencias de ejecución
├── renv.lock + renv/ + .Rprofile # scaffolding renv REAL
├── .github/workflows/render.yml # CI: render + link check + deploy gh-pages
└── _freeze/                     # solo execute-results/figure-* (site_libs → .gitignore)
```

**Regla de oro:** cada recurso del sitio es alcanzable desde exactamente un índice de curso, y cada guía de instalación es un archivo único referenciado por las guías de configuración.

---

## 4. Fases de implementación

### P0 — Correcciones inmediatas (ya ejecutadas en esta sesión)
- [x] Índices: enlaces corregidos/agregados (PID, slidev, python→programming, git_ros_wsl2, niveles ROS2, TGS v2, TGS en guides/, slides 08, about en navbar).
- [x] `[TOC]` y `!!! Nota` eliminados (sintaxis no-Quarto).
- [x] Guías de instalación separadas: creada `vscode_install.qmd`; `vscode_latex_setup` y `vscode_python_install` la referencian (eliminada duplicación).
- [x] Estructura: frontmatter YAML en guías tocadas, jerarquías H1→H2→H3, encabezados vacíos eliminados, caracteres invisibles eliminados, fórmulas corregidas, título RLC corregido, `git_ros_wsl2` reescrito como guía en español.
- [x] `_quarto.yml`: título del sitio, `lang: es`, navbar con "Acerca de".
- [x] Render de validación: 56/57 páginas OK (2 dependen de R), **0 enlaces rotos**, 0 imágenes faltantes.

### P1 — Reproducibilidad (hacer que el entorno funcione en máquina limpia)
- [ ] **R**: inicializar renv real (`renv::init()`), regenerar `renv.lock`, añadir `.Rprofile` y `.gitignore` para `renv/library/`. Verificar `renv::restore()` en una máquina limpia.
- [ ] **Python**: reducir `requirements.txt` a dependencias de ejecución: `jupyter` (o `ipykernel`), `numpy`, `pandas`, `matplotlib`, `schemdraw`. Documentar la versión de Python (`.python-version` o nota en README). Eliminar el resto del volcado de freeze.
- [ ] **Rutas frágiles**: `use_virtualenv("../../../.venv", required = TRUE)` en `instrumentation_01_intro.qmd` depende de la ruta relativa; documentar la estructura esperada o parametrizar (p. ej. `.Renviron` con `RETICULATE_PYTHON`).
- [ ] **Verificación**: en una máquina con R + Python, `quarto render` completo sin errores (hoy los chunks `{r}` y `{python}` de los archivos modificados re-ejecutan — correcto con freeze:auto).

### P2 — CI/CD y validación automática
- [ ] Crear `.github/workflows/render.yml`:
  1. `quarto render` (con R + Python instalados vía `r-lib/actions/setup-r`, `renv::restore()`, y setup-python + `pip install -r requirements.txt`).
  2. **Link check** de `docs/` (p. ej. `lychee` o `htmltest`): 0 enlaces rotos.
  3. Deploy a `gh-pages` con `peaceiris/actions-gh-pages` (o `quarto publish gh-pages`).
- [ ] Decidir el flujo de salida: mantener `output-dir: docs` (gh-pages branch) o cambiar a `_site` + `actions/configure-pages`. Recomendación: **gh-pages branch + workflow**, dejando `main` limpia de artefactos.
- [ ] Añadir `.github/workflows/check.yml` para PRs: render + link check (sin deploy) como gate de revisión.
- [ ] `.gitignore`: añadir `_freeze/site_libs/`, `.DS_Store`, `renv/library/`, `*.Rproj.user`; depurar entradas irrelevantes de la plantilla Python.

### P3 — Contenido pendiente (completar o eliminar)
- [ ] `ros2_basics_install.qmd` (solo título) y `ros2_basics_level_1/2/3.qmd` (0 bytes): redactar contenido (el autor ya domina ROS2 Jazzy en su entorno) o marcarlas explícitamente "Próximamente" en el índice (ya enlazadas con 🚧).
- [ ] `labs/instrumentation_08_actuators_diagrams.qmd`: redactar (esqueleto con secciones).
- [ ] Slides de instrumentación 06 (Sensores) y 07 (Actuadores): redactar contenido bajo los títulos existentes; 08 (Diagramas Industriales): crear contenido o eliminar.
- [ ] `templates/_*.qmd`: rellenar con plantillas funcionales (estructura de guía, práctica y slide) o eliminar la carpeta.
- [ ] `utils/export_diagrams.py` / `export_all_diagrams.py`: parametrizar (rutas relativas, sin dependencia de Windows), eliminar el código muerto, o retirar los archivos y el `pre-render` comentado.
- [ ] Guías solo-imagen (codesys_install, factoryio_install, codesys_modbus, vscode_git_install): añadir texto descriptivo por paso y `alt` semántico en las imágenes.
- [ ] Eliminar imágenes duplicadas (`codesys_factoryio_opcua/01.png==codesys_install/15.png`, `02==16`) y las imágenes huérfanas de `vscode_python_install` (07–14) que quedaron sin uso tras la extracción de VSCode.

### P4 — Estandarización y mantenimiento
- [ ] Política de estilo (para incluir en `CONTRIBUTING.md` o plantilla):
  - Frontmatter YAML obligatorio: `title` + `description`.
  - Un solo H1 por archivo (en frontmatter); jerarquía sin saltos (H2→H3, nunca H2→H4).
  - Rutas de imagen canónicas `assets/images/<recurso>/...` (sin `../` redundantes).
  - Sin sintaxis de otros ecosistemas (`[TOC]`, `!!!`, admoniciones de MkDocs).
  - Idiomas: español por defecto; el inglés solo en extractos citados.
- [ ] Renombrar `vscode_shorcuts.qmd` → `vscode_shortcuts.qmd` (typo histórico) con `git mv` y actualizar índice.
- [ ] Revisar `search.json`/metadatos del sitio (fecha de última actualización, autor) para una página de "Acerca de" más rica.
- [ ] Auditoría periódica (cada N meses o antes de cada convocatoria): repetir el script de chequeo de enlaces/estructura incluido en esta sesión.

---

## 5. Métricas de éxito

| Métrica | Objetivo |
|---|---|
| Enlaces internos rotos en el sitio renderizado | **0** |
| Archivos sin frontmatter YAML | **0** (estándar P4) |
| Guías de instalación duplicadas | **0** (una fuente de verdad por software) |
| `quarto render` completo en CI | **verde en cada PR** |
| `renv::restore()` + `pip install -r` en máquina limpia | **sin errores** |
| Archivos vacíos/esqueletos | **0** (completados, marcados o eliminados) |
| `_freeze/site_libs/` versionado | **no** (gitignored) |

---

## 6. Resumen ejecutivo

El repositorio tiene una base sólida (taxonomía clara, freeze versionado, intenciones de reproducibilidad) pero arrastra deuda técnica de "documento en evolución": sintaxis de otros ecosistemas, enlaces rotos en índices, duplicación de guías de instalación, archivos vacíos y un pipeline de despliegue manual sin validación. La corrección se organiza en 4 fases: **P0** (ya ejecutada, validada con render y 0 enlaces rotos), **P1** reproducibilidad real (renv funcional + requirements curado), **P2** CI/CD con link check y deploy automático, **P3** completar/eliminar contenido pendiente, **P4** estándares de estilo y mantenimiento. La metodología (Diátaxis + Docs-as-Code + reproducibilidad pragmática) garantiza que las decisiones de estructura respondan a la intención del lector y a las buenas prácticas que el propio repositorio enseña.
