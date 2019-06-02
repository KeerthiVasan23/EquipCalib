# main.py

from app import app
from db_setup import init_db, db_session
from forms import EquipmentSearchForm,iEquipmentForm,gEquipmentForm,uiEquipmentForm,ugEquipmentForm 
from flask import flash, render_template, request, redirect,url_for
from models import Equipment,History
from tables import Resultsupdate, Resultsview, mResultsupdate
import os
from flask import Flask, render_template, request, send_file
from datetime import timedelta,datetime

APP_FOLDER = os.path.dirname(os.path.abspath(__file__))

init_db()

Date=datetime.today()
print(Date)
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route("/download", methods=['POST'])
def download():
    os.system('python report.py')
    return send_file(APP_FOLDER+'/output.pdf', as_attachment=True)


@app.route('/history_add', methods=['GET', 'POST'])
def history_add():
    return render_template('history_add.html')

@app.route('/reports', methods=['GET', 'POST'])
def reports():
    return render_template('reports.html')


@app.route('/searchi', methods=['GET', 'POST'])
def searchi():    
    search = EquipmentSearchForm(request.form)
    if request.method == 'POST':
        return search_instrument(search)
    return render_template('search.html', form=search)


@app.route('/searchg', methods=['GET', 'POST'])
def searchg():
    search = EquipmentSearchForm(request.form)
    if request.method == 'POST':
        return search_gauge(search)
    return render_template('search.html', form=search)


@app.route('/resultsg')
def search_gauge(search):
    results = []
    search_string = search.data['search']
    qry = db_session.query(History).filter(History.itemcode == search_string)
    results = qry.all()
    table = mResultsupdate(results)
    table.border = True 
    return render_template('historyresults.html', table=table)
gtable=""
@app.route('/resultsi')
def search_instrument(search):
    global gtable
    results = []
    search_string = search.data['search']
    qry = db_session.query(History).filter(History.itemcode == search_string)
    results = qry.all()
    gtable = Resultsupdate(results)
    gtable.border = True 
    return render_template('historyresults.html', table=gtable)

@app.route("/downloadh", methods=['GET', 'POST'])
def downloadh():
	global gtable    
	return render_template('historyresults.html',table=gtable)

@app.route("/downloadhistory", methods=['GET', 'POST'])
def downloadhistory():
	os.system('python historyr.py')
        return send_file(APP_FOLDER+'/output.pdf', as_attachment=True)

@app.route('/view')
def view():
    qry = db_session.query(Equipment)
    results = qry.all()
    table = Resultsview(results)
    table.border = True 
    return render_template('results.html', table=table)

@app.route('/new_add', methods=['GET', 'POST'])
def new_add():
    return render_template('new_add.html')

@app.route('/new_instrument', methods=['GET', 'POST'])
def new_instrument():
    """
    Add a new Equipment
    """
    form = iEquipmentForm(request.form)

    if request.method == 'POST' and form.validate():
        # save the album
        equipment = Equipment()
	his=History()
        isave_changes(his,equipment, form, new=True)
        flash('Equipment added successfully!')
	flash('Itemcode is '+equipment.itemcode)
        return redirect('/')

    return render_template('new_instrument.html', form=form)
	

