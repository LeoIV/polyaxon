import uuid

from django.conf import settings
from django.core.validators import validate_slug
from django.db import models
from django.utils.functional import cached_property

from db.models.abstract_jobs import TensorboardJobMixin
from db.models.unique_names import PROJECT_UNIQUE_NAME_FORMAT
from db.models.utils import DescribableModel, DiffModel, ReadmeModel, TagModel
from libs.blacklist import validate_blacklist_name


class Project(DiffModel, DescribableModel, ReadmeModel, TagModel, TensorboardJobMixin):
    """A model that represents a set of experiments to solve a specific problem."""
    CACHED_PROPERTIES = ['notebook', 'has_notebook', 'tensorboard', 'has_tensorboard']

    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        null=False)
    name = models.CharField(
        max_length=128,
        validators=[validate_slug, validate_blacklist_name])
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='projects')
    is_public = models.BooleanField(
        default=True,
        help_text='If project is public or private.')

    def __str__(self):
        return self.unique_name

    class Meta:
        app_label = 'db'
        unique_together = (('user', 'name'),)

    @property
    def unique_name(self):
        return PROJECT_UNIQUE_NAME_FORMAT.format(
            user=self.user.username,
            project=self.name)

    @property
    def has_code(self):
        return hasattr(self, 'repo')

    @cached_property
    def notebook(self):
        return self.notebook_jobs.last()

    @cached_property
    def has_notebook(self):
        notebook = self.notebook
        return notebook and notebook.is_running

    @cached_property
    def tensorboard(self):
        return self.tensorboard_jobs.filter(experiment=None, experiment_group=None).last()

    @cached_property
    def has_tensorboard(self):
        tensorboard = self.tensorboard
        return tensorboard and tensorboard.is_running
