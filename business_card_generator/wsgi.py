from .app import create_app


# Create the app without .env file for production/serverless deployments
app = create_app(env_file=None)
