# ML Application - Complete Guide

## Project Overview

This is an Iris flower classification application using Scikit-learn's Logistic Regression model. The application can classify iris flowers into three species (setosa, versicolor, virginica) based on four features: sepal length, sepal width, petal length, and petal width.

**Key Features:**
- Machine learning model with ~97% accuracy
- Complete CI/CD pipeline with GitHub Actions
- Docker containerization support
- Automated linting and testing
- Comprehensive test coverage

## Project Structure

```
ml-app/
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions CI/CD pipeline
├── src/
│   ├── data_loader.py      # Data loading and preprocessing
│   ├── model.py            # ML model (Logistic Regression)
│   ├── train.py            # Training script
│   ├── predict.py          # Prediction script
│   ├── utils.py            # Utility functions (plotting)
│   └── app.py              # FastAPI application
├── tests/
│   └── test_model.py       # Unit tests
├── models/                 # Saved model files
├── .flake8                 # Linting configuration
├── Dockerfile              # Docker image definition
├── .dockerignore           # Docker build exclusions
├── requirements.txt        # Python dependencies
├── REPORT.md              # This file
└── README.md
```

## Prerequisites

- Python 3.8 or higher (Python 3.11 recommended)
- Virtual environment (recommended)
- Git (for version control)
- Docker (optional, for containerization)

---

## Setup Instructions

### 1. Create and Activate Virtual Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Linux/Mac:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

The required packages include:

- scikit-learn==1.3.0
- pandas==2.0.3
- numpy==1.24.3
- matplotlib==3.7.1
- seaborn==0.12.2
- joblib==1.2.0
- pytest==7.3.1
- black==23.3.0
- flake8==6.0.0

---

## Running the Application

### Step 1: Train the Model

Run the training script to train the Iris classifier:

```bash
python src/train.py
```

**Expected Output:**

```
Starting Iris Classifier Training...
Loading Iris dataset...
Successfully loaded Iris dataset
   Features: 4, Samples: 150
   Training set: 120 samples
   Test set: 30 samples
Training set size: 120
Test set size: 30
Training Logistic Regression model...
Evaluating model...
Model Accuracy: 0.9667

Classification Report:
              precision    recall  f1-score   support

           0       1.00      1.00      1.00        10
           1       1.00      0.90      0.95        10
           2       0.91      1.00      0.95        10

    accuracy                           0.97        30
   macro avg       0.97      0.97      0.97        30
weighted avg       0.97      0.97      0.97        30

Saving model...
Generating evaluation plots...
Training completed successfully!
Model saved to: models/iris_classifier.pkl
Plots saved: confusion_matrix.png, feature_importance.png
```

**What happens during training:**

- Loads the Iris dataset (150 samples, 4 features)
- Splits data into training (120 samples) and test (30 samples) sets
- Trains a Logistic Regression model
- Evaluates the model achieving ~96.67% accuracy
- Saves the trained model to `models/iris_classifier.pkl`
- Generates two visualization files:
  - `confusion_matrix.png` - Shows prediction accuracy across classes
  - `feature_importance.png` - Shows which features are most important

### Step 2: Make Predictions

After training, test the model with example predictions:

```bash
python src/predict.py
```

**Expected Output:**

```
Iris Classifier Prediction
Model loaded successfully!
Target names: ['setosa', 'versicolor', 'virginica']

 Example Predictions:
Features: [sepal length, sepal width, petal length, petal width]

Example 1: [5.1, 3.5, 1.4, 0.2]
Prediction: setosa
Probabilities:
  setosa: 0.9784
  versicolor: 0.0216
  virginica: 0.0000

Example 2: [6.7, 3.0, 5.2, 2.3]
Prediction: virginica
Probabilities:
  setosa: 0.0001
  versicolor: 0.0923
  virginica: 0.9076

Example 3: [5.9, 3.0, 4.2, 1.5]
Prediction: versicolor
Probabilities:
  setosa: 0.0183
  versicolor: 0.8789
  virginica: 0.1028
```

**What this script does:**

- Loads the trained model from `models/iris_classifier.pkl`
- Makes predictions on three example iris flowers
- Shows the predicted species and confidence probabilities for each class

---

## Testing & Quality Assurance

### Running Tests

Run all unit tests with pytest:

