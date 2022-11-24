from group_c import app,db
from group_c.models import Exsam
from group_c.convert_csv import return_from_main
from flask import render_template

'''
Getting infos from database
'''





@app.route('/get_group_c')
def group_c():
    result = Exsam.query.all()
    return render_template('index.html', list=result)


'''
Setting inforamtions to databases
'''



@app.route('/set_group_c')
def set_group_c():
    group_c_list = return_from_main('c')

    for item in group_c_list:
        db.session.add(item)
        db.session.commit()
    return "Added to group c"
