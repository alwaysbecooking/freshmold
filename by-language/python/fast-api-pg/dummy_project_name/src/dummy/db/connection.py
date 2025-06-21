from dataclasses import dataclass

from psycopg_pool import AsyncConnectionPool

from dummy.telemetry.log import get_logger

logger = get_logger(__name__)

# Database Architecture:

# 1. Factory Pattern for DatabaseClient:
#    - Use DatabaseClient.create() instead of direct instantiation
#    - Ensures pool is properly initialized and never None
#    - Example: db_client = await DatabaseClient.create(db_name="unwash")

# 2. Hybrid Query Approach:
#    - AdHocQueries class for simple standalone queries
#      - Dependency injection via constructor
#      - Each method manages its own connection
#      - Example: queries = AdHocQueries(db_client); await queries.find_by_hash(...)

#    - Connection-based functions for transaction support
#      - Take connection as parameter
#      - Can be composed within a transaction block
#      - Example: async with conn.transaction():
#        await insert_platform_to_db(conn, platform)

# This approach balances code organization with practical transaction support,
# avoiding unnecessary complexity while still improving on the global variable pattern.


@dataclass
class DatabaseClient:
    """Manages the database connection pool and provides methods for operations."""

    pool: AsyncConnectionPool
    min_size: int = 5
    max_size: int = 20
    conn_str: str = ""  # Complete connection string, or empty to use env vars

    @classmethod
    async def create(
        cls,
        min_size: int = 5,
        max_size: int = 20,
        conn_str: str = "",
    ) -> "DatabaseClient":
        """Initialize a new DatabaseClient instance with a connection pool."""
        # If conn_str is empty, psycopg_pool will automatically pick up connection
        # details from environment variables (e.g., PGDATABASE, PGUSER, etc.).
        # If conn_str is provided, it can contain 'dbname=your_db_name' or a full
        # connection string.
        conn_str_final = conn_str
        pool = AsyncConnectionPool(
            min_size=min_size,
            max_size=max_size,
            conninfo=conn_str_final,
            open=False,
        )
        await pool.open()
        logger.info(
            f"Database connection pool initialized with conn_str: '{conn_str_final}'",
        )
        return cls(
            pool=pool,
            min_size=min_size,
            max_size=max_size,
            conn_str=conn_str_final,
        )

    async def close(self) -> None:
        """Close the database connection pool."""
        await self.pool.close()
        logger.info("Database connection pool closed")

    async def seed(self) -> None:
        """
        Seed the database with initial data if needed.

        Note: Implement actual seeding logic here, considering ON CONFLICT DO NOTHING.
        """
        async with self.pool.connection() as _:
            logger.info("seeded successfully")
