"Medicine Data Scraper and API Backend"


This Django project, backed by Django Rest Framework, serves as a backend system focusing on data scraping and APIs related to medicine information. The primary objective is to aggregate medicine data from external sources, process it, and provide APIs for user authentication, data retrieval, and manipulation.

"Features"

Data Scraping: Utilizes scraping techniques to gather medicine-related information from external sources.
API Endpoints: Provides endpoints for user authentication, including login and signup functionalities, as well as main page API for accessing medicine data.
Database Models: Defines models for storing scraped medicine data in a SQLite database.
Serializers: Implements serializers for converting medicine data into a suitable format for API consumption, including medicine serializer and signup serializer.
REST Framework: Utilizes Django Rest Framework for building robust APIs.
JWT Token Authentication: Implements JWT (JSON Web Tokens) for secure authentication and authorization of API requests.

"Setup Instructions"


Clone the Repository
Create Virtual Environment (Optional but recommended)
Install Dependencies
Database Migration
Run the Development Server
Accessing the APIs:browsable API at http://localhost:8000/api/.


"Technologies Used"

Django: Python web framework for building powerful web applications.
Django Rest Framework: Toolkit for building Web APIs in Django.
SQLite: Lightweight, serverless database engine.
JWT: JSON Web Tokens for secure authentication.
Python: Programming language used for backend development.


"Contributing"


Contributions are welcome! Feel free to open issues or submit pull requests to contribute to the project.

"License"


This project is licensed under the MIT License - see the LICENSE file for details.