def isave_changes(his,equipment, form, new=False):
    """
    Save the changes to the database
    """
    # Get data from form and assign it to the correct attributes
    # of the SQLAlchemy table object
    equipment.typee=form.typee.data
    if("Outside micrometer" in form.typee.data):
	data="01"+"001"
	if db_session.query(Equipment).filter(Equipment.itemcode.startswith("01")).count()==0:	
		data=data
	else:
		qry = db_session.query(Equipment).filter(Equipment.itemcode.startswith("01"))
		equipment1 = qry[-1]	
		if(data.startswith("0")):
			data=str(int(int(equipment1.itemcode)+1))
			data="0"+data
		else:	
			data=str(int(int(equipment1.itemcode)+1))
	equipment.itemcode=data
    elif("Inside micrometer" in form.typee.data):
	data="02"+"001"
	if db_session.query(Equipment).filter(Equipment.itemcode.startswith("02")).count()==0:	
		data=data
	else:
		qry = db_session.query(Equipment).filter(Equipment.itemcode.startswith("02"))
		equipment1 = qry[-1]	
		if(data.startswith("0")):
			data=str(int(int(equipment1.itemcode)+1))
			data="0"+data
		else:	
			data=str(int(int(equipment1.itemcode)+1))
	equipment.itemcode=data    	
    elif("Vernier caliper" in form.typee.data):
   	data="03"+"001"
   	if db_session.query(Equipment).filter(Equipment.itemcode.startswith("03")).count()==0:	
   		data=data
   	else:
   		qry = db_session.query(Equipment).filter(Equipment.itemcode.startswith("03"))
		equipment1 = qry[-1]	
		if(data.startswith("0")):
			data=str(int(int(equipment1.itemcode)+1))
			data="0"+data
		else:	
			data=str(int(int(equipment1.itemcode)+1))
	equipment.itemcode=data    	
    elif("Vernier Depth gauge" in form.typee.data):
   	data="04"+"001"
   	if db_session.query(Equipment).filter(Equipment.itemcode.startswith("04")).count()==0:	
   		data=data
   	else:
   		qry = db_session.query(Equipment).filter(Equipment.itemcode.startswith("04"))
		equipment1 = qry[-1]	
		if(data.startswith("0")):
			data=str(int(int(equipment1.itemcode)+1))
			data="0"+data
		else:	
			data=str(int(int(equipment1.itemcode)+1))
	equipment.itemcode=data    	
    elif("Depth micrometer" in form.typee.data):
   	data="05"+"001"
   	if db_session.query(Equipment).filter(Equipment.itemcode.startswith("05")).count()==0:	
   		data=data
   	else:
   		qry = db_session.query(Equipment).filter(Equipment.itemcode.startswith("05"))
		equipment1 = qry[-1]	
		if(data.startswith("0")):
			data=str(int(int(equipment1.itemcode)+1))
			data="0"+data
		else:	
			data=str(int(int(equipment1.itemcode)+1))
	equipment.itemcode=data
    equipment.rangee=form.rangee.data
    equipment.make=form.make.data
    equipment.procdate=form.make.data
    equipment.source=form.source.data
    equipment.accept=form.accept.data
    equipment.lc=form.lc.data
    equipment.freq=form.freq.data
    equipment.stock=form.stock.data
    equipment.center=form.center.data
    equipment.locid=form.locid.data
    equipment.status=form.status.data
    #equipment.lastissue=form.lastissue.data
    #equipment.creationdate=form.creationdate.data
    #equipment.lastedit=form.lastedit.data
    equipment.ticketno=form.ticketno.data
    equipment.empname=form.empname.data
    #his.itemcode=equipment.itemcode
    #his.chkdate=Date
    #his.nextcalib=Date + timedelta(int(form.freq.data))


    if new:
        # Add the new album to the database
        db_session.add(equipment)
	db_session.add(his)
	
    # commit the data to the database
    db_session.commit()


@app.route('/new_gauge', methods=['GET', 'POST'])
def new_gauge():
    """
    Add a new Equipment
    """
    form = gEquipmentForm(request.form)

    if request.method == 'POST' and form.validate():
        # save the album
        equipment = Equipment()
	his=History()
        gsave_changes(his,equipment, form, new=True)
        flash('Equipment added successfully!')
        return redirect('/')
    print(form.make)
    return render_template('new_gauge.html', form=form)

