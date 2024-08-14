# Flask Blog Site

This is a small blog site built using Flask, allowing users to register, log in, create posts, and manage their accounts. The site includes basic CRUD (Create, Read, Update, Delete) operations for blog posts and user authentication features.

## Features

- **User Authentication:** Register, log in, and manage user accounts securely using hashed passwords.
- **User Profiles:** Users can update their profile information, including uploading a profile picture.
- **Blog Posts:** Users can create, view, update, and delete their blog posts.
- **Pagination:** Posts are paginated for easy navigation.
- **Password Reset:** Users can request a password reset via email.
- **User-Specific Pages:** View posts by specific users.

# Usage

## Home Page

The home page displays all blog posts with pagination. Users can navigate through different pages to view older posts.

## User Registration and Login

Users can register and log in using the respective forms. Logged-in users can access additional features such as creating, editing, and deleting posts.

## Creating and Managing Posts

Users can create new posts, update existing ones, and delete their posts. Each post is associated with the user who created it.

## User Profiles

Each user has a profile page that displays their information and posts. Users can update their profile picture, username, and email address.

## Password Reset

If a user forgets their password, they can request a reset link via email, which will allow them to set a new password.

# Project Structure

- **app.py:** The main application file where routes and views are defined.
- **models.py:** Contains the database models for the User and Post.
- **forms.py:** Contains the WTForms for registration, login, account update, post creation, and password reset.
- **templates/:** Directory containing HTML templates for rendering the views.
- **static/:** Directory containing static files like CSS and profile pictures.

# Dependencies

- Flask
- Flask-SQLAlchemy
- Flask-Bcrypt
- Flask-Login
- Flask-Mail
- Flask-WTF
- Pillow

# Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue.
