# Docker Project

Projet Docker multi-services avec Nginx, Flask et Stripe.

## Architecture

- **static-webapp**  
  Site statique servi par Nginx (page d’accueil avec liens).

- **reverse-proxy**  
  Nginx utilisé comme reverse proxy pour exposer les services Flask sur différents ports.

- **flask-frontend**  
  Application Flask simple (frontend).

- **flask-api**  
  API Flask exposant une route `/api`.

- **stripe-flask**  
  Application Flask intégrant Stripe Checkout.

## Ports exposés

| Service           | Port |
|-------------------|------|
| Static WebApp     | 80   |
| Flask API         | 81   |
| Flask Frontend    | 82   |
| Stripe App        | 83   |

## Prérequis

- Docker
- Docker Compose

## Configuration

Créer un fichier `.env` à partir de `.env-sample` :

```env
STRIPE_SECRET_KEY=sk_test_xxx
```
## Accès

- Page principale : http://localhost  
- API : http://localhost:81  
- Frontend Flask : http://localhost:82  
- Stripe App : http://localhost:83  

## Arrêt

```bash
docker compose down
