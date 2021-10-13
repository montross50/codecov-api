from core.models import Repository
from codecov.commands.base import BaseInteractor

from codecov_auth.helpers import current_user_part_of_org


class GetUploadTokenInteractor(BaseInteractor):
    def execute(self, repository):
        if not current_user_part_of_org(self.current_user, repository.author):
            return None
        return repository.upload_token
