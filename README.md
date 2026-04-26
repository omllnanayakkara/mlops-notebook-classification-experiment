# MLOps Notebook Classification Experiment

A comprehensive machine learning project demonstrating the complete ML model lifecycle on Azure Machine Learning (Azure ML) using Python SDK. This project covers infrastructure setup, data handling, model training, experiment tracking, and monitoring.

## 📋 Project Overview

This project is a hands-on learning initiative to master Azure Machine Learning and MLOps practices. It implements a full-stack ML workflow including:

- **Infrastructure Setup**: Azure resources provisioning and workspace configuration
- **Data Management**: Data asset creation and handling with MLTable
- **Model Training**: ML model development with scikit-learn
- **Experiment Tracking**: Experiment and metric logging with MLFlow
- **Job Management**: Training job orchestration through Azure ML

## 🏗️ Project Structure

```
mlops-notebook-classification-experiment/
├── requirements.txt              # Python dependencies
├── setup_job.ipynb              # Job setup and training execution
├── infra-setup/
│   ├── conda.yml                # Conda environment configuration
│   └── infra.ipynb              # Infrastructure provisioning notebook
└── src/
    └── trainning_script.py      # Training script with MLFlow integration
```

## 🛠️ Prerequisites

- Python 3.10.11 or higher
- Azure subscription with appropriate permissions
- Azure CLI installed
- Conda or pip for dependency management

## 📦 Installation

### 1. Clone or Download the Project
```bash
cd mlops-notebook-classification-experiment
```

### 2. Set Up Conda Environment
```bash
conda env create -f infra-setup/conda.yml
conda activate my-env
```

Or install dependencies with pip:
```bash
pip install -r requirements.txt
```

### 3. Authenticate with Azure
```bash
az login
az account set --subscription <your-subscription-id>
```

## 🚀 Getting Started

### Step 1: Infrastructure Setup
Run the infrastructure notebook to provision Azure ML resources:

```bash
jupyter notebook infra-setup/infra.ipynb
```

This notebook:
- Creates an Azure ML Workspace
- Provisions a Compute Instance for training
- Sets up Azure Blob Storage datastore
- Defines the training environment with necessary dependencies

**Key Resources Created:**
- Azure ML Workspace
- Compute Instance
- Azure Blob Storage Datastore
- Custom Python Environment

### Step 2: Configure Data and Jobs
Execute the setup job notebook to prepare data assets and training jobs:

```bash
jupyter notebook setup_job.ipynb
```

This notebook:
- Connects to the Azure ML Workspace
- Creates and registers data assets with MLTable
- Configures training job parameters
- Defines the command job for model training

### Step 3: Run Training
The training script (`src/trainning_script.py`) will execute with the following capabilities:

- **Input Data**: Accepts CSV data through `--input-data` argument
- **MLFlow Integration**: Logs parameters and metrics for experiment tracking
- **Data Processing**: Uses pandas for data manipulation

## 🔧 Key Components

### Training Script (`src/trainning_script.py`)

The training script is the core ML component:

```python
python src/trainning_script.py --input-data <path-to-data>
```

**Features:**
- Command-line argument parsing for flexible data input
- CSV data loading and preprocessing
- MLFlow parameter logging for experiment tracking
- Integration with Azure ML for seamless tracking

### Infrastructure Components

#### Conda Environment (`infra-setup/conda.yml`)
- Python 3.10.11
- Core ML libraries: scikit-learn, pandas, numpy
- Visualization: matplotlib
- Experiment tracking: mlflow, azureml-mlflow
- Azure ML SDK: azure-ai-ml

#### MLTable Integration
- Structured data asset management
- Integration with Azure ML datasets
- Reproducible data versioning

## 📊 Experiment Tracking with MLFlow

This project uses MLFlow for comprehensive experiment tracking:

- **Parameter Logging**: Dataset information and configuration parameters
- **Metrics Tracking**: Model performance metrics
- **Artifact Management**: Model artifacts and outputs
- **Experiment Comparison**: Easy comparison of different runs

View experiment results:
```bash
mlflow ui
```

## 🔄 ML Model Lifecycle Coverage

### 1. **Data Preparation**
   - Data ingestion from CSV files
   - Data asset registration in Azure ML
   - MLTable for structured data handling

### 2. **Model Development**
   - Scikit-learn for machine learning models
   - Flexible training script with parameter control
   - Data preprocessing and feature engineering

### 3. **Experiment Tracking**
   - MLFlow for parameter and metric logging
   - Integration with Azure ML tracking backend
   - Reproducible experiment runs

### 4. **Job Orchestration**
   - Command job submission to Azure ML
   - Compute instance utilization
   - Job status monitoring and logging

### 5. **Monitoring & Logging**
   - Experiment tracking and visualization
   - Parameter and output logging
   - Job execution logs and metrics

## 🔐 Azure Authentication

The project uses Azure SDK authentication. Ensure your credentials are configured:

```bash
# Login to Azure
az login

# Set default subscription
az account set --subscription <subscription-id>
```

The MLClient will automatically use your authenticated Azure session.

## 📝 Dependencies

| Package | Purpose |
|---------|---------|
| `azure-ai-ml` | Azure ML SDK for workspace and job management |
| `azureml-mlflow` | MLFlow integration with Azure ML |
| `mlflow` | Experiment tracking and management |
| `scikit-learn` | Machine learning algorithms and tools |
| `pandas` | Data manipulation and analysis |
| `numpy` | Numerical computing |
| `matplotlib` | Data visualization |
| `mltable` | Structured data asset handling |

## 🎯 Learning Objectives

This project helps you master:

- ✅ Azure ML workspace and resource provisioning
- ✅ Data asset management in Azure ML
- ✅ Training job orchestration
- ✅ Experiment tracking with MLFlow
- ✅ MLOps best practices
- ✅ ML model lifecycle management
- ✅ Python ML development with scikit-learn
- ✅ Infrastructure as Code patterns

## 🐛 Troubleshooting

### Azure Authentication Issues
```bash
# Clear cached credentials
az logout
az login
```

### MLFlow Connection Issues
Ensure Azure ML and MLFlow dependencies are properly installed:
```bash
pip install --upgrade azureml-mlflow mlflow
```

### Conda Environment Problems
```bash
# Remove and recreate environment
conda env remove --name my-env
conda env create -f infra-setup/conda.yml
```

## 📚 Additional Resources

- [Azure ML Documentation](https://learn.microsoft.com/azure/machine-learning/)
- [MLFlow Documentation](https://mlflow.org/docs/)
- [scikit-learn Documentation](https://scikit-learn.org/stable/)
- [Azure ML Python SDK](https://learn.microsoft.com/python/api/overview/azure/ai-ml-readme/)

## 📄 License

This project is for learning purposes.

## 📧 Notes

This is an educational project designed to develop expertise in:
- Azure Machine Learning platform
- ML model lifecycle management
- MLOps and experiment tracking
- Production-ready ML workflows