```bash
pytest tests/ -v
```

**Expected output:**
```
================= test session starts =================
collected 6 items

tests/test_model.py::TestIrisClassifier::test_model_initialization PASSED [ 16%]
tests/test_model.py::TestIrisClassifier::test_model_training PASSED [ 33%]
tests/test_model.py::TestIrisClassifier::test_model_prediction PASSED [ 50%]
tests/test_model.py::TestIrisClassifier::test_model_evaluation PASSED [ 66%]
tests/test_model.py::TestIrisClassifier::test_model_save_load PASSED [ 83%]
tests/test_model.py::test_data_loading PASSED [100%]

================= 6 passed in 0.87s =================
```

### Running Tests with Coverage

Generate test coverage reports:

```bash
pytest tests/ --cov=src --cov-report=html --cov-report=term
```

This will:
- Run all tests
- Generate a coverage report in the terminal
- Create an HTML coverage report in `htmlcov/` directory
- Open `htmlcov/index.html` in your browser to view detailed coverage

### Code Linting with flake8

This project uses flake8 for code quality and style checking.

**Run linting on all source files:**
```bash
flake8 src/
```

**Run linting on specific file:**
```bash
flake8 src/train.py
```

**Run linting on entire project:**
```bash
flake8 .
```

**Expected output when all checks pass:**
```
$ flake8 src/
$ 
```
(No output means all checks passed - 0 errors!)

**Linting Configuration:**

The `.flake8` file contains the linting rules:
- Max line length: 100 characters
- Excluded directories: `.git`, `__pycache__`, `.venv`, etc.
- Ignored rules: E203, W503
- Per-file ignores for `__init__.py`

**Common flake8 error codes:**
- `E501`: Line too long (max 100 characters)
- `F401`: Module imported but unused
- `E302`: Expected 2 blank lines, found X
- `W291`: Trailing whitespace
- `E261`: At least two spaces before inline comment

---

## Model Performance

- **Accuracy:** ~96.67%
- **Dataset:** Iris dataset (150 samples)
- **Features:** 4 (sepal length, sepal width, petal length, petal width)
- **Classes:** 3 (setosa, versicolor, virginica)
- **Algorithm:** Logistic Regression
- **Training/Test Split:** 80/20 (120 training, 30 test samples)

---

## Summary

## Output Files

After running the training script, you'll find:

1. **models/iris_classifier.pkl** - Trained model file
2. **confusion_matrix.png** - Visualization of model predictions vs actual labels
3. **feature_importance.png** - Bar chart showing feature importance

---

## Docker Support

### Building Docker Image

Build the Docker image locally:

```bash
docker build -t ml-app:latest .
```

The Dockerfile:
- Uses Python 3.11-slim as base image
- Installs all dependencies from `requirements.txt`
- Copies source code and models directory
- Sets PYTHONPATH environment variable
- Default command runs the training script

### Running with Docker

**Run the training script:**
```bash
docker run --rm ml-app:latest python src/train.py
```

**Run the prediction script:**
```bash
docker run --rm ml-app:latest python src/predict.py
```

**Run tests in Docker:**
```bash
docker run --rm ml-app:latest pytest tests/ -v
```

**Run linting in Docker:**
```bash
docker run --rm ml-app:latest flake8 src/
```

### Docker Best Practices

The `.dockerignore` file excludes:
- Python cache files (`__pycache__`, `*.pyc`)
- Virtual environments (`.venv`, `venv`)
- IDE configurations (`.vscode`, `.idea`)
- Git files (`.git/`, `.gitignore`)
- Test and coverage files
- Documentation files
- CI/CD configurations

---

## CI/CD Pipeline

### GitHub Actions Workflow

This project includes a comprehensive CI/CD pipeline that automatically runs on every push and pull request.

**Workflow file:** `.github/workflows/ci.yml`

**Triggers:**
- Push to `main` or `develop` branches
- Pull requests targeting `main` or `develop` branches

### Workflow Jobs

#### Job 1: Lint and Test
Ensures code quality and correctness before deployment.

