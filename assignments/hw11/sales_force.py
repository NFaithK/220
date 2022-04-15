"""Faith Kelley
 hw 11.py
"""


class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        open_file = open(file_name, "r")
        self.sales_people = open_file.readlines()

    def quota_report(self, quota):
        id = []
        employee = []
        sales = []
        total = []
        list = []
        nlist = []
        olist = []
        for i in self.sales_people:
            sales_list = i.split(", ")
            id.append(sales_list[0])
            employee.append(sales_list[1])
            sales.append(sales_list[2])
        for j in sales:
            sales_spl = j.split(" ")
            acc = 0
            for d in sales_spl:
                acc += float(d)
            total.append(acc)
        for y in total:
            if y >= quota:
                list.append(bool(1))
        for f in range(4):
            nlist.append(int(id[f]))
            nlist.append(employee[f])
            nlist.append(total[f])
            nlist.append(list[f])
            olist.append(nlist)

    def top_seller(self):
        name_list = []
        max = 0
        for person in self.sales_people:
            if person.total_sales() > max:
                max = person.total_sales()
        for person in self.sales_people:
            if max == person.total_sales():
                name_list.append(person)
        return name_list

    def individual_sales(self, employee_id):
        for person in self.sales_people:
            if person == employee_id:
                return person
        return None

    def get_sale_frequences(self):
        frequency = {}
        for people in self.sales_people:
            sales = people.get.sales()
            for sale in sales:
                if frequency.get(sale,None) == None:
                    frequency[sale] = 1
                else:
                    frequency[sale] += 1
        return frequency








