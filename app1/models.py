from django.db import models

# Create your models here.
class ScheduleManager(models.Manager):
    def create_schedule(self, name, subject_code, day, start_hour, end_hour):
        schedule = self.create(name=name, subject_code=subject_code, day=day, start_hour=start_hour, end_hour=end_hour)
        return schedule

class Schedule(models.Model):
    name = models.CharField(max_length=256)
    subject_code = models.CharField(max_length=256)
    day = models.CharField(max_length=256)
    start_hour = models.CharField(max_length=256)
    end_hour = models.CharField(max_length=256)

    objects = ScheduleManager()

class SubjectsAvailableManager(models.Manager):
            # subject.name = attribute_array[0]
            # subject.subject_code = attribute_array[1]
            # subject.semester = attribute_array[2]
            # subject.sks = attribute_array[3]
            # subject.day = attribute_array[4]
            # subject.start_hour = attribute_array[5]
            # subject.end_hour = attribute_array[6]
            # subject.class_name = attribute_array[7]
            # subject.lecturer = attribute_array[8]
            # subject.status = attribute_array[9]
    def create_subject(self, arr):
        subject = self.create(name=arr[0], subject_code=arr[1], semester=arr[2], sks=arr[3], day=arr[4], start_hour=arr[5], end_hour=arr[6], class_name=arr[7], lecturer=arr[8], status=arr[9])
        return subject

class SubjectsAvailable(models.Model):
    name = models.CharField(max_length=256)
    subject_code = models.CharField(max_length=256)
    semester = models.CharField(max_length=256)
    sks = models.IntegerField()
    day = models.CharField(max_length=256)
    start_hour = models.CharField(max_length=256)
    end_hour = models.CharField(max_length=256)
    class_name = models.CharField(max_length=256)
    lecturer = models.CharField(max_length=256)
    status = models.CharField(max_length=256)

    objects = SubjectsAvailableManager()

class UserSemesterManager(models.Manager):
    def create_semester(self, semester):
        usersemester = self.create(semester=semester)
        return usersemester

class UserSemester(models.Model):
    semester = models.IntegerField()

    objects = UserSemesterManager()

