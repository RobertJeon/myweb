from django.db import models

# Create your models here.
class Post(models.Model):
    subject = models.CharField(max_length=200)  # 게시글 제목
    content = models.TextField()                # 게시글 내용
    create_date = models.DateTimeField()        # 게시글 작성일

    def __str__(self):
        return self.subject

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)    # 연결된 게시글 삭제시 같이 삭제됨.
    content = models.TextField()                # 댓글 내용
    create_date = models.DateTimeField()        # 댓글 작성일