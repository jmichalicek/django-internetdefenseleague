from setuptools import setup, find_packages

package_data = ['templates/internetdefenseleague/*.html']
dependencies = []
setup(name = "django-internetdefenseleague",
      version = "0.0.1",
      description = "A django app to manage Internet Defense League javascript on sites",
      author = "Justin Michalicek",
      author_email = "jmichalicek@gmail.com",
      url = "https://github.com/jmichalicek/djukebox/",
      license = "www.opensource.org/licenses/bsd-license.php",
      packages = find_packages(),
      #'package' package must contain files (see list above)
      package_data = {'internetdefenseleague' : package_data },
      install_requires = dependencies,
      long_description = "A django app to manage Internet Defense League javascript on sites"
      #This next part it for the Cheese Shop, look a little down the page.
      #classifiers = []
)
