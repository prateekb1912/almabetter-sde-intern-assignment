from app import create_app

if __name__ == '__main__':
    app = create_app()

    @app.route('/', methods=['GET'])
    def home():
        return 'Hello'
    
    print(app.url_map)


    app.run(debug=True)
