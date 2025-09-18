OceanGPT-Demo/
│
├── .gitattributes
├── README.md
├── requirements.txt
│
├── config/
│   ├── config.json
│   ├── generation_config.json
│   ├── special_tokens_map.json
│   ├── tokenizer_config.json
│   ├── vocab.json
│
├── src/
│   ├── api/                        # FastAPI Endpoints
│   │   ├── main.py
│   │   └── routes.py
│   │
│   ├── orchestrator/               # MCP Protocol Layer
│   │   ├── mcp_router.py
│   │   ├── query_handler.py
│   │
│   ├── llm/                        # OceanGPT Wrapper
│   │   ├── ocean_gpt.py
│   │   ├── prompts.py
│   │
│   ├── rag/                        # Retrieval + Vector DB
│   │   ├── rag_pipeline.py
│   │   ├── embeddings.py
│   │   └── vector_store.py
│   │
│   ├── database/                   # PostgreSQL ORM
│   │   ├── db_setup.py
│   │   ├── models.py
│   │   └── queries.py
│   │
│   ├── ingestion/                  # Data ingestion from NetCDF
│   │   ├── netcdf_loader.py
│   │   ├── preprocess.py
│   │
│   ├── visualization/              # Dashboards
│   │   ├── dashboard.py
│   │   └── charts.py
│   │
│   └── utils/
│       ├── logger.py
│       └── helpers.py
│
├── data/                           # Sample ARGO datasets
│   ├── indian_ocean/
│   │   └── 19991021_prof.nc
│
└── notebooks/
    ├── demo_query.ipynb
