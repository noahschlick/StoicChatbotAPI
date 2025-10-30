param(
    [Parameter(Mandatory=$true)]
    [string]$Command,
    [string]$Package
)

switch ($Command) {
    "build" {
        Write-Host "Building Docker image..." -ForegroundColor Green
        docker-compose build
    }
    "run" {
        Write-Host "Running StoicChatBot in interactive mode..." -ForegroundColor Green
        docker-compose up stoic-chatbot
    }
    "web" {
        Write-Host "Running StoicChatBot in web mode..." -ForegroundColor Green
        docker-compose --profile web up stoic-chatbot-web
    }
    "shell" {
        Write-Host "Opening shell in container..." -ForegroundColor Green
        docker-compose run --rm stoic-chatbot bash
    }
    "install" {
        if (-not $Package) {
            Write-Host "Usage: .\docker-run.ps1 install -Package <package_name>" -ForegroundColor Red
            exit 1
        }
        Write-Host "Installing package: $Package..." -ForegroundColor Green
        docker-compose run --rm stoic-chatbot pip install $Package
        Write-Host "Don't forget to update requirements.txt!" -ForegroundColor Yellow
    }
    "logs" {
        Write-Host "Showing container logs..." -ForegroundColor Green
        docker-compose logs -f stoic-chatbot
    }
    "stop" {
        Write-Host "Stopping all containers..." -ForegroundColor Green
        docker-compose down
    }
    "clean" {
        Write-Host "Cleaning up Docker resources..." -ForegroundColor Green
        docker-compose down --volumes --remove-orphans
        docker system prune -f
    }
    default {
        Write-Host "StoicChatBot Docker Management" -ForegroundColor Cyan
        Write-Host "Usage: .\docker-run.ps1 <command> [-Package <package_name>]" -ForegroundColor White
        Write-Host ""
        Write-Host "Commands:" -ForegroundColor White
        Write-Host "  build   - Build the Docker image" -ForegroundColor Gray
        Write-Host "  run     - Run in interactive/CLI mode" -ForegroundColor Gray
        Write-Host "  web     - Run as web server (Flask)" -ForegroundColor Gray
        Write-Host "  shell   - Open bash shell in container" -ForegroundColor Gray
        Write-Host "  install - Install a new Python package" -ForegroundColor Gray
        Write-Host "  logs    - Show container logs" -ForegroundColor Gray
        Write-Host "  stop    - Stop all containers" -ForegroundColor Gray
        Write-Host "  clean   - Clean up Docker resources" -ForegroundColor Gray
        Write-Host ""
        Write-Host "Examples:" -ForegroundColor White
        Write-Host "  .\docker-run.ps1 build" -ForegroundColor Yellow
        Write-Host "  .\docker-run.ps1 install -Package requests" -ForegroundColor Yellow
    }
}