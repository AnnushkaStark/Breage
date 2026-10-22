from typing import Any

from pydantic import BaseModel
from sqlalchemy import delete
from sqlalchemy import insert
from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession

from src.databases.pg import Base


class RepositoryBase:
    def __init__(self, session: AsyncSession, model: Base):
        self.session = session
        self.model = model

    async def create(self, schema: BaseModel, commit: bool = True) -> Base:
        result = await self.session.execute(
            insert(self.model)
            .values(schema.model_dump(exclude_unset=True, exclude_none=True))
            .returning(self.model)
        )
        if commit:
            await self.session.commit()
        return result.scalar()

    async def update(
        self,
        schema: BaseModel,
        obj_id: int,
        commit: bool = True,
        exclude_unset: bool = False,
    ) -> Base:
        result = await self.session.execute(
            update(self.model)
            .values(**schema.model_dump(exclude_unset=exclude_unset))
            .where(self.model.id == obj_id)
            .returning(self.model)
        )
        if commit:
            await self.session.commit()
        return result.scalar()

    async def get_by_id(self, obj_id) -> Base:
        result = await self.session.execute(
            select(self.model).where(self.model.id == obj_id)
        )
        return result.scalar_one_or_none()

    async def delete(self, obj_id: int, commit: bool = True) -> None:
        statement = delete(self.model).where(self.model.id == obj_id)
        await self.session.execute(statement)
        if commit:
            await self.session.commit()

    async def partitial_update(
        self, obj_id: int, new_value: Any, value_name: str, commit: bool = True
    ) -> None:
        obj = await self.get_by_id(obj_id=obj_id)
        if obj:
            obj.__setattr__(value_name, new_value)

        if commit:
            await self.session.commit()

        return obj

    async def get_multi_by_ids(self, ids: list[int] | None) -> list[Base]:
        result = await self.session.execute(
            select(self.model).where(self.model.id.in_(ids))
        )
        return result.scalars().all()

    async def get_active_by_id(self, obj_id: int) -> Base | None:
        result = await self.session.execute(
            select(self.model).where(
                self.model.id == obj_id, self.model.is_active.is_(True)
            )
        )
        return result.scalar_one_or_none()

    async def create_bulk(
        self, schemas: list[BaseModel], commit: bool = True
    ) -> list[Base]:
        data = [s.model_dump() for s in schemas]
        objs = await self.session.execute(
            insert(self.model).values(data).returning(self.model)
        )
        if commit:
            await self.session.commit()
        return objs.scalars().all()
