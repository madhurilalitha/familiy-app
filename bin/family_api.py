

class Family_api:
    def __init__(self, gender, family_name, age, count):
        self.gender = gender
        self.family_name = family_name
        self.age = age
        self.count = count

    def get_size(self):
        pass
        # DB Connection, count the number of rows with same family name(input1)

    def get_female_count(self):
        pass
        # DB connection, count(input1) the number of rows with gender column as female

    def get_children_count(self):
        pass
        # DB connection, count(input1) the number of rows with AGE column less than 10 years

    def add_new_member(self):
        pass
        # DB connection, add family name(input1), age(input2), gender(input3)

    def remove_member(self):
        pass
        # DB connection, remove row based on family name(input1), age(input2), gender(input3)