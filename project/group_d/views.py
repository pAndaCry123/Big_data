from group_d import app,db
from group_d.models import Exsam
from group_d.convert_csv import return_from_main
from flask import render_template

'''
Getting infos from database
'''




@app.route('/get_group_d')
def group_d():
    result = Exsam.query.all()
    return render_template('index.html',list = result)


'''
Setting inforamtions to databases
'''



@app.route('/set_group_d')
def set_group_d():
    group_d_list = return_from_main('d')

    for item in group_d_list:
        db.session.add(item)
        db.session.commit()
    return "Added to group d"
