from config.appconfig import create_app

MP = create_app()

if __name__ == "__main__":
    
    MP.run(debug=True)