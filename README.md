# 🧠 Exercice Git

Ce dépôt contient un ensemble d’exercices pratiques pour apprendre à utiliser **Git** et **GitHub** de manière professionnelle.  
Les commandes ci-dessous permettent d’initialiser un projet local et de le connecter à un dépôt distant sur GitHub.

---

## 🚀 Initialisation du dépôt

### 1️⃣ Créer un dépôt Git local

```bash
git init
```

> Initialise un nouveau dépôt Git dans le dossier courant.

---

### 2️⃣ Ajouter tous les fichiers au suivi Git

```bash
git add .
```

> Ajoute tous les fichiers du projet à la zone de staging (préparation pour le commit).

---

### 3️⃣ Créer le premier commit

```bash
git commit -m "first commit"
```

> Enregistre les fichiers suivis dans l’historique Git avec un message de commit.

---

### 4️⃣ Renommer la branche principale en `main`

```bash
git branch -M main
```

> Par défaut Git crée la branche `master`, cette commande la renomme en `main`.

---

### 5️⃣ Lier le dépôt local à GitHub

```bash
git remote add origin git@github.com:erickolamar/exercice-git.git
```

> Connecte ton dépôt local à ton dépôt GitHub distant via SSH.

---

### 6️⃣ Envoyer le code sur GitHub

```bash
git push -u origin main
```

> Envoie la branche `main` et son historique sur GitHub.  
> Le `-u` crée un lien entre la branche locale et la branche distante.

---

## 🧩 Résumé des commandes

| Étape | Commande                       | Description                              |
| :---- | :----------------------------- | :--------------------------------------- |
| 1     | `git init`                     | Initialise le dépôt local                |
| 2     | `git add .`                    | Prépare tous les fichiers pour le commit |
| 3     | `git commit -m "first commit"` | Sauvegarde les changements               |
| 4     | `git branch -M main`           | Renomme la branche principale            |
| 5     | `git remote add origin <url>`  | Connecte à GitHub                        |
| 6     | `git push -u origin main`      | Envoie les fichiers sur GitHub           |

---

## 📦 Dépôt GitHub

🔗 [https://github.com/erickolamar/exercice-git](https://github.com/erickolamar/exercice-git)

---

## 💡 Astuce

Si tu veux vérifier la connexion à ton dépôt GitHub, exécute :

```bash
git remote -v
```

Cela affichera :

```
origin  git@github.com:erickolamar/exercice-git.git (fetch)
origin  git@github.com:erickolamar/exercice-git.git (push)
```

---

## 🧰 Outils utilisés

- **Git** ≥ 2.30
- **GitHub**
- **Terminal / Bash / CMD**

---

## 👨‍💻 Auteur

**EricKo lamar**  
📧 [Contact GitHub](https://github.com/erickolamar)
