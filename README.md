# El Ritmo Acelerado de Lima y su Impacto en las Relaciones Personales
### Un Análisis Multidimensional para Comunicación Audiovisual

Landing page y plataforma documental interactiva basada en el informe académico de investigación social elaborado por **Celeste Ruiz, Fernanda Reyes, Santiago Tovar, Andree Puente, Jonathan Cisneros y Frank Culquipoma** (Universidad de Lima, Facultad de Ciencias Sociales y Humanidades, 2026).

---

## 🎞️ Enfoque Visual y Audiovisual
- **Sensibilidad cinematográfica y documental**: Inspirada en la cinematografía documental peruana contemporánea (*Docuperú*, *Sucedió en el Perú*, "Lima la Gris").
- **Sin estridencias futuristas**: Utiliza una paleta orgánica y humana de asfalto mojado, garúa, neblina costera y el característico alumbrado cálido de sodio limeño.
- **Narrativa visual en 35mm**: Integración de crónicas fotográficas realistas que retratan tres dimensiones clave:
  1. *El transporte público y el viaje de retorno* (la combi como no-lugar y antesala de la fatiga).
  2. *La sobremesa interrumpida y el fenómeno Spillover* (la paradoja de la soledad emocional en el hogar hiperconectado).
  3. *La carretilla y el comercio informal* (donde la subsistencia económica y los afectos familiares conviven en la misma vereda).
- **Paisaje sonoro inmersivo (Web Audio API)**: Sintetizador acústico sutil que recrea el sonido de la garúa costera y el murmullo de baja frecuencia del tráfico metropolitano.

---

## 🛠️ Arquitectura Técnica

### 1. Back-end en Python ([`app.py`](file:///c:/Users/luish/Documents/Trabajo%20cele/app.py))
- Programado en **Flask**, con código directo, comentado y didáctico.
- **Ruta Principal (`/`)**: Renderiza la plantilla Jinja2 inyectando los datos estructurados del informe.
- **API REST (`/api/investigacion`)**: Retorna las estadísticas, crónicas, pautas y referencias bibliográficas en formato JSON estándar.
- **Calculadora Sociológica del Tiempo (`/api/calcular-tiempo`)**: Procesa el impacto cuantitativo del tráfico en Lima (días anuales perdidos en combis/buses), las horas reales de presencia activa y el índice de riesgo de derrame de estrés (*Spillover*).

### 2. Front-end en HTML5 y CSS3 Puro
- **Plantilla ([`templates/index.html`](file:///c:/Users/luish/Documents/Trabajo%20cele/templates/index.html))**: Estructura semántica, accesible, con metadatos y claqueta de autores.
- **Diseño CSS ([`static/css/style.css`](file:///c:/Users/luish/Documents/Trabajo%20cele/static/css/style.css))**:
  - Tipografía editorial (*Newsreader* y *Plus Jakarta Sans*).
  - Micro-interacciones sutiles con aceleración de hardware.
  - Diseño 100% responsivo para móviles, tablets y monitores panorámicos.
  - Textura analógica de grano cinematográfico y sangría francesa para la bibliografía APA 7.
- **Lógica e Interactividad ([`static/js/main.js`](file:///c:/Users/luish/Documents/Trabajo%20cele/static/js/main.js))**:
  - Conexión dinámica vía `fetch()` con el backend de Python.
  - Generador de audio web atmosférico.
  - Buscador reactivo para las referencias bibliográficas APA.

---

## 🚀 Cómo Ejecutar el Proyecto Localmente

1. Abre una terminal en esta carpeta:
   ```powershell
   cd "c:\Users\luish\Documents\Trabajo cele"
   ```

2. Ejecuta el servidor en Python:
   ```powershell
   python app.py
   ```

3. Abre tu navegador web favorito e ingresa a:
   **`http://127.0.0.1:5000`**

---

## 📚 Estructura de Secciones de la Landing Page
1. **Hero**: Portada cinematográfica con créditos de los autores y filiación institucional.
2. **La Metrópoli y la Fricción del Tiempo**: Métricas clave del BCRP (Céspedes-Reynaga, 2025), INEI (ENUT 2024), Salas Blas et al. (2022) y Fellows et al. (2016).
3. **Crónicas de la Desconexión Cotidiana**: Tres historias visuales y fotográficas documentadas.
4. **Dimensiones Invisibles del Desgaste Afectivo**: Soledad social vs. emocional, Spillover conyugal, brecha de género y análisis cinematográfico de *The Pursuit of Happyness* (Muccino, 2006).
5. **Simulador Sociológico de Campo**: Calculadora interactiva que dialoga con Python.
6. **Decálogo de Preservación Vincular**: Las 10 pautas prácticas organizadas en los 3 Ejes Estratégicos del informe.
7. **Archivo Documental y Bibliografía**: Referencias estandarizadas en norma APA 7.ª edición con enlaces activos.
