
# Wordle Implementation

This directory contains a implementation of the Wordle game.

---

## Getting Started

Follow these steps to set up, run, and test the Wordle game implementation.

---

### Prerequisites

- **Python**: Python 3.7 or higher (if running locally)
- **Docker**: Installed and configured
- **Docker Compose**: Installed and available for use

---

### Local Installation

1. **Clone this repository**:

   ```shell
   git clone https://github.com/carlcapozza/my-wordle.git
   cd my-wordle
   ```

2. **(Optional) Create and activate a virtual environment**:

   ```shell
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install required dependencies**:
   Ensure you have a `requirements.txt` file. Install dependencies with:

   ```shell
   pip install -r requirements.txt
   ```

4. **Run the Game Locally**:
   Start the Wordle game:

   ```shell
   FLASK_APP=app/routes.py flask run
   ```

   Follow the on-screen instructions to play.

---

### Docker Setup

1. **Build the Docker Image**:

   ```shell
   docker build -t flask-wordle-app .
   ```

2. **Run the Application**:

   ```shell
   docker run --rm -p 8080:8080 --name flask-wordle-app-container -e FLASK_APP=app/routes.py flask-wordle-app
   ```

   Access the game in your browser at `http://localhost:8080`.

3. **Run Tests Locally**:
   Use the following command to build and run tests:

   ```bash
   docker run --rm flask-wordle-app pytest --maxfail=1 --disable-warnings
   ```

---

### Docker Compose Setup

This project includes a `docker-compose.yml` file to simplify running the application and tests.

1. **Build and Run the Application with Tests**:

   ```bash
   docker compose up --build
   ```

   - The `test` service runs `pytest` during the build process.
   - The `web` service starts only if the tests pass.

2. **Run Tests Separately**:
   Run tests directly without starting the web service:

   ```bash
   docker compose run --rm test
   ```

3. **Run the Web Application Without Tests**:

   ```bash
   docker compose up web
   ```

---

### Troubleshooting

- **Port Conflict**:
  If port `8080` is in use, update the `docker-compose.yml` file or the `docker run` command to use a different port:

  ```yaml
  ports:
    - "8081:8080"  # Change 8081 to your desired avialable port
  ```

  Run the container with:

  ```shell
  docker-compose up
  ```

- **Container Name Conflict**:
  Remove conflicting containers:

  ```shell
  docker rm -f flask-wordle-app-container
  ```

---

### License

This project is licensed under the MIT License.
