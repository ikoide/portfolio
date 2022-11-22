from portfolio.app import create_app, register_scheduler

app = create_app()
register_scheduler(app)

if __name__ == '__main__':
    app.run()
