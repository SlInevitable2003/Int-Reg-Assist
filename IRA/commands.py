import click
import os

from IRA import app, db
from IRA.models import illnessModel

from openpyxl import load_workbook

@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')

@app.cli.command()
def loaddb():
    db.create_all()
    prefix = 'raw_data/excel'

    excel_name_list = os.listdir(prefix)
    for excel_name in excel_name_list:
        if excel_name[0] == '~':
            continue

        path = prefix + '/' + excel_name
        wb = load_workbook(path, read_only=True)
        ws = wb.active
        
        department = excel_name.split('.')[0]

        is_top_row = True
        for row in ws.values:
            if is_top_row:
                is_top_row = False
                continue
            name = row[0]
            sympton1 = row[1]
            sympton2 = row[2]
            sympton3 = row[3]
            sympton4 = row[4]
            sympton5 = row[5]
            sympton6 = row[6]

            illness = illnessModel(name=name, 
                                   sympton1=sympton1, 
                                   sympton2=sympton2, 
                                   sympton3=sympton3, 
                                   sympton4=sympton4, 
                                   sympton5=sympton5, 
                                   sympton6=sympton6, 
                                   department=department)
            db.session.add(illness)
    
    db.session.commit()
    click.echo('Done.')