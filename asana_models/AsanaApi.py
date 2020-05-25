import asana

from typing import Optional, Tuple


class AsanaApi:

    def __init__(self, access_token: str, target_workspace: str = 'TEST_WORKSPACE'):
        self._asana_client = asana.Client.access_token(access_token)

        workspaces = dict((ws['name'], ws['gid']) for ws in self._asana_client.workspaces.find_all())

        if target_workspace not in workspaces:
            raise Exception(f'target workspace ({target_workspace}) not found!')

        self._target_workspace_id = workspaces[target_workspace]

    def create_project(self, proj_name: str) -> Tuple[Optional[str], str]:
        try:
            result = self._asana_client.projects.create({'name': proj_name, 'workspace': self._target_workspace_id})
        except Exception as ex:
            return None, f'Error while creating project: {str(ex)}'

        if 'errors' in result:
            return None, result['errors']

        return result['gid'], ''

    def update_project(self, proj_id: str, proj_name: str) -> str:
        try:
            result = self._asana_client.projects.update(proj_id, {'name': proj_name})
        except Exception as ex:
            return f'Error while updating {proj_id} project: {str(ex)}'

        if 'errors' in result:
            return result['errors']

        return ''

    def create_user(self, name: str) -> Tuple[Optional[str], str]:
        try:
            result = self._asana_client.workspaces.add_user(self._target_workspace_id, {'user': name})
        except Exception as ex:
            return None, f'Error while creating user: {str(ex)}'

        if 'errors' in result:
            return None, result['errors']

        return result['gid'], ''
