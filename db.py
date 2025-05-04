import sqlite3
import logging
from flask import current_app, g

def get_db():
    """Get a database connection from the current Flask application context.
    
    Returns:
        sqlite3.Connection: The database connection object.
        
    Raises:
        RuntimeError: If this function is called outside of a Flask application context.
        sqlite3.Error: If there is an error connecting to the database.
    """
    # Ensure we're within an application context
    if not hasattr(g, 'app_context'):
        raise RuntimeError("get_db() called outside of application context")
    
    try:
        # Check if there's already a connection in the current context
        if 'db' not in g:
            # Get database path from configuration or use default
            database_path = current_app.config.get('DATABASE', './instance/german.db')
            
            # Configure the connection - return Row objects that behave like dicts
            g.db = sqlite3.connect(
                database_path,
                detect_types=sqlite3.PARSE_DECLTYPES
            )
            g.db.row_factory = sqlite3.Row
            
            # Enable foreign key constraints
            g.db.execute("PRAGMA foreign_keys = ON")
            
        return g.db
    except sqlite3.Error as e:
        logging.error(f"Database connection error: {e}")
        # Re-raise to let the caller handle it
        raise


def close_db(e=None):
    """Close the database connection if it exists.
    
    This function is designed to be registered as a teardown function with Flask.
    
    Args:
        e: An optional exception that occurred during the request.
    """
    db = g.pop('db', None)
    
    if db is not None:
        try:
            db.close()
        except sqlite3.Error as e:
            logging.error(f"Error closing database connection: {e}")


def init_app(app):
    """Initialize the database connection for a Flask application.
    
    Args:
        app: The Flask application object.
    """
    # Set default database configuration
    app.config.setdefault('DATABASE', './instance/german.db')
    
    # Register a function to close the database connection when the application context ends
    app.teardown_appcontext(close_db)
    
    # Mark that we're inside an application context
    @app.before_request
    def mark_app_context():
        g.app_context = True