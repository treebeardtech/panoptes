from typing import List

from pydantic import BaseModel


class App(BaseModel):
    name: str


class CheckRun(BaseModel):
    databaseId: str
    conclusion: str
    name: str


class CheckRuns(BaseModel):
    nodes: List[CheckRun]


class CheckSuite(BaseModel):
    app: App
    checkRuns: CheckRuns


class CheckSuites(BaseModel):
    nodes: List[CheckSuite]


class Commit(BaseModel):
    oid: str
    checkSuites: CheckSuites


class Commits(BaseModel):
    commit: List[Commit]


class PRCommit(BaseModel):
    commit: Commit


class PRCommits(BaseModel):
    nodes: List[PRCommit]


class PullRequest(BaseModel):
    number: int
    commits: PRCommits