from .milvus.milvus_memory import MilvusMemory
from .base_storage import BaseStorage


class MilvusStorage(BaseStorage):
    '''Milvus向量存储记忆模块'''
    milvus_memory: MilvusMemory

    def __init__(self, memory_storage_config: dict[str, str]):
        host = memory_storage_config["host"]
        port = memory_storage_config["port"]
        user = memory_storage_config["user"]
        password = memory_storage_config["password"]
        db_name = memory_storage_config["db_name"]
        self.milvus_memory = MilvusMemory(
            host=host, port=port, user=user, password=password, db_name=db_name)

    def search(self, query_text: str, limit: int, expr: str) -> list[str]:

        self.milvus_memory.loda()
        # 查询记忆，并且使用 关联性 + 重要性 + 最近性 算法进行评分
        memories = self.milvus_memory.compute_relevance(
            query_text, limit, expr)
        self.milvus_memory.compute_importance(memories)
        self.milvus_memory.compute_recency(memories)
        self.milvus_memory.normalize_scores(memories)
        self.milvus_memory.release()

        # 排序获得最高分的记忆
        memories = sorted(
            memories, key=lambda m: m["total_score"], reverse=True)

        if len(memories) > 0:
            memories_text = [item['text'] for item in memories]
            memories_text = memories_text[0]
            return [memories_text]
        else:
            return []

    def pageQuery(self, page_num: int, page_size: int, expr: str) -> list[str]:
        self.milvus_memory.loda()
        offset = (page_num - 1) * page_size
        limit = page_size
        result = self.milvus_memory.pageQuery(
            expr=expr, offset=offset, limit=limit)
        self.milvus_memory.release()
        return result

    def save(self, pk: int,  quer_text: str, owner: str) -> None:
        self.milvus_memory.loda()
        self.milvus_memory.insert_memory(pk=pk, text=quer_text, owner=owner)
        self.milvus_memory.release()

    def clear(self, owner: str) -> None:
        self.milvus_memory.loda()
        self.milvus_memory.clear(owner)
        self.milvus_memory.release()
