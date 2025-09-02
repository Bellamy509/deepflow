#!/usr/bin/env python3
"""
Script pour mettre à jour l'URL de redirection vers l'interface publique Railway
"""

import re
import sys

def update_redirect_url(new_url):
    """Met à jour l'URL de redirection dans app.py"""
    
    # Lire le fichier app.py
    with open('src/server/app.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern pour trouver l'URL de redirection
    pattern = r'window\.location\.href\s*=\s*[\'"]([^\'"]*localhost:3000[^\'"]*)[\'"]'
    
    # Remplacer l'URL
    new_content = re.sub(pattern, f'window.location.href = "{new_url}"', content)
    
    # Vérifier si le remplacement a été fait
    if new_content == content:
        print("❌ Aucune URL localhost:3000 trouvée à remplacer")
        return False
    
    # Écrire le nouveau contenu
    with open('src/server/app.py', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ URL de redirection mise à jour vers : {new_url}")
    return True

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 update_redirect_url.py <URL_PUBLIQUE_RAILWAY>")
        print("Exemple: python3 update_redirect_url.py https://deerflow-web-production.up.railway.app")
        sys.exit(1)
    
    new_url = sys.argv[1]
    
    # Validation basique de l'URL
    if not new_url.startswith('https://'):
        print("❌ L'URL doit commencer par https://")
        sys.exit(1)
    
    print(f"🔄 Mise à jour de la redirection vers : {new_url}")
    
    if update_redirect_url(new_url):
        print("\n📋 Prochaines étapes :")
        print("1. Commiter les changements :")
        print("   git add .")
        print("   git commit -m 'feat: update redirect to public web interface'")
        print("2. Pousser vers GitHub :")
        print("   git push bellamy main")
        print("3. Attendre le redéploiement automatique sur Railway")
        print("\n🎯 Après le redéploiement, /chat redirigera vers l'interface publique !")
    else:
        print("❌ Échec de la mise à jour")
        sys.exit(1)

if __name__ == "__main__":
    main()
