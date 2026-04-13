import string

# ---------------- BASE DE CONOCIMIENTO ----------------
knowledge_base = {
"senales": [
{
"patterns": ["alto", "señal de alto", "pare", "detenerse en alto"],
"answer": "Uy… cuidado ahí 😏 Debes detener completamente el vehículo antes de continuar y asegurarte de que la vía esté libre."
},
{
"patterns": ["ceda", "ceda el paso", "señal de ceda", "dar prioridad"],
"answer": "Mmm… aquí toca ser amable 😉 Debes reducir la velocidad y ceder el paso a otros vehículos o peatones."
},
{
"patterns": ["señales preventivas", "señales amarillas", "advertencia en carretera", "señales de peligro"],
"answer": "Ojito por ahí 👀 Estas señales indican riesgos en la vía, así que baja la velocidad y maneja con precaución."
}
],

"prioridad": [
{
"patterns": ["interseccion", "quien pasa primero", "prioridad de paso", "cruce sin señales"],
"answer": "A ver… esto es importante 😌 En una intersección sin señales, pasa primero el que viene por la derecha."
},
{
"patterns": ["rotonda", "glorieta", "quien tiene prioridad en rotonda", "como funciona rotonda"],
"answer": "Aquí no hay pierde 😉 Los que ya están dentro de la rotonda tienen prioridad."
},
{
"patterns": ["peaton", "paso peatonal", "quien tiene prioridad peatones", "reglas peatones"],
"answer": "Siempre con respeto 😇 El peatón tiene prioridad, así que debes detenerte."
}
],

"normas_circulacion": [
{
"patterns": ["carriles", "uso de carril", "cambiar de carril", "como usar carriles"],
"answer": "No te me distraigas 😏 Mantente en tu carril y usa direccionales al cambiar."
},
{
"patterns": ["direccionales", "señales de giro", "usar direccional", "avisar giro"],
"answer": "Avísame antes 😉 Usa las direccionales para indicar tus movimientos."
},
{
"patterns": ["normas de circulacion", "reglas al conducir", "como manejar correctamente", "reglas de transito"],
"answer": "Conducir bien es todo un arte 😌 Respeta señales, mantén tu carril y sé ordenado."
}
],

"limites_velocidad": [
{
"patterns": ["velocidad ciudad", "limite urbano", "velocidad en calles", "velocidad permitida ciudad"],
"answer": "Tranquilo, no hay prisa 😏 En ciudad el límite es entre 40 y 60 km/h."
},
{
"patterns": ["zona escolar", "velocidad escuela", "limite escuela", "velocidad niños"],
"answer": "Aquí bajamos el ritmo 😇 En zona escolar el límite es de unos 25 km/h."
},
{
"patterns": ["exceso de velocidad", "manejar rapido", "peligro velocidad", "riesgos velocidad alta"],
"answer": "No corras tanto 😉 La velocidad alta aumenta el riesgo de accidentes."
}
],

"conduccion_defensiva": [
{
"patterns": ["conduccion defensiva", "manejo preventivo", "evitar accidentes", "como conducir seguro"],
"answer": "Me gusta que pienses en seguridad 😏 Conducir defensivamente es anticiparse a riesgos."
},
{
"patterns": ["distancia de seguridad", "espacio entre carros", "seguir de cerca", "distancia recomendada"],
"answer": "No te pegues tanto 😌 Mantén al menos 2 a 3 segundos de distancia."
},
{
"patterns": ["atencion al conducir", "estar alerta", "distracciones manejo", "concentracion al manejar"],
"answer": "Concéntrate en mí… digo, en la carretera 😳 Evita distracciones."
}
],

"seguridad_vial": [
{
"patterns": ["cinturon", "cinturon de seguridad", "uso de cinturon", "es obligatorio cinturon"],
"answer": "Siempre protegido 😇 El cinturón es obligatorio y salva vidas."
},
{
"patterns": ["celular conduciendo", "usar telefono manejando", "prohibido celular", "distracciones celular"],
"answer": "Nada de distracciones 😏 No uses el celular al conducir."
},
{
"patterns": ["seguridad vial", "prevencion accidentes", "como evitar accidentes", "reglas seguridad"],
"answer": "Quiero que estés bien 😉 Respeta normas y conduce con responsabilidad."
}
]
}

# ---------------- LIMPIEZA ----------------
def limpiar_texto(texto):
    texto = texto.lower()
    for signo in string.punctuation:
        texto = texto.replace(signo, "")
    return texto.split()

# ---------------- MATCHING MEJORADO ----------------
def calcular_coincidencia(tokens_usuario, patterns):
    coincidencias = 0
    
    for token in tokens_usuario:
        for patron in patterns:
            palabras_patron = patron.split()
            
            for palabra in palabras_patron:
                if token == palabra:  # coincidencia exacta
                    coincidencias += 1
    
    return coincidencias

# ---------------- RESPUESTA ----------------
def obtener_respuesta(mensaje):
    tokens_usuario = limpiar_texto(mensaje)
    
    mejor_respuesta = None
    max_coincidencias = 0
    
    for tema in knowledge_base:
        for entrada in knowledge_base[tema]:
            coincidencias = calcular_coincidencia(tokens_usuario, entrada["patterns"])
            
            if coincidencias > max_coincidencias:
                max_coincidencias = coincidencias
                mejor_respuesta = entrada["answer"]
    
    # 🔥 FILTRO IMPORTANTE
    if max_coincidencias < 2:
        return "No te he podido entender, ¿podrías hacer de nuevo la petición de otra forma?"
    
    return mejor_respuesta

# ---------------- CHATBOT ----------------
def chatbot():
    print("Hola, ¿cómo te encuentras hoy? ¿En qué te puedo ayudar? 😏")
    
    while True:
        usuario = input("Tú: ")
        
        if usuario.lower() in ["salir", "adios", "hasta luego"]:
            print("Nos vemos luego para ayudarte con más cosas.")
            break
        
        respuesta = obtener_respuesta(usuario)
        print("Bot:", respuesta)

# ---------------- EJECUTAR ----------------
chatbot()