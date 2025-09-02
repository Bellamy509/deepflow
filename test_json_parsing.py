#!/usr/bin/env python3
"""
Script de test pour vérifier le parsing JSON côté backend
"""
import json
import requests

def test_json_parsing():
    """Test du parsing JSON avec différents formats"""
    
    print("🧪 Test du Parsing JSON DeerFlow")
    print("=" * 50)
    
    # Test 1: JSON valide simple
    test_cases = [
        {
            "name": "JSON valide simple",
            "data": '{"url": "https://example.com", "title": "Test"}',
            "expected": "success"
        },
        {
            "name": "JSON avec backticks",
            "data": '```json\n{"url": "https://example.com"}\n```',
            "expected": "success"
        },
        {
            "name": "JSON malformé",
            "data": '{"url": "https://example.com", "title": "Test"',
            "expected": "error"
        },
        {
            "name": "Chaîne vide",
            "data": "",
            "expected": "fallback"
        },
        {
            "name": "Chaîne avec caractères spéciaux",
            "data": '{"url": "https://example.com/测试", "title": "Test"}',
            "expected": "success"
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n📝 Test {i}: {test_case['name']}")
        print(f"Données: {test_case['data']}")
        
        try:
            # Test de parsing côté Python
            if test_case['data']:
                parsed = json.loads(test_case['data'])
                print(f"✅ Parsing Python réussi: {parsed}")
            else:
                print("⚠️ Données vides")
                
        except json.JSONDecodeError as e:
            print(f"❌ Erreur de parsing Python: {e}")
        except Exception as e:
            print(f"❌ Erreur inattendue: {e}")
    
    print("\n" + "=" * 50)
    print("✅ Tests de parsing terminés")

def test_backend_json_endpoint():
    """Test de l'endpoint backend avec JSON"""
    
    print("\n🌐 Test de l'endpoint backend")
    print("=" * 30)
    
    try:
        # Test de l'endpoint de chat avec un message simple
        response = requests.post(
            "http://localhost:8000/api/chat/stream",
            json={"message": "Test de parsing JSON"},
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        
        if response.status_code == 200:
            print("✅ Endpoint accessible")
            
            # Lire quelques lignes de la réponse
            lines = response.text.split('\n')[:5]
            print("📝 Premières lignes de réponse:")
            for line in lines:
                if line.strip():
                    print(f"  {line}")
        else:
            print(f"❌ Erreur HTTP: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur de connexion: {e}")
    except Exception as e:
        print(f"❌ Erreur inattendue: {e}")

if __name__ == "__main__":
    test_json_parsing()
    test_backend_json_endpoint()
