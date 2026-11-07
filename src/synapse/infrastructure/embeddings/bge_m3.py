from sentence_transformers import SentenceTransformer

from synapse.application.rag.embedding_provider import EmbeddingProvider


class BgeM3EmbeddingProvider(EmbeddingProvider):

    def __init__(self, model_name: str):
        self._model = SentenceTransformer(model_name)

    def embed(self, text: str) -> list[float]:
        vector = self._model.encode(
            text,
            normalize_embeddings=True,
        )

        return vector.tolist()

    def embed_batch(
        self,
        texts: list[str],
    ) -> list[list[float]]:

        vectors = self._model.encode(
            texts,
            normalize_embeddings=True,
        )

        return vectors.tolist()