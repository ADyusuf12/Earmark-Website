# EARMARKWEB

Earmark Website is a real estate platform that allows users to browse, list, update, and manage property listings. The platform includes features such as property details, user permissions for managing listings, and a responsive design.

---

## Overview

Earmark-Website is a powerful Django-based web application designed to streamline real estate management and enhance user engagement.

### Why Earmark-Website?

This project simplifies the complexities of real estate management while providing a seamless user experience. The core features include:

- ⚙️ **Django Management**: Streamlines administrative tasks, making it easier for developers to manage the application lifecycle.
- 📦 **Dependency Management**: Ensures a cohesive development environment by defining essential libraries, reducing compatibility issues.
- ⚡ **Asynchronous Support**: Enhances performance with ASGI configuration, allowing for efficient handling of asynchronous requests.
- 🔑 **User Authentication**: Simplifies user management with built-in registration and profile management features.
- 🖼️ **Dynamic Templates**: Provides user-friendly templates for various functionalities, enhancing the overall user experience.
- 🧪 **Robust Testing Framework**: Ensures reliability and stability through comprehensive testing capabilities.

---

## Features

- **Property Listings**: View detailed information about properties, including images, price, and features.
- **User Permissions**: 
  - Only authorized users can delete or update their own listings.
  - Permissions are managed using Django's built-in permission system.
- **Responsive Design**: The website is designed to work seamlessly across devices.
- **Social Sharing**: Share property details on social media platforms.
- **Search Functionality**: Filter properties by location, category, price, and more.

---

## Technologies Used

- **Frontend**:
  - HTML5, CSS3
  - Bootstrap for responsive design
  - Font Awesome for icons

- **Backend**:
  - Django Framework
  - Django Template Engine
  - Python

- **Database**:
  - SQLite (default for Django, can be replaced with PostgreSQL or MySQL)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/earmark-website.git
   cd earmark-website
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Open the website in your browser:
   ```
   http://127.0.0.1:8000/
   ```

---

## Usage

1. **Home Page**: Browse available properties.
2. **Property Details**: Click on a property to view its details, including images, price, and features.
3. **User Actions**:
   - **Delete Listing**: Available only to users with the `delete_properties_listing` permission.
   - **Update Listing**: Available only to users with the `change_properties_listing` permission.
4. **Search**: Use the search form to filter properties by location, category, price, and more.

---

## File Structure

```
Earmark-Website/
├── EarmarkWeb/
│   ├── e_web/
│   │   ├── migrations/          # Database migration files
│   │   ├── static/              # Static files (CSS, JS, images)
│   │   │   ├── css/
│   │   │   ├── js/
│   │   │   └── images/
│   │   ├── templates/           # HTML templates
│   │   │   ├── base.html
│   │   │   ├── properties-detail.html
│   │   │   └── ...
│   │   ├── __init__.py          # Package initialization
│   │   ├── admin.py             # Admin site configuration
│   │   ├── apps.py              # App configuration
│   │   ├── models.py            # Database models
│   │   ├── tests.py             # Test cases
│   │   ├── urls.py              # URL routing
│   │   ├── views.py             # View functions
│   │   └── ...
│   ├── __init__.py              # Project initialization
│   ├── asgi.py                  # ASGI configuration
│   ├── settings.py              # Project settings
│   ├── urls.py                  # Project-level URL routing
│   ├── wsgi.py                  # WSGI configuration
│   └── manage.py                # Django management script
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact

For questions or support, please contact:
- **Email**:  adyusuf68@gmil.com