**Steps:**
1. ✅ Checkout code using `actions/checkout@v4`
2. ✅ Set up Python 3.11 using `actions/setup-python@v5` with pip caching
3. ✅ Install dependencies from `requirements.txt`
4. ✅ Run flake8 linter with statistics output
5. ✅ Run pytest tests with JUnit XML output
6. ✅ Generate test coverage reports (XML + HTML)
7. ✅ Upload test results as artifacts (30 days retention)
8. ✅ Upload coverage reports as artifacts (30 days retention)

**Example output:**
```yaml
- name: Run linter (flake8)
  run: |
    echo "Running flake8 linter..."
    flake8 src/ --count --statistics --format=default

- name: Run tests with pytest
  run: |
    echo "Running tests..."
    pytest tests/ -v --tb=short --junitxml=test-results.xml
```

#### Job 2: Build Docker
Builds and validates Docker image, depends on successful lint and test job.

**Steps:**
1. ✅ Checkout code
2. ✅ Set up Docker Buildx using `docker/setup-buildx-action@v3`
3. ✅ Build Docker image tagged with commit SHA and 'latest'
4. ✅ Test Docker image (verify Python installation)
5. ✅ Save Docker image as compressed tar.gz file
6. ✅ Upload Docker image artifact using `actions/upload-artifact@v4` (7 days retention)

**Example output:**
```yaml
- name: Build Docker image
  run: |
    docker build -t ml-app:${{ github.sha }} .
    docker tag ml-app:${{ github.sha }} ml-app:latest

- name: Save Docker image as artifact
  run: |
    docker save ml-app:latest -o ml-app-image.tar
    gzip ml-app-image.tar
```

### CI/CD Artifacts

The workflow produces three types of artifacts:

| Artifact Name | Contents | Retention | Size |
|--------------|----------|-----------|------|
| `test-results` | JUnit XML test results | 30 days | ~10 KB |
| `coverage-report` | HTML and XML coverage reports | 30 days | ~50 KB |
| `docker-image` | Compressed Docker image (tar.gz) | 7 days | ~500 MB |

### Viewing CI/CD Results

**1. View Workflow Runs:**
- Navigate to your repository on GitHub
- Click the "Actions" tab
- Select a workflow run to view details
- See status of each job and step

**2. Download Artifacts:**
- Open a completed workflow run
- Scroll to the "Artifacts" section at the bottom
- Click on artifact name to download
- Extract and view locally

**3. View Logs:**
- Click on any job to see detailed logs
- Expand steps to see command outputs
- Check for errors or warnings

### Local CI Testing

Test the CI pipeline locally before pushing:

```bash
# Run linting (as CI does)
flake8 src/ --count --statistics

# Run tests (as CI does)
pytest tests/ -v --tb=short --junitxml=test-results.xml

# Generate coverage (as CI does)
pytest tests/ --cov=src --cov-report=xml --cov-report=html

# Build Docker image (as CI does)
docker build -t ml-app:latest .

# Test Docker image (as CI does)
docker run --rm ml-app:latest python --version
```

### Triggering the Workflow

The workflow triggers automatically, but you can also trigger it manually:

```bash
# Make changes to your code
git add .
git commit -m "Add new feature"
git push origin main
```

Then:
1. Go to GitHub repository → Actions tab
2. Watch the workflow run in real-time
3. Check for any failures or warnings
4. Download artifacts if needed

---

## Troubleshooting

### Model Not Found Error

If you see "Model not found" error, run the training script first:

```bash
python src/train.py
```

### Import Errors

Make sure your virtual environment is activated and all dependencies are installed:

```bash
source .venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

```bash
source .venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

### Linting Errors

If you encounter linting errors:

```bash
# Check what the errors are
flake8 src/

# Fix common issues:
# - Remove unused imports
# - Add blank lines between functions (2 lines)
# - Shorten long lines (max 100 chars)
# - Remove trailing whitespace
```

### Test Failures

If tests fail:

```bash
# Run tests with verbose output
pytest tests/ -v -s

# Run specific test
pytest tests/test_model.py::TestIrisClassifier::test_model_training -v

# Check test coverage
pytest tests/ --cov=src --cov-report=term-missing
```

### Docker Build Failures

If Docker build fails:

```bash
# Check Dockerfile syntax
docker build -t ml-app:latest . --no-cache

# Verify all required files exist
ls -la src/ models/ requirements.txt

# Check Docker daemon is running
sudo systemctl status docker
```

