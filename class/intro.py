class House:
    bed_type = "Hao"
    bedroom = "3 Bedroom"
    color = ""
    designer = "Engineer"
    location = ""
    reg_no = ""

    def __init__(self):
        print("You have been called")

    def info(self):
        print("House 3 bedroom house")

#hao_1 = House()
# print(hao_1)

# print(hao_1.bed_type)
# print(hao_1.bedroom)
# print(hao_1.designer)

#hao_1.__init__()
    def setup(self, house, color, location, reg_no):
        house.bed_type = "Hao"
        house.bedroom = "3 Bedroom"
        house.color = color
        house.designer = "Engineer"
        house.location = location
        house.reg_no = reg_no
hao_1 = House()
hao_1.bed_type = "Hao"
hao_1.bedroom = "3 bedroom"
hao_1.location = "Kilimani"
hao_1.reg_no = "3453AX"
print(hao_1.__dict__)
