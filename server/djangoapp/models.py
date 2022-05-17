from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30)
    description = models.CharField(null=False, max_length=100)
    country = models.CharField(null=False, max_length=30)
    
    # Create a toString method for object string representation
    def __str__(self):
        return "Name: " + self.name + " " +  \
            "Description: " + self.description+ " " +  \
            "Country: " + self.country


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    make = models.ForeignKey(CarMake, null=False, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=30)
    dealer_id = models.IntegerField(null=False)
    type = models.CharField(null=False, max_length=30, choices=[('Sedan', 'Sedan'), ('SUV', 'SUV'), ('WAGON','WAGON')])
    year = models.DateField(null=True)
    length = models.IntegerField(null=True)
    width = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    
    # Create a toString method for object string representation
    def __str__(self):
        return "Name: " +self.name + " " + \
            "Dealer ID: " + str(self.dealer_id) + " " +  \
            "Type: " + self.type + " " +  \
            "Year: " + str(self.year) + " " +  \
            "Length: " + str(self.length) + " " +  \
            "Width: " + str(self.width) + " " +  \
            "Height: " + str(self.height)

# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