def gsave_changes(his,equipment, form, new=False):
    """
    Save the changes to the database
    """
    # Get data from form and assign it to the correct attributes
    # of the SQLAlchemy table object
    equipment.typee=form.typee.data
    if("Outside micrometer" in form.typee.data):
	data="01"+"001"
	if db_session.query(Equipment).filter(Equipment.itemcode.startswith("01")).count()==0:	
		data=data
	else:
		qry = db_session.query(Equipment).filter(Equipment.itemcode.startswith("01"))
		equipment1 = qry[-1]	
		if(data.startswith("0")):
			data=str(int(int(equipment1.itemcode)+1))
			data="0"+data
		else:	
			data=str(int(int(equipment1.itemcode)+1))
	equipment.itemcode=data
    elif("Inside micrometer" in form.typee.data):
	data="02"+"001"
	if db_session.query(Equipment).filter(Equipment.itemcode.startswith("02")).count()==0:	
		data=data
	else:
		qry = db_session.query(Equipment).filter(Equipment.itemcode.startswith("02"))
		equipment1 = qry[-1]	
		if(data.startswith("0")):
			data=str(int(int(equipment1.itemcode)+1))
			data="0"+data
		else:	
			data=str(int(int(equipment1.itemcode)+1))
	equipment.itemcode=data    	
    elif("Vernier caliper" in form.typee.data):
   	data="03"+"001"
   	if db_session.query(Equipment).filter(Equipment.itemcode.startswith("03")).count()==0:	
   		data=data
   	else:
   		qry = db_session.query(Equipment).filter(Equipment.itemcode.startswith("03"))
		equipment1 = qry[-1]	
		if(data.startswith("0")):
			data=str(int(int(equipment1.itemcode)+1))
			data="0"+data
		else:	
			data=str(int(int(equipment1.itemcode)+1))
	equipment.itemcode=data    	
    elif("Vernier Depth gauge" in form.typee.data):
   	data="04"+"001"
   	if db_session.query(Equipment).filter(Equipment.itemcode.startswith("04")).count()==0:	
   		data=data
   	else:
   		qry = db_session.query(Equipment).filter(Equipment.itemcode.startswith("04"))
		equipment1 = qry[-1]	
		if(data.startswith("0")):
			data=str(int(int(equipment1.itemcode)+1))
			data="0"+data
		else:	
			data=str(int(int(equipment1.itemcode)+1))
	equipment.itemcode=data    	
    elif("Depth micrometer" in form.typee.data):
   	data="05"+"001"
   	if db_session.query(Equipment).filter(Equipment.itemcode.startswith("05")).count()==0:	
   		data=data
   	else:
   		qry = db_session.query(Equipment).filter(Equipment.itemcode.startswith("05"))
		equipment1 = qry[-1]	
		if(data.startswith("0")):
			data=str(int(int(equipment1.itemcode)+1))
			data="0"+data
		else:	
			data=str(int(int(equipment1.itemcode)+1))
	equipment.itemcode=data
    equipment.rangee=form.rangee.data
    equipment.make=form.make.data
    equipment.procdate=form.make.data
    equipment.source=form.source.data
    equipment.accept=form.accept.data
    equipment.lc=form.lc.data
    equipment.freq=form.freq.data
    equipment.stock=form.stock.data
    equipment.center=form.center.data
    equipment.locid=form.locid.data
    equipment.status=form.status.data
    #equipment.lastissue=form.lastissue.data
    #equipment.creationdate=form.creationdate.data
    #equipment.lastedit=form.lastedit.data
    equipment.ticketno=form.ticketno.data
    equipment.empname=form.empname.data
    equipment.ngmin=form.ngmin.data
    equipment.ngmax=form.ngmax.data
    equipment.gumin=form.gumin.data
    equipment.gumax=form.gumax.data
    equipment.nogmin=form.nogmin.data
    equipment.nogmax=form.nogmax.data
    equipment.sizemin=form.sizemin.data
    equipment.sizemax=form.sizemax.data
    #his.itemcode=equipment.itemcode
    #his.chkdate=Date
    #his.nextcalib=Date+timedelta(days=int(form.freq.data))

    if new:
        # Add the new album to the database
        db_session.add(equipment)
	db_session.add(his)
	
    # commit the data to the database
    db_session.commit()

'''
@app.route('/item/<int:id>', methods=['GET', 'POST'])
def edit(id):
    qry = db_session.query(Equipment).filter(
                Equipment.id==id)
    equipment = qry.first()

    if equipment:
        form = EquipmentForm(formdata=request.form, obj=equipment)
        if request.method == 'POST' and form.validate():
            # save edits
            isave_changes(equipment, form)
            flash('Data updated successfully!')
            return redirect('/')
        return render_template('edit_album.html', form=form)
    else:
        return 'Error loading #{id}'.format(id=id)

@app.route('/item/<int:id>', methods=['GET', 'POST'])
def edit(id):
    qry = db_session.query(Equipment).filter(
                Equipment.id==id)
    equipment = qry.first()

    if equipment:
        form = EquipmentForm(formdata=request.form, obj=equipment)
        if request.method == 'POST' and form.validate():
            # save edits
            gsave_changes(equipment, form)
            flash('Data updated successfully!')
            return redirect('/')
        return render_template('edit_album.html', form=form)
    else:
        return 'Error loading #{id}'.format(id=id) '''


