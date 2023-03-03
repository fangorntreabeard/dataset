from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Event(models.Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()

    class Meta:
        table = "event"

    def __str__(self):
        return self.name


class Provider(models.Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    address = fields.TextField()


class Currency(models.Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    provider = fields.ForeignKeyField('models.ProviderRouter', on_delete=fields.CASCADE)


class Stat(models.Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    provider = fields.ForeignKeyField('models.ProviderRouter', on_delete=fields.CASCADE)


EventSchema = pydantic_model_creator(Event)
