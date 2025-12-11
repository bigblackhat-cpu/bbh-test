class OCRRouter:
    """
    A router to control all database operations on models in the
    ocr.
    """

    route_app_labels = {"ocrapp",}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "ocr_db"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "ocr_db"
        return None