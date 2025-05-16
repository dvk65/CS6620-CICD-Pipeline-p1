# CS6620-CICD-Pipeline-p1
This is a simple Pokémon-themed Python module to show unit testing/automation with GitHub Workflows. HW assignment for CS6620 (Cloud Computing) at the Roux Institute at Northeastern.

## Continuous Integration
This project makes use of GitHub Actions to to automatically run tests whenever code is pushed to the main repo, a pull request is opened, or the workflow is manually triggered on GitHub. Test workflow can be triggered manually by going to the `Actions` tab and clicking on the `Run Workflow` button under the Pokemon Tests workflow. You can view the configuration in `workflows/main.yml`.

## Setup
You can run this project using either `pip` or `conda`. First make sure to properly clone and enter the repository.

### Using `pip`:
```bash
# Create/activate venv (optional)
python3 -m venv venv
source venv/bin/activate
# Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests
PYTHONPATH=src pytest tests/
```

### Using `conda`:
```bash
# Create/activate the environment
conda env create -f environment.yml
conda activate cicd_pipeline_p1_env

# Run tests
PYTHONPATH=src pytest tests/
# Windows: set PYTHONPATH=src && pytest tests/
```