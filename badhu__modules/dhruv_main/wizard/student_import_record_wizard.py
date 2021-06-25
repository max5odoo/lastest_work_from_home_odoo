from odoo import api, models, fields, _
try:
    import xlrd
    try:
        from xlrd import xlsx
    except ImportError:
        xlsx = None
except ImportError:
    xlrd = xlsx = None
import base64

from odoo.exceptions import UserError, ValidationError




class StudentRecordWizard(models.TransientModel):
    _name = "school.student.record.wizard"

   

    data = fields.Binary('File')



    def check_and_save(self, row): #['max_W','male','g@gmail.com']
        """
                 Verify and save
                 :param row: excel line
                 :return: task object id
        """
        name = row[0].value if row[0].value else False
        gender = row[1].value if row[1].value else False
        email_id = row[2].value if row[2].value else False
        

        if not name and email_id:
            raise ValidationError("Name and Email Id cannot be empty!")

        vals = {
                'name': name,
                'gender': gender,
                'email_id': email_id,
              
            }

        return self.env['school.student.detail'].create(vals).id

    def import_records(self):
        file = self.data
        workbook = xlrd.open_workbook(file_contents=base64.decodebytes(file))
        if workbook:
            print("\n\n\n workbook is opened... \n\n\n")
            sheet = workbook.sheet_by_index(0)

            res_id = []

            for rowx in range(1, sheet.nrows):
                print(f"\n\n\n {sheet.row(rowx)} \n\n\n")
                
                row = sheet.row(rowx)

                try:
                    res = self.check_and_save(row)#based upon no of rows  ->  no. of create will be called
                except:
                    raise ValidationError(_('Excel file error, please check if the excel file matches the import template format!'))

                res_id.append(res) 

            print(f"\n\n\n final records : {res_id} \n\n\n")

            return  {
                'type': 'ir.actions.act_window',
                'name': 'Students',
                'view_mode': 'tree,form', 
                'res_model': 'school.student.detail',
            }

        






            


      
