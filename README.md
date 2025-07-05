# Phishing URL Detection System

## Overview
This project implements a machine learning-based system for detecting phishing URLs. It uses a Random Forest Classifier trained on various URL features to identify potentially malicious websites.

## Features
- Real-time URL analysis
- Machine learning-based detection using Random Forest Classifier
- GUI interface for easy interaction
- 21 distinct features for URL analysis including:
  - URL structure analysis (length, domain, subdomain)
  - Character pattern analysis (special characters, numbers, dots, dashes)
  - Security indicators (SSL, port numbers, IP addresses)
  - Suspicious content detection (high-risk keywords, suspicious TLDs)
  - Domain legitimacy verification
  - Path and query parameter analysis

## Project Structure
```
├── data/
│   ├── dataset.csv          # Training dataset
│   └── models/              # Trained model storage
├── logs/                    # Application logs
├── src/
│   ├── feature_extractor.py # URL feature extraction
│   ├── gui.py              # GUI implementation
│   ├── model.py            # ML model implementation
│   └── url_processor.py     # URL processing and validation
├── tests/                   # Test cases
├── main.py                 # Application entry point
└── requirements.txt        # Project dependencies
```

## Installation
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Start the application:
   ```bash
   python main.py
   ```
2. Enter a URL in the input field
3. Click "Analyze" to check if the URL is potentially malicious

## Features Description

### URL Analysis Features
1. **Basic URL Properties**
   - URL length
   - Domain length
   - Subdomain length
   - Path depth and length
   - Parameter count

2. **Character Analysis**
   - Special character count
   - Number count
   - Dot count
   - Dash count
   - URL entropy score

3. **Security Indicators**
   - IP address detection
   - Hexadecimal character detection
   - @ symbol presence
   - Double slash in path
   - Port number usage
   - HTTPS protocol verification

4. **Content Analysis**
   - Suspicious word detection
   - High-risk keyword identification
   - Suspicious TLD checking
   - Domain imitation detection

### Machine Learning Model
- Algorithm: Random Forest Classifier
- Training Accuracy: 100%
- Features: 21 distinct URL characteristics

## Security Features
- SSL certificate verification
- Domain legitimacy checking
- Phishing pattern recognition
- Real-time URL analysis

## Contributing
Contributions are welcome! Please feel free to submit pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.