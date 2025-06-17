# 🐳 Dockerized Flask App

This is a beginner-to-intermediate level Flask web application containerized using Docker. It features:

- Multiple routes (`/`, `/about`, `/messages`)
- HTML templates with Jinja2
- SQLite database integration
- Dockerized build and run support

---

## 🚀 Features

- 📋 Submit and view messages
- 🧠 Jinja2-based templating
- 🗃️ SQLite database with SQLAlchemy
- 🐳 Dockerized deployment

---

## 📦 Requirements

- [Docker](https://www.docker.com/products/docker-desktop)

---

## 🛠️ Setup Instructions

### 🔨 Build the Docker Image

```bash
docker build -t flask-docker-app .
