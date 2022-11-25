from group_e import app,db
from group_e.models import Exsam
from group_e.convert_csv import return_from_main
from flask import render_template

'''
Getting infos from database
'''





@app.route('/get_group_e')
def group_b():
    result = Exsam.query.all()
    list_data = [0] * 4
    for item in result:
        if item.math_score < 50:
            list_data[0] += 1
        elif item.math_score >= 50 and item.math_score < 70:
            list_data[1] += 1
        elif item.math_score >= 70 and item.math_score < 85:
            list_data[2] += 1
        else:
            list_data[3] += 1

    return render_template('index.html', list=list_data)

@app.route('/group_e')
def groupb():
    return render_template('index.html')

@app.route('/get_group_e_test_prep')
def get_group_b_test_prep():
    result = Exsam.query.all()
    list_data = [0] * 2
    for item in result:
        if item.test_prep == 'none':
            list_data[0] += 1
        else:
            list_data[1] += 1

    return render_template('index.html', prep=list_data)


@app.route('/get_group_e_writting')
def get_group_b_writting():
    result = Exsam.query.all()
    list_data = [0] * 4
    for item in result:
        if item.writing_score < 50:
            list_data[0] += 1
        elif item.writing_score >= 50 and item.writing_score < 70:
            list_data[1] += 1
        elif item.writing_score >= 70 and item.writing_score < 85:
            list_data[2] += 1
        else:
            list_data[3] += 1

    return render_template('index.html', writting=list_data)


@app.route('/get_group_e_reading')
def get_group_b_reading():
    result = Exsam.query.all()
    list_data = [0] * 4
    for item in result:
        if item.reading_score < 50:
            list_data[0] += 1
        elif item.reading_score >= 50 and item.reading_score < 70:
            list_data[1] += 1
        elif item.reading_score >= 70 and item.reading_score < 85:
            list_data[2] += 1
        else:
            list_data[3] += 1

    return render_template('index.html', reading=list_data)


@app.route('/get_group_e_diff_read_write')
def get_group_b_diff_writting_reading():
    result = Exsam.query.all()
    list_data = [0] * 4
    list_data_write = [0] * 4
    for item in result:
        if item.reading_score < 50:
            list_data[0] += 1
        elif item.reading_score >= 50 and item.reading_score < 70:
            list_data[1] += 1
        elif item.reading_score >= 70 and item.reading_score < 85:
            list_data[2] += 1
        elif item.reading_score > 85:
            list_data[3] += 1

        if item.writing_score < 50:
            list_data_write[0] += 1
        elif item.writing_score >= 50 and item.writing_score < 70:
            list_data_write[1] += 1
        elif item.writing_score >= 70 and item.writing_score < 85:
            list_data_write[2] += 1
        elif item.writing_score > 85:
            list_data_write[3] += 1

    return render_template('index.html', read=list_data,write=list_data_write)


@app.route('/get_group_e_diff_math_write')
def get_group_b_diff_math_write():
    result = Exsam.query.all()
    list_data = [0] * 4
    list_data_write = [0] * 4
    for item in result:
        if item.math_score < 50:
            list_data[0] += 1
        elif item.math_score >= 50 and item.math_score < 70:
            list_data[1] += 1
        elif item.math_score >= 70 and item.math_score < 85:
            list_data[2] += 1
        elif item.math_score > 85:
            list_data[3] += 1

        if item.writing_score < 50:
            list_data_write[0] += 1
        elif item.writing_score >= 50 and item.writing_score < 70:
            list_data_write[1] += 1
        elif item.writing_score >= 70 and item.writing_score < 85:
            list_data_write[2] += 1
        elif item.writing_score > 85:
            list_data_write[3] += 1

    return render_template('index.html', math=list_data,write_m=list_data_write)


@app.route('/get_group_e_diff_math_read')
def get_group_b_diff_math_read():
    result = Exsam.query.all()
    list_data = [0] * 4
    list_data_write = [0] * 4
    for item in result:
        if item.math_score < 50:
            list_data[0] += 1
        elif item.math_score >= 50 and item.math_score < 70:
            list_data[1] += 1
        elif item.math_score >= 70 and item.math_score < 85:
            list_data[2] += 1
        elif item.math_score > 85:
            list_data[3] += 1

        if item.reading_score < 50:
            list_data_write[0] += 1
        elif item.reading_score >= 50 and item.reading_score < 70:
            list_data_write[1] += 1
        elif item.reading_score >= 70 and item.reading_score < 85:
            list_data_write[2] += 1
        elif item.reading_score > 85:
            list_data_write[3] += 1

    return render_template('index.html', math_m=list_data,read_m=list_data_write)


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