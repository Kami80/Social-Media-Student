# Social-Media-Student

## Project Overview
Social-Media-Student is a dynamic and interactive social networking platform tailored specifically for students. The platform facilitates easy communication, collaboration, and sharing of resources among users. Built using Django, the project showcases full-stack development capabilities and provides an excellent learning environment for aspiring developers. The application allows users to create personalized profiles, share posts, engage with others through comments and likes, and efficiently search for content and users.

![Project Overview](https://github.com/Kami80/Social-Media-Student/blob/main/static/images/Social-Media.png)

### Goals of the Project:
- **Enhance communication**: Establish a seamless communication channel for students to share knowledge and resources.
- **Foster community**: Create an inclusive online environment that encourages collaboration and interaction.
- **Scalability**: Design a system that can easily accommodate an increasing number of users and features.

## Features
### 1. User Authentication
- Secure registration and login functionality.
- Passwords are encrypted for enhanced security.
- Support for token-based sessions to ensure safe user interactions.

### 2. Profile Management
- Users can create and customize profiles, including profile pictures, bios, and academic interests.
- Profiles showcase a user's posts, comments, and engagement metrics, promoting user visibility.

### 3. Post Creation
- Users can craft rich-text posts using formatting options (bold, italic, lists).
- Authors can edit or delete their posts to maintain content quality.
- Tagging system to categorize posts, making them easier to find.

### 4. Comments & Likes
- Interactive commenting system that allows users to engage in discussions.
- Posts and comments can be liked, creating a feedback mechanism.
- Real-time notifications for user interactions to keep users informed.

### 5. Search Functionality
- Advanced search capabilities for finding posts by keywords, tags, or user names.
- Users can easily discover relevant content and connect with others based on shared interests.

### 6. Admin Panel
- Comprehensive admin dashboard for managing users and content.
- Moderation tools to oversee posts and handle user reports, ensuring a safe environment.

## Tech Stack
- **Backend**: Django (Python)
  - Utilizes Django REST Framework for building robust APIs.
  - Admin interface for streamlined management of site content.

- **Frontend**: HTML, CSS, JavaScript
  - Responsive design principles to ensure compatibility across devices.
  - JavaScript for dynamic content loading and enhanced user experience.

- **Database**: SQLite (Django default)
  - Stores all user data, posts, comments, and interactions.
  - Future adaptability to PostgreSQL or MySQL for larger scale deployment.

- **APIs**: RESTful API
  - Endpoints for user authentication, post management, and interaction handling.
  - JSON responses facilitate easy integration with frontend applications.

## Setup and Installation

### Prerequisites
Make sure you have Python 3.x and pip installed on your machine.

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Kami80/Social-Media-Student.git
   cd Social-Media-Student
   ```
3. **Create a virtual environment**:
 
  ```bash
  python -m venv venv
  source venv/bin/activate   # On Windows: venv\Scripts\activate
  ```
3. **Install dependencies**:
 
  ```bash
  pip install -r requirements.txt
  ```
4. **Apply migrations to set up the database**:
  
  ```bash
  python manage.py migrate
  ```
5. **Run the development server**:
 
  ```bash
  python manage.py runserver
  ```

Access the application in your web browser at http://127.0.0.1:8000/.

## Usage
- Register: Sign up to create a new user profile.
- Create Posts: After logging in, users can create posts, apply text formatting, and categorize them using tags.
- Interact: Like and comment on posts to foster community engagement. Users can view their notification feed to keep track of interactions.
- Search: Utilize the search functionality to find posts or connect with other users.
### Future Enhancements
- Direct Messaging: Implement a private messaging feature for users to communicate directly.
- Group Creation: Allow users to create and manage study groups or interest-based communities.
- Analytics Dashboard: Provide insights into user engagement, popular content, and growth metrics.
## License
This project is licensed under the MIT License. See the LICENSE file for more details.


