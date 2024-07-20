from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    relation_with_user = models.OneToOneField(User, on_delete = models.CASCADE)
    rating = models.IntegerField(default = 0)

    def update_rating(self):
        sum_article_rating = self.article_rating * 3
        sum_comment_rating = self.comment_rating
        pass


class Category(models.Model):
    name_category = models.CharField(unique = True)


class Post(models.Model):
    news = "NW"
    section = "SE"

    POST_TYPES = [
        (news, "Новость"),
        (section, "Статья")]

    relation_with_author = models.ForeignKey(Author, on_delete = models.CASCADE)
    choice_field = models.CharField(max_length=2, choices=POST_TYPES, default=news)
    time_of_text_creation = models.DateTimeField(auto_now_add = True)
    relation_with_post_and_category = models.ManyToManyField(Category, through="PostCategory", on_delete = models.CASCADE)
    article_title = models.CharField()
    article_text = models.TextField()
    article_rating = models.IntegerField(default = 0)

    def preview(self):
        preview_text = self.article_text(max_length = 124)
        return f"{preview_text}..."

    def like(self):
        self.article_rating += 1
        self.save()

    def dislike(self):
        self.article_rating -= 1
        self.save()


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)


class Comment(models.Model):
    relation_with_post = models.ForeignKey(Post, on_delete = models.CASCADE)
    relation_with_user = models.ForeignKey(User, on_delete = models.CASCADE)
    comment_text = models.TextField()
    time_of_comment_creation = models.DateTimeField(auto_now_add = True)
    comment_rating = models.IntegerField(default = 0)

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        self.comment_rating -= 1
        self.save()
