### What is this?

This is **not** a comprehensive documentation of the whole project. This is simply an overview of the general project structure.

New maintainers will probably find this useful as it describes the project at a high level without specific implementation details.

If you *are* looking documentation on a specific feature or implementation, dive into the source code and look at the docstrings and other inline documentation, there should be enough of it.

### Structure.

Within the project folder, there are many different subdirectories. Each subdirectory is a Django app.

App/Subdirectory | Role
-----------------|------
moldyWebsite     | The base app containing general project settings and the base url conf.
common           | Contains files and features that are a commonality among all apps
home             | Contains files and features specific to the home page.
faqs             | Contains files and features specific to the faqs page.

### Common.

Contains a base template that all apps extend. This base template includes a header and navigation menu and has basic styling for the body.

The navigation menu a model to represent each item in the navigation menu. The order, display text and link of these menu items can be altered in the admin site.

### Home.

Contains a template which extends the common base template, and styling specific for the home page.

### Faqs.



### Database.

Currently all models are registered with the django admin.
