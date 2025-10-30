#!/bin/bash

# StoicChatBot Docker Management Script

case "$1" in
  "build")
    echo "Building Docker image..."
    docker-compose build
    ;;
  "run")
    echo "Running StoicChatBot in interactive mode..."
    docker-compose up stoic-chatbot
    ;;
  "web")
    echo "Running StoicChatBot in web mode..."
    docker-compose --profile web up stoic-chatbot-web
    ;;
  "shell")
    echo "Opening shell in container..."
    docker-compose run --rm stoic-chatbot bash
    ;;
  "install")
    echo "Installing new packages..."
    if [ -z "$2" ]; then
      echo "Usage: ./docker-run.sh install <package_name>"
      exit 1
    fi
    docker-compose run --rm stoic-chatbot pip install "$2"
    echo "Don't forget to update requirements.txt!"
    ;;
  "logs")
    echo "Showing container logs..."
    docker-compose logs -f stoic-chatbot
    ;;
  "stop")
    echo "Stopping all containers..."
    docker-compose down
    ;;
  "clean")
    echo "Cleaning up Docker resources..."
    docker-compose down --volumes --remove-orphans
    docker system prune -f
    ;;
  *)
    echo "StoicChatBot Docker Management"
    echo "Usage: $0 {build|run|web|shell|install|logs|stop|clean}"
    echo ""
    echo "Commands:"
    echo "  build   - Build the Docker image"
    echo "  run     - Run in interactive/CLI mode"
    echo "  web     - Run as web server (Flask)"
    echo "  shell   - Open bash shell in container"
    echo "  install - Install a new Python package"
    echo "  logs    - Show container logs"
    echo "  stop    - Stop all containers"
    echo "  clean   - Clean up Docker resources"
    exit 1
    ;;
esac