from chunk_analysis import evaluate_chunk_relevance, evaluate_chunk_completeness


chunk = "TiDB is an open-source distributed SQL database designed to support hybrid transactional and analytical processing (HTAP) workloads. " \
        "It provides MySQL compatibility, horizontal scalability, and strong consistency. TiDB is built with a layered architecture, " \
        "including TiKV for storage and PD (Placement Driver) for cluster management. TiDB supports distributed transactions and " \
        "offers features like online DDL changes, automatic sharding, and SQL support for complex queries. For analytics, TiFlash, " \
        "an optional columnar storage engine, enhances performance by enabling real-time HTAP capabilities."

q1 = "How does TiDB achieve real-time HTAP capabilities?"
q2 = "Does TiDB support HTAP workloads?"

result = evaluate_chunk_relevance(chunk, q1)
print(result)
result = evaluate_chunk_relevance(chunk, q2)
print(result)

result = evaluate_chunk_completeness(chunk, q1)
print(result)
result = evaluate_chunk_completeness(chunk, q2)
print(result)