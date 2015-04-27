from django.db import models

class Shell( models.Model):
	class Meta:
		managed = False
		verbose_name_plural = "Bash Shell"

class PyShell( models.Model):
	class Meta:
		managed = False
		verbose_name_plural = "Python Shell"

class DBShell( models.Model):
	class Meta:
		managed = False
		verbose_name_plural = "Database Shell"

class Site( models.Model):
	class Meta:
		managed = False
