# Preliminary Evaluation of Existing Data Storage Design

This report analyzes the current reference tools and data structure design. By comparing their structures and evaluating their strengths and weaknesses, we provide a preliminary assessment of the existing data storage approach and propose suggestions for field expansion.

## 1. Introduction to Reference Tools and Current Data Storage Design

### 1.1 MinerU JSON Format

| Field Name      | Description                                                                       |
| --------------- | --------------------------------------------------------------------------------- |
| pdf\_info       | List where each element is a dict representing the parsing result of one PDF page |
| \_parse\_type   | ocr \| txt, indicates the parsing mode used                                       |
| \_version\_name | String, version of magic-pdf used                                                 |

**Structure of `pdf_info` Field**

| Field Name           | Description                                                                                                |
| -------------------- | ---------------------------------------------------------------------------------------------------------- |
| preproc\_blocks      | Intermediate results after PDF preprocessing, before segmentation                                          |
| layout\_bboxes       | Layout segmentation result, includes direction (vertical/horizontal) and bbox, ordered by reading sequence |
| page\_idx            | Page index, starting from 0                                                                                |
| page\_size           | Width and height of the page                                                                               |
| \_layout\_tree       | Layout tree structure                                                                                      |
| images               | List of dicts, each representing an img\_block                                                             |
| tables               | List of dicts, each representing a table\_block                                                            |
| interline\_equations | List of dicts, each representing an interline\_equation\_block                                             |
| discarded\_blocks    | List of blocks the model suggests dropping                                                                 |
| para\_blocks         | Result after segmenting preproc\_blocks                                                                    |

**Level-1 Block**

| Field Name | Description                               |
| ---------- | ----------------------------------------- |
| type       | Block type (table \| image)               |
| bbox       | Bounding box coordinates                  |
| blocks     | List of dicts representing level-2 blocks |

> Note: Level-1 blocks are optional.

**Level-2 Block**

| Field Name | Description                             |
| ---------- | --------------------------------------- |
| type       | Block type                              |
| bbox       | Bounding box coordinates                |
| lines      | List of dicts, each representing a line |

**Level-2 Block Types**

| Type                | Description               |
| ------------------- | ------------------------- |
| image\_body         | Main content of the image |
| image\_caption      | Caption of the image      |
| image\_footnote     | Footnote of the image     |
| table\_body         | Main content of the table |
| table\_caption      | Caption of the table      |
| table\_footnote     | Footnote of the table     |
| text                | Text block                |
| title               | Title block               |
| index               | Index block               |
| list                | List block                |
| interline\_equation | Interline equation block  |

**Lines**

| Field Name | Description                         |
| ---------- | ----------------------------------- |
| bbox       | Bounding box of the line            |
| span       | List of spans that compose the line |

**Span**

| Field Name           | Description                                                     |
| -------------------- | --------------------------------------------------------------- |
| bbox                 | Bounding box of the span                                        |
| type                 | Type of span                                                    |
| content \| img\_path | For text spans use `content`; for visual content use `img_path` |

**Span Types**

| Type                | Description        |
| ------------------- | ------------------ |
| image               | Image              |
| table               | Table              |
| text                | Text               |
| inline\_equation    | Inline equation    |
| interline\_equation | Interline equation |

### 1.2 Marker JSON Format

| Field Name  | Description                                                      |
| ----------- | ---------------------------------------------------------------- |
| id          | Unique identifier of the block                                   |
| block\_type | Type of block                                                    |
| html        | HTML content of the page                                         |
| polygon     | Four-corner polygon of the page in clockwise order from top-left |
| children    | Child blocks                                                     |

> Note: Child blocks include:
>
> * `section_hierarchy`: Section to which the block belongs
> * `images`: Base64-encoded images

### 1.3 Current Data Storage Design

| Field Name      | Description                                                    |
| --------------- | -------------------------------------------------------------- |
| metadata        | Document metadata                                              |
| sections        | Section tree, each object is a title block                     |
| chunks          | Text slices, each object is a fixed-length token slice         |
| doc\_references | References including figures, tables, equations, and citations |

**1. Metadata**

| Field Name    | Description                |
| ------------- | -------------------------- |
| title         | Paper title                |
| authors\_info | Author information         |
| abstract      | Abstract                   |
| keywords      | Keywords                   |
| publish\_info | Publication details        |
| doc\_id       | Document ID (SHA-256 hash) |
| total\_pages  | Total number of pages      |

**2. Sections**

| Field Name    | Description                                         |
| ------------- | --------------------------------------------------- |
| sec\_id       | Unique identifier in format {doc\_id}\_sec{n}       |
| name          | Section title                                       |
| level         | Section level (1 = top level)                       |
| parent\_id    | Parent section ID (null for root)                   |
| children\_ids | List of child section IDs                           |
| full\_path    | Path from root to this section (as list of strings) |

