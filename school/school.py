from openerp import fields,models,api


class HRinherit(models.Model):
    _inherit ="hr.employee"
    pass

# tabt  to term to each  student  many2ne
class termInEachYear(models.Model):
    _name = "school.student"
    name = fields.Char(string="Student", required=True)
    grade_class =fields.Char()
    school_year= fields.Char()
    sujects_ids=fields.One2many("school.score_subject","term_id",string="Subjects")

#table many2one term
class ScoreForSubjects(models.Model):
    _name = "school.score_subject"

    term = fields.Selection([('first_term', 'First Term'),
                             ('second_term', 'Second Term'),
                             ('final_term', 'Final Term'),
                             ('third_term', 'Third Term'),
                             ('fourth_term', 'Fourth Term'),
                             ('final_exam2', 'Final Term')], string="Term")
    sub_english = fields.Char()
    sub_social_student = fields.Char()
    sub_math = fields.Char()
    sub_science = fields.Char()
    sub_french = fields.Char()
    sub_arabic = fields.Char()
    sub_art = fields.Char()
    sub_pe = fields.Char()
    sub_music = fields.Char()
    sub_computer = fields.Char()
    sub_religion = fields.Char()
    term_id = fields.Many2one('school.student' , string="Term")

    pass