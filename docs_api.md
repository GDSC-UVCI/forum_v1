# **API Documentation - Forum**

## **Base URL**: `/api/`

### **Endpoints**:

---

## 1. **Forums**
### a. **Liste des forums & Création d’un forum**

- **URL**: `/api/forums/`
- **Méthode**: `GET` | `POST`
- **Description**:
    - `GET` : Liste tous les forums disponibles.
    - `POST` : Crée un nouveau forum.

- **Paramètres**:
    - `name` (string) : Nom du forum. *(Requis pour POST)*
    - `description` (string) : Description du forum. *(Requis pour POST)*

- **Exemple de requête (GET)** :
    ```json
    GET /api/forums/
    ```

- **Exemple de requête (POST)** :
    ```json
    POST /api/forums/
    Content-Type: application/json
    {
        "name": "Forum Django",
        "description": "Discussions sur Django"
    }
    ```

- **Réponse (POST)** :
    ```json
    {
        "id": 1,
        "name": "Forum Django",
        "description": "Discussions sur Django",
        "created_at": "2024-09-14T10:00:00Z"
    }
    ```

---

## 2. **Topics (Sujets)**
### a. **Liste des sujets & Création d’un sujet**

- **URL**: `/api/forums/<forum_id>/topics/`
- **Méthode**: `GET` | `POST`
- **Description**:
    - `GET` : Liste tous les sujets d’un forum donné.
    - `POST` : Crée un nouveau sujet dans un forum.

- **Paramètres**:
    - `title` (string) : Titre du sujet. *(Requis pour POST)*
    - `content` (string) : Contenu du sujet. *(Requis pour POST)*

- **Exemple de requête (GET)** :
    ```json
    GET /api/forums/topics/1/
    ```

- **Exemple de requête (POST)** :
    ```json
    POST /api/forum/topics/1/
    Content-Type: application/json
    {
        "title": "Sujet sur Django REST",
        "content": "Comment bien structurer une API REST avec Django ?"
    }
    ```

- **Réponse (POST)** :
    ```json
    {
        "id": 1,
        "forum": 1,
        "title": "Sujet sur Django REST",
        "content": "Comment bien structurer une API REST avec Django ?",
        "created_at": "2024-09-14T10:15:00Z"
    }
    ```

---

## 3. **Messages**
### a. **Liste des messages & Création d’un message**

- **URL**: `/api/topics/<topic_id>/messages/`
- **Méthode**: `GET` | `POST`
- **Description**:
    - `GET` : Liste tous les messages d’un sujet donné.
    - `POST` : Crée un nouveau message dans un sujet.

- **Paramètres**:
    - `content` (string) : Contenu du message. *(Requis pour POST)*

- **Exemple de requête (GET)** :
    ```json
    GET /api/topics/1/messages/
    ```

- **Exemple de requête (POST)** :
    ```json
    POST /api/topics/1/messages/
    Content-Type: application/json
    {
        "content": "Je suis d'accord, Django REST Framework est un bon choix !"
    }
    ```

- **Réponse (POST)** :
    ```json
    {
        "id": 1,
        "topic": 1,
        "content": "Je suis d'accord, Django REST Framework est un bon choix !",
        "created_at": "2024-09-14T10:30:00Z"
    }
    ```

---

### **Codes de statut HTTP communs** :
- `200 OK` : La requête a été traitée avec succès.
- `201 Created` : Ressource créée avec succès (pour POST).
- `400 Bad Request` : Erreur dans les données fournies.
- `404 Not Found` : Ressource non trouvée.
- `500 Internal Server Error` : Erreur serveur.
