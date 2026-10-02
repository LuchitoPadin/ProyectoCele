"""
=============================================================================
PROYECTO: EL RITMO DE VIDA ACELERADO EN LIMA Y SU IMPACTO EN LAS RELACIONES
CURSO: Metodología de la Investigación Social / Comunicación Audiovisual
AUTORES: Celeste Ruiz, Fernanda Reyes, Santiago Tovar, Andree Puente,
         Jonathan Cisneros, Frank Culquipoma.
=============================================================================
Este servidor en Python (Flask) actúa como el núcleo lógico de la landing page.
Está programado con un estilo directo, limpio y accesible para facilitar su
lectura y modificación por parte de estudiantes y docentes de áreas creativas.
"""

from flask import Flask, render_template, jsonify, request
import math

app = Flask(__name__)

# =============================================================================
# BASE DE DATOS DOCUMENTAL Y ACADÉMICA (Extraída del informe)
# =============================================================================

INVESTIGACION = {
    "titulo": "El Ritmo de Vida Acelerado en Lima y su Impacto en las Relaciones Personales",
    "subtitulo": "Un análisis multidimensional desde la comunicación, la sociología urbana y la vida cotidiana",
    "autores": [
        "Celeste Ruiz",
        "Fernanda Reyes",
        "Santiago Tovar",
        "Andree Puente",
        "Jonathan Cisneros",
        "Frank Culquipoma"
    ],
    "filiacion": "Facultad de Ciencias Sociales y Humanidades — Instituto de Educación Superior Toulouse Lautrec",
    "curso": "Metodología de la Investigación Social / Comunicación Audiovisual",
    "año": 2026,
    
    # Métricas y estadísticas clave citadas en el informe
    "metricas_clave": [
        {
            "cifra": "3 a 4 hrs",
            "etiqueta": "Traslado diario promedio",
            "descripcion": "Tiempo perdido en transporte público y congestión en Lima Metropolitana.",
            "fuente": "BCRP (Céspedes-Reynaga, 2025)"
        },
        {
            "cifra": "60%+",
            "etiqueta": "Uso excesivo de pantallas",
            "descripcion": "Universitarios limeños conectados más de 3 horas al día en redes sociales.",
            "fuente": "Salas Blas et al. (2022)"
        },
        {
            "cifra": "+4 hrs",
            "etiqueta": "Brecha de género en cuidado",
            "descripcion": "Carga adicional no remunerada asumida por mujeres en el hogar limeño.",
            "fuente": "INEI (ENUT, 2024)"
        },
        {
            "cifra": "p < .01",
            "etiqueta": "Impacto Spillover",
            "descripcion": "Correlación significativa negativa entre el conflicto trabajo-familia y satisfacción conyugal.",
            "fuente": "Metaanálisis Fellows et al. (2016)"
        }
    ],

    # Crónicas documentales (narrativa audiovisual)
    "cronicas": [
        {
            "id": "transporte",
            "titulo": "El largo viaje de retorno",
            "subtitulo": "La combi como no-lugar y antesala de la fatiga",
            "imagen": "transporte_combi.jpg",
            "cita": "«La prisa constante deteriora el estado de ánimo y elimina los momentos de descanso indispensables, perjudicando la empatía.»",
            "autor_cita": "M. Bustamante (El Comercio, 2026)",
            "relato": (
                "Para millones de limeños, la jornada no concluye al salir del trabajo o la universidad. "
                "Comienza entonces la segunda batalla: dos horas en una combi o en el Metropolitano, entre "
                "bocinazos, frenadas abruptas y el vapor de la garúa sobre las ventanillas. Al llegar a casa, "
                "la energía afectiva se ha evaporado en el asfalto."
            ),
            "enfoque_audiovisual": "Plano medio cerrado, reflejos de luces de freno en el vidrio mojado, sonido diegético de tráfico distante."
        },
        {
            "id": "intimidad",
            "titulo": "La sobremesa interrumpida",
            "subtitulo": "La paradoja de compartir techo en soledad emocional",
            "imagen": "desconexion_hogar.jpg",
            "cita": "«Se puede estar en un entorno concurrido y experimentar simultáneamente una profunda soledad emocional.»",
            "autor_cita": "Salas Blas et al. (2022) / Castillo García (2023)",
            "relato": (
                "La cena ya no convoca al diálogo intrafamiliar de antaño. En lugar de miradas y preguntas sinceras "
                "sobre el día, el resplandor azul de los teléfonos inteligentes ilumina platos que se consumen deprisa. "
                "El fenómeno del 'Spillover' (desborde de la tensión laboral) transforma el hogar en un espacio de silencio "
                "defensivo o reactividad verbal."
            ),
            "enfoque_audiovisual": "Plano general tenue, contraste entre la luz cálida de una lámpara y el brillo frío del smartphone en penumbra."
        },
        {
            "id": "calle",
            "titulo": "La carretilla: afecto y trabajo en la vereda",
            "subtitulo": "La realidad del comercio informal donde el hogar se traslada a la acera",
            "imagen": "trabajo_informal.jpg",
            "cita": "«En el comercio informal, las relaciones afectivas no transcurren fuera del trabajo: se construyen durante la misma jornada.»",
            "autor_cita": "Docuperú ('La Huerta', 2012) & TVPerú (2020)",
            "relato": (
                "En sectores informales, la conciliación entre vida familiar y trabajo no se da a través de políticas corporativas, "
                "sino en la resistencia comunitaria. Las carretilleras y comerciantes ambulantes comparten el espacio de venta "
                "con sus hijos que hacen tareas en cajones de fruta o comen juntos al pie del puesto. El afecto se defiende en la trinchera de la supervivencia."
            ),
            "enfoque_audiovisual": "Plano detalle de manos trabajando sobre el vapor del carbón, niños jugando en un banquillo de plástico."
        }
    ],

    # Los 3 Ejes Estratégicos con las 10 Pautas del informe
    "ejes_estrategicos": [
        {
            "eje": "Eje I: Planificación Intencional del Tiempo Compartido",
            "descripcion": "Frente a la escasez de horas en la metrópoli, el tiempo de calidad se diseña y se defiende como un derecho vincular.",
            "pautas": [
                {
                    "num": "01",
                    "nombre": "Ritualización de micro-momentos",
                    "detalle": "Acordar espacios breves y fijos de interacción diaria (el desayuno compartido, un café de 15 minutos o una pausa en el puesto ambulante)."
                },
                {
                    "num": "02",
                    "nombre": "Reserva intencional de descanso",
                    "detalle": "Bloques inamovibles en días de menor carga comercial dedicados con exclusividad a la pareja, familia o red de amigos."
                },
                {
                    "num": "03",
                    "nombre": "Priorización de presencia activa",
                    "detalle": "La escucha atenta y la mirada directa deben prevalecer sobre la mera coincidencia de cuerpos en la misma habitación."
                }
            ]
        },
        {
            "eje": "Eje II: Autorregulación Emocional y Comunicación Asertiva",
            "descripcion": "Prevenir que el estrés, la contaminación acústica y la frustración del tráfico se derramen en violencia o distanciamiento con los seres queridos.",
            "pautas": [
                {
                    "num": "04",
                    "nombre": "Pausas de descompresión pre-contacto",
                    "detalle": "Tomar de 5 a 10 minutos de transición y silencio antes de entrar a casa o tras cerrar el negocio para soltar la irritabilidad urbana (MINSA, 2024)."
                },
                {
                    "num": "05",
                    "nombre": "Expresión asertiva del agotamiento",
                    "detalle": "Decir 'estoy muy cansado hoy, necesito un momento' en lugar de responder con agresividad o desdén a la demanda afectiva."
                },
                {
                    "num": "06",
                    "nombre": "Práctica de la escucha empática",
                    "detalle": "Validar y contener el relato del otro sin apresurarse a juzgar o comparar niveles de cansancio diario."
                },
                {
                    "num": "07",
                    "nombre": "Manejo preventivo del estrés urbano",
                    "detalle": "Ejercicios de respiración y autorregulación para mitigar los efectos del claxon, el hacinamiento y la prisa colectiva."
                }
            ]
        },
        {
            "eje": "Eje III: Higiene Digital y Trazado de Fronteras Laborales",
            "descripcion": "Recuperar el control de la atención frente a la tiranía de la notificación y la sobreexigencia del multitasking.",
            "pautas": [
                {
                    "num": "08",
                    "nombre": "Zonas y momentos libres de tecnología",
                    "detalle": "Teléfonos guardados o en modo no molestar durante el almuerzo y las charlas íntimas. Detener la atención comercial en momentos familiares."
                },
                {
                    "num": "09",
                    "nombre": "Horarios de cierre productivo",
                    "detalle": "Límite temporal estricto para revisar correos de oficina o dar por concluida la jornada en la calle para retornar al hogar."
                },
                {
                    "num": "10",
                    "nombre": "Protección de las horas de sueño",
                    "detalle": "Salvaguardar el descanso reparador y el ocio como requisitos biológicos e irrenunciables para la sostenibilidad afectiva."
                }
            ]
        }
    ],

    # Referencias bibliográficas completas formateadas en APA 7
    "referencias": [
        {
            "autor": "Arias Gallegos, W. L., & Ceballos Canaza, K. D. (2016)",
            "titulo": "Síndrome de burnout, satisfacción laboral e integración familiar en trabajadores de una tienda por departamento de Arequipa.",
            "fuente": "Illustro, 7, 39–52.",
            "link": "https://doi.org/10.36901/illustro.v7i0.1246"
        },
        {
            "autor": "Błachnio, A., Przepiórka, A., Cudo, A., Kot, P., Sobol, M., & Hou, W. K. (2026)",
            "titulo": "The role of social interactions in the relationship between daily stressful events and well-being: A diary study.",
            "fuente": "European Review of Applied Psychology, 76(3), Article 101162.",
            "link": "https://doi.org/10.1016/j.erap.2026.101162"
        },
        {
            "autor": "Bustamante, M. (2026, 15 de enero)",
            "titulo": "El costo invisible de vivir siempre apurados.",
            "fuente": "El Comercio (Somos).",
            "link": "https://elcomercio.pe/somos/estilo/el-costo-invisible-de-vivir-siempre-apurados-noticia/"
        },
        {
            "autor": "Cassaretto, M., Vilela, P., & Gamarra, L. (2021)",
            "titulo": "Estrés académico en universitarios peruanos: Importancia de las conductas de salud, características sociodemográficas y académicas.",
            "fuente": "Liberabit, 27(2), Article e482.",
            "link": "https://doi.org/10.24265/liberabit.2021.v27n2.07"
        },
        {
            "autor": "Castellanos, R. (2003)",
            "titulo": "El diálogo intrafamiliar y sus transformaciones en la sociedad contemporánea.",
            "fuente": "Editorial Ciencias Sociales.",
            "link": None
        },
        {
            "autor": "Castillo García, J. (2023)",
            "titulo": "Adicción a las redes sociales, rasgos de personalidad y soledad en estudiantes universitarios de Lima Metropolitana.",
            "fuente": "Tesis de licenciatura, Universidad Privada del Norte.",
            "link": "https://repositorio.upn.edu.pe/"
        },
        {
            "autor": "Céspedes-Reynaga, N. (2025)",
            "titulo": "El muy prolongado viaje al trabajo en Perú.",
            "fuente": "Documento de Trabajo N.° 009-2025, Banco Central de Reserva del Perú (BCRP).",
            "link": "https://investigacion.bcrp.gob.pe/es/investigaciones/documentos-de-trabajo/dt-2025/dt-2025-009"
        },
        {
            "autor": "Del Castillo Mory, E., Fuchs Ángeles, R. M., Vera Linares, S., Arizkuren Eleta, A., & Agarwala, T. (2011)",
            "titulo": "Balance trabajo-familia: Cultura, nivel de conflicto y voluntad de permanencia en la empresa.",
            "fuente": "Journal of Business, Universidad del Pacífico, 3(1), 3–14.",
            "link": "https://doi.org/10.21678/jb.2011.41"
        },
        {
            "autor": "Docuperú (2012)",
            "titulo": "La Huerta [Documental participativo].",
            "fuente": "YouTube.",
            "link": "https://www.youtube.com/watch?v=QzdsGLF5p5I"
        },
        {
            "autor": "Fellows, K. J., Chiu, H.-Y., Hill, E. J., & Hawkins, A. J. (2016)",
            "titulo": "Work-family conflict and couple relationship quality: A meta-analytic study.",
            "fuente": "Journal of Family and Economic Issues, 37(4), 509–518.",
            "link": "https://doi.org/10.1007/s10834-015-9450-7"
        },
        {
            "autor": "García Gil, N. C., & Quiñones Pedrozo, W. M. (2022)",
            "titulo": "Habilidades sociales y estrés académico en estudiantes universitarios de Lima Metropolitana.",
            "fuente": "Tesis de licenciatura, Universidad Privada del Norte.",
            "link": "https://repositorio.upn.edu.pe/item/e12f972d-807e-4185-a152-0340cdec6db1"
        },
        {
            "autor": "INEI (2024)",
            "titulo": "Encuesta Nacional de Uso del Tiempo – ENUT 2024.",
            "fuente": "Instituto Nacional de Estadística e Informática, Gobierno del Perú.",
            "link": "https://www.gob.pe/institucion/inei/campa%C3%B1as/99771-resultados-de-la-encuesta-nacional-de-uso-del-tiempo-enut"
        },
        {
            "autor": "Mejía Madrid, R. (2014)",
            "titulo": "La tensión entre el trabajo y la vida familiar.",
            "fuente": "IUS ET VERITAS, 24(49), 190–201.",
            "link": "https://revistas.pucp.edu.pe/index.php/iusetveritas/article/view/13624"
        },
        {
            "autor": "Muccino, G. (Director) (2006)",
            "titulo": "The pursuit of happyness (En busca de la felicidad) [Película].",
            "fuente": "Columbia Pictures.",
            "link": None
        },
        {
            "autor": "Salas Blas, E., Vieira Ipince, C. M., & Manzanares Medina, E. (2022)",
            "titulo": "Adicción a las redes sociales y soledad en estudiantes universitarios limeños.",
            "fuente": "Informació Psicològica, (123), 2–14.",
            "link": "https://doi.org/10.14635/IPSIC.1926"
        },
        {
            "autor": "TVPerú (2020)",
            "titulo": "Sucedió en el Perú: 'Ambulantes en Lima' [Especial documental].",
            "fuente": "YouTube.",
            "link": "https://www.youtube.com/watch?v=r2rwXEcjqa8"
        }
    ]
}


