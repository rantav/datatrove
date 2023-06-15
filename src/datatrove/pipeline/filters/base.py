from abc import ABC, abstractmethod

from datatrove.data import DocumentsPipeline, Document
from datatrove.pipeline.base import PipelineStep


class BaseFilter(PipelineStep, ABC):
    @abstractmethod
    def __init__(
            self,
            **kwargs
    ):
        """
        Abstract Filter pipeline step.
        A Filter drops samples

        @param args:
        @param kwargs:
        """
        super().__init__(**kwargs)

    @abstractmethod
    def filter(self, doc: Document) -> bool:
        """
        Filter modules' main method.
        Returns true if a sample should be filtered.

        @param doc: sample to (maybe) filter
        @return: bool - whether the doc should be filtered
        """
        return True

    def __call__(self, data: DocumentsPipeline, rank: int = 0, world_size: int = 1) -> DocumentsPipeline:
        """
        step method for Filters.
        Drops documents that if .filter() is False

        @param datapipe: input DocumentsPipeline
        @return: DocumentsPipeline
        """

        for doc in data:
            if self.filter(doc):
                yield doc
