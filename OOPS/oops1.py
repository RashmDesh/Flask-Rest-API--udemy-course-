class ClassTest:

    def instance_method(self):
        print(f"called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"called class_method of {cls}")

    @staticmethod
    def static_method():
        print("called static method")
# test=ClassTest()
# test.instance_method()
# ClassTest.instance_method(test)
# ClassTest.class_method()
ClassTest.static_method()