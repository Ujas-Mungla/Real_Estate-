class ListingRouter:
    route_app_labels = {'listing'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read listing models go to 'listings' database.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'listings'
        return None

    def db_for_write(self, model, **hints):
        """ 
        Attempts to write listing models go to 'listings' database.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'listings'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relationships if a model in the listing app is involved.
        """
        if (obj1._meta.app_label in self.route_app_labels or 
            obj2._meta.app_label in self.route_app_labels):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Ensure the listing app's models get migrated only to the 'listings' database.
        """
        if app_label in self.route_app_labels:
            return db == 'listings'
        return None
