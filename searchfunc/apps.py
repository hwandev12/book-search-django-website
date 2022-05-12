from django.apps import AppConfig


class SearchfuncConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'searchfunc'
    
    # add this
    def ready(self):
        import searchfunc.signals
