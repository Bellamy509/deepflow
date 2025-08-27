# Configuration des Variables d'Environnement Railway

## 🚀 Guide de Configuration

### Variables Obligatoires

#### 1. OPENAI_API_KEY
```bash
# Obtenir votre clé : https://platform.openai.com/api-keys
OPENAI_API_KEY=sk-votre-cle-openai-ici
```

#### 2. TAVILY_API_KEY
```bash
# Obtenir votre clé : https://tavily.com/
TAVILY_API_KEY=tvly-votre-cle-tavily-ici
```

### Variables Optionnelles

#### 3. ALLOWED_ORIGINS
```bash
# Domaines autorisés pour CORS
ALLOWED_ORIGINS=https://votre-app.railway.app,http://localhost:3000
```

#### 4. SEARCH_API
```bash
# Moteur de recherche (défaut: tavily)
SEARCH_API=tavily
```

## 📋 Configuration dans Railway

### Étape 1 : Accéder à Railway
1. Allez sur https://railway.app/
2. Connectez-vous à votre compte
3. Sélectionnez votre projet `deepflow`

### Étape 2 : Ajouter les Variables
1. Cliquez sur l'onglet **"Variables"**
2. Cliquez sur **"New Variable"**
3. Ajoutez chaque variable une par une

### Étape 3 : Redéployer
1. Après avoir ajouté toutes les variables
2. Railway redéploiera automatiquement
3. Vérifiez les logs pour confirmer le succès

## 🔍 Vérification

### Test des Variables
```bash
# Utilisez le script de diagnostic
python diagnose_railway.py https://votre-app.railway.app
```

### Endpoints de Test
- **Health Check** : `https://votre-app.railway.app/health`
- **API Docs** : `https://votre-app.railway.app/docs`
- **Test Chat** : `https://votre-app.railway.app/docs#/default/chat_stream_api_chat_stream_post`

## ⚠️ Sécurité

### Bonnes Pratiques
- ✅ Ne partagez jamais vos clés API
- ✅ Utilisez des clés API avec des permissions limitées
- ✅ Surveillez l'utilisation de vos clés
- ✅ Régénérez les clés si nécessaire

### Variables Sensibles
- `OPENAI_API_KEY` : Accès à GPT-4, GPT-3.5
- `TAVILY_API_KEY` : Accès à la recherche web

## 🛠️ Dépannage

### Problèmes Courants

#### 1. "Missing API Key"
```bash
# Vérifiez que les variables sont correctement nommées
# Pas d'espaces avant/après le nom
OPENAI_API_KEY=sk-...  # ✅ Correct
OPENAI_API_KEY = sk-... # ❌ Incorrect
```

#### 2. "Invalid API Key"
```bash
# Vérifiez le format des clés
OPENAI_API_KEY=sk-...  # ✅ Format OpenAI
TAVILY_API_KEY=tvly-... # ✅ Format Tavily
```

#### 3. "CORS Error"
```bash
# Ajoutez votre domaine à ALLOWED_ORIGINS
ALLOWED_ORIGINS=https://votre-app.railway.app
```

## 📞 Support

Si vous rencontrez des problèmes :
1. Vérifiez les logs Railway
2. Testez avec le script de diagnostic
3. Vérifiez le format des variables
4. Redéployez après modification
