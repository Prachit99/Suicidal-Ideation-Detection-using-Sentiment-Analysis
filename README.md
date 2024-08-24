# Suicidal Ideation Detection

<img src="https://github.com/Prachit99/Suicidal-Ideation-Detection-using-Sentiment-Analysis/blob/main/Logo.png" width="1000" height="450"/>
<div align="center">
  <a href="https://github.com/Prachit99/Suicidal-Ideation-Detection-using-Sentiment-Analysis"><img src="https://img.shields.io/github/repo-size/Prachit99/Suicidal-Ideation-Detection-using-Sentiment-Analysis?style=for-the-badge"></a>
  <a href="https://github.com/Prachit99/Suicidal-Ideation-Detection-using-Sentiment-Analysis/blob/main/LICENSE"><img src="https://img.shields.io/github/license/Prachit99/Suicidal-Ideation-Detection-using-Sentiment-Analysis?style=for-the-badge"></a>
  <a href="https://github.com/Prachit99/Suicidal-Ideation-Detection-using-Sentiment-Analysis/graphs/contributors"><img src="https://img.shields.io/github/contributors/Prachit99/Suicidal-Ideation-Detection-using-Sentiment-Analysis?style=for-the-badge"/></a>
  <a href="https://github.com/Prachit99/Suicidal-Ideation-Detection-using-Sentiment-Analysis/issues"><img src="https://img.shields.io/github/issues/Prachit99/Suicidal-Ideation-Detection-using-Sentiment-Analysis?style=for-the-badge"</a>
</div>

## Overview
The Suicidal Ideation Detection project is designed to identify and assess suicidal thoughts from social media posts. Utilizing advanced natural language processing (NLP) techniques, this project leverages a fine-tuned LSTM model based on BERT from TensorFlow Hub to analyze text data. The model achieves an impressive 97% accuracy and performs well on false negatives, ensuring reliable detection.

## Background
Suicidal ideation is a critical issue that can be identified through social media activity. This project aims to create a safer online environment by detecting signs of suicidal thoughts in social media posts. Data is collected from Reddit, Twitter, and Tumblr using their respective APIs and is annotated by our team. The backend functionality is showcased using Django, with potential to expand the system as an API or integrate it into a Chrome extension. This model could also be adopted by social media platforms to enhance user safety.

## Features
- High Accuracy Detection: Leveraging an LSTM-based model fine-tuned with BERT for precise suicidal ideation detection.
- Data Collection: Utilizes Reddit, Twitter, and Tumblr APIs for comprehensive social media data.
- Backend Implementation: Showcased through a Django application, with potential to expose as an API or integrate into other platforms.
- Future Integration: Possibility to develop a Chrome extension or integrate into social media platforms for enhanced safety.

## How to Run
1. Clone the Repository:
```bash
git clone https://github.com/yourusername/suicidal-ideation-detection.git
cd suicidal-ideation-detection
```

2. Create and Activate a Virtual Environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install Dependencies:
```bash
pip install -r requirements.txt
```

4. Run Migrations:
```bash
python manage.py migrate
```

5. Start the Django Development Server:
```bash
python manage.py runserver
```

6. Access the Application: Open your web browser and navigate to [Localhost](http://127.0.0.1:8000) to view the Django application.

## Usage
- Backend Functionality: The model processes social media posts to identify potential suicidal ideation.
- API Exposure: Future developments may include exposing the functionality as an API for integration.
- Chrome Extension: Plans to create a Chrome extension for real-time analysis of social media posts.

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the Apache-2.0 License. See the [LICENSE](https://github.com/Prachit99/Suicidal-Ideation-Detection-using-Sentiment-Analysis/blob/main/LICENSE) file for details.

## Contributors 
<table>
  <tr>
    <td align="center"><a href="https://github.com/Prachit99"><img src="https://avatars.githubusercontent.com/Prachit99" width="100px;" alt=""/><br /><sub><b>Prachit Mhalgi</b></sub></a></td>
    <td align="center"><a href="https://github.com/rdoshi29"><img src="https://avatars.githubusercontent.com/rdoshi29" width="100px;" alt=""/><br /><sub><b>Riddhi Doshi</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/iathmika"><img src="https://avatars.githubusercontent.com/iathmika" width="100px;" alt=""/><br /><sub><b>Athmika Hebbar</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/aditi12200"><img src="https://avatars.githubusercontent.com/aditi12200" width="100px;" alt=""/><br /><sub><b>Aditi Bhagwat</b></sub></a><br /></td>
  </tr>
</table>
