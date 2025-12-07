# Alexa LoL Meta Assistant

## Integrantes
- Fabricio Daniel Lara Valencia
- Diego Alonso Martin del Campo

## Descripción del Proyecto
Alexa LoL Meta Assistant** es una skill para Amazon Alexa pensada como un **asistente estratégico de League of Legends.  
Permite consultar builds, runas, counters, estadísticas del meta (WR/PR/BR) y recibir consejos estratégicos mediante comandos de voz rápidos, claros y accesibles.

El objetivo es que los jugadores puedan tomar decisiones óptimas durante la fase de selección sin tener que abrir pestañas externas como OP.GG o U.GG.

---

## Objetivo del Proyecto
Brindar a los jugadores de LoL una herramienta auditiva que permita:

- Obtener builds optimizadas del meta actual
- Consultar runas recomendadas
- Identificar matchups favorables y desfavorables
- Conocer estadísticas clave de campeones (winrate, pickrate, banrate)
- Recibir consejos útiles y concisos antes de jugar


---

## Problema que Resuelve

Los jugadores deben alternar entre ventanas o dispositivos para consultar builds y estadísticas durante el draft, lo que consume tiempo y provoca elecciones subóptimas.

La skill resuelve esto mediante:

- Acceso rápido por voz  
- Información condensada  
- Consejos prácticos  

---

## Casos de Uso Principales

- “Alexa, ¿cuál es la mejor build para Jinx?”
- “Alexa, ¿qué runas usa Ahri?”
- “Alexa, ¿contra quién pierde Yasuo?”
- “Alexa, dame un consejo antes de jugar.”
- “Alexa, ¿qué winrate tiene Ekko?”

---

## Requerimientos Funcionales

| ID | Descripción | Actor | Criterio de Aceptación |
|----|-------------|--------|------------------------|
| RF-01 | Consultar build recomendada | Usuario | Alexa devuelve objetos principales y runas |
| RF-02 | Consultar runas | Usuario | Entrega árbol principal, secundario y runas clave |
| RF-03 | Consultar counters/favorables | Usuario | Indica matchups y winrates |
| RF-04 | Consultar WR/PR/BR | Usuario | Respuestas actualizadas |
| RF-05 | Dar consejos estratégicos | Usuario | Consejos claros y accionables |
| RF-06 | Reconocer variaciones de intención | Usuario | Respuestas coherentes |
| RF-07 | Responder < 30 segundos | Usuario | Respuesta corta y clara |
| RF-08 | Consultar cualquier campeón | Usuario | Cobertura total del roster |
| RF-09 | Mantener contexto | Usuario | Recuerda el campeón previo |

---

##  Requerimientos No Funcionales

| ID | Descripción | Prioridad | Criterio |
|----|-------------|-----------|----------|
| RNF-01 | Respuesta del backend < 15s | Media | 95% en < 3s |
| RNF-02 | Código modular y documentado | Alta | Cambios fáciles |
| RNF-03 | Actualización diaria de datos | Alta | Meta < 24h |
| RNF-04 | Respuestas claras auditivamente | Media | Entendibles sin repetir |
| RNF-05 | Mantener coherencia en sesión | Alta | Contexto al 100% |
| RNF-06 | No almacenar datos personales | Alta | Sin riesgos |
| RNF-07 | Manejo de errores robusto | Baja | Se recupera sin colapsar |

---