# =============================================================================
# RUTAS DEL SERVIDOR WEB
# =============================================================================

@app.route('/')
def index():
    """
    Ruta principal: Renderiza la landing page inyectando toda la estructura
    conceptual del informe en la plantilla HTML.
    """
    return render_template('index.html', data=INVESTIGACION)


@app.route('/api/investigacion')
def get_investigacion():
    """
    Endpoint API: Devuelve la base de datos completa de la investigación en JSON.
    Permite consumo asíncrono o integración externa.
    """
    return jsonify(INVESTIGACION)


@app.route('/api/calcular-tiempo', methods=['POST'])
def calcular_tiempo():
    """
    Calculadora Sociológica del Tiempo en Lima:
    Recibe las horas diarias que el usuario pasa en tráfico y pantallas,
    y calcula el impacto acumulativo anual en sus relaciones y salud vincular.
    """
    payload = request.get_json() or {}
    
    # Parámetros recibidos con valores por defecto razonables
    horas_transporte = float(payload.get('horas_transporte', 3.0))
    horas_pantalla = float(payload.get('horas_pantalla', 3.5))
    ocupacion = payload.get('ocupacion', 'universitario')
    
    # 260 días laborables / académicos promedio al año
    dias_anuales_activos = 260
    
    total_horas_transporte_anual = horas_transporte * dias_anuales_activos
    dias_completos_perdidos_trafico = round(total_horas_transporte_anual / 24, 1)
    
    # Horas despierto útiles al día (asumiendo 7h de sueño y 9h de estudio/trabajo)
    # Restan 8 horas diarias para vida personal, transporte, aseo y alimentación
    horas_libres_brutas = max(0.0, 17.0 - 9.0) # 8.0 horas
    horas_reales_vinculo = max(0.2, horas_libres_brutas - horas_transporte - (horas_pantalla * 0.6))
    
    # Índice de Riesgo Spillover (0 a 100)
    # A mayor transporte y mayor tiempo en pantalla sin presencia activa, mayor riesgo de reactividad emocional
    factor_transporte = min(50.0, (horas_transporte / 4.5) * 50.0)
    factor_pantalla = min(35.0, (horas_pantalla / 5.0) * 35.0)
    riesgo_spillover = min(98.0, round(factor_transporte + factor_pantalla + 10.0, 1))
    
    # Diagnóstico adaptado
    if riesgo_spillover > 75:
        nivel_alerta = "Crítico: Sobrecarga y desconexión severa"
        diagnostico = (
            f"Estás perdiendo el equivalente a {dias_completos_perdidos_trafico} días enteros al año atrapado "
            "en el transporte limeño. La tensión acumulada tiene una alta probabilidad de desbordarse "
            "(efecto 'Spillover') en irritabilidad o apatía con tu entorno cercano."
        )
        estrategia_sugerida = "Pausa de descompresión pre-contacto (mínimo 10 min de silencio antes de hablar) y rescate de micro-momentos sin celular."
    elif riesgo_spillover > 45:
        nivel_alerta = "Moderado: Desgaste relacional progresivo"
        diagnostico = (
            f"Inviertes aproximadamente {round(total_horas_transporte_anual)} horas al año en traslados. "
            "Tus espacios de conversación tienden a ser funcionales o mediatizados por pantallas."
        )
        estrategia_sugerida = "Establecer la cena o el desayuno como zona libre de notificaciones y agendar un bloque inamovible de descanso en la semana."
    else:
        nivel_alerta = "Bajo: Vínculos protegidos con margen de mejora"
        diagnostico = (
            "Tu distribución temporal preserva un margen saludable de presencia consciente. "
            "Aun así, la inmediatez urbana de Lima exige vigilar la calidad de la escucha activa."
        )
        estrategia_sugerida = "Profundizar en la escucha empática y ritualizar micro-conversaciones de validación mutua."

    return jsonify({
        "horas_transporte_diarias": horas_transporte,
        "dias_perdidos_anual_en_trafico": dias_completos_perdidos_trafico,
        "horas_anuales_en_trafico": round(total_horas_transporte_anual),
        "horas_afectivas_diarias_reales": round(horas_reales_vinculo, 1),
        "riesgo_spillover_porcentaje": riesgo_spillover,
        "nivel_alerta": nivel_alerta,
        "diagnostico": diagnostico,
        "estrategia_sugerida": estrategia_sugerida
    })


if __name__ == '__main__':
    # Ejecución local en modo accesible y puerto estándar 5000
    print("=================================================================")
    print("Iniciando Servidor Web — Landing Page: El Ritmo Acelerado de Lima")
    print("Accede en tu navegador a: http://127.0.0.1:5000")
    print("=================================================================")
    app.run(host='127.0.0.1', port=5000, debug=True)
