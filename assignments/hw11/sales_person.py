"""Faith Kelley
"""


class SalesPerson:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def enter_sale(self, sales):
        self.sales = sales

    def total_sales(self):
        return float(self.sales) + float(self.sales)

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if self.total_sales >= quota:
            return True
        return False

    def compare_to(self, other):
        if other > self.total_sales:
            return -1
        if other == self.total_sales:
            return 0
        if other < self.total_sales:
            return 1

    def __str__(self):
        return self.employee_id, self.name, self.total_sales



