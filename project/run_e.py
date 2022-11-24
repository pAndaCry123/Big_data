from group_e import app,db


def run_all_services(app,db,port):
    app.app_context().push()
    db.create_all()
    app.run(port=port,debug=True)



if __name__ == "__main__":
    run_all_services(app,db,5004)
