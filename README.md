# Microservices Application with two services - Users Service and Orders Service. 

## Setup
### Project Structure: 
The project is organized with a top-level microservices-docker directory containing the docker-compose.yml file and subdirectories for the individual services (users_service and orders_service). 
### Containerization: 
Each service is containerized using Docker. The Dockerfile for each service defines the build process, including installing dependencies and copying the service code.
### Docker Compose Configuration:
The docker-compose.yml file defines the services, their network, and other configurations. It sets up a microservices-network for communication between the services.
### Service Deployment: 
The services are deployed using Docker Compose. Running docker-compose up builds the images and starts the containers, with the Users Service and Orders Service running on ports 5001 and 5002, respectively.
### Web Interface: 
A simple web interface, implemented in the index.html file, is used to interact with the services. It communicates with the running services using the defined URLs (USERS_SERVICE_URL and ORDERS_SERVICE_URL).
