class student:
    def name(self):
        print('name...')
class academic_performance(student):
    def Acad_score(self):
        print('academic score..90% and above')
class ECA(student):
    def ECA_score(self):
        print('ECA score...60% and above')
class result(academic_performance,ECA):
    def Eligibility(self):
        print("***minimum eligiblity to apply *****")
        self.Acad_score()
        self.ECA_score()
R=result()
R.Eligibility()

