from redis.asyncio import Redis


class PhonesRepository:
    def __init__(self, redis: Redis):
        self.redis = redis
        self.prefix = "phone"

    def name(self, key: str):
        return f"{self.prefix}:{key}"

    async def set_data(self, phone: str, address: str):
        await self.redis.set(self.name(phone), address)

    async def get_data(self, phone: str):
        return await self.redis.get(self.name(phone))
