"""Git operations for autogpt"""
# from git.repo import Repo

from autogpt.commands.command import command
from autogpt.config import Config
from autogpt.url_utils.validators import validate_url

global_config = Config()


@command(
    "clone_repository",
    "Clone Repository",
    '"repository_url": "<repository_url>", "clone_path": "<clone_path>"',
    global_config.github_username and global_config.github_api_key,
    "Configure github_username and github_api_key.",
)
@validate_url
def clone_repository(repository_url: str, clone_path: str) -> str:
    """Clone a GitHub repository locally.

    Args:
        repository_url (str): The URL of the repository to clone.
        clone_path (str): The path to clone the repository to.

    Returns:
        str: The result of the clone operation.
    """
    split_url = repository_url.split("//")
    auth_repo_url = f"//{global_config.github_username}:{global_config.github_api_key}@".join(split_url)
    try:
        Repo.clone_from(auth_repo_url, clone_path)
        return f"""Cloned {repository_url} to {clone_path}"""
    except Exception as e:
        return f"Error: {str(e)}"
