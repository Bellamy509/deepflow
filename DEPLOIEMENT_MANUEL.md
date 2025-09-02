# 🚀 Déploiement Manuel de l'Interface DeerFlow sur Railway

## 🎯 **Alternative au CLI : Déploiement via Dashboard Web**

Puisque l'installation du CLI Railway pose problème, utilisons le **Dashboard Web** de Railway pour déployer l'interface.

## 📋 **Étapes de Déploiement Manuel :**

### **Étape 1 : Accéder à Railway Dashboard**
1. Aller sur [railway.app](https://railway.app)
2. Se connecter avec votre compte GitHub
3. Cliquer sur "New Project"

### **Étape 2 : Créer un nouveau projet**
1. Choisir "Deploy from GitHub repo"
2. Sélectionner le repository `deepflow`
3. Choisir le dossier `web/` comme source
4. Cliquer sur "Deploy Now"

### **Étape 3 : Configuration automatique**
Railway va automatiquement :
- Détecter le `Dockerfile` dans `web/`
- Construire l'image Docker
- Déployer l'application
- Générer une URL publique

### **Étape 4 : Variables d'environnement**
Dans le projet Railway créé, aller dans "Variables" et ajouter :
```
NODE_ENV=production
NEXT_TELEMETRY_DISABLED=1
NEXT_PUBLIC_API_URL=https://deepflow-production.up.railway.app
```

### **Étape 5 : Récupérer l'URL publique**
1. Aller dans l'onglet "Deployments"
2. Copier l'URL générée (ex: `https://deerflow-web-production.up.railway.app`)

## 🔄 **Mise à jour de la redirection :**

Une fois l'URL publique obtenue, mettre à jour `src/server/app.py` :

```python
# Remplacer localhost:3000 par l'URL publique Railway
REDIRECT_URL = "https://deerflow-web-production.up.railway.app"  # URL à remplacer
```

## 🧪 **Test du déploiement :**

### **1. Vérifier l'interface web :**
- Ouvrir l'URL publique Railway
- Vérifier que l'interface DeerFlow s'affiche

### **2. Tester la redirection :**
- Aller sur `/chat`
- Vérifier la redirection vers l'interface publique

## 🚨 **En cas de problème :**

### **Build échoue :**
- Vérifier les logs dans Railway Dashboard
- S'assurer que le Dockerfile est correct
- Vérifier que le dossier `web/` contient tous les fichiers

### **Interface ne se charge pas :**
- Vérifier les variables d'environnement
- S'assurer que `NEXT_PUBLIC_API_URL` pointe vers le bon backend
- Vérifier les logs de déploiement

## 🎯 **Avantages du déploiement Dashboard :**

1. **🚀 Pas besoin de CLI** - Interface web intuitive
2. **🔧 Configuration automatique** - Détection Dockerfile
3. **📊 Monitoring intégré** - Logs et métriques
4. **🔄 Déploiement automatique** - Depuis GitHub
5. **🌐 URL publique** - Accessible à tous

---

**Statut** : 🚧 Prêt pour déploiement manuel  
**Méthode** : Dashboard Web Railway  
**Prochaine étape** : Créer le projet Railway et déployer
