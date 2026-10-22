from typing import Literal

from pydantic import BaseModel

from src.repositories import RepositoryBase


class ServiceBase:
    def __init__(self, repository: RepositoryBase):
        self.repository = repository

    async def manage_obj(
        self,
        action: Literal["create", "update", "remove"],
        schema: BaseModel | None = None,
        obj_id: int | None = None,
        exclude_unset: bool = False,
        commit: bool = True,
    ) -> BaseModel | None:
        match action:
            case "create":
                return await self.repository.create(
                    schema=schema, commit=commit
                )

            case "update":
                return await self.repository.update(
                    schema=schema,
                    commit=commit,
                    exclude_unset=exclude_unset,
                    obj_id=obj_id,
                )

            case "remove":
                return await self.repository.delete(
                    obj_id=obj_id, commit=commit
                )
