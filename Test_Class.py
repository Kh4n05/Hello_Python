class Food:
    def __init__(self, price, protein_content, caloric_content, significant_micros):
        self.price = price
        self.protein_content = protein_content
        self.caloric_content = caloric_content
        self.significant_micros = significant_micros
        self.protein_per_money = protein_content/ price
        self.is_Worth_it = (self.protein_per_money <= 1/3)
