from app import create_app
from app.posts.routes import posts_bp
from app.weather.routes import weather_bp

if __name__ == '__main__':
    app = create_app()

    app.register_blueprint(posts_bp)
    app.register_blueprint(weather_bp)

    @app.route('/')
    def ready():
        response = {
            'status': 'ready',
        }

        return response

    app.run(debug=True)
