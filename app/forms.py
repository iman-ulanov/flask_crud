import string
from datetime import date

from flask_login import current_user
from flask_wtf import FlaskForm
import wtforms as ws

from .models import Course
from app import app



class UserForm(FlaskForm):
    username = ws.StringField('Имя пользователя', validators=[
        ws.validators.DataRequired(), ws.validators.Length(min=4, max=20)])
    password = ws.PasswordField('Пароль', validators=[
        ws.validators.DataRequired(), ws.validators.Length(min=8, max=24)])


class StudentForm(FlaskForm):
    name = ws.StringField('ФИО студента', validators=[ws.validators.DataRequired()])
    birth_date = ws.DateField('Дата рождения', validators=[ws.validators.DataRequired()])
    phone_number = ws.TelField('Номер телефона', validators=[ws.validators.DataRequired(), ws.validators.Length(min=13, max=20)])
    course_id = ws.SelectField('Курс', choices=[])
    admin_name = current_user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.course_choose = []

        with app.app_context():
            for course in Course.query.all():
                self.course_choose.append((course.id, course.name))
        self._fields['course_id'].choices = self.course_choose

    def validate_name(self, field):
        spiltted_name = field.data.split(' ')
        if len(spiltted_name) == 1:
            raise ws.ValidationError('ФИО не может состоять из одного слова')
        for name in spiltted_name:
            if not name.isalpha():
                raise ws.ValidationError('В ФИО не должно быть спец.символов и чисел')
        for i in string.ascii_letters:
            if i in field.data:
                raise ws.ValidationError('ФИО должен состоять только из кириллицы')


    def validate_phone_number(self, field):
        if field.data[0] != '+':
            raise ws.ValidationError('введите номер через код страны. Например(Кыргызстан: +996)')


    def validate_birth_date(self, field):
        if date.today().year - field.data.year < 16:
            raise ws.ValidationError('Студенту не может быть меньше 16 лет')



class CourseForm(FlaskForm):
    name = ws.StringField('Название курса')
    time = ws.IntegerField('Длительность курса в месяцах')





