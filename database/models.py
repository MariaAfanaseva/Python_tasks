from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Categories(Base):
    __tablename__ = 'categories'
    category_id = Column(Integer, primary_key=True)
    category_name = Column(String(50), nullable=False)
    category_description = Column(String(255), nullable=False)

    def __init__(self, name, description):
        self.category_name = name
        self.category_description = description

    def __repr__(self):
        return self.category_name


class Units(Base):
    __tablename__ = 'units'
    unit_id = Column(Integer, primary_key=True)
    unit_name = Column(String(128), nullable=False)

    def __init__(self, name):
        self.unit_name = name

    def __repr__(self):
        return self.unit_name


class Goods(Base):
    __tablename__ = 'goods'
    goods_id = Column(Integer, primary_key=True)
    goods_name = Column(String(50), nullable=False)
    goods_unit = Column(Integer, ForeignKey('units.unit_id'))
    goods_category = Column(Integer, ForeignKey('categories.category_id'))

    def __init__(self, name, unit, category):
        self.goods_name = name
        self.goods_unit = unit
        self.goods_category = category

    def __repr__(self):
        return self.goods_name


class Positions(Base):
    __tablename__ = 'positions'
    position_id = Column(Integer, primary_key=True)
    position_name = Column(String(128), nullable=False)

    def __init__(self, position):
        self.position_name = position

    def __repr__(self):
        return self.position_name


class Employees(Base):
    __tablename__ = 'employees'
    employee_id = Column(Integer, primary_key=True)
    employee_fio = Column(String(125), nullable=False)
    employee_position = Column(Integer, ForeignKey('positions.position_id'))

    def __init__(self, fio, position):
        self.employee_fio = fio
        self.employee_position = position

    def __repr__(self):
        return self.employee_fio


class Vendors(Base):
    __tablename__ = 'vendors'
    vendor_id = Column(Integer, primary_key=True)
    vendor_name = Column(String(128), nullable=False)
    vendor_form = Column(String(255), nullable=False)
    vendor_address = Column(String(128), nullable=False)
    vendor_phone = Column(String(50), nullable=False)
    vendor_email = Column(String(128), nullable=False)

    def __init__(self, name, form, address, phone, email):
        self.vendor_name = name
        self.vendor_form = form
        self.vendor_address = address
        self.vendor_phone = phone
        self.vendor_email = email

    def __repr__(self):
        return self.vendor_name

