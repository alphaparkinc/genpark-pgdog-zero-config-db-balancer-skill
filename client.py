class PgDogDbBalancerClient:
    def get_route(self, sql_statement: str) -> dict:
        stmt = sql_statement.upper()
        target = "replica_read_node" if stmt.startswith("SELECT") else "primary_write_node"
        return {"route_target": target}