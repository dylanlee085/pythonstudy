#! /usr/bin/env python
# coding: utf-8


from flask import Flask, render_template, sessions, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = sessions.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you hava change your name')
        sessions['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))


#启动程序
if __name__ == '__main__':
    app.run(debug=True,port = 8888, host = '0.0.0.0')




