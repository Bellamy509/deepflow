# 🚂 Déploiement DeerFlow sur Railway

Ce guide vous explique comment déployer DeerFlow sur Railway.

## 📋 Prérequis

1. Un compte [Railway](https://railway.app/)
2. Votre projet DeerFlow configuré
3. Les clés API nécessaires

## 🚀 Déploiement rapide

### Option 1: Déploiement via GitHub (Recommandé)

1. **Connectez votre repository GitHub à Railway**
   - Allez sur [Railway Dashboard](https://railway.app/dashboard)
   - Cliquez sur "New Project"
   - Sélectionnez "Deploy from GitHub repo"
   - Choisissez votre repository `Bellamy509/deepflow`

2. **Configuration automatique**
   - Railway détectera automatiquement le Dockerfile
   - Le déploiement commencera automatiquement

### Option 2: Déploiement via CLI

1. **Installez Railway CLI**
   ```bash
   npm install -g @railway/cli
   ```

2. **Connectez-vous à Railway**
   ```bash
   railway login
   ```

3. **Déployez votre projet**
   ```bash
   railway up
   ```

## ⚙️ Configuration des variables d'environnement

Dans votre projet Railway, configurez les variables d'environnement suivantes :

### Variables obligatoires
```bash
# Configuration LLM (OpenAI)
OPENAI_API_KEY=sk-your-openai-api-key

# Moteur de recherche
TAVILY_API_KEY=your-tavily-api-key
SEARCH_API=tavily

# Configuration CORS
ALLOWED_ORIGINS=https://your-frontend-domain.com,http://localhost:3000
```

### Variables optionnelles
```bash
# Configuration MCP
ENABLE_MCP_SERVER_CONFIGURATION=true

# Configuration RAG
RAG_PROVIDER=ragflow
RAGFLOW_API_URL=http://localhost:9388
RAGFLOW_API_KEY=ragflow-xxx

# Configuration TTS
VOLCENGINE_TTS_ACCESS_KEY=your-tts-key
VOLCENGINE_TTS_SECRET_KEY=your-tts-secret
```

## 🔧 Configuration du fichier conf.yaml

Railway ne peut pas directement monter le fichier `conf.yaml`. Vous devez :

1. **Créer le fichier via Railway CLI**
   ```bash
   railway variables set CONFIG_YAML="$(cat conf.yaml | base64)"
   ```

2. **Ou utiliser les variables d'environnement directement**

## 🌐 Domaines et HTTPS

Railway fournit automatiquement :
- Un domaine HTTPS (ex: `your-app.railway.app`)
- Certificats SSL automatiques
- Load balancing

## 📊 Monitoring

Railway offre :
- Logs en temps réel
- Métriques de performance
- Health checks automatiques
- Redémarrage automatique en cas d'échec

## 🔄 Déploiement continu

Une fois configuré, Railway déploiera automatiquement à chaque push sur la branche `main`.

## 🛠️ Dépannage

### Problèmes courants

1. **Erreur de port**
   - Assurez-vous que l'application écoute sur `$PORT`
   - Vérifiez la commande de démarrage

2. **Erreur de variables d'environnement**
   - Vérifiez que toutes les clés API sont configurées
   - Assurez-vous que les noms de variables sont corrects

3. **Erreur de build**
   - Vérifiez que le Dockerfile est valide
   - Consultez les logs de build dans Railway

### Logs et debugging

```bash
# Voir les logs en temps réel
railway logs

# Voir les logs d'un service spécifique
railway logs --service backend

# Redémarrer le service
railway service restart
```

## 📞 Support

- [Documentation Railway](https://docs.railway.app/)
- [Discord Railway](https://discord.gg/railway)
- [Issues GitHub](https://github.com/Bellamy509/deepflow/issues)

## 🎉 Félicitations !

Votre DeerFlow est maintenant déployé sur Railway ! 🦌
