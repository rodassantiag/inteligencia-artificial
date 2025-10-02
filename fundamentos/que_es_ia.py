#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
¿Qué es la Inteligencia Artificial?
Ejemplo educativo sobre los conceptos básicos de IA

Autor: Santiago Rodas
Fecha: Octubre 2025
"""

def explicar_ia():
    """
    Función que explica qué es la Inteligencia Artificial
    """
    print("🤖 ¿QUÉ ES LA INTELIGENCIA ARTIFICIAL?\n")
    
    print("La Inteligencia Artificial (IA) es la capacidad de las máquinas")
    print("para realizar tareas que normalmente requieren inteligencia humana.\n")
    
    print("📋 CARACTERÍSTICAS PRINCIPALES:")
    caracteristicas = [
        "Aprendizaje automático a partir de datos",
        "Reconocimiento de patrones",
        "Toma de decisiones",
        "Resolución de problemas",
        "Procesamiento del lenguaje natural",
        "Percepción visual"
    ]
    
    for i, caracteristica in enumerate(caracteristicas, 1):
        print(f"{i}. {caracteristica}")
    
    print("\n🔄 TIPOS DE IA:")
    tipos_ia = {
        "IA Débil (Narrow AI)": "Diseñada para tareas específicas (ej: reconocimiento de voz)",
        "IA General (AGI)": "Capacidad humana en cualquier tarea cognitiva",
        "IA Fuerte (Super AI)": "Supera la inteligencia humana en todos los aspectos"
    }
    
    for tipo, descripcion in tipos_ia.items():
        print(f"• {tipo}: {descripcion}")

def ejemplos_ia_cotidiana():
    """
    Muestra ejemplos de IA en la vida cotidiana
    """
    print("\n🌟 EJEMPLOS DE IA EN LA VIDA COTIDIANA:\n")
    
    ejemplos = [
        "🔍 Motores de búsqueda (Google, Bing)",
        "🎵 Recomendaciones de música (Spotify, YouTube)",
        "📱 Asistentes virtuales (Siri, Alexa, Google Assistant)",
        "🚗 Vehículos autónomos",
        "📧 Filtros de spam en email",
        "📷 Reconocimiento facial en fotos",
        "💬 Traductores automáticos",
        "🏥 Diagnóstico médico asistido",
        "🛒 Sistemas de recomendación (Amazon, Netflix)",
        "🎮 IA en videojuegos"
    ]
    
    for ejemplo in ejemplos:
        print(ejemplo)

def algoritmo_simple_ia():
    """
    Ejemplo simple de un "algoritmo" de IA - clasificación básica
    """
    print("\n🔬 EJEMPLO SIMPLE DE CLASIFICACIÓN (Tipo de IA básica):\n")
    
    # Base de conocimiento simple
    animales_caracteristicas = {
        "perro": ["cuatro patas", "ladra", "mamífero"],
        "gato": ["cuatro patas", "maúlla", "mamífero"],
        "pájaro": ["dos patas", "vuela", "pone huevos"],
        "pez": ["aletas", "nada", "vive en agua"]
    }
    
    def clasificar_animal(caracteristicas_observadas):
        """
        Clasifica un animal basado en características observadas
        """
        mejor_coincidencia = ""
        mayor_puntuacion = 0
        
        for animal, caracteristicas in animales_caracteristicas.items():
            coincidencias = len(set(caracteristicas_observadas) & set(caracteristicas))
            if coincidencias > mayor_puntuacion:
                mayor_puntuacion = coincidencias
                mejor_coincidencia = animal
        
        return mejor_coincidencia, mayor_puntuacion
    
    # Ejemplo de clasificación
    print("Observamos un animal con: ['cuatro patas', 'ladra', 'mamífero']")
    animal, puntuacion = clasificar_animal(["cuatro patas", "ladra", "mamífero"])
    print(f"🎯 Clasificación: {animal} (puntuación: {puntuacion}/3)")
    
    print("\nObservamos un animal con: ['dos patas', 'vuela']")
    animal, puntuacion = clasificar_animal(["dos patas", "vuela"])
    print(f"🎯 Clasificación: {animal} (puntuación: {puntuacion}/3)")

def futuro_ia():
    """
    Perspectivas del futuro de la IA
    """
    print("\n🚀 EL FUTURO DE LA IA:\n")
    
    tendencias = [
        "🧠 Redes neuronales más avanzadas",
        "🤖 Robótica inteligente",
        "🏥 IA en medicina personalizada",
        "🌱 IA para el cambio climático",
        "🎓 Educación personalizada con IA",
        "🏭 Automatización industrial inteligente",
        "🧬 IA en biotecnología",
        "🌐 IA conversacional más natural"
    ]
    
    for tendencia in tendencias:
        print(tendencia)

def main():
    """
    Función principal que ejecuta toda la explicación
    """
    print("="*60)
    print("    INTRODUCCIÓN A LA INTELIGENCIA ARTIFICIAL")
    print("="*60)
    
    explicar_ia()
    ejemplos_ia_cotidiana()
    algoritmo_simple_ia()
    futuro_ia()
    
    print("\n" + "="*60)
    print("¡Gracias por aprender sobre Inteligencia Artificial!")
    print("Visita: https://github.com/rodassantiag/inteligencia-artificial")
    print("="*60)

if __name__ == "__main__":
    main()