#!/usr/bin/env python3
"""
Script de vérification pour le déploiement Railway
"""

import os
import sys

def verifier_structure():
    """Vérifie que tous les fichiers nécessaires sont présents"""
    
    print("🔍 Vérification de la structure du projet...")
    
    fichiers_requis = [
        "web/Dockerfile",
        "web/railway.toml", 
        "web/package.json",
        "web/next.config.js",
        "src/server/app.py",
        "update_redirect_url.py"
    ]
    
    tous_presents = True
    
    for fichier in fichiers_requis:
        if os.path.exists(fichier):
            print(f"✅ {fichier}")
        else:
            print(f"❌ {fichier} - MANQUANT")
            tous_presents = False
    
    return tous_presents

def verifier_configuration():
    """Vérifie la configuration Railway"""
    
    print("\n🔧 Vérification de la configuration Railway...")
    
    # Vérifier railway.toml
    if os.path.exists("web/railway.toml"):
        print("✅ railway.toml présent")
        
        with open("web/railway.toml", "r") as f:
            content = f.read()
            if "builder = \"dockerfile\"" in content:
                print("✅ Configuration Dockerfile détectée")
            else:
                print("⚠️  Configuration Dockerfile non trouvée")
    else:
        print("❌ railway.toml manquant")
        return False
    
    return True

def verifier_endpoint_chat():
    """Vérifie que l'endpoint /chat est configuré"""
    
    print("\n🎯 Vérification de l'endpoint /chat...")
    
    if os.path.exists("src/server/app.py"):
        with open("src/server/app.py", "r", encoding="utf-8") as f:
            content = f.read()
            
            if "@app.get(\"/chat\")" in content:
                print("✅ Endpoint /chat détecté")
                
                if "localhost:3000" in content:
                    print("⚠️  Redirection vers localhost:3000 (à mettre à jour)")
                else:
                    print("✅ Redirection configurée")
                    
                return True
            else:
                print("❌ Endpoint /chat non trouvé")
                return False
    
    return False

def afficher_instructions():
    """Affiche les instructions de déploiement"""
    
    print("\n" + "="*60)
    print("🚀 INSTRUCTIONS DE DÉPLOIEMENT RAILWAY")
    print("="*60)
    
    print("\n📋 Étapes à suivre :")
    print("1. Aller sur [railway.app](https://railway.app)")
    print("2. Créer un nouveau projet")
    print("3. Sélectionner le repository Bellamy509/deepflow")
    print("4. Choisir le dossier web/ comme source")
    print("5. Déployer automatiquement")
    
    print("\n🔧 Variables d'environnement à configurer :")
    print("NODE_ENV=production")
    print("NEXT_TELEMETRY_DISABLED=1")
    print("NEXT_PUBLIC_API_URL=https://deepflow-production.up.railway.app")
    
    print("\n🔄 Après obtention de l'URL publique :")
    print("python3 update_redirect_url.py <URL_PUBLIQUE>")
    
    print("\n📤 Déploiement final :")
    print("git add . && git commit -m 'update redirect' && git push bellamy main")
    
    print("\n" + "="*60)

def main():
    """Fonction principale"""
    
    print("🦌 Vérification du déploiement DeerFlow sur Railway")
    print("="*60)
    
    # Vérifications
    structure_ok = verifier_structure()
    config_ok = verifier_configuration()
    endpoint_ok = verifier_endpoint_chat()
    
    print("\n" + "="*60)
    print("📊 RÉSUMÉ DES VÉRIFICATIONS")
    print("="*60)
    
    if structure_ok:
        print("✅ Structure du projet : OK")
    else:
        print("❌ Structure du projet : PROBLÈMES DÉTECTÉS")
    
    if config_ok:
        print("✅ Configuration Railway : OK")
    else:
        print("❌ Configuration Railway : PROBLÈMES DÉTECTÉS")
    
    if endpoint_ok:
        print("✅ Endpoint /chat : OK")
    else:
        print("❌ Endpoint /chat : PROBLÈMES DÉTECTÉS")
    
    if structure_ok and config_ok and endpoint_ok:
        print("\n🎉 TOUT EST PRÊT POUR LE DÉPLOIEMENT !")
        afficher_instructions()
    else:
        print("\n⚠️  CORRIGER LES PROBLÈMES AVANT LE DÉPLOIEMENT")
        sys.exit(1)

if __name__ == "__main__":
    main()
