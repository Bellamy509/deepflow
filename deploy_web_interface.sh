#!/bin/bash

# 🚀 Script de déploiement de l'interface DeerFlow sur Railway
# Ce script déploie l'interface Next.js sur Railway pour avoir une URL publique

echo "🦌 Déploiement de l'interface DeerFlow sur Railway..."

# Vérifier que Railway CLI est installé
if ! command -v railway &> /dev/null; then
    echo "❌ Railway CLI n'est pas installé. Installation..."
    npm install -g @railway/cli
fi

# Aller dans le dossier web
cd web

echo "📦 Construction de l'image Docker..."
# Construire l'image localement pour tester
docker build -t deerflow-web .

echo "🚀 Déploiement sur Railway..."
# Déployer sur Railway
railway up

echo "✅ Interface web déployée sur Railway !"
echo "🌐 L'URL publique sera affichée ci-dessus"
echo ""
echo "📋 Prochaines étapes :"
echo "1. Copier l'URL publique affichée"
echo "2. Mettre à jour la redirection dans src/server/app.py"
echo "3. Redéployer le backend"
echo ""
echo "🔗 Exemple d'URL : https://deerflow-web-production.up.railway.app"
