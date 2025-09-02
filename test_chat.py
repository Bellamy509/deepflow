#!/usr/bin/env python3
"""
Script de test simple pour l'API de chat DeerFlow
"""
import requests
import json
import time

def test_chat_api():
    """Test de l'API de chat"""
    url = "http://localhost:8000/api/chat/stream"
    
    # Message de test
    message = {
        "message": "Salut ! Peux-tu me dire ce que fait DeerFlow ?"
    }
    
    print("🧪 Test de l'API de chat DeerFlow")
    print("=" * 50)
    print(f"URL: {url}")
    print(f"Message: {message['message']}")
    print("-" * 50)
    
    try:
        # Envoi de la requête POST
        response = requests.post(
            url,
            json=message,
            headers={"Content-Type": "application/json"},
            stream=True
        )
        
        if response.status_code == 200:
            print("✅ Requête réussie !")
            print("📝 Réponse reçue:")
            print("-" * 30)
            
            # Lecture du stream
            for line in response.iter_lines():
                if line:
                    line_str = line.decode('utf-8')
                    if line_str.startswith('data: '):
                        try:
                            data = json.loads(line_str[6:])
                            if 'content' in data:
                                print(f"💬 {data['content']}", end='', flush=True)
                        except json.JSONDecodeError:
                            continue
                    elif line_str.startswith('event: '):
                        event = line_str[7:]
                        if event == 'message_chunk':
                            continue
                        print(f"\n📡 Événement: {event}")
            
            print("\n" + "=" * 50)
            print("✅ Test terminé avec succès !")
            
        else:
            print(f"❌ Erreur HTTP: {response.status_code}")
            print(f"Réponse: {response.text}")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur de connexion: {e}")
    except Exception as e:
        print(f"❌ Erreur inattendue: {e}")

def test_health_endpoint():
    """Test de l'endpoint de santé"""
    url = "http://localhost:8000/health"
    
    print("\n🏥 Test de l'endpoint de santé")
    print("=" * 30)
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("✅ Endpoint de santé accessible")
            data = response.json()
            print(f"📊 Statut: {data.get('status', 'N/A')}")
        else:
            print(f"❌ Erreur: {response.status_code}")
    except Exception as e:
        print(f"❌ Erreur: {e}")

if __name__ == "__main__":
    test_health_endpoint()
    test_chat_api()
