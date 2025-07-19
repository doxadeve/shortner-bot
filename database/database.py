from config import *
from motor.motor_asyncio import AsyncIOMotorClient
import helpers


class Database:
    def __init__(self, uri, database_name):
        self._client = AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.method = self.db["methods"]
        self.stats = self.db["stats"]
        self.users = self.db["users"]

    async def get_db_size(self):
        return (await self.db.command("dbstats"))["dataSize"]

    async def get_bot_stats(self):
        return await self.stats.find_one({"bot": helpers.temp.BOT_USERNAME})

    async def create_stats(self):
        await self.stats.insert_one(
            {
                "bot": helpers.temp.BOT_USERNAME,
                "posts": 0,
                "links": 0,
                "mdisk_links": 0,
                "shortener_links": 0,
            }
        )
    
    async def update_posts(self, count: int):
     try:
        myquery = {
            "bot": helpers.temp.BOT_USERNAME,
        } # Ensure your MongoDB stats collection has a unique `_id` field
        newvalues = {"$inc": {"post_count": count}}  # Increment the `post_count` field
        return await self.stats.update_one(myquery, newvalues)
     except Exception as e:
        logger.error(f"Error in update_posts: {e}")

  

    async def update_links(self, total_links: int, droplink_links: int, mdisk_links: int):
     try:
        myquery = {
            "bot": helpers.temp.BOT_USERNAME,
        } # Ensure the query matches the stats document
        newvalues = {
            "$inc": {
                "total_links": total_links,
                "droplink_links": droplink_links,
                "mdisk_links": mdisk_links,
            }
        }
        return await self.stats.update_one(myquery, newvalues)
     except Exception as e:
        logger.error(f"Error in update_links: {e}")



db = Database(DATABASE_URL, DATABASE_NAME)

