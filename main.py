from app.init import create_app
from app.modules.database.module.database_context import DatabaseContext
from app.modules.database.database_module import DatabaseModule


def run():
    app = create_app(__name__)

    @app.current.route('/t')
    def t():
        module: DatabaseContext = app.get_module(DatabaseModule)

        row = module.entity.movie.get_by(year=2018)
        print(row)

        print(
            module.entity.movie.replace(
                module.entity.movie(title='999')
            )
        )

        return ''

    app.current.run(debug=True)


if __name__ == '__main__':
    run()
