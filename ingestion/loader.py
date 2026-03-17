import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader, PyPDFLoader

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_PATH = os.path.join(BASE_DIR, "documents")

def load_documents(doc_path=DOCS_PATH):
    """
    Load all supported documents from the directory.
    Supports TXT and PDF files.
    """

    txt_loader = DirectoryLoader(
        doc_path,
        glob="**/*.txt",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": 'utf-8'}
    )

    pdf_loader = DirectoryLoader(
        doc_path,
        glob="**/*.pdf",
        loader_cls=PyPDFLoader
    )

    print("Loadding Documents....... in loader.py")
    txt_documents = txt_loader.load()
    pdf_documents = pdf_loader.load()

    documents = txt_documents + pdf_documents

    print("Finished Loading documents..... in loader.py")
    # for i, doc in enumerate(documents[:2]):
    #     print(f"\nDocument {i+1}: ")
    #     print(f"Source: {doc.metadata['source']}")
    #     print(f"Content Length: {len(doc.page_content)} characters")
    #     print(f"Content Preview: {doc.page_content[:100]}")
    #     print(f"Metadata: {doc.metadata}")

    return documents

# load_documents()
