from datetime import datetime, timedelta
import unittest
from app import app, db
from app.models import User


class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def password_test(self):
        u = User(username='susan')
        u.set_password('cat')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))

    def test_to_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isUPPER(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_spliting(self):
        s = 'hello beautiful world'
        self.assertEqual(s.split(), ['hello', 'beautiful', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_hashing(self):
        u = User(username='avekomisia')
        u.set_password('1234')
        self.assertFalse(u.check_password('4321'))
        self.assertTrue(u.check_password('1234'))


if __name__ == '__main__':
    unittest.main(verbosity=2)