@app.route('/update_add', methods=['GET', 'POST'])
def update_add():
    return render_template('update_add.html')

@app.route('/update_instrument', methods=['GET', 'POST'])
def update_instrument():
    """
    Update date Instrument
    """
    form = uiEquipmentForm(request.form)

    if request.method == 'POST' and form.validate():
        # save the album
        history = History()
        uisave_changes(history, form, new=True)
        flash('Equipment added successfully!')
        return redirect('/')

    return render_template('update_instrument.html', form=form)

def uisave_changes(equipment, form, new=False):
    """
    Save the changes to the database
    """
    # Get data from form and assign it to the correct attributes
    # of the SQLAlchemy table object
    equipment.itemcode=form.itemcode.data
    equipment.masterref=form.masterref.data
    #equipment.chkdate=form.chkdate.data
    equipment.chkdate=Date							#automatic check date update
    equipment.calibby=form.calibby.data
    equipment.remarks=form.remarks.data
    #equipment.nextcalib=form.nextcalib.data
    equipment.nextcalib=equipment.chkdate+timedelta(days=int(equipment.calibby)) #auto nextcalib date update ,calibby is freaquency
    equipment.sd1=form.sd1.data
    equipment.sd2=form.sd2.data
    equipment.sd3=form.sd3.data
    equipment.sd4=form.sd4.data
    equipment.sd5=form.sd5.data
    equipment.od1=form.od1.data
    equipment.od2=form.od2.data
    equipment.od3=form.od3.data
    equipment.od4=form.od4.data
    equipment.od5=form.od5.data

    if new:
        # Add the new album to the database
        db_session.add(equipment)
	
    # commit the data to the database
    db_session.commit()

@app.route('/update_gauge', methods=['GET', 'POST'])
def update_gauge():
    """
    Update date gauge
    """
    form = ugEquipmentForm(request.form)

    if request.method == 'POST' and form.validate():
        # save the album
        history = History()
        ugsave_changes(history, form, new=True)
        flash('Equipment added successfully!')
        return redirect('/')

    return render_template('update_gauge.html', form=form)

def ugsave_changes(equipment, form, new=False):
    """
    Save the changes to the database
    """
    # Get data from form and assign it to the correct attributes
    # of the SQLAlchemy table object
    equipment.itemcode=form.itemcode.data
    equipment.masterref=form.masterref.data
    #equipment.chkdate=form.chkdate.data
    equipment.chkdate=Date								#automatic check date update
    equipment.calibby=form.calibby.data
    equipment.remarks=form.remarks.data
    #equipment.nextcalib=form.nextcalib.data
    equipment.nextcalib=equipment.chkdate+timedelta(days=int(equipment.calibby))	#auto nextcalib date update ,calibby is freaquency
    equipment.gmajd1=form.gmajd1.data
    equipment.ngmajd1=form.ngmajd1.data
    equipment.geffd1=form.geffd1.data
    equipment.ngeffd1=form.ngeffd1.data
    equipment.gpitd1=form.gpitd1.data
    equipment.ngpitd1=form.ngpitd1.data
    equipment.gmajd2=form.gmajd2.data
    equipment.ngmajd2=form.ngmajd2.data
    equipment.geffd2=form.geffd2.data
    equipment.ngeffd2=form.ngeffd2.data
    equipment.gpitd2=form.gpitd2.data
    equipment.ngpitd2=form.ngpitd2.data

    if new:
        # Add the new album to the database
        db_session.add(equipment)

    # commit the data to the database
    db_session.commit()

if __name__ == '__main__':
    import os
    if 'WINGDB_ACTIVE' in os.environ:
        app.debug = False
    app.run(host='127.0.0.1',port=5001)
