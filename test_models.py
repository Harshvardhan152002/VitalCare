import os
import pickle
import sys

def test_model_loading():
    try:
        # Get the directory of the current script
        current_dir = os.path.dirname(os.path.abspath(__file__))
        models_dir = os.path.join(current_dir, 'models sav')
        
        print(f"Looking for models in: {models_dir}")
        
        # Check if directory exists
        if not os.path.exists(models_dir):
            print(f"Error: Models directory '{models_dir}' does not exist")
            return False
        
        # List files in the directory
        print("Files in the models directory:")
        for file in os.listdir(models_dir):
            print(f"  - {file}")
        
        # Try to load each model
        model_files = [
            'diabetes_model.sav',
            'heart_disease_model.sav',
            'parkinsons_model.sav'
        ]
        
        for model_file in model_files:
            model_path = os.path.join(models_dir, model_file)
            print(f"\nTrying to load {model_file}...")
            
            if not os.path.exists(model_path):
                print(f"Error: Model file '{model_path}' does not exist")
                continue
            
            try:
                model = pickle.load(open(model_path, 'rb'))
                print(f"Successfully loaded {model_file}")
                print(f"Model type: {type(model)}")
            except Exception as e:
                print(f"Error loading {model_file}: {e}")
                return False
        
        return True
    
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

if __name__ == "__main__":
    success = test_model_loading()
    print("\nModel loading test:", "PASSED" if success else "FAILED")
    sys.exit(0 if success else 1)
