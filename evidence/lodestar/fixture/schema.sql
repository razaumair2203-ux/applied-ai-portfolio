-- Minimal public Lodestar fixture schema exercising the real published retrieval SQL.
CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS pgcrypto;

DROP TABLE IF EXISTS chunks;
DROP TABLE IF EXISTS documents;

CREATE TABLE documents (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  source_type text NOT NULL,
  citation_label text NOT NULL,
  title text NOT NULL,
  url text,
  binding_weight smallint NOT NULL CHECK (binding_weight BETWEEN 1 AND 5)
);

CREATE TABLE chunks (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  document_id uuid NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
  chunk_text text NOT NULL,
  chunk_index integer NOT NULL,
  section_label text,
  tsv tsvector GENERATED ALWAYS AS (
    to_tsvector('english', coalesce(section_label, '') || ' ' || chunk_text)
  ) STORED,
  embedding vector(1024),
  criterion_tags text[] NOT NULL DEFAULT '{}',
  visa_class text[] NOT NULL DEFAULT '{}',
  metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
  CONSTRAINT chunks_document_chunk_uidx UNIQUE (document_id, chunk_index)
);

CREATE INDEX chunks_embedding_hnsw_idx ON chunks USING hnsw (embedding vector_cosine_ops);
CREATE INDEX chunks_tsv_gin_idx ON chunks USING gin (tsv);
CREATE INDEX chunks_visa_class_gin_idx ON chunks USING gin (visa_class);
CREATE INDEX chunks_criterion_tags_gin_idx ON chunks USING gin (criterion_tags);
