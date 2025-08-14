# Social Network API

This is a RESTful API for a simple social networking application built with Django and Django REST Framework.

## Features

### ✅ User Registration and Authentication
- Register with email and password to create an account.
- Login with credentials and receive a token for authentication.
- Logout and invalidate the token.

### ✅ User Profile
- Create and update profile including profile picture, bio, and other details.
- Retrieve own profile and view profiles of other users.
- Search users by username or other criteria.

### ✅ Follow/Unfollow
- Follow and unfollow other users.
- View the list of followed users and followers.

### ✅ Post Creation and Retrieval
- Create posts with text content and optional media attachments (images).
- Retrieve own posts and posts from followed users.
- Retrieve posts by hashtags or other criteria.

### 🧩 Likes and Comments (Optional)
- Like/unlike posts.
- View liked posts.
- Add/view comments on posts.

### 🧩 Schedule Post Creation using Celery (Optional)
- Schedule post creation by selecting a future time.

### ✅ API Permissions
- Only authenticated users can create posts, like posts, follow/unfollow, etc.
- Users can update/delete only their own posts, comments, and profiles.

### ✅ API Documentation
- Detailed documentation with instructions, sample API requests and responses.

## Technical Stack

- Django
- Django REST Framework (DRF)
- Token-based Authentication
- Django Serializers for data validation and representation
- DRF ViewSets and Routers for API endpoints
- Custom Permissions and Authentication classes

## Notes

This project focuses on backend RESTful API development. No frontend interface is included.

---

Visit [gptonline.ai](https://gptonline.ai/) — your reliable assistant for learning, development, and automation!
