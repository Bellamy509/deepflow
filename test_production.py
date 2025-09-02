#!/usr/bin/env python3
"""
Script de test pour l'application DeerFlow déployée sur Railway
"""
import requests
import json
import time

def test_production_api():
    """Test de l'API de production"""
    base_url = "https://deepflow-production.up.railway.app"
    
    print("🚀 Test de l'API DeerFlow en Production")
    print("=" * 50)
    print(f"URL: {base_url}")
    print("-" * 50)
    
    # Test 1: Endpoint racine
    print("\n📋 Test 1: Endpoint racine")
    try:
        response = requests.get(f"{base_url}/", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Statut: {data.get('status', 'N/A')}")
            print(f"📊 Version: {data.get('version', 'N/A')}")
            print(f"🔗 Endpoints disponibles: {list(data.get('endpoints', {}).keys())}")
        else:
            print(f"❌ Erreur HTTP: {response.status_code}")
    except Exception as e:
        print(f"❌ Erreur: {e}")
    
    # Test 2: Endpoint de santé
    print("\n🏥 Test 2: Endpoint de santé")
    try:
        response = requests.get(f"{base_url}/health", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Statut: {data.get('status', 'N/A')}")
            print(f"🔧 Service: {data.get('service', 'N/A')}")
        else:
            print(f"❌ Erreur HTTP: {response.status_code}")
    except Exception as e:
        print(f"❌ Erreur: {e}")
    
    # Test 3: API de chat
    print("\n💬 Test 3: API de chat")
    try:
        message = {
            "message": "Bonjour ! Test de l'API déployée sur Railway"
        }
        
        response = requests.post(
            f"{base_url}/api/chat/stream",
            json=message,
            headers={"Content-Type": "application/json"},
            timeout=30,
            stream=True
        )
        
        if response.status_code == 200:
            print("✅ API de chat accessible")
            print("📝 Réponse reçue (premières lignes):")
            
            # Lire les premières lignes
            lines_read = 0
            for line in response.iter_lines():
                if line and lines_read < 5:
                    line_str = line.decode('utf-8')
                    if line_str.startswith('data: '):
                        try:
                            data = json.loads(line_str[6:])
                            if 'content' in data:
                                print(f"  💬 {data['content']}")
                            else:
                                print(f"  📡 {line_str}")
                        except json.JSONDecodeError:
                            print(f"  ⚠️ Ligne non-JSON: {line_str}")
                    lines_read += 1
                elif lines_read >= 5:
                    break
                    
        else:
            print(f"❌ Erreur HTTP: {response.status_code}")
            print(f"Réponse: {response.text}")
            
    except requests.exceptions.Timeout:
        print("⏰ Timeout - L'API prend trop de temps à répondre")
    except Exception as e:
        print(f"❌ Erreur: {e}")
    
    # Test 4: Documentation
    print("\n📚 Test 4: Documentation API")
    try:
        response = requests.get(f"{base_url}/docs", timeout=10)
        if response.status_code == 200:
            print("✅ Documentation accessible")
            print(f"📄 Taille de la réponse: {len(response.text)} caractères")
        else:
            print(f"❌ Erreur HTTP: {response.status_code}")
    except Exception as e:
        print(f"❌ Erreur: {e}")
    
    print("\n" + "=" * 50)
    print("✅ Tests de production terminés")

def test_chat_with_different_messages():
    """Test de l'API de chat avec différents types de messages"""
    base_url = "https://deepflow-production.up.railway.app"
    
    print("\n🧪 Test de l'API de chat avec différents messages")
    print("=" * 50)
    
    test_messages = [
        "Salut ! Comment ça va ?",
        "Peux-tu me dire ce que fait DeerFlow ?",
        "Test avec caractères spéciaux: éàçùñ",
        "Test avec chiffres: 12345",
        "Test avec URL: https://example.com"
    ]
    
    for i, message in enumerate(test_messages, 1):
        print(f"\n📝 Test {i}: {message}")
        try:
            response = requests.post(
                f"{base_url}/api/chat/stream",
                json={"message": message},
                headers={"Content-Type": "application/json"},
                timeout=15
            )
            
            if response.status_code == 200:
                print("✅ Réponse reçue")
                # Compter les lignes de réponse
                lines = response.text.count('\n')
                print(f"📊 Lignes de réponse: {lines}")
            else:
                print(f"❌ Erreur HTTP: {response.status_code}")
                
        except Exception as e:
            print(f"❌ Erreur: {e}")
        
        # Pause entre les tests
        time.sleep(1)

if __name__ == "__main__":
    test_production_api()
    test_chat_with_different_messages()
