from django.db import models


class Course(models.model):
    id = models.AutoField(primary_key=True)
    department = models.ForeignKey(Department, null=True)
    title = models.CharField()
    name = models.CharField()
    gpa = models.FloatField()
    professor = models.CharField()

    def __repr__(self):
        return '%s%s %s: %s' % (self.department.tag, self.number,
                                self.professor, self.gpa)


class Department(models.model):
    id = models.AutoField(primary_key=True)
    school = models.ForeignKey(School, null=True)
    tag = models.CharField(max_length=5)
    name = models.CharField()
    gpa = models.FloatField()

    def __repr__(self):
        return '%s (%s): %s' % (self.name, self.number, self.gpa)


class School(models.model):
    id = models.AutoField(primary_key=True)
    school_id = models.IntegerField()
    name = models.CharField()
