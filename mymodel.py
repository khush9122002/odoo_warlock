from odoo import fields, models

class Demo(models.Model):
    _name = "examkt"  # Table name
    _description = "Demo Description"

    clname = fields.Char("Write Name:", required=True)
    dob = fields.Date("Date of Birth:")
    gen = fields.Selection([("m", "Male"), ("f", "Female")], "Gender")
    age = fields.Integer("Age")
    salary = fields.Float(string="Salary")
    is_active = fields.Boolean(string="Is Active", default=True)
    desc=fields.Text("Description")
    # fi = fields.Binary("File", attachment=True)

    company_id = fields.Many2one("res.company", string="Company")
    task_ids = fields.One2many("project.task", "demo_id", string="Tasks")
    partner_ids = fields.Many2many("res.partner", string="Partners")

class ProjectTask(models.Model):
    _name = "project.task"  # Table name for Task
    _description = "Project Task"

    # Fields in 'project.task'
    name = fields.Char("Task Name", required=True)
    description = fields.Text("Task Description")
    demo_id = fields.Many2one("examkt", string="Related Demo")  # Many-to-one (reverse relation)
    assigned_to = fields.Many2one("res.partner", string="Assigned Partner")  # Many-to-one (link to partner)