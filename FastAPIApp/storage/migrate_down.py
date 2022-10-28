from migrate_up import User, Product, Purchase, engine


def migrate_down():
        Purchase.__table__.drop(engine)
        User.__table__.drop(engine)
        Product.__table__.drop(engine)
        print('Success')


if __name__ == '__main__':
    migrate_down()