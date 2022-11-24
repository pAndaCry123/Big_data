from group_e import app,db
from group_e.models import Exsam
from group_e.convert_csv import return_from_main
from flask import render_template

'''
Getting infos from database
'''



@app.route('/get_group_e')
def group_e():
    result = Exsam.query.all()
    return render_template('index.html', list=result)


'''
Setting inforamtions to databases
'''



@app.route('/set_group_e')
def set_group_e():
    group_e_list = return_from_main('e')

    for item in group_e_list:
        db.session.add(item)
        db.session.commit()
    return "Added to group e"