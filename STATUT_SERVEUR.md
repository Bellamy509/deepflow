# 🚀 Statut du Serveur DeerFlow

## ✅ État Actuel : FONCTIONNEL

### 🖥️ Services en cours d'exécution

1. **Backend FastAPI** (Port 8000)
   - ✅ Serveur Python démarré avec `start_server.py`
   - ✅ Endpoint de santé accessible : `/health`
   - ✅ Endpoint racine accessible : `/`
   - ✅ API de chat fonctionnelle : `/api/chat/stream`
   - ✅ Documentation Swagger accessible : `/docs`

2. **Frontend Next.js** (Port 3000)
   - ✅ Serveur de développement démarré avec `pnpm dev`
   - ✅ Interface utilisateur accessible
   - ✅ Application web fonctionnelle

### 🔧 Comment accéder

#### Interface Web (Recommandé)
```bash
# Ouvrir dans le navigateur
http://localhost:3000
```

#### API Backend
```bash
# Test de santé
curl http://localhost:8000/health

# Test de l'API
curl http://localhost:8000/

# Test du chat
curl -X POST -H "Content-Type: application/json" \
  -d '{"message": "Bonjour"}' \
  http://localhost:8000/api/chat/stream

# Documentation API
http://localhost:8000/docs
```

### 🚀 Commandes de démarrage

#### Backend
```bash
# Dans le répertoire racine
uv run python start_server.py
```

#### Frontend
```bash
# Dans le répertoire web/
cd web
pnpm dev
```

### 🧪 Tests disponibles

1. **Script de test automatique**
   ```bash
   uv run python test_chat.py
   ```

2. **Test manuel avec curl**
   ```bash
   curl -X POST -H "Content-Type: application/json" \
     -d '{"message": "test"}' \
     http://localhost:8000/api/chat/stream
   ```

### 📊 Monitoring

- **Processus actifs** : Vérifier avec `ps aux | grep -E "(start_server.py|next dev)"`
- **Ports utilisés** : 8000 (backend), 3000 (frontend)
- **Logs** : Affichés dans les terminaux respectifs

### 🔍 Résolution de problèmes

#### Si le chat ne fonctionne pas :
1. ✅ Vérifier que le backend est démarré (port 8000)
2. ✅ Vérifier que le frontend est démarré (port 3000)
3. ✅ Tester l'API directement avec curl
4. ✅ Vérifier les variables d'environnement

#### Si un service ne démarre pas :
1. Vérifier les dépendances : `uv sync`
2. Vérifier les variables d'environnement
3. Consulter les logs d'erreur

### 🌐 Déploiement Railway

- ✅ Application déployée avec succès
- ✅ Endpoints accessibles publiquement
- ⚠️ Variables d'environnement à configurer pour fonctionnalité complète

---

**Dernière mise à jour** : 27 août 2025  
**Statut** : 🟢 Tous les services fonctionnent correctement
