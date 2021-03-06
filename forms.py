from flask_wtf import FlaskForm  # to use wtforms
from wtforms import StringField, SubmitField, PasswordField, TextAreaField  # to use the relevant fields in flaskform
from wtforms.validators import DataRequired, URL, Email  # to use validators
from flask_ckeditor import CKEditorField


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField(label="Blog Post Title", validators=[DataRequired()])
    subtitle = StringField(label="Subtitle", validators=[DataRequired()])
    img_url = StringField(label="Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Sign Me Up")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let Me In")


class CommentForm(FlaskForm):
    body = CKEditorField("Comment")
    submit = SubmitField("Submit Comment")


class ContactForm(FlaskForm):
    name = StringField(label="Name", validators=[DataRequired()])
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    subject = StringField(label="Subject")
    body = CKEditorField("Message")
    submit = SubmitField(label="Send")