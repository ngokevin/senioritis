from django.db import models


class School(models.Model):
    id = models.AutoField(primary_key=True)
    school_id = models.IntegerField()
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return '%s %s' % (self.name, self.school_id)

    def __repr__(self):
        return '%s %s' % (self.name, self.school_id)

class Department(models.Model):
    id = models.AutoField(primary_key=True)
    school = models.ForeignKey(School, null=True)
    tag = models.CharField(max_length=10, null=True)
    name = models.CharField(max_length=100, null=True)
    gpa = models.FloatField(null=True)

    def __str__(self):
        return '%s (%s)' % (self.tag, self.name)

    def __repr__(self):
        return '%s (%s)' % (self.tag, self.name)


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    department = models.ForeignKey(Department, null=True)
    name = models.CharField(max_length=10, null=True)
    title = models.CharField(max_length=400, null=True)
    gpa = models.FloatField(null=True)
    professor = models.CharField(max_length=100, null=True)

    def __str__(self):
        return '%s %s: %s' % (self.title, self.professor, self.gpa)

    def __repr__(self):
        return '%s %s: %s' % (self.title, self.professor, self.gpa)
