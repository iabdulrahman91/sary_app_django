# sary_app_django

[![Build, Test, Push](https://github.com/iabdulrahman91/sary_app_django/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/iabdulrahman91/sary_app_django/actions/workflows/ci-cd.yml)

---

## APP URL

**Main APP URL**

[Main API URL] (http://a173b9962a8184534a44a4226ef0c9cd-a797f83e3788bf39.elb.us-east-2.amazonaws.com/)

This Repo is to Demonstrate my ability to:

- Build RESTful API using Django rest_framework

- Setup CI/CD pipeline using GitHub Actions

- Dockerizing Django App

- Setup Development Environment using docker-compose

- Test-Driven Development (TDD)

---

## APP: Stackoverflow clone

### Models and relationship

Question:

- Can have many Answers (one to many)
- Belong to many Tags (many to many)
- Can have many Comments (One To Many (Polymorphic / GenericRelation))

Answer:

- Belong to a Question (one to many)
- Can have many Comments (One To Many (Polymorphic / GenericRelation))

Tag:

- Belong to many Qusitons (many to many)

Comment:

- Belong to a CommentedItem (such as Question or Answer)  (One To Many (Polymorphic))

---

## CI/CD

Use GitHub Actions to:

- Build the app

- Test the app using `./manage.py test`

- Containerize the app

- Push the Docker Image to Docker Hub

---

## docker-compose

Setup django app + postgres to simulated production environment.

---

## TDD

Follow Test-Driven Development process to assure quility and continiuos integration
