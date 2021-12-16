
class Company:
    def __init__(self, country, name, workers, revenue):
        self.country = country
        self.name = name
        self.workers = workers
        self.revenue = revenue

    def check_origin_country(self):
        origin = self.country
        return origin

    def check_number_of_workers(self):
        workforce = f'{self.workers} Total Employees'
        return workforce
    
    def check_taxed_revenue(self):
        tax = .05
        taxed_amount  = float(self.revenue) * .05
        final_revenue = float(self.revenue) - taxed_amount
        return final_revenue
