**Abstract:**

The project aimed to develop a web document retrieval system focusing on video game-related content. It involved three main phases: crawling web documents, indexing them using TF-IDF, and building a query processor using Flask. The objectives were to collect web documents, create an inverted index for efficient retrieval, and implement a user-friendly interface for querying the indexed documents.

**Development Summary:**

1. **Web Crawling (Phase 1):** 
   - Utilized Scrapy to crawl web documents from Wikipedia, focusing on video game-related pages.
   - Implemented a CrawlSpider to traverse links and extract relevant content.
   - Limited the crawling MAX_DEPTH and MAX_PAGES to avoid excessive resource consumption.

2. **Indexing (Phase 2):**
   - Employed TF-IDF (Term Frequency-Inverse Document Frequency) for indexing the crawled documents.
   - Processed HTML documents to extract text content and generate TF-IDF vectors.
   - Calculated cosine similarity between documents to enable efficient retrieval.

3. **Query Processing (Phase 3):**
   - Developed a RESTful API using Flask to handle text queries.
   - Integrated the TF-IDF indexing functionality into the query processor.
   - Implemented error checking and validation for incoming queries.
   - Returned search results in JSON format, including document titles, scores, and indices.

**Objectives Achieved:**
- Successfully crawled web documents from Wikipedia, focusing on video game-related content.
- Implemented TF-IDF indexing for efficient document retrieval.
- Built a user-friendly query processor using Flask, allowing users to search for documents based on text queries.

**Next Steps:**
- Enhance the web crawler to include more sources and improve coverage of video game-related content.
- Implement additional features in the query processor, such as query expansion and spelling correction, to improve search accuracy.
- Explore advanced techniques for document indexing and retrieval, such as word embeddings and semantic search.
