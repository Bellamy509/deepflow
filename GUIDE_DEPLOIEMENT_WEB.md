# 🚀 Guide de Déploiement de l'Interface DeerFlow sur Railway

## 🎯 **Objectif :**
Déployer l'interface Next.js DeerFlow sur Railway pour avoir une **URL publique** accessible à tous les utilisateurs, pas seulement en local.

## 🔧 **Prérequis :**
- Compte Railway (gratuit)
- Railway CLI installé
- Docker installé localement
- Accès au projet GitHub

## 📋 **Étapes de Déploiement :**

### **Étape 1 : Installation de Railway CLI**
```bash
npm install -g @railway/cli
```

### **Étape 2 : Connexion à Railway**
```bash
railway login
```

### **Étape 3 : Créer un nouveau projet Railway**
```bash
# Aller dans le dossier web
cd web

# Initialiser un nouveau projet Railway
railway init
```

### **Étape 4 : Configuration du projet**
- Choisir "Deploy from GitHub repo"
- Sélectionner votre repository `deepflow`
- Choisir le dossier `web/` comme source

### **Étape 5 : Variables d'environnement**
Dans Railway Dashboard, ajouter :
```
NODE_ENV=production
NEXT_TELEMETRY_DISABLED=1
NEXT_PUBLIC_API_URL=https://deepflow-production.up.railway.app
```

### **Étape 6 : Déploiement**
```bash
railway up
```

## 🌐 **Après le Déploiement :**

### **1. Récupérer l'URL publique :**
- Aller dans Railway Dashboard
- Copier l'URL du service (ex: `https://deerflow-web-production.up.railway.app`)

### **2. Mettre à jour la redirection :**
Modifier `src/server/app.py` pour rediriger vers cette URL publique au lieu de `localhost:3000`

### **3. Redéployer le backend :**
```bash
git add .
git commit -m "feat: update redirect to public web interface URL"
git push bellamy main
```

## 🔄 **Flux Final :**

### **Avant (Problème) :**
```
https://deepflow-production.up.railway.app/chat
→ Redirection vers localhost:3000 (❌ Local seulement)
```

### **Après (Solution) :**
```
https://deepflow-production.up.railway.app/chat
→ Redirection vers https://deerflow-web-production.up.railway.app (✅ Public)
```

## 🧪 **Test du Déploiement :**

### **1. Vérifier l'interface web :**
- Ouvrir l'URL publique de Railway
- Vérifier que l'interface DeerFlow s'affiche

### **2. Tester la redirection :**
- Aller sur `/chat`
- Vérifier la redirection vers l'interface publique

### **3. Tester les fonctionnalités :**
- Vérifier que le chat fonctionne
- Tester la connexion avec le backend

## 🚨 **Dépannage :**

### **Problème : Build échoue**
```bash
# Vérifier les logs Railway
railway logs

# Tester le build localement
cd web
docker build -t test .
```

### **Problème : Variables d'environnement**
- Vérifier dans Railway Dashboard
- S'assurer que `NEXT_PUBLIC_API_URL` pointe vers le bon backend

### **Problème : Interface ne se charge pas**
- Vérifier les logs Railway
- Tester l'URL directement
- Vérifier la configuration Next.js

## 📊 **Avantages du Déploiement Railway :**

1. **🌐 URL publique** - Accessible à tous les utilisateurs
2. **🚀 Déploiement automatique** - Depuis GitHub
3. **📱 Responsive** - Fonctionne sur tous les appareils
4. **🔒 HTTPS** - Sécurisé par défaut
5. **📈 Scalabilité** - Gestion automatique de la charge

## 🎯 **Résultat Final :**

- ✅ **Interface publique** accessible à tous
- ✅ **Redirection fonctionnelle** depuis `/chat`
- ✅ **Intégration complète** avec le backend
- ✅ **Expérience utilisateur** fluide et professionnelle

---

**Statut** : 🚧 En cours de déploiement  
**Prochaine étape** : Déployer l'interface sur Railway
