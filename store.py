class Post:

    def __init__(self, id, photo_url, name, body):

        self.id = id
        self.photo_url = photo_url
        self.name = name
        self.body = body

posts = []

class PostStore:

    def get_all(self):
        # get all posts - الحصول على كل المنشورات
        return posts

    def add(self, post):
        # append post - إضافة منشور
        posts.append(post)
        return posts

    def get_by_id(self, id):
        # search for post by id -id البحث عن منشور بالمعرف
        result = None
        self.id = id
        for post in posts :
            if post.id == id :
                result = post
                break

        return result

    def update(self, id, fields):
        # update post data - id تعديل منشور بالمعرف
        post = self.get_by_id(id)
        post.name = fields['name']
        post.photo_url = fields['photo_url']
        post.body = fields['body']
        return post

    def delete(self, id):
        # delete post by id - id حذف المنشور بالمعرف
        post = self.get_by_id(id)
        posts.remove(post)
        return posts