**3. Chunks**

| Field Name            | Description                                        |
| --------------------- | -------------------------------------------------- |
| chunk\_id             | Unique ID in format {doc\_id}\_{sec\_id}\_chunk{n} |
| sec\_id               | ID of the section this chunk belongs to            |
| text                  | Text of the chunk                                  |
| tokens                | Number of tokens after encoding                    |
| page\_idx             | Page index of the chunk                            |
| position\_in\_section | Position within the section                        |
| ref\_ids              | List of referenced ref\_id elements                |

**4. Doc References**

| Field Name | Description                                               |
| ---------- | --------------------------------------------------------- |
| ref\_id    | Unique ID in format {doc\_id}\_ref{m}                     |
| type       | Type: "image", "table", "equation", "cite", "outer\_link" |
| content    | Reference content, empty for some types                   |
| path       | File path                                                 |
| caption    | Caption text (empty for equations)                        |
| page\_idx  | Page where the reference appears                          |
| chunk\_ids | List of chunk IDs referencing this element                |

## 2. Applicability Analysis of Reference Tools

| Feature / Tool           | Marker                                           | MinerU                                           |
| ------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| **Document Types**       | Reports, business/technical docs, simple papers  | Academic papers, scientific charts, whitepapers  |
| **Recognition Method**   | Rule + BERT-based extraction                     | Visual layout + OCR + multimodal models          |
| **Structure Extraction** | Good for paragraphs, titles, TOC, tables, images | Good for sections, formulas, references          |
| **Equation Recognition** | Average (misses inline formulas sometimes)       | Strong (structured LaTeX, supports MathML)       |
| **Chart Extraction**     | Extracts images only                             | Supports images with captions and numbers        |
| **Table Recognition**    | Layout-based                                     | Supports tables + names + context                |
| **Citation Extraction**  | Basic (only formatted text)                      | Strong (supports BibTeX/APA/IEEE)                |
| **Semantic Structure**   | Titles, TOC, pagination                          | Sections, paragraphs, references                 |
| **Complex Layouts**      | Sensitive to layout changes                      | Handles complex two-column, multi-column layouts |
| **Image-Text Alignment** | Not supported                                    | Supported                                        |

## 3. Applicability of Current Data Storage Design

### 1. General Field Analysis

| Field            | Generality | Applicable to           | Reason                                     |
| ---------------- | ---------- | ----------------------- | ------------------------------------------ |
| `metadata`       | High       | Almost all documents    | Includes essential document metadata       |
| `sections`       | High       | Documents with headings | Supports multi-level labeling              |
| `chunks`         | High       | All medium/long texts   | Suitable for LLMs but may fragment meaning |
| `doc_references` | High       | Docs with references    | Supports figures, formulas, citations      |

### 2. Document Type Analysis

| Document Type      | Applicability Summary                   |
| ------------------ | --------------------------------------- |
| Academic Papers    | Good, rich in formulas/references       |
| Reports            | Good, includes charts and structure     |
| Industry Standards | Moderate, needs extra metadata fields   |
| Textbooks          | Moderate, needs extra metadata fields   |
| Policies and Laws  | Good, standard structure and references |
| Legal Judgments    | Good, only has main body and no figures |
| Manuals            | Structured with titles and images       |
| News/Articles      | Unclear, lacks structure/references     |
| Fiction            | Good, has hierarchical structure        |
| Resumes            | Unclear, free-structured and image-rich |
| Certificates       | Unclear, mostly short with tables       |

### 3. Conclusion

The current data storage design is broadly applicable to most document types. For metadata-heavy documents, additional fields can enhance adaptability. For unstructured or semi-structured documents, applicability remains uncertain.

### 4. Suggestions

* In academic contexts, storing all author info in a single string under `"authors_info"` makes it hard to distinguish authors or attach detailed info. Use an array structure instead:

```json
"authors_info":[
  {
    "name": "A",
    "email": "A@A.com",
    "affiliation": "A"
  },
  {
    "name": "B",
    "email": "B@B.com",
    "affiliation": "B"
  }
]
```

* Fixed-length `"chunks"` may mix unrelated content (e.g., text with footnotes or tables). Consider other segmentation methods and add a `"type"` field to distinguish types.

* For standard documents and books, add an `"extra_info"` field to `"metadata"` as a dictionary for various supplementary data.

## 5. Uncertainty factors

- Sections lack page index info—does this affect usability?

- Chunks may include tables—should tables be split into chunks? (Arguably not)

- Is the `"sections"` field mandatory? Can it be null for unstructured docs like transcripts?

