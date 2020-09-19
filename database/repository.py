from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models import Base, Categories, Units, Goods, Positions, Employees, Vendors

PATH_DB = 'test_db.sqlite3'

class Repository:

    def __init__(self, path_db):
        self.engine = create_engine(f'sqlite:///{path_db}?check_same_thread=False')
        self.create_db()
        self.session = self.get_session()

    def create_db(self):
        Base.metadata.create_all(self.engine)

    def get_session(self):
        session = sessionmaker(bind=self.engine)
        session = session()
        return session

    def create_category(self, name, description):
        category = Categories(name, description)
        self.session.add(category)

    def create_unit(self, name):
        unit = Units(name)
        self.session.add(unit)

    def create_goods(self, name, unit, category):
        goods = Goods(name, unit, category)
        self.session.add(goods)

    def create_positions(self, name):
        position = Positions(name)
        self.session.add(position)

    def create_employer(self, fio, position):
        employer = Employees(fio, position)
        self.session.add(employer)

    def create_vendors(self, name, form, address, phone, email):
        vendor = Vendors(name, form, address, phone, email)
        self.session.add(vendor)

    def add_data(self):
        self.session.commit()



if __name__ == '__main__':
    db = Repository(PATH_DB)
    db.create_category('Milk', 'Good milk')
    db.create_unit('Liter')
    db.create_goods('Murenka', 1, 2)
    db.add_data()
