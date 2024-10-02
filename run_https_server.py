import os
import sys

# Add the path to your Django project
current_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.join(current_dir, 'backend')
sys.path.append(backend_dir)

# Set the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main_conf.settings")

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    
    # Set up the command to run the server with HTTPS
    sys.argv = [
        sys.argv[0],
        'runserver_plus',
        '--cert-file', 'cert.pem',
        '--key-file', 'key.pem',
        '0.0.0.0:8443',
    ]
    
    execute_from_command_line(sys.argv)