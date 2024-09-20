# Forum API - Setup Guide

Ce guide explique comment cloner et exécuter une application API Django localement à l'aide d'une base de données PostgreSQL. La base de données utilisée est `forum_bd`, avec l'utilisateur `admin` et le mot de passe `1234`.

## Prerequies

Avant de commencer, assurez-vous que le logiciel suivant est installé sur votre ordinateur:

- **Python 3.12**
- **PostgreSQL**
- **pip** 
- **git** 
- **Virtualenv** 

---

## 1. Clone the Project Repository

Start by cloning the project repository to your local machine using git:

```bash
git clone https://github.com/GDSC-UVCI/forum_v1.git
cd forum_project
```
## 2. Creer environnement virtuel et l'activer

```bash
python -m venv venv
venv/Scripts/activate
```
## 3. Installer les dépendances

```bash
pip install -r requirements.txt
```
## 4. Créer une base de donnée Postgresql forum_bd
## 6. Créer un utilisateur admin avec le mot de passe '1234' et lui donner les droit sur notre base de donnée
## 7. Faire les migrations dans notre base de donnée

```bash
python manage.py makemigrations
python manage.py migrate
```
## 8. Enfin on peut lançer le serveur
```bash
python manage.py runserver
```