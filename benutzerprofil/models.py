from django.db import models
# our Database
class Post(models.Model):    # our discriptor-> ist ein Klass in anderes Klass benuzt werden
    title = models.CharField(max_length=50)
    text = models.TextField(blank=True)
    is_enable = models.BooleanField(default=False)
    publish_date = models.DateField(null=True, blank=True)  #null=true heißt können wir Wert "null" speeichern
    created_time = models.DateTimeField(auto_now_add=True)   # gelöscht, weil ich als Automatik definiert
    updated_time = models.DateTimeField(auto_now=True)


    def __str__(self):
        # return self.title  -> ohne id neben
        return '{}- {}' .format(self.pk, self.title) # id neben der post

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)