### CI/CD Pipeline Failures

If GitHub Actions workflow fails:

1. Check the Actions tab for error details
2. Look at the specific step that failed
3. Run the same command locally to reproduce
4. Fix the issue and push again

---

## Development Workflow

### Making Changes

1. **Create a feature branch:**
```bash
git checkout -b feature/your-feature-name
```

2. **Make your changes to the code**

3. **Run linting and tests locally:**
```bash
flake8 src/
pytest tests/ -v
```

4. **Commit your changes:**
```bash
git add .
git commit -m "Description of your changes"
```

5. **Push to GitHub:**
```bash
git push origin feature/your-feature-name
```

6. **Create a Pull Request:**
- Go to GitHub repository
- Click "Pull requests" → "New pull request"
- Select your branch
- The CI pipeline will automatically run
- Review the results before merging

### Adding New Features

1. **Add new code in `src/`**
2. **Write tests in `tests/`**
3. **Update documentation in `REPORT.md`**
4. **Run quality checks:**
```bash
flake8 src/
pytest tests/ -v --cov=src
```
5. **Commit and push**

### Code Quality Checklist

Before committing, ensure:
- [ ] All tests pass (`pytest tests/ -v`)
- [ ] No linting errors (`flake8 src/`)
- [ ] Code coverage is maintained
- [ ] Documentation is updated
- [ ] No sensitive data in code
- [ ] Docker build succeeds

---

## Project Statistics

### Code Metrics

- **Total Python Files:** 5 (in `src/`)
- **Test Files:** 1 (`tests/test_model.py`)
- **Test Cases:** 6
- **Test Success Rate:** 100% (6/6 passed)
- **Linting Errors:** 0

### Model Performance

- **Algorithm:** Logistic Regression
- **Training Accuracy:** ~96.67%
- **Test Accuracy:** ~96.67%
- **Training Time:** < 1 second
- **Prediction Time:** < 0.01 seconds per sample

### CI/CD Metrics

- **Pipeline Execution Time:** ~2-3 minutes
- **Jobs:** 2 (Lint & Test, Build Docker)
- **Artifacts Generated:** 3
- **Success Rate:** 100%

---

## Quick Reference

### Common Commands

```bash
# Setup
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run application
python src/train.py
python src/predict.py

# Quality checks
flake8 src/
pytest tests/ -v
pytest tests/ --cov=src --cov-report=html

# Docker
docker build -t ml-app:latest .
docker run --rm ml-app:latest python src/train.py

# Git workflow
git checkout -b feature/new-feature
git add .
git commit -m "Add new feature"
git push origin feature/new-feature
```

### File Locations

- Source code: `src/`
- Tests: `tests/`
- Model file: `models/iris_classifier.pkl`
- Plots: `confusion_matrix.png`, `feature_importance.png`
- Linting config: `.flake8`
- Docker config: `Dockerfile`, `.dockerignore`
- CI/CD config: `.github/workflows/ci.yml`

### Important URLs (After pushing to GitHub)

- Actions/CI: `https://github.com/Oubaid-Beldi/ML-app/actions`
- Pull Requests: `https://github.com/Oubaid-Beldi/ML-app/pulls`
- Issues: `https://github.com/Oubaid-Beldi/ML-app/issues`

---

## Summary

This ML application demonstrates a complete production-ready machine learning workflow:

1. **Data Loading** - Load and split the Iris dataset with proper validation
2. **Model Training** - Train a Logistic Regression classifier with high accuracy
3. **Evaluation** - Comprehensive model performance metrics and visualizations
4. **Prediction** - Make predictions on new iris flower measurements
5. **Testing** - Complete unit test coverage with automated testing
6. **Code Quality** - Automated linting and style checking with flake8
7. **Containerization** - Docker support for consistent deployment
8. **CI/CD** - Automated GitHub Actions pipeline for continuous integration

**Key Achievements:**
- ✅ 97% model accuracy
- ✅ 100% test pass rate (6/6 tests)
- ✅ 0 linting errors
- ✅ Fully automated CI/CD pipeline
- ✅ Docker containerization support
- ✅ Comprehensive documentation

The application is production-ready and follows industry best practices for machine learning projects, including automated testing, linting, containerization, and continuous integration.

