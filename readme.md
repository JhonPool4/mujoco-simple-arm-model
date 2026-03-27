## Workspace configuration

- Clone the repository with submodules
```bash
git clone --recurse-submodules https://github.com/JhonPool4/mujoco-simple-arm-model.git
```
- Create conda environment
```bash
conda create --name myosuite python=3.10
conda activate myosuite
pip install -r requirements.txt
```

## Simulation
To simulate the arm with random muscle commands
```bash
python run_model.py
```
