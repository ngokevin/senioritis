from django.db import models


class Course(models.model):
    id = models.AutoField(primary_key=True)
    department = models.ForeignKey(Department, null=True)
    title = models.CharField()
    number = models.CharField()
    gpa = models.FloatField()
    professor = models.CharField()

    def __repr__(self):
        return '%s%s %s: %s' % (self.department.tag, self.number,
                                self.professor, self.gpa)


class Department(models.model):
    id = models.AutoField(primary_key=True)
    university = models.ForeignKey(University, null=True)
    tag = models.CharField(max_length=5)
    name = models.CharField()
    gpa = models.FloatField()

    def __repr__(self):
        return '%s (%s): %s' % (self.name, self.number, self.gpa)


class University(models.model):
    id = models.AutoField(primary_key=True)
    university_id = models.IntegerField()
    name = models.CharField()
