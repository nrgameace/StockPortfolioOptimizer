from pathlib import Path

def get_data_path():
    data_dir = Path(__file__).parent.parent
    data_dir = data_dir / 'data' / 'raw'
    return data_dir

def get_models_path():
    model_dir = Path(__file__).parent.parent
    model_dir = model_dir / 'models'
    return model_dir