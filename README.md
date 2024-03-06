# Personal Health Record System (PHR-System)
# CHENGHAO HU

## Project Overview

The Personal Health Record System (PHR-System) is a secure, cloud-based platform designed to allow users to manage their health information in one centralized location. This system enables users to add, view, and share their health data with healthcare providers securely, facilitating better health management and care coordination.

## Features

- **User Management**: Secure registration and authentication for users.
- **Health Data Management**: Users can add and manage their health records, including medical history, medications, and lab results.
- **Data Sharing**: Facilitates secure sharing of health information with authorized healthcare providers.
- **Cloud-Based Architecture**: Leverages cloud services for scalability, reliability, and security.

## Technologies Used

- **Backend**: Python, Flask
- **Database**: MySQL
- **Containerization**: Docker
- **Version Control**: Git, GitHub

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Docker
- Docker Compose
- Git

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/garyhch0702/PHR-System.git
cd PHR-System
```
1. **Start the application**
Using Docker Compose, build and start the services:
```bash
docker-compose up --build -d
```
## Accessing the Application
The user_service is accessible at http://localhost:5000.
The health_data_service is accessible at http://localhost:5001.

## Development
Details about the project structure and guidelines for contributing to the project.

## Project Structure
Provide an overview of the project directories and files, explaining the purpose of significant parts.

## Contributing
Instructions for how developers can contribute to the project. Encourage contributions and collaboration.
