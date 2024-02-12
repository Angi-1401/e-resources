from django.apps import apps
from django.contrib import admin


models = apps.get_app_config("library").get_models()


for model in models:
    try:
        if model.__name__ == "Author":
            admin_class = type(
                model.__name__ + "Admin",
                (admin.ModelAdmin,),
                {"ordering": ["last_name"]},
            )
        elif model.__name__ == "Resource":
            admin_class = type(
                model.__name__ + "Admin", (admin.ModelAdmin,), {"ordering": ["title"]}
            )
        else:
            admin_class = type(
                model.__name__ + "Admin", (admin.ModelAdmin,), {"ordering": ["name"]}
            )
        admin.site.register(model, admin_class)
    except admin.sites.AlreadyRegistered:
        pass
