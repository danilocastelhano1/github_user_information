from typing import Optional

from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class GithubUser:
    """
    Dataclass to serialize the GITHUB response
    """
    id: int = 0
    login: str = ""
    node_id: Optional[str] = ""
    avatar_url: Optional[str] = ""
    gravatar_id: Optional[str] = ""
    url: str = ""
    html_url: str = ""
    followers_url: str = ""
    following_url: str = ""
    gists_url: str = ""
    starred_url: str = ""
    subscriptions_url: str = ""
    organizations_url: str = ""
    repos_url: Optional[str] = ""
    events_url: Optional[str] = ""
    received_events_url: Optional[str] = ""
    type: str = ""
    site_admin: bool = False
    name: Optional[str] = ""
    company: Optional[str] = ""
    blog: Optional[str] = ""
    location: Optional[str] = ""
    email: Optional[str] = ""
    hireable: Optional[str] = ""
    bio: Optional[str] = ""
    twitter_username: Optional[str] = ""
    public_repos: int = ""
    public_gists: int = ""
    followers: int = ""
    following: int = ""
    created_at: str = ""
    updated_at: str = ""
