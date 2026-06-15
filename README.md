
# README (RU)

# Online Shop Backend API

Backend API для интернет-магазина с товарами, категориями, отзывами и системой пользователей. Проект реализован на Django REST Framework с поддержкой Celery, Redis и Docker.

---

## О проекте

Это backend система интернет-магазина, которая позволяет:

* управлять категориями и товарами
* оставлять отзывы и рейтинги
* работать с пользователями
* использовать авторизацию (JWT / OAuth / Token)
* выполнять фоновые задачи через Celery
* запускать проект в Docker окружении

---

## Основной функционал

### Категории

* создание и получение категорий
* подсчет количества товаров в категории
* кэширование списка категорий
* проверка возраста пользователя (18+)

### Товары

* CRUD операции
* привязка к категории
* автоматическая генерация product code (Celery task)
* список отзывов внутри товара
* средний рейтинг товара

### Отзывы

* добавление отзывов
* оценка от 1 до 5
* привязка к товару
* автоочистка старых отзывов (Celery task)

### Пользователи

* регистрация и авторизация
* email подтверждение
* Google OAuth login
* JWT / Token authentication
* удаление неактивных пользователей

---

## Асинхронные задачи (Celery)

* генерация product code
* удаление старых отзывов
* отправка email уведомлений
* генерация и проверка confirmation code

---

## Технологии

* Python 3.12
* Django 5
* Django REST Framework
* PostgreSQL
* Redis
* Celery / Celery Beat / Flower
* Docker / Docker Compose
* Nginx
* Gunicorn
* SimpleJWT
* OAuth2 (Google Login)

---

## Аутентификация

Поддерживаются:

* Email + Password
* Token Authentication
* JWT (Access / Refresh)
* Google OAuth

---

## API Endpoints


### Products

* `GET /products/`
* `POST /products/`
* `GET /products/{id}/`
* `GET /categories/`
* `POST /categories/`
* `GET /categories/{id}/`
* `PUT /PATCH /categories/{id}/`
* `DELETE /categories/{id}/`
* `GET /reviews/`
* `POST /reviews/`

### Users

* `POST /registration/`
* `POST /confirm/`
* `POST /authorization/`
* `POST /jwt/`
* `POST /jwt/refresh/`
* `POST /jwt/verify/`
* `POST /google-login/`

---

## Запуск через Docker

```bash
docker compose up --build
```

### Миграции

```bash
docker compose exec web python manage.py migrate
```

### Создание суперпользователя

```bash
docker compose exec web python manage.py createsuperuser
```

---

## Архитектура

* Django apps:

  * users
  * products
* Custom permissions (IsModerator)
* Age validation (18+ restriction)
* Redis caching
* Celery background tasks
* Nginx + Gunicorn production setup

---

## Особенности проекта

* автоматическая генерация кодов товаров
* email уведомления
* OAuth авторизация
* очистка старых данных через Celery Beat
* кэширование категорий
* защита по возрасту (18+)
* Docker-ready production конфигурация

---

---


# README (EN)


# Online Shop Backend API

A backend system for an online store built with Django REST Framework. The project includes products, categories, reviews, authentication, background tasks, and production-ready Docker setup.

---

## Overview

This project allows users to:

* manage product categories
* create and browse products
* leave reviews and ratings
* authenticate via multiple methods
* run background tasks using Celery
* deploy using Docker

---

## Features

### Products

* full CRUD operations
* category relation
* automatic product code generation (Celery)
* product reviews
* average rating calculation

* create / retrieve categories
* product count per category
* caching for optimization
* age restriction validation (18+)

* add reviews
* rating system (1–5 stars)
* product relation
* automatic cleanup of old reviews


### Users

* registration & login
* email confirmation system
* Google OAuth login
* JWT / Token authentication
* inactive user cleanup

---

## Background Tasks (Celery)

* product code generation
* old review deletion
* email notifications
* confirmation code handling

---

## Tech Stack

* Python 3.12
* Django 5
* Django REST Framework
* PostgreSQL
* Redis
* Celery / Celery Beat / Flower
* Docker / Docker Compose
* Nginx
* Gunicorn
* SimpleJWT
* Google OAuth2

---

## Authentication

* Email & Password login
* Token authentication
* JWT (Access / Refresh tokens)
* Google OAuth login

---

## API Endpoints

### Products

* `GET /products/`
* `POST /products/`
* `GET /products/{id}/`
* `GET /categories/`
* `POST /categories/`
* `GET /categories/{id}/`
* `PUT /PATCH /categories/{id}/`
* `DELETE /categories/{id}/`
* `GET /reviews/`
* `POST /reviews/`

### Users

* `POST /registration/`
* `POST /confirm/`
* `POST /authorization/`
* `POST /jwt/`
* `POST /jwt/refresh/`
* `POST /jwt/verify/`
* `POST /google-login/`

---

## Docker Setup

```bash
docker compose up --build
```

### Run migrations

```bash
docker compose exec web python manage.py migrate
```

### Create superuser

```bash
docker compose exec web python manage.py createsuperuser
```

---

## Architecture

* Modular Django apps:

  * users
  * products
* Custom permission system
* Redis caching layer
* Celery background workers
* Nginx + Gunicorn deployment

---

## Highlights

* automatic product code generation
* email notifications
* OAuth2 authentication (Google)
* scheduled background cleanup tasks
* caching optimization
* age-based restrictions (18+)
* production-ready Docker setup

