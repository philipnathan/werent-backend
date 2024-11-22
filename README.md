# WERENT Backend

WERENT is a backend service that supports property rental applications. It provides API functionalities for user management, property listings, booking services, and payment processing.

## Table of Contents

-   [Overview](#overview)
-   [ERD](#erd)
-   [Prerequisites](#prerequisites)
-   [Installation](#installation)
-   [Environment Variables](#environment-variables)
-   [Database Setup](#database-setup)
-   [Running the Application](#running-the-application)
-   [Stopping the Application](#stopping-the-application)
-   [Resetting the Application](#resetting-the-application)
-   [API Endpoints](#api-endpoints)
-   [API Documentation](#api-documentation)
-   [Deployment](#deployment)

## Overview

WERENT Backend is a Dockerized Flask application that interacts with a MySQL database to manage the platform's core functionalities. It supports migrations, user authentication, and data management for seamless operations.

## ERD

The Entity-Relationship Diagram (ERD) provides an overview of the database structure:

![Entity-Relationship-Diagram](./ERD.drawio.png)

## Prerequisites

Ensure the following are installed on your system:

-   **Docker** (for containerized application setup)
-   **Python 3.10** (optional, for non-Docker local development)

## Installation

### Install Docker

To install Docker, follow the official guide for your operating system:

-   [Docker installation guide](https://docs.docker.com/get-docker/)

---

## Environment Variables

Create a `.env` file in the root directory of your project and configure the following variables:

FLASK_ENV=development
FLASK_DEBUG=True

DATABASE_HOST=localhost
DATABASE_PORT=3307
DATABASE_NAME=db
DATABASE_USER=root
DATABASE_PASSWORD=db
JWT_SECRET_KEY=your_secret_key

## Database Setup

### Ensure MySQL is Running

Make sure MySQL is running and matches the configuration in your `.env` file.

### Run Migrations

To initialize and update the database schema, run the following commands inside the Docker container:

````bash
docker-compose exec backend flask db migrate -m "Initial migration"
docker-compose exec backend flask db upgrade


## Running the Application

### Build the Application

Build the required Docker images:

```bash
docker-compose build --no-cache

## Start the Application

Run the following command to start the application:

```bash
docker-compose up


## Once the Application is Running

Once the application is running, visit [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## Stopping the Application

To stop the application gracefully, follow these steps:

1. Press `CTRL+C` to stop the process.
2. Run the following command to clean up containers:

```bash
docker-compose down


## Resetting the Application

If you encounter errors or need a fresh start, follow these steps:

1. Delete the `migrations` folder (if applicable).
2. Run the following command to remove all volumes, networks, and containers:

```bash
docker-compose down -v


## API Endpoints

Below are the available API endpoints in the application:

### **Users**

- `GET /users`: Retrieve a list of all users.
- `POST /users`: Create a new user.

### **Products**

- `GET /products`: Retrieve a list of all products.
- `POST /products`: Add a new product.

### **Transactions**

- `POST /transactions`: Create a new transaction.
- `GET /transactions/:id`: Retrieve transaction details by ID.

---

## API Documentation

Detailed API documentation is available at:
[WERENT API Documentation](https://documenter.getpostman.com/view/example)

---

## Deployment

### **Build Docker Image**

Install the following dependencies for production:

```bash
poetry add gunicorn docker


## Build the Docker Image

To build the Docker image, run the following command:

```bash
docker build -t werent-backend .


## Run the Docker Container

To run the Docker container, execute the following command:

```bash
docker run -p 5000:5000 --env-file .env werent-backend


## Deploy on Railway

### 1. Login to Railway
Log in to Railway using your GitHub account.

### 2. Select the Repository
Choose your GitHub repository for deployment.

### 3. Configure Environment Variables
Add all the `.env` variables in the Railway settings.

### 4. Update Deployment Settings
- Set `FLASK_DEBUG=False`.
- Change `FLASK_ENV=development` to `FLASK_ENV=production`.

### 5. Deploy the Application
Follow Railway's deployment process, and your application will be live.

---

## Notes

- Changes to the code are automatically reflected in the Docker container if the app is running.
- For accessing the database directly, use a tool like **DBeaver** with the following connection details:
  - **Host**: `localhost`
  - **Port**: `3307`
  - **Database**: `db`
  - **Username**: `root`
  - **Password**: `db`

---

## Contributing

If you'd like to contribute to the project, feel free to create a pull request. For major changes, open an issue first to discuss your proposed updates.


````
