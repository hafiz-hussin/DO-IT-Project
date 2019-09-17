from django.db import models

# Create your models here.
class Turtles(models.Model):
    turtle_type = models.CharField(max_length=40)
    image_url = models.ImageField(upload_to='turtle_pics/')
    locations = models.CharField(max_length=200)
    size = models.CharField(max_length=200)
    lifespan = models.CharField(max_length=200)
    diet = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.turtle_type

    class Meta:
        verbose_name = "Turtle"
        verbose_name_plural = "Turtles"


class Answer_Options(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Answer Option"
        verbose_name_plural = "Answer Options"

class Quiz(models.Model):
    quiz_name = models.CharField(max_length=200)
    image_url = models.ImageField(upload_to='question_pics/', default='img_1')
    question_count = models.IntegerField(default=0)
    question_type = models.CharField(max_length=100, default="this is type")
    description = models.TextField(default="this is description")
    quiz_reward = models.DecimalField(max_digits=10 ,decimal_places= 2, default=0.00)
    quiz_statues = models.BooleanField(default=False)

    def __str__(self):
        return self.quiz_name

    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizes"


class Quiz_Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, blank=True, default=None, null=True)
    q_type = models.CharField(max_length=50)
    text = models.CharField(max_length=200)
    possible_answers = models.ManyToManyField(Answer_Options)
    selected = models.ForeignKey(Answer_Options, related_name="selected", default=None, on_delete=models.CASCADE, blank=True, null=True)
    correct = models.ForeignKey(Answer_Options, related_name="correct", default=None, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Quiz Question"
        verbose_name_plural = "Quiz Questions"

