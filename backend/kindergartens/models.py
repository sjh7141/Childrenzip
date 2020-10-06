from django.db import models
from django.conf import settings

# Create your models here.

class Kindergarten(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    lat = models.FloatField(null=True, blank=True, default=0.0)
    lng = models.FloatField(null=True, blank=True, default=0.0)
    organization_name = models.CharField(max_length=100)
    director_name = models.CharField(max_length=50)
    establishment_type = models.CharField(max_length=50)
    created_date = models.DateField()
    agency = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    homepage = models.TextField()
    address = models.CharField(max_length=255)
    school_bus = models.BooleanField()
    grade = models.SmallIntegerField()
    start_time = models.IntegerField()
    finish_time = models.IntegerField()
    general = models.BooleanField()
    infants = models.BooleanField()
    disabled = models.BooleanField()
    disabled_integration = models.BooleanField()
    after_school = models.BooleanField()
    after_school_inclusion = models.BooleanField()
    extension = models.BooleanField()
    holiday = models.BooleanField()
    all_day = models.BooleanField()
    part_time = models.BooleanField()
    office = models.BooleanField()
    public = models.BooleanField()
    private = models.BooleanField()
    family = models.BooleanField()
    corporate = models.BooleanField()
    cooperation = models.BooleanField()
    welfare = models.BooleanField()

    score = models.FloatField()
    area_columns = models.CharField(max_length=255)
    area_info = models.TextField()
    building_columns = models.CharField(max_length=255)
    building_info = models.TextField()
    cctv_columns = models.CharField(max_length=255)
    cctv_info = models.TextField()
    area_per_cctv = models.FloatField()
    
    age_by_class_columns = models.CharField(max_length=255)
    age_by_class_info = models.TextField()
    staff_columns = models.CharField(max_length=255)
    staff_info = models.TextField()
    continuous_columns = models.CharField(max_length=255)
    continuous_info = models.TextField()
    child_per_staff = models.FloatField()
    fee_columns = models.CharField(max_length=255)
    fee_info = models.TextField()
    other_fee_columns = models.CharField(max_length=255)
    other_fee_info = models.TextField()
    special_activity_columns = models.CharField(max_length=255)
    special_activity_info = models.TextField()
    monthly_fee = models.CharField(max_length=255)

    zero_year_old = models.CharField(max_length=20)
    one_year_old = models.CharField(max_length=20)
    two_year_old = models.CharField(max_length=20)
    three_year_old = models.CharField(max_length=20)
    four_year_old = models.CharField(max_length=20)
    five_year_old = models.CharField(max_length=20)

    poisoning_columns = models.CharField(max_length=255)
    poisoning_info = models.TextField()
    air_quality_columns = models.CharField(max_length=255)
    air_quality_info = models.TextField()
    disinfection_columns = models.CharField(max_length=255)
    disinfection_info = models.TextField()
    water_quality_columns = models.CharField(max_length=255)
    water_quality_info = models.TextField()
    rating_certificate_columns = models.CharField(max_length=255)
    rating_certificate_info = models.TextField()
    rating_history_columns = models.CharField(max_length=255)
    rating_history_info = models.TextField()
    extension_class_status_columns = models.CharField(max_length=255)
    extension_class_status_info = models.TextField()
    extension_class_program_columns = models.CharField(max_length=255)
    extension_class_program_info = models.TextField()
    has_extension_class = models.BooleanField()
    language = models.BooleanField()
    culture = models.BooleanField()
    sport = models.BooleanField()
    science = models.BooleanField()
    other = models.BooleanField()
    program_by_age = models.TextField()
    cctv_grade = models.IntegerField()
    staff_grade = models.IntegerField()
    image = models.ImageField(upload_to="kindergarten", null=True)

    weight_users = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Weight', related_name='weight_kindergartens')
    wish_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='wish_kindergartens')
    
    
class Weight(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    kindergarten = models.ForeignKey(Kindergarten, on_delete=models.CASCADE)
    weight = models.IntegerField()


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
    kindergarten = models.ForeignKey(Kindergarten, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    score_teacher = models.FloatField()
    score_director = models.FloatField()
    score_environment = models.FloatField()
    pros = models.TextField()
    cons = models.TextField()


class City(models.Model):
    name = models.CharField(max_length=10)


class Borough(models.Model):
    name = models.CharField(max_length=20)
    city = models.ForeignKey(City, on_delete=models.CASCADE)


class Village(models.Model):
    name = models.CharField(max_length=20)
    borough = models.ForeignKey(Borough, on_delete=models.CASCADE)


