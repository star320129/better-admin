class DBRouter(object):
    def db_for_read(self, model, **hints):
        # 从库
        return 'read'

    def db_for_write(self, model, **hints):
        # 主库
        return 'default'
