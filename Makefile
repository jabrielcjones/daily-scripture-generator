# Makefile for Docker container management

# Color definitions
RED=\033[0;31m
GREEN=\033[0;32m
YELLOW=\033[1;33m
NC=\033[0m # No Color

# Ensure Docker is installed and set to the correct context
DOCKER := $(shell command -v docker 2> /dev/null)
DOCKER_CONTEXT := $(shell docker context show 2> /dev/null)
REQUIRED_DOCKER_CONTEXT := desktop-linux

ifndef DOCKER
    $(error "Docker is not available, please install Docker to use this Makefile.")
endif

ifeq ($(DOCKER_CONTEXT),$(REQUIRED_DOCKER_CONTEXT))
    # Docker is in the required context
else
    $(error "Docker context is not set to $(REQUIRED_DOCKER_CONTEXT). Please use 'docker context use $(REQUIRED_DOCKER_CONTEXT)' to switch contexts.")
endif

# Docker Compose project name
COMPOSE_PROJECT_NAME ?= daily-scripture-generator

# Help command
help:
	@echo "$(YELLOW)Available commands:$(NC)"
	@echo "  build            - Build all Docker images."
	@echo "  up               - Start all services."
	@echo "  stop             - Stop all services."
	@echo "  clean            - Remove containers, networks, and volumes."
	@echo "  rebuild          - Rebuild and start all services."
	@echo "  logs             - View output from containers."
	@echo "  build-frontend   - Build the frontend service."
	@echo "  run-frontend     - Run the frontend service."
	@echo "  clean-frontend   - Remove the frontend service."
	@echo "  build-api        - Build the api service."
	@echo "  run-api          - Run the api service."
	@echo "  clean-api        - Remove the api service."
	@echo "  build-db         - Build the db service."
	@echo "  run-db           - Run the db service."
	@echo "  clean-db         - Remove the db service."

# Build all Docker images
build:
	@echo "$(GREEN)Building all Docker images...$(NC)"
	@docker-compose -p $(COMPOSE_PROJECT_NAME) build

# Start all services
up: build
	@echo "$(GREEN)Starting all services...$(NC)"
	@docker-compose -p $(COMPOSE_PROJECT_NAME) up -d

# Stop all services
stop:
	@echo "$(GREEN)Stopping all services...$(NC)"
	@docker-compose -p $(COMPOSE_PROJECT_NAME) stop

# Remove all containers, networks, and volumes
clean:
	@echo "$(RED)Removing all containers, networks, and volumes...$(NC)"
	@docker-compose -p $(COMPOSE_PROJECT_NAME) down --volumes

# Rebuild and start all services
rebuild: stop build up
	@echo "$(GREEN)Rebuilding and starting all services...$(NC)"

# View logs
logs:
	@docker-compose -p $(COMPOSE_PROJECT_NAME) logs -f

# Build the frontend service
build-frontend:
	@echo "$(GREEN)Building frontend service...$(NC)"
	@docker-compose -p $(COMPOSE_PROJECT_NAME) build frontend

# Run the frontend service
run-frontend:
	@echo "$(GREEN)Running frontend service...$(NC)"
	@docker-compose -p $(COMPOSE_PROJECT_NAME) up -d frontend

# Remove the frontend service
clean-frontend:
	@echo "$(RED)Removing frontend service...$(NC)"
	@docker-compose -p $(COMPOSE_PROJECT_NAME) rm -f -s -v frontend

# Build the api service
build-api:
	@echo "$(GREEN)Building api service...$(NC)"
	@docker-compose -p $(COMPOSE_PROJECT_NAME) build api

# Run the api service
run-api:
	@echo "$(GREEN)Running api service...$(NC)"
	@docker-compose -p $(COMPOSE_PROJECT_NAME) up -d api

# Remove the api service
clean-api:
	@echo "$(RED)Removing api service...$(NC)"
	@docker-compose -p $(COMPOSE_PROJECT_NAME) rm -f -s -v api

# Build the db service
build-db:
	@echo "$(GREEN)Building db service...$(NC)"
	@docker-compose -p $(COMPOSE_PROJECT_NAME) build db

# Run the db service
run-db:
	@echo "$(GREEN)Running db service...$(NC)"
	@docker-compose -p $(COMPOSE_PROJECT_NAME) up -d db

# Remove the db service
clean-db:
	@echo "$(RED)Removing db service...$(NC)"
	@docker-compose -p $(COMPOSE_PROJECT_NAME) rm -f -s -v db

.PHONY: build up down rebuild logs help build-frontend run-frontend build-api run-api build-db run-db clean clean-frontend clean-api clean-db
