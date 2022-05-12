from datetime import date, timedelta
from django.db import models
from django.contrib.auth.models import User
from treebeard.mp_tree import MP_Node
# Create your models here.

class LeaveRequest(models.Model): 

  LEAVE_TYPES = (
    ('Annual', 'Annual'),
    ('Sick', 'Sick'),
    ('Maternity', 'Maternity'),
    ('Paternity', 'Paternity'),
    ('Other', 'Other'),
  )

  LEAVE_STATUS = (
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Rejected', 'Rejected'),
  )

  user = models.ForeignKey(User, on_delete=models.CASCADE)
  start_date = models.DateField()
  end_date = models.DateField()
  number_of_days = models.PositiveIntegerField()
  status = models.CharField(max_length=100, choices=LEAVE_STATUS, default='Pending')
  type = models.CharField(max_length=100, choices=LEAVE_TYPES, default='Annual')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.user.username + ' - ' + self.type + ' Leave'

  def get_number_of_days(self):
    # We calculate the number of days here


    start_date = self.start_date
    end_date = self.end_date
    number_of_days = end_date - start_date
    count = 0
    for days in range(number_of_days.days):
      if (start_date + timedelta(days)).isoweekday() in [6, 7]:
        continue
      count += 1

    return count 


  def save(self, *args, **kwargs):
    self.number_of_days = self.get_number_of_days() 
    super(LeaveRequest, self).save(*args, **kwargs)
    

class Category(MP_Node):
  name = models.CharField(max_length=100)

  node_order_by = ['name']


  def __str__(self):
    return f'Category: {self.name}'

    

class Product(models.Model):
  name = models.CharField(max_length=100)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)

  def __str__(self):
    return f'Product: {self.name}'
