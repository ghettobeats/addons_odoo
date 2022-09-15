import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-oca-hr",
    description="Meta package for oca-hr Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-hr_branch',
        'odoo14-addon-hr_contract_currency',
        'odoo14-addon-hr_contract_multi_job',
        'odoo14-addon-hr_contract_reference',
        'odoo14-addon-hr_contract_type',
        'odoo14-addon-hr_course',
        'odoo14-addon-hr_course_survey',
        'odoo14-addon-hr_department_code',
        'odoo14-addon-hr_employee_age',
        'odoo14-addon-hr_employee_birth_name',
        'odoo14-addon-hr_employee_calendar_planning',
        'odoo14-addon-hr_employee_digitized_signature',
        'odoo14-addon-hr_employee_firstname',
        'odoo14-addon-hr_employee_id',
        'odoo14-addon-hr_employee_lastnames',
        'odoo14-addon-hr_employee_medical_examination',
        'odoo14-addon-hr_employee_partner_external',
        'odoo14-addon-hr_employee_phone_extension',
        'odoo14-addon-hr_employee_ppe',
        'odoo14-addon-hr_employee_relative',
        'odoo14-addon-hr_employee_service',
        'odoo14-addon-hr_employee_service_contract',
        'odoo14-addon-hr_employee_ssn',
        'odoo14-addon-hr_holidays_settings',
        'odoo14-addon-hr_job_category',
        'odoo14-addon-hr_org_chart_overview',
        'odoo14-addon-hr_period',
        'odoo14-addon-hr_personal_equipment_request',
        'odoo14-addon-hr_personal_equipment_request_tier_validation',
        'odoo14-addon-hr_personal_equipment_stock',
        'odoo14-addon-hr_recruitment_notification',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)