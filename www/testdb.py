import transwarp.db
import hashlib
from models import User, Blog, Comment
if __name__ == '__main__':
    transwarp.db.create_engine('root', 'root', 'awesome', host='192.168.56.104')
    u = User(name='admin', email='admin@example.com', password='admin', image='about:blank')
    u.update()
    import logging
    logging.basicConfig(level=logging.DEBUG)
    # u = User(name='Test', email='test@example.com', password='ttttt', image='about:blank').update()
    user = User.findall(where='name=?', args=['Test'])
    print user
