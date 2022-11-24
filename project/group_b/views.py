from group_b import app,db
from group_b.models import Exsam
from group_b.convert_csv import return_from_main
from group_b.app_schemas import ExsamSchema
from flask import render_template


'''
Getting infos from database
'''





@app.route('/get_group_b')
def group_b():
    result = Exsam.query.all()
    return render_template('index.html', list=result)






'''
Setting inforamtions to databases
'''



@app.route('/set_group_b')
def set_group_b():
    group_b_list = return_from_main('b')

    for item in group_b_list:
        db.session.add(item)
        db.session.commit()
    return "Added to group b"
