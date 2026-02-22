# AI Knowledge Gateway

The AI Knowledge Gateway is responsible for ingesting code and documentation,
chunking it intelligently, generating embeddings, and storing them in a vector database.

It acts as a bridge between raw source files and semantic search.


## Architecture Overview

The system is composed of the following components:

- API Layer (FastAPI)
- Ingestion Service
- Chunking Module
- Embedding Service
- Vector Storage

Each layer has a clear separation of responsibility.


## Ingestion Flow

When a file is submitted for ingestion:

1. The API validates the file path.
2. The file is loaded into memory.
3. The appropriate chunker is selected using a factory.
4. The content is chunked into semantically meaningful segments.
5. Embeddings are generated for each chunk.
6. Chunks and embeddings are stored in the vector database.

This ensures scalability and modularity.


## Chunking Strategy

Chunking is not random splitting.

The system must preserve semantic meaning by:

- Splitting Markdown by headings.
- Splitting code by class and function boundaries.
- Adding overlap between chunks.
- Maintaining metadata for better retrieval.

A poor chunking strategy reduces retrieval quality significantly.


## Shard Routing Example

In a distributed system, shard routing determines where data is stored.

For example:

- If tag_id % 4 == 0 → shard_0
- If tag_id % 4 == 1 → shard_1
- If tag_id % 4 == 2 → shard_2
- If tag_id % 4 == 3 → shard_3

This ensures even distribution of data across shards.


## Large Section Example

Below is a deliberately long section to test chunk splitting behavior.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

Repeat this paragraph several times to simulate a large section.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
