#!/usr/bin/env python3
"""
Script de test pour le nouvel endpoint /chat
"""
import requests
import json

def test_chat_endpoint():
    """Test du nouvel endpoint /chat"""
    base_url = "https://deepflow-production.up.railway.app"
    
    print("🧪 Test du nouvel endpoint /chat")
    print("=" * 50)
    print(f"URL: {base_url}")
    print("-" * 50)
    
    # Test 1: Endpoint /chat
    print("\n📋 Test 1: Endpoint /chat")
    try:
        response = requests.get(f"{base_url}/chat", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Statut: {data.get('status', 'N/A')}")
            print(f"📊 Message: {data.get('message', 'N/A')}")
            print(f"🔗 Endpoints disponibles: {list(data.get('endpoints', {}).keys())}")
            
            # Afficher l'exemple curl
            if 'example' in data and 'curl' in data['example']:
                print(f"\n📝 Exemple d'utilisation:")
                print(f"  {data['example']['curl']}")
                
        else:
            print(f"❌ Erreur HTTP: {response.status_code}")
            print(f"Réponse: {response.text}")
    except Exception as e:
        print(f"❌ Erreur: {e}")
    
    # Test 2: Endpoint racine mis à jour
    print("\n🏠 Test 2: Endpoint racine mis à jour")
    try:
        response = requests.get(f"{base_url}/", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Endpoints listés: {list(data.get('endpoints', {}).keys())}")
            
            # Vérifier que /chat est maintenant listé
            if 'chat' in data.get('endpoints', {}):
                print(f"✅ Endpoint /chat trouvé: {data['endpoints']['chat']}")
            else:
                print(f"❌ Endpoint /chat non trouvé")
                
        else:
            print(f"❌ Erreur HTTP: {response.status_code}")
    except Exception as e:
        print(f"❌ Erreur: {e}")
    
    # Test 3: Test de l'API de chat
    print("\n💬 Test 3: API de chat (/api/chat/stream)")
    try:
        message = {
            "message": "Test du nouvel endpoint /chat"
        }
        
        response = requests.post(
            f"{base_url}/api/chat/stream",
            json=message,
            headers={"Content-Type": "application/json"},
            timeout=15
        )
        
        if response.status_code == 200:
            print("✅ API de chat accessible")
            print(f"📊 Taille de la réponse: {len(response.text)} caractères")
            
            # Compter les lignes de réponse
            lines = response.text.count('\n')
            print(f"📝 Lignes de réponse: {lines}")
            
        else:
            print(f"❌ Erreur HTTP: {response.status_code}")
            print(f"Réponse: {response.text}")
            
    except Exception as e:
        print(f"❌ Erreur: {e}")
    
    print("\n" + "=" * 50)
    print("✅ Tests de l'endpoint /chat terminés")

if __name__ == "__main__":
    test_chat_endpoint()
