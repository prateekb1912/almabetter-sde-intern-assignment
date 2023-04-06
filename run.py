from app import create_app
from app.posts.routes import posts_bp

if __name__ == '__main__':
    app = create_app()

    app.register_blueprint(posts_bp)

    @app.route('/')
    def ready():
        response = {
            'status': 'ready',
        }

        return response

    app.run(debug=True)
