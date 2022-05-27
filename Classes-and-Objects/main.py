
class Student():
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name,age,tracks,score):
        self.name = name
        self.age = int(age)
        self.tracks = tracks
        self.score = float(score)

    def change_name(self, new_name):
        self.new_name = new_name
        print(self.new_name)

    def change_age(self, new_age):
        self.new_age =int(new_age)
        print(self.new_age)

    def add_track(self, add_track):
        self.add_track = add_track
        print(self.add_track)

    def get_score(self, get_score):
        self.get_score = get_score
        print(self.get_score)
    



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(70)
