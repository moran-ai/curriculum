from datetime import datetime

from ext import db

class Article_type(db.Model):
    __tablename__ = 'type'  # 自定义数据表的名字
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type_name = db.Column(db.String(20), nullable=False)
    articles = db.relationship('Article', backref='type')

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 文章标题
    title = db.Column(db.String(50), nullable=False)
    # 文章内容
    content = db.Column(db.Text, nullable=False)
    # 文章发布时间
    pdatetime = db.Column(db.DateTime, default=datetime.now)

    # 文章的收藏量
    save_num = db.Column(db.Integer, default=0)
    # 文章的点赞
    love_num = db.Column(db.Integer, default=0)

    # 建立外键关系
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('type.id'),nullable=False)
    comments = db.relationship('Comment', backref='article')

class Comment(db.Model):
    # 自定义表名 __tablename__ = '表名'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    comment = db.Column(db.String(255), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))
    cdatetime = db.Column(db.DateTime, default=datetime.now)

    def __str__(self):
        return self.comment
