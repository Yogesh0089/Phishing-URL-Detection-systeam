from src.feature_extractor import FeatureExtractor
from src.model import PhishingDetector
from src.url_processor import URLProcessor
from src.gui import PhishingDetectorGUI
import pandas as pd
import os

def main():
    # Initialize components
    detector = PhishingDetector()
    
    # Ensure model directory exists
    model_dir = "data/models"
    os.makedirs(model_dir, exist_ok=True)
    
    # Check if trained model exists
    model_path = os.path.join(model_dir, "phishing_detector.joblib")
    try:
        if os.path.exists(model_path):
            detector.load_model(model_path)
    except Exception as e:
        print(f"Error loading model: {e}\nTraining new model...")
        os.remove(model_path) if os.path.exists(model_path) else None
    else:
        # Train new model if no existing model found
        print("Training new model...")
        dataset = pd.read_csv("data/dataset.csv")
        
        # Extract features from URLs
        feature_extractor = FeatureExtractor()
        features_list = []
        for url in dataset['url']:
            # Extract features and reshape to 1D array
            features = feature_extractor.extract_features(url)
            features_list.append(features.ravel())
        
        # Convert to DataFrame with feature names
        feature_names = [
            'url_length', 'domain_length', 'subdomain_length', 'special_chars',
            'numbers', 'dots', 'dashes', 'suspicious_words',
            'suspicious_tld', 'domain_mismatch', 'url_entropy', 'high_risk_words',
            'path_depth', 'path_length', 'param_count', 'has_ip',
            'has_hex', 'has_at_symbol', 'has_double_slash', 'has_port', 'is_https'
        ]
        X = pd.DataFrame(features_list, columns=feature_names)
        
        # Use all 15 features for consistency
        X = X[feature_names]
        
        y = dataset['is_phishing']
        
        # Train the model
        accuracy = detector.train(X, y)
        print(f"Model trained with accuracy: {accuracy:.2%}")
        
        # Save the model
        detector.save_model(model_path)
        # X = dataset.drop('label', axis=1)
        # y = dataset['label']
        # detector.train(X, y)
        # detector.save_model(model_path)
    
    # Launch GUI
    app = PhishingDetectorGUI(detector)
    app.run()

if __name__ == "__main__":
    main()