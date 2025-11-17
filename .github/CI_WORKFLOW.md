# GitHub Actions CI/CD Workflow

## Overview
This project uses GitHub Actions for continuous integration and deployment. The workflow automatically runs on every push and pull request.

## Workflow File
Location: `.github/workflows/ci.yml`

## Jobs

### 1. Lint and Test
- **Purpose:** Ensure code quality and correctness
- **Steps:**
  1. Checkout repository
  2. Set up Python 3.11
  3. Install dependencies
  4. Run flake8 linter
  5. Run pytest tests
  6. Generate coverage reports
  7. Upload artifacts

### 2. Build Docker
- **Purpose:** Build and validate Docker image
- **Depends on:** Lint and Test job must pass
- **Steps:**
  1. Checkout repository
  2. Set up Docker Buildx
  3. Build Docker image
  4. Test Docker image
  5. Save image as compressed artifact
  6. Upload artifact

## Artifacts

| Name | Description | Retention |
|------|-------------|-----------|
| test-results | JUnit XML test results | 30 days |
| coverage-report | HTML/XML coverage reports | 30 days |
| docker-image | Compressed Docker image (tar.gz) | 7 days |

## Triggers

The workflow runs on:
- Push to `main` branch
- Push to `develop` branch
- Pull requests to `main` branch
- Pull requests to `develop` branch

## How to Use

### View Workflow Runs
1. Navigate to your repository on GitHub
2. Click the "Actions" tab
3. Select a workflow run to view details

### Download Artifacts
1. Open a completed workflow run
2. Scroll to the "Artifacts" section
3. Click on the artifact name to download

### Local Testing Before Push

```bash
# Run linter locally
flake8 src/

# Run tests locally
pytest tests/ -v

# Build Docker image locally
docker build -t ml-app:latest .
```

## Troubleshooting

### Workflow Fails on Linting
- Check flake8 errors in the workflow logs
- Run `flake8 src/` locally to see issues
- Fix code style issues before pushing

### Workflow Fails on Tests
- Check pytest output in the workflow logs
- Run `pytest tests/ -v` locally
- Fix failing tests before pushing

### Docker Build Fails
- Check if Dockerfile syntax is correct
- Verify all required files are present
- Run `docker build -t ml-app:latest .` locally

## Configuration Files

- `.github/workflows/ci.yml` - Workflow definition
- `.flake8` - Flake8 configuration
- `Dockerfile` - Docker image definition
- `.dockerignore` - Files to exclude from Docker build
- `requirements.txt` - Python dependencies
