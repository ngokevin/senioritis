from django.db import models


class School(models.Model):
    id = models.AutoField(primary_key=True)
    school_id = models.IntegerField()
    name = models.CharField(max_length=100)


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    school = models.ForeignKey(School, null=True)
    tag = models.CharField(max_length=5)
    name = models.CharField(max_length=100)
    gpa = models.FloatField()

    def __repr__(self):
        return '%s (%s): %s' % (self.name, self.number, self.gpa)


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    department = models.ForeignKey(Department, null=True)
    name = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    gpa = models.FloatField()
    professor = models.CharField(max_length=100)

    def __repr__(self):
        return '%s%s %s: %s' % (self.department.tag, self.number,
                                self.professor, self.gpa)

