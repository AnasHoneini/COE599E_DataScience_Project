<h1>COE599E Prog for Data Science Project</h1>

<h2>Lebanese Identity Recognition with OCR</h2>

This project focuses on enhancing the accuracy, efficiency, and security of Lebanese identity recognition using Optical Character Recognition (OCR) technology. The objective is to explore the potential of OCR in processing various Lebanese identity documents, including passports, ID cards, licenses, and voter ID cards. By leveraging machine learning techniques, the project aims to develop a robust OCR model capable of extracting essential information from these documents.

<b>Project Overview:</b>
<br>
The project involves a comprehensive analysis of the variables influencing OCR accuracy and reliability, drawing insights from extensive literature review. Based on this analysis, we have implemented a machine learning model for OCR using various algorithms, including K-Nearest Neighbors (KNN), Support Vector Classification (SVC), Multi-Layer Perceptron (MLP), and others. These models have been trained to recognize and extract crucial information from Lebanese identity documents.

<b>Project Features:</b>
<br>
Accurate and efficient recognition of Lebanese identity documents and Cropping functionality for ID card images, enhancing the user experience.
Machine learning models trained on diverse algorithms, including KNN, SVC, MLP, and more.
Extraction of vital information, such as names, identification numbers, and other relevant details.
User-friendly interface showcasing the implemented models and their results.
Face Recognition: In order to recognize faces in images, we employed the LBP (Local Binary Patterns) Cascade Classifier, which is a well-liked and effective technique. As soon as the face was located, we collected the bounding box coordinates and utilized them to trim the original picture to create the profile picture. 

<b>Technology Stack:</b>
<br>
Frontend: HTML and CSS for creating an intuitive user interface.
Backend: Python Flask framework for handling requests and integrating the OCR models.
Machine Learning: Python libraries for implementing various algorithms, including KNN, SVC, MLP, and others.
