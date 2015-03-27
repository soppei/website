from flask import render_template, request, session
from app import app
from schedule_api import get_terms
from schedule_api import get_schools
from schedule_api import get_subjects
from schedule_api import get_catalognbrs
from schedule_api import get_sections

@app.route('/')
def index():
    options = {}
    options['terms'] = get_terms()
    return render_template('index.html', **options)
def get_termcode():
	return {{term['TermCode']}} % TermCode

@app.route('/<TermCode>')
def schools(TermCode):
	options ={}
	options['TermCode'] = TermCode
	options['schools'] = get_schools(TermCode)
	session['schoolpage'] = request.url
	return render_template('schools.html', **options)
def get_schoolcode():
	return {{school['SchoolCode']}} % SchoolCode


@app.route('/<TermCode>/<SchoolCode>')
def subjects(TermCode, SchoolCode):
	options = {}
	options['TermCode'] = TermCode
	options['SchoolCode'] = SchoolCode
	options['subjects'] = get_subjects(TermCode, SchoolCode)
	options['backtoschool'] = session['schoolpage']
	session['subjectpage'] = request.url
	return render_template('subjects.html', **options)
def get_subjectCode():
	return {{subject['SubjectCode']}} % SubjectCode

@app.route('/<TermCode>/<SchoolCode>/<SubjectCode>')
def catalognbrs(TermCode, SchoolCode, SubjectCode):
	options = {}
	options['TermCode'] = TermCode
	options['SchoolCode'] = SchoolCode
	options['SubjectCode'] = SubjectCode
	options['catalognbrs'] = get_catalognbrs(TermCode, SchoolCode, SubjectCode)
	options['backtosubject'] = session['subjectpage']
	session['classpage'] = request.url
	return render_template('catalognbrs.html', **options)

def get_catalogNumber():
	return {{catalognbr['CatalogNumber']}} % CatalogNumber

@app.route('/<TermCode>/<SchoolCode>/<SubjectCode>/<CatalogNumber>')
def sections(TermCode, SchoolCode, SubjectCode, CatalogNumber):
	options = {}
	options['TermCode'] = TermCode
	options['SchoolCode'] = SchoolCode
	options['SubjectCode'] = SubjectCode
	options['CatalogNumber'] = CatalogNumber
	options['sections'] = get_sections(TermCode, SchoolCode, SubjectCode, CatalogNumber)
	options['backtoclass'] = session['classpage']
	session['sectionpage'] = request.url
	return render_template('sections.html', **options)
def get_sectionnbr():
	return {{section['SectionNumber']}} % SectionNumber

@app.route('/backpack', methods=['GET', 'POST'])
def backpack():
    options = {}
    if 'backpack' not in session:
        session['backpack'] = []

    if request.method == 'POST':
    	if request.form['type'] =='add':
        	session['backpack'].append({'subject_code':request.form['subject_code'],'catalog_num':request.form['catalog_num'],'section_num': request.form['section_num'], 'meeting_day': request.form['meeting_day'], 'meeting_time': request.form['meeting_time'], 'instructor':request.form['instructor']})
        if request.form['type'] =='remove':
        	session['backpack'].remove({'subject_code':request.form['subject_code'],'catalog_num':request.form['catalog_num'],'section_num': request.form['section_num'], 'meeting_day': request.form['meeting_day'], 'meeting_time': request.form['meeting_time'], 'instructor':request.form['instructor']})
    options['backpack'] = session['backpack']
    options['backtosection'] = session['sectionpage']
    return render_template('backpack.html', **options)

 		



