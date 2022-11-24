from app import app,db
from app.models import Exsam
from app.convert_csv import return_from_main
from flask import render_template


'''
Getting infos from database
'''



@app.route('/get_group_a')
def group_a():
    result = Exsam.query.all()
    return render_template('index.html', list=result)





'''
Setting inforamtions to databases
'''

@app.route('/set_group_a')
def set_group_a():
    group_a_list = return_from_main('a')

    for item in group_a_list:
        db.session.add(item)
        db.session.commit()

    return "Added to group